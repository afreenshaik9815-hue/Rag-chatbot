from pypdf import PdfReader

def extract_text(pdf_path):
    reader=PdfReader(pdf_path)
    text=""
    for page in reader.pages:
        page_text=page.extract_text()
        if page_text:
            text+=page_text
    return text
pdf_path = r"C:\RAG_Chatbot\data\sample.pdf.pdf"
# Replace with the actual path to your PDF file
text = extract_text(pdf_path)
print(text)