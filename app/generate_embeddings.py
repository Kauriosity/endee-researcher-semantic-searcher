from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np

# Load model
print("Loading embedding model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load dataset
df = pd.read_csv("researchers.csv")

print("Generating embeddings...")

# We will use profile_text column (already combined meaningful text)
texts = df["profile_text"].tolist()

embeddings = model.encode(texts, show_progress_bar=True)

# Save embeddings separately
np.save("researcher_embeddings.npy", embeddings)

print("✅ Embeddings generated and saved successfully!")
print(f"Shape of embeddings: {embeddings.shape}")