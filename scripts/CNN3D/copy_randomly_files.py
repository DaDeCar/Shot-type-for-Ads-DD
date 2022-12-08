# -*- coding: utf-8 -*-

" This script generates a new folder(the files are take in a randomly way) with a max_number of files from the original folder"


import argparse
import csv
import os
import json
import os
import random
import sys

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
        "output_data_folder",
        type=str,
        help=(
            "Full path to the directory in which we will store the resulting "
            "train/test splits. E.g. `./data/trailer_v5`."
        ),
    )

    args = parser.parse_args()

    return args


def main(data_folder, output_data_folder):
    
    
    def move_data(max_len):

        files_list = []
        get_files = os.listdir(data_folder)
        for id_movie in get_files:
            files_list.append(id_movie)
        random.shuffle(files_list)
        if not os.path.exists(output_data_folder):
                os.makedirs(output_data_folder)
        for item in files_list[0:max_len]:
            path_source = data_folder + '/'+ item
            path_dest = output_data_folder + '/'+ item
            
            os.link(path_source, path_dest)
   
    move_data(max_len = 800)

if __name__ == "__main__":
    args = parse_args()
    main(args.data_folder, args.output_data_folder)