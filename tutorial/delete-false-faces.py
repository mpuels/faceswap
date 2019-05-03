#!/usr/bin/env python3

from config import FACE_DIR

FALSE_FACES_TXT = "false-faces.txt"


def main():
    png_name_to_path = {}
    for png in FACE_DIR.glob('**/*.png'):
        png_name_to_path[png.name] = png

    with open(FALSE_FACES_TXT) as f:
        false_face_png_names = [line.strip() for line in f]

    for false_face_png_name in false_face_png_names:
        if false_face_png_name in png_name_to_path:
            png_to_delete = png_name_to_path[false_face_png_name]
            print(f"Deleting {png_to_delete}")
            png_to_delete.unlink()
        else:
            print(f"File {false_face_png_name} does not exist.")


if __name__ == "__main__":
    main()
