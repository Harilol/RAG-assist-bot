from langchain_community.document_loaders import PyPDFLoader
import re
def load_pdf(file_path):
    loader = PyPDFLoader(file_path)
    documents = loader.load()




    for doc in documents:
     doc.page_content = re.sub(
        r'(?<=\b\w) (?=\w\b)',
        '',
        doc.page_content
    )

    return documents

