from pdf_reader import extract_text
from chunking import chunk_text
from embeddings import create_embeddings
from vector_store import VectorStore
from rag import ask_llm

#read pdf
text= extract_text("data/sample.pdf")
#chunks
chunks=chunk_text(text)
#embedd
vectors=create_embeddings(chunks)
#vectordb  store
store= VectorStore(vectors.shape[1])
store.add(vectors,chunks)

print("PDF Uploaded successfully")
while True:
    question = input("Ask a question or type exit")
    
    if question.lower() == "exit":
        break
    query_vector = create_embeddings([question])[0]
    retrived = store.search(query_vector,top_k=5)
    context = "\n\n".join(retrived)
    answer = ask_llm(question,context)

    print(answer)