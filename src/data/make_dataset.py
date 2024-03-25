import argparse
import shutil
from glob import glob


def extract_data(dataset):
    all_images = glob(f'data/raw/*.jpg')
    if dataset == 'tiny':
        print('Extracting tiny dataset')
        images = all_images[:10]
        
    elif dataset == 'full':
        print('Extracting full dataset')
        images = all_images[:1000]

    shutil.rmtree(f'data/processed/{dataset}', ignore_errors=True)
    shutil.os.makedirs(f'data/processed/{dataset}')

    for image in images:
        shutil.copy(image, f'data/processed/{dataset}/')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('dataset', type=str, choices=['tiny', 'full'], help='Choose between tiny and full dataset (10 vs. 1000 images)')
    args = parser.parse_args()
    extract_data(args.dataset)
