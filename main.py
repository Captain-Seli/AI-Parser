import os
import parserL
import preprocess

def main():
    # Get the path to the PDF file
    pdf_path = input("Enter the path to the PDF file: ")

    # Parse the PDF file
    raw_text = parserL.extract_text(pdf_path)

    # Preprocess the text
    preprocessed_text = preprocess.preprocess_text(raw_text)

    # Print the preprocessed text
    print(preprocessed_text)

    # Save the preprocessed text to a file
    script_dir = os.path.dirname(__file__)
    output_file_path = os.path.join(script_dir, 'preprocessed_text.txt')
    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.write(preprocessed_text)

if __name__ == '__main__':
    main()