import os

import chromadb
from sentence_transformers import SentenceTransformer


# --------------------------------------------------
# 1. Find the RAG folder
# --------------------------------------------------

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)


# --------------------------------------------------
# 2. Find the policy documents folder
# --------------------------------------------------

POLICY_FOLDER = os.path.join(
    BASE_DIR,
    "policy_documents"
)


# --------------------------------------------------
# 3. Create a folder for ChromaDB
# --------------------------------------------------

CHROMA_FOLDER = os.path.join(
    BASE_DIR,
    "chroma_db"
)


# --------------------------------------------------
# 4. Load embedding model
# --------------------------------------------------

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# --------------------------------------------------
# 5. Create ChromaDB client
# --------------------------------------------------

chroma_client = chromadb.PersistentClient(
    path=CHROMA_FOLDER
)


# --------------------------------------------------
# 6. Create or get policy collection
# --------------------------------------------------

policy_collection = chroma_client.get_or_create_collection(
    name="ecommerce_policies"
)


# --------------------------------------------------
# 7. Read policy documents
# --------------------------------------------------

def load_policy_documents():

    documents = []
    ids = []

    for filename in os.listdir(POLICY_FOLDER):

        if not filename.endswith(".txt"):
            continue

        file_path = os.path.join(
            POLICY_FOLDER,
            filename
        )

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            content = file.read()

        documents.append(content)

        document_id = filename.replace(
            ".txt",
            ""
        )

        ids.append(document_id)

    return ids, documents


# --------------------------------------------------
# 8. Build RAG index
# --------------------------------------------------

def build_policy_index():

    ids, documents = load_policy_documents()

    if not documents:

        return "No policy documents found."

    embeddings = embedding_model.encode(
        documents
    ).tolist()

    policy_collection.upsert(
        ids=ids,
        documents=documents,
        embeddings=embeddings
    )

    return (
        f"{len(documents)} policy documents indexed."
    )


# --------------------------------------------------
# 9. Search policies
# --------------------------------------------------

def search_policy(query):

    query_embedding = embedding_model.encode(
        [query]
    ).tolist()

    results = policy_collection.query(
        query_embeddings=query_embedding,
        n_results=2
    )

    documents = results.get(
        "documents",
        []
    )

    if not documents:

        return "No relevant policy was found."

    relevant_policies = []

    for document_list in documents:

        for document in document_list:

            relevant_policies.append(document)

    return "\n\n--- RELEVANT POLICY ---\n\n".join(
        relevant_policies
    )