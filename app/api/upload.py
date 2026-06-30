from fastapi import APIRouter
import os
from app.database.chroma_db import get_vector_store
from app.loaders.pdf_loader import load_pdf
from fastapi import UploadFile,File
router = APIRouter()
from app.chunking.text_splitter import split_documents
#uvicorn app.main:app --reload
@router.post('/upload')
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    
    # Ensure uploads directory exists
    os.makedirs('data/uploads', exist_ok=True)

    print(os.getcwd())
    print(file.filename)
    with open(f'data/uploads/{file.filename}','wb') as f:
        f.write(contents)
    documents = load_pdf(f'data/uploads/{file.filename}')
    chunks = split_documents(documents)
    vector_store = get_vector_store()
    vector_store.add_documents(chunks)
    print(vector_store._collection.count())
    #print(doc[0].page_content[:500])
    return {
        'message': file.filename,
        'filename': file.filename,
    }
        
