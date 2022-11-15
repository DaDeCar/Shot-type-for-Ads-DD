# -*- coding: utf-8 -*-
"""
This script will be used to separate and copy images coming from
`./data/trailer` between `train` and `test`
folders according to the key `train` or `test` from `v1_split_trailer.json`.
It will also create all the needed subfolders inside `train`/`test` in order
to copy each video to the folder corresponding to its class.
The resulting directory structure should look like this:
    data/
    ├── trailer
    ├── trailer_v2
    ├── README.pdf
    ├── v1_full_trailer.json
    ├── v1_split_trailer.json
    ├── v2_full_trailer.json
    ├── trailer_v3
    │   ├── test
    │   │   ├── shot_<id_movie>_<id_shot>.mp4
    │   ├── train
    │   │   ├── shot_<id_movie>_<id_shot>.mp4
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
            "train/test splits. E.g. `./data/trailer_v3/train`."
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

    no_load_list= []
    def move_data(type_):
        dest_type = type_
        if type_ == 'val':
            dest_type = 'train'
        for id_movie in data[type_]:
            for id_shot in data[type_][id_movie]:
                
                path_video = f"{data_folder}/{id_movie}/shot_{id_shot}.mp4"
                path_dir_dest = f"{output_data_folder}/{dest_type}"
                if not os.path.exists(path_dir_dest):
                    os.makedirs(path_dir_dest)
                path_video_dest = f"{path_dir_dest}/shot_{id_movie}_{id_shot}.mp4"
                os.link(path_video, path_video_dest)
               

    move_data('train')
    move_data('test')
    move_data('val')

if __name__ == "__main__":
    args = parse_args()
    main(args.data_folder, args.labels, args.output_data_folder)