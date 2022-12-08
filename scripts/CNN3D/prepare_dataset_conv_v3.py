# -*- coding: utf-8 -*-
"""
This script will be used to separate and copy images coming from
`./data/trailer` between `train` and `test` and 'val' needed to run 
Conv_3d model.

The resulting directory structure should look like this:
    data/
    ├── trailer
    ├── trailer_v2
    ├── README.pdf
    ├── v1_full_trailer.json
    ├── v1_split_trailer.json
    ├── v2_full_trailer.json
    ├── trailer_v5
    │   ├── test
    |   |   |̣̣── Static
    │   │       ├── shot_<id_movie>_<id_shot>.mp4
    |   |   |̣̣── Motion
    │   │       ├── shot_<id_movie>_<id_shot>.mp4
    |   |   |̣̣── Pull
    │   │       ├── shot_<id_movie>_<id_shot>.mp4
    |   |   |̣̣── Push
    │   │       ├── shot_<id_movie>_<id_shot>.mp4
    |   |
    │   ├── train
    |   |   |̣̣── Static
    │   │       ├── shot_<id_movie>_<id_shot>.mp4
    |   |   |̣̣── Motion
    │   │       ├── shot_<id_movie>_<id_shot>.mp4
    |   |   |̣̣── Pull
    │   │       ├── shot_<id_movie>_<id_shot>.mp4
    |   |   |̣̣── Push
    │   │       ├── shot_<id_movie>_<id_shot>.mp4
    |   |
    │   ├── val
    |   |   |̣̣── Static
    │   │       ├── shot_<id_movie>_<id_shot>.mp4
    |   |   |̣̣── Motion
    │   │       ├── shot_<id_movie>_<id_shot>.mp4
    |   |   |̣̣── Pull
    │   │       ├── shot_<id_movie>_<id_shot>.mp4
    |   |   |̣̣── Push
    │   │       ├── shot_<id_movie>_<id_shot>.mp4


Besides, It's possible to limit the number of videos per folder, which allows 
to get a balance dataset, using "max_len_folder" param

"""
import argparse
import csv
import os
import json

def parse_args():
    parser = argparse.ArgumentParser(description="Train your model.")
    parser.add_argument(
        "data_folder",
        type=str,
        help=(
            "Full path to the directory having all the videos. E.g. "
            "`./data/trailer/`."
        ),
    )
    parser.add_argument(
        "labels",
        type=str,
        help=(
            "Full path to the JSON file with data labels. E.g. "
            "`./data/v1_split_trailer.json`."
        ),
    )
    parser.add_argument(
        "output_data_folder",
        type=str,
        help=(
            "Full path to the directory in which we will store the resulting "
            "train/test splits. E.g. `./data/trailer_v5`."
        ),
    )

    args = parser.parse_args()

    return args


def main(data_folder, labels, output_data_folder):
    """
    Parameters
    ----------
    data_folder : str
        Full path to raw videos folder.
    labels : str
        Full path to JSON file with data annotations.
    output_data_folder : str
        Full path to the directory in which we will store the resulting
        train/test splits.
    """

    with open(labels, "r") as data_json:
        data = json.load(data_json)

    
    def move_data(type_, max_len_folder = 200):
        dest_type = type_
        for id_movie in data[type_]:
            for id_shot in data[type_][id_movie]:
                
                path_video = f"{data_folder}/{id_movie}/shot_{id_shot}.mp4"
                video_label = data[type_][id_movie][id_shot]['movement']['label']
                if video_label == 'Multi_movement':
                    pass
                else:
                    path_dir_dest = f"{output_data_folder}/{dest_type}/{video_label}"
                    
                    # Checking for class folders and controling their long
                    try: 
                        len_class_folder = len([name for name in os.listdir(path_dir_dest) if os.path.isfile(os.path.join(path_dir_dest, name))])
                    except: 
                        len_class_folder = 0
                    if len_class_folder >= max_len_folder:
                        pass
                    else: 
                        if not os.path.exists(path_dir_dest):
                            os.makedirs(path_dir_dest)
                        path_video_dest = f"{path_dir_dest}/shot_{id_movie}_{id_shot}.mp4"
                        os.link(path_video, path_video_dest)
                            

    move_data('train', max_len_folder = 2000)
    move_data('test', max_len_folder = 10000)
    move_data('val', max_len_folder = 200)

if __name__ == "__main__":
    args = parse_args()
    main(args.data_folder, args.labels, args.output_data_folder)