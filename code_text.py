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


def empty_directory(directory=""):
    files = get_files(directory)

    for file in files:
        if os.path.isfile(file):
            os.remove(file)


def rename_text_files(prefix="", suffix=""):
    files = get_files("./TEXT")

    for file in files:
        path = file.split("\\")
        file_name = path[-1]
        extension = file_name.split(".")[-1]
        file_name = file_name.split(".")[0]

        new_file_name = prefix + file_name + "_" + suffix + "." + extension
        new_file_name = os.path.join("./TEXT", new_file_name)
        os.rename(file, new_file_name)


def code_to_text():
    files = get_files("./CODE")
    empty_directory("./TEXT")

    for file in files:
        file_content = None
        with open(file, "r") as f:
            file_content = str(f.read())

        # Changes file extension to txt
        # Removes upto the last slash
        new_file = file.split("\\")[-1]

        # Removes the extension
        new_file_without_extension = new_file.split(".")[0]
        old_file_extension = new_file.split(".")[-1]
        # Adds the new extension
        new_file = (
            new_file_without_extension + "_" + old_file_extension.upper() + ".txt"
        )

        # Adds the new path
        new_file = os.path.join("./TEXT", new_file)

        try:
            # Creates the file
            with open(new_file, "x") as f:
                # Writes the content
                f.write(file_content)
        except FileExistsError:
            number: int = 1
            while True:
                # Adds a number to the file name
                new_file = new_file.split(".")[0] + f"_{number}.txt"
                # Checks if the file exists

                if os.path.exists(new_file):
                    continue
                else:
                    break

            with open(new_file, "x") as f:
                f.write(file_content)
