from pypdf import PdfReader


def load_pdf(pdf_path):
    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text


if __name__ == "__main__":
    pdf_path = "data/docs/sample.pdf"

    document_text = load_pdf(pdf_path)

    print(document_text[:1000])  # preview first 1000 chars