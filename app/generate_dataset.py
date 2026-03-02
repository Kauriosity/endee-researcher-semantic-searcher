import pandas as pd
import random

# Reproducibility
random.seed(42)

names = [
    "Aarav Sharma", "Meera Iyer", "Rohan Singh", "Ananya Gupta",
    "Kabir Verma", "Ishita Rao", "Aditya Nair", "Sneha Kapoor",
    "Vivaan Malhotra", "Priya Menon", "Arjun Patel", "Diya Sethi",
    "Kunal Mehta", "Ritika Desai", "Rahul Khanna", "Neha Joshi"
]

research_domains = [
    "Natural Language Processing and Large Language Models",
    "Computer Vision for Medical Imaging",
    "Healthcare AI and Clinical Decision Systems",
    "Graph Neural Networks for Drug Discovery",
    "Reinforcement Learning for Robotics",
    "Explainable AI in Healthcare",
    "Cybersecurity using Machine Learning",
    "AI for Climate Change Modeling",
    "Financial Fraud Detection using AI",
    "Autonomous Systems and Self Driving Cars"
]

skills = [
    "Python", "PyTorch", "TensorFlow", "HuggingFace",
    "Transformers", "Vector Databases", "LangChain",
    "Deep Learning", "Machine Learning",
    "FastAPI", "Scikit-Learn", "Data Analysis"
]

publications = [
    "Transformer models for medical text analysis",
    "CNN-based tumor detection system",
    "RAG-based conversational AI framework",
    "Bias detection in large language models",
    "Graph neural networks for drug discovery",
    "Explainable AI for clinical diagnostics",
    "AI-driven climate prediction models",
    "Financial anomaly detection system",
    "Multi-agent reinforcement learning framework",
    "Semantic search engine for academic research"
]

data = []

for i in range(1, 201):  # 200 researchers
    name = random.choice(names) + f" {i}"
    domain = random.choice(research_domains)
    skill_set = ", ".join(random.sample(skills, 3))
    publication = random.choice(publications)

    combined_interest = f"{domain}. Expertise in {skill_set}. Published work on {publication}."

    data.append({
        "id": i,
        "name": name,
        "research_interests": domain,
        "skills": skill_set,
        "publications": publication,
        "profile_text": combined_interest
    })

df = pd.DataFrame(data)
df.to_csv("researchers.csv", index=False)

print("✅ researchers.csv generated successfully with 200 synthetic researcher profiles!")