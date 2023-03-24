import os
from fpdf import FPDF


def get_files(dir="", only_txt=False):
    files = []
    for file in os.listdir(dir):
        if only_txt:
            if file.endswith(".txt"):
                files.append(file)
        else:
            files.append(file)

    return files


def empty_directory(directory=""):
    files = get_files(directory)

    for file in files:
        if os.path.isfile(file):
            os.remove(file)


def rename_pdf_files(prefix="", suffix=""):
    files = get_files("./PDF")

    for file in files:
        path = file.split("\\")
        file_name = path[-1]
        extension = file_name.split(".")[-1]
        file_name = file_name.split(".")[0]

        file = os.path.join("./PDF", file)

        language = file_name.split("_")[-1]
        language_length = len(language)
        language = file_name[-language_length:]
        file_name = file_name[:-language_length]

        file_name = f"{file_name[:-1]}.{language}"
        new_file_name = f"{prefix}{file_name}_{suffix}.{extension}"
        new_file_name = os.path.join("./PDF", new_file_name)
        os.rename(file, new_file_name)

        try:
            os.remove(file)
        except FileNotFoundError:
            pass


def convert_files_text_to_pdf():
    files = get_files("./TEXT")
    empty_directory("./PDF")
    # Converts the text to pdf

    for file in files:
        file = os.path.join("./TEXT", file)

        pdf = FPDF()
        pdf.add_page()

        # Adds Header

        with open(file) as f:
            # File Name
            pdf.set_font("Arial", size=24)
            file_name = file.split("\\")[-1]

            # Removes the extension
            file_name = file_name.split(".")[0]

            # Gets Language
            language = file_name.split("_")[-1]
            language_length = len(language)
            # Removes the language by removing the last character by calculating the length
            # of the language. (This allows '_' in the file name)

            file_name = file_name[: -language_length - 1]

            file_name = file_name.capitalize() + " (" + language + ")"

            pdf.cell(200, 10, txt=file_name, ln=1, align="C")
            pdf.set_font("Arial", size=12)

            # Adds a large space
            pdf.cell(200, 10, txt="", ln=1, align="C")

            for x in f:
                pdf.multi_cell(w=0, h=6, txt=x)

        # Removes path
        new_file = file.split("\\")[-1]

        # Removes the extension
        new_file_without_extension = new_file.split(".")[0]

        # Adds the new extension
        new_file = new_file_without_extension + ".pdf"
        new_file = os.path.join("./PDF", new_file)

        try:
            pdf.output(new_file)
        except:
            pass


if __name__ == "__main__":
    convert_files_text_to_pdf()
