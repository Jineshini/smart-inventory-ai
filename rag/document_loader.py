import os
from pathlib import Path
from pypdf import PdfReader


def load_documents(folder_path="knowledge"):
    documents = []

    folder = Path(folder_path)

    if not folder.exists():
        return documents

    for file in folder.iterdir():

        if file.suffix.lower() == ".pdf":

            reader = PdfReader(file)

            text = ""

            for page in reader.pages:
                page_text = page.extract_text()

                if page_text:
                    text += page_text

            documents.append({
                "filename": file.name,
                "content": text
            })

    return documents


if __name__ == "__main__":

    docs = load_documents()

    print(f"Loaded documents: {len(docs)}")

    for doc in docs:
        print(doc["filename"])