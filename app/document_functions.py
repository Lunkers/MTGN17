import os
from sqlalchemy import desc, asc
from app.models.blandaren import Document
from app import db


SAVE_FOLDER = os.path.join(os.getcwd(), "static", "Schmeck", "blandaren")

def upload_document(request):
    files = request.files.getlist("files")
    print(request.files)
    if files is not None:
        for document in files:
            filename = document.filename
            filename = filename.replace(" ", "_")
            print(filename)
            document.save(os.path.join(SAVE_FOLDER, filename))
            new_doc = Document(filename = filename)
            db.session.add(new_doc)
    db.session.commit()
    return True

def get_documents():
    output = []
    docs = Document.query.all()
    for result in docs:
        doc_dict = result.as_dictionary()
        output.append(doc_dict)
    
    return output