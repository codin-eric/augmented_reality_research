from pathlib import Path
import numpy as np

def searching_all_files(directory: Path):   
    file_list = [] # A list for storing files existing in directories

    for x in directory.iterdir():
        if x.is_file():

           file_list.append(x)
        else:

           file_list.append(searching_all_files(directory/x))

    return file_list


def random_pokemon_img(img_path):
    p = Path(img_path)
    img_lst = searching_all_files(p)
    return f"{np.random.choice(img_lst)}"

if __name__ == "__main__":
    print(random_pokemon_img())