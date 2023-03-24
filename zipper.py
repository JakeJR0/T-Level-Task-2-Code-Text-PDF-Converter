from zipfile import ZipFile
import os


def get_files(directory=""):
    files = []

    for file in os.listdir(directory):
        item = os.path.join(directory, file)

        if os.path.isfile(item) and not item.endswith(".jpg"):
            files.append(item)
        elif os.path.isdir(item):
            if item.endswith(".git"):
                continue

            files.extend(get_files(item))

    return files


def zipOutput(prefix="", suffix=""):
    output_file_name = f"{prefix}_CodeExport_{suffix}"
    if os.path.exists(f"./OUTPUT/{output_file_name}.zip"):
        os.remove(f"./OUTPUT/{output_file_name}.zip")

    with ZipFile(f"./OUTPUT/{output_file_name}.zip", "w") as zip:

        pdf_files = get_files("./PDF")

        for i in pdf_files:
            zip.write(i)

        text_files = get_files("./TEXT")

        for i in text_files:
            zip.write(i)
