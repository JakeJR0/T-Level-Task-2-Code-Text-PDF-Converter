from code_text import code_to_text, rename_text_files
from text_pdf import convert_files_text_to_pdf, rename_pdf_files


def rename_files():
    task_name = "Task_2"
    while True:
        registration_number = input("Enter your registration number: ")
        if len(registration_number) > 5 and len(registration_number) < 10:
            break

    while True:
        first_name = input("Enter your first name: ")

        if len(first_name) > 0 and len(first_name) < 20:
            break

    while True:
        last_name = input("Enter your last name: ")
        if len(last_name) > 0 and len(last_name) < 30:
            break

    prefix = f"{task_name}_"
    suffix = f"{registration_number}_{last_name}_{first_name[0:1].upper()}"

    rename_text_files(prefix, suffix)
    rename_pdf_files(prefix, suffix)
    print("Exported files are in the PDF folder and TEXT folder.")


if __name__ == "__main__":
    code_to_text()
    convert_files_text_to_pdf()
    rename_files()
