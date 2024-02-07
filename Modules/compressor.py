import zipfile
import pathlib


def zip_files(file_location, folder_path):
    des_dir = pathlib.Path(folder_path, "compressed.zip")
    with zipfile.ZipFile(des_dir, 'w') as archive:
        for file in file_location:
            file = pathlib.Path(file)
            archive.write(file, arcname=file.name)


if __name__ == "__main__":
    zip_files(file_location=["../Files/climate.csv"], folder_path="../Files")
