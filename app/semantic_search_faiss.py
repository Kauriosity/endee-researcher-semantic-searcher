import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

# Load dataset
df = pd.read_csv("researchers.csv")

# Load embedding model
print("Loading model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

print("Generating embeddings...")
embeddings = model.encode(df["research_interests"].tolist())

# Convert to float32
embeddings = np.array(embeddings).astype("float32")

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

print("FAISS index created successfully!")

# Query loop
while True:
    query = input("\nEnter research query (or type 'exit'): ")
    if query.lower() == "exit":
        break

    query_vector = model.encode([query])
    query_vector = np.array(query_vector).astype("float32")

    k = 5
    distances, indices = index.search(query_vector, k)

    print("\nTop Matching Researchers:\n")

    for i in indices[0]:
        print("Name:", df.iloc[i]["name"])
        print("Research Interests:", df.iloc[i]["research_interests"])
        print("-" * 50)
        import pandas as pd
