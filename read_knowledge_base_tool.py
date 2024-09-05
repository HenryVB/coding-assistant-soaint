import re
from langchain.tools import tool
from PyPDF2 import PdfReader

# Tool to fetch and preprocess Kwowledge Base in different formats


@tool
def read_pdf_tool(file_path) -> str:
    """
    Fetches and preprocesses content from a PDF.
    Returns the text of the PDF.
    """
    # response = requests.get(url)
    # with open('temp.pdf', 'wb') as f:
    #    f.write(response.content)

    with open(file_path, 'rb') as file:
        pdf = PdfReader(file)
        text = '\n'.join(page.extract_text()
                         for page in pdf.pages if page.extract_text())

    # Optional preprocessing of text
    processed_text = re.sub(r'\s+', ' ', text).strip()
    return processed_text
