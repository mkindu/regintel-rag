from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_documents(pages, source_name):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    chunks = []

    for page in pages:
        page_chunks = splitter.split_text(page["text"])

        for chunk in page_chunks:
            chunks.append({
                "text": chunk,
                "metadata": {
                    "source": source_name,
                    "page": page["page"]
                }
            })

    return chunks