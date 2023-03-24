from code_text import code_to_text, rename_text_files
from text_pdf import convert_files_text_to_pdf, rename_pdf_files
from zipper import zipOutput


def rename_files():
    while True:
        task_name = input("\nEnter your task name: ")

        if len(task_name) > 0 and len(task_name) < 20:
            break

    task_name = task_name.replace(" ", "_")

    while True:
        registration_number = input("\nEnter your registration number: ")
        if len(registration_number) > 5 and len(registration_number) < 20:
            break

    while True:
        first_name = input("\nEnter your first name: ")

        if len(first_name) > 0 and len(first_name) < 20:
            break

    while True:
        last_name = input("\nEnter your last name: ")
        if len(last_name) > 0 and len(last_name) < 30:
            break

    prefix = f"{task_name}_"
    suffix = f"{registration_number}_{last_name}_{first_name[0:1].upper()}"

    rename_text_files(prefix, suffix)
    rename_pdf_files(prefix, suffix)
    zipOutput(prefix, suffix)
    print(
        "\nExported files are in the PDF folder and TEXT folder and a zip file in the OUTPUT folder."
    )


if __name__ == "__main__":
    code_to_text()
    convert_files_text_to_pdf()
    rename_files()
