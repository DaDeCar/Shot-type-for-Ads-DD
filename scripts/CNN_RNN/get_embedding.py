#from tensorflow_docs.vis import embed
from tensorflow import keras
#from imutils import paths

import matplotlib.pyplot as plt
import tensorflow as tf
import pandas as pd
import numpy as np
#import imageio
import cv2
import os
import json




data_df = pd. read_csv('/home/app/src/data/CSV/dataset_df.csv', dtype={"shot": str})

data_df.drop(columns=['scale_val'], inplace=True)
data_df.drop(columns = ['move_val'], inplace=True)

train_path = '/home/app/src/data/shot-type-dataset/trailer_v3/train/'
data_df['video_name'] = train_path + 'shot_' + data_df['movie'] + '_' + data_df['shot'] + '.mp4'
train_df = data_df[(data_df['dataset']=='train') | (data_df['dataset']=='val') ]
train_df = train_df[['video_name', 'move_label','scale_label']]
train_df = train_df.rename(columns ={'scale_label': 'tag'})

test_path = '/home/app/src/data/shot-type-dataset/trailer_v3/test/'
data_df['video_name'] = test_path + 'shot_' + data_df['movie'] + '_' + data_df['shot'] + '.mp4'
test_df = data_df[data_df['dataset']=='test']
test_df = test_df[['video_name', 'move_label','scale_label']]
test_df = test_df.rename(columns ={'scale_label': 'tag'})




train_df_bal_static = train_df[train_df.move_label == 'Static'][0:700]
train_df_bal_motion = train_df[train_df.move_label == 'Motion'][0:700]

len_push_tag = train_df.move_label[train_df.move_label == 'Push'].shape[0]
len_pull_tag = train_df.move_label[train_df.move_label == 'Pull'].shape[0]

train_df_bal_push = train_df[train_df.move_label == 'Push'][0:len_push_tag]
train_df_bal_pull = train_df[train_df.move_label == 'Pull'][0:len_pull_tag]

train_df_bal = pd.concat([train_df_bal_static, train_df_bal_motion, train_df_bal_pull, train_df_bal_push], axis=0)




test_df_bal_static = test_df[test_df.move_label == 'Static'][0:150]
test_df_bal_motion = test_df[test_df.move_label == 'Motion'][0:150]

len_push_tag = test_df.move_label[test_df.move_label == 'Push'].shape[0]
len_pull_tag = test_df.move_label[test_df.move_label == 'Pull'].shape[0]

test_df_bal_push = test_df[test_df.move_label == 'Push'][0:len_push_tag]
test_df_bal_pull = test_df[test_df.move_label == 'Pull'][0:len_pull_tag]
test_df_bal = pd.concat([test_df_bal_static, test_df_bal_motion, test_df_bal_pull, test_df_bal_push], axis=0)


train_df_bal = train_df_bal.rename(columns ={'tag':'scale_label'})
train_df_bal = train_df_bal.rename(columns ={'move_label':'tag'})
train_df_bal = train_df_bal.reset_index(drop = True)

test_df_bal = test_df_bal.rename(columns ={'tag':'scale_label'})
test_df_bal = test_df_bal.rename(columns ={'move_label':'tag'})
test_df_bal = test_df_bal.reset_index(drop = True)


train_df= train_df_bal
test_df = test_df_bal

print(f"Total videos for training: {len(train_df)}")
print(f"Total videos for testing: {len(test_df)}")

train_df.sample(10)


# reading the JSON data using json.load()
json_path = '/home/app/src/data/shot-type-dataset/v1_split_trailer.json'

with open(json_path) as train_file:
    dict_v1= json.load(train_file)


def tag_ckecker (df, json_dict, df_name_to_check):
    tag_chek_list = []

    for i in range(len(df.index)):
        movie = df['video_name'][i]
        df_tag = df['tag'][df['video_name'] == movie][i]
        find_char_st = movie.find('_', 55,60)
        find_char_end = movie.find('_', 65,70)
        movie_key = movie[find_char_st+1:find_char_end]
        trailer_key =  movie[find_char_end+1:find_char_end+5]
        try:
            dict_tag = json_dict[df_name_to_check][movie_key][trailer_key]['movement']['label']
        except KeyError:
            dict_tag = json_dict['val'][movie_key][trailer_key]['movement']['label']

            if dict_tag == df_tag:
                pass
            else:
                tag_chek_list.append(movie)

    if len(tag_chek_list) == 0:
        print(f'tag check {df_name_to_check} OK')
    else: print (tag_chek_list)


tag_ckecker(train_df, dict_v1, 'train')
tag_ckecker(test_df, dict_v1, 'test')


print(f'Train value counts' +'/n',train_df['tag'].value_counts(), '/n')
print(f'Test value counts' +'/n',test_df['tag'].value_counts(), '/n')




IMG_SIZE = 224
BATCH_SIZE = 64
EPOCHS = 20

MAX_SEQ_LENGTH = 20
NUM_FEATURES = 2048



def crop_center_square(frame):
    y, x = frame.shape[0:2]
    min_dim = min(y, x)
    start_x = (x // 2) - (min_dim // 2)
    start_y = (y // 2) - (min_dim // 2)
    return frame[start_y : start_y + min_dim, start_x : start_x + min_dim]


def load_video(path, max_frames=0, resize=(IMG_SIZE, IMG_SIZE)):
    cap = cv2.VideoCapture(path)
    frames = []
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frame = crop_center_square(frame)
            frame = cv2.resize(frame, resize)
            frame = frame[:, :, [2, 1, 0]]
            frames.append(frame)

            if len(frames) == max_frames:
                break
    finally:
        cap.release()
    return np.array(frames)



def build_feature_extractor():
    feature_extractor = keras.applications.InceptionV3(
        weights="imagenet",
        include_top=False,
        pooling="avg",
        input_shape=(IMG_SIZE, IMG_SIZE, 3),
    )
    preprocess_input = keras.applications.inception_v3.preprocess_input

    inputs = keras.Input((IMG_SIZE, IMG_SIZE, 3))
    preprocessed = preprocess_input(inputs)

    outputs = feature_extractor(preprocessed)
    return keras.Model(inputs, outputs, name="feature_extractor")


feature_extractor = build_feature_extractor()
print(feature_extractor.summary())



label_processor = keras.layers.StringLookup(
    num_oov_indices=0, vocabulary=np.unique(train_df["tag"])
)
print(label_processor.get_vocabulary())





def prepare_all_videos(df, root_dir):
    num_samples = len(df)
    video_paths = df["video_name"].values.tolist()
    labels = df["tag"].values
    labels = label_processor(labels[..., None]).numpy()

    # `frame_masks` and `frame_features` are what we will feed to our sequence model.
    # `frame_masks` will contain a bunch of booleans denoting if a timestep is
    # masked with padding or not.
    frame_masks = np.zeros(shape=(num_samples, MAX_SEQ_LENGTH), dtype="bool")
    frame_features = np.zeros(
        shape=(num_samples, MAX_SEQ_LENGTH, NUM_FEATURES), dtype="float32"
    )

    # For each video.
    for idx, path in enumerate(video_paths):
        # Gather all its frames and add a batch dimension.
        frames = load_video(os.path.join(root_dir, path))
        frames = frames[None, ...]

        # Initialize placeholders to store the masks and features of the current video.
        temp_frame_mask = np.zeros(shape=(1, MAX_SEQ_LENGTH,), dtype="bool")
        temp_frame_features = np.zeros(
            shape=(1, MAX_SEQ_LENGTH, NUM_FEATURES), dtype="float32"
        )

        # Extract features from the frames of the current video.
        for i, batch in enumerate(frames):
            video_length = batch.shape[0]
            length = min(MAX_SEQ_LENGTH, video_length)
            for j in range(length):
                temp_frame_features[i, j, :] = feature_extractor.predict(
                    batch[None, j, :]
                )
            temp_frame_mask[i, :length] = 1  # 1 = not masked, 0 = masked

        frame_features[idx,] = temp_frame_features.squeeze()
        frame_masks[idx,] = temp_frame_mask.squeeze()

    return (frame_features, frame_masks), labels


train_data, train_labels = prepare_all_videos(train_df, "train")
test_data, test_labels = prepare_all_videos(test_df, "test")

print(f"Frame features in train set: {train_data[0].shape}")
print(f"Frame masks in train set: {train_data[1].shape}")



path_save_embeddings= '/home/app/src/embeddings/mov_bal_2k_embeddings_20F/'

# Train
train_data_embedding_0 = np.save(path_save_embeddings + 'train_data_embedding_0.npy', train_data[0])
train_data_embedding_1 = np.save(path_save_embeddings + 'train_data_embedding_1.npy', train_data[1])
train_labels_embedding = np.save(path_save_embeddings + 'train_labels_embedding.npy', train_labels)

#Test
test_data_embedding_0 = np.save(path_save_embeddings + 'test_data_embedding_0.npy', test_data[0])
test_data_embedding_1 = np.save(path_save_embeddings + 'test_data_embedding_1.npy', test_data[1])
test_labels_embedding = np.save(path_save_embeddings + 'test_labels_embedding.npy', test_labels)