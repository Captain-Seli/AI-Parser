
import PyPDF2

def parse_pdf():
    # Prompt the user for the PDF file path
    pdf_path = input("Enter the path to the PDF file: ")

    # Open the PDF file in read mode
    try:
        with open(pdf_path, "rb") as pdf_file:
            # Create a PDF reader object
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            # Get the number of pages in the PDF document
            num_pages = len(pdf_reader.pages)

            # Loop through each page and extract the text
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                print(text)

    except FileNotFoundError:
        print(f"Error: Could not find file {pdf_path}")
    except PermissionError:
        print(f"Error: Permission denied for file {pdf_path}")

def main():
    # Call the parse_pdf_file method
    pdf_text = parse_pdf()

    # Print the parsed text
    print(pdf_text)

if __name__ == '__main__':
    main()