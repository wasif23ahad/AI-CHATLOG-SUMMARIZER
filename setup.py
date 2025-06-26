import os

# Base path of this project
base_path = r"F:\my_AI_Projects\JobAssesments\QtecSolutionLimited\AI_ChatLog_Summarizer"

# Defining internal folder and file structure
structure = {
    "sampleChatLog": {
        "chat.txt": """User: Hello!
AI: Hi! How can I assist you today?
User: Can you explain what machine learning is?
AI: Certainly! Machine learning is a field of AI that allows systems to learn from data.
""",
        "chat2.txt": """User: What is natural language processing?
AI: NLP is a branch of AI that helps computers understand human language.
User: Can it translate languages?
AI: Yes, NLP powers translation tools like Google Translate.
User: What libraries are used in Python for NLP?
AI: Popular NLP libraries in Python include NLTK and spaCy.
""",
        "chat3.txt": """User: I want to build a website.
AI: Great! You can use frameworks like Django or Flask in Python.
User: Which one is better for beginners?
AI: Flask is simpler and good for small apps, Django is more feature-rich for larger projects.
User: Can I connect it to a database?
AI: Yes, both support databases like SQLite and PostgreSQL.
"""
    },
    "main.py": "",
    "requirements.txt": "nltk\nscikit-learn\n"
}

def create_structure(base, struct):
    for name, content in struct.items():
        path = os.path.join(base, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Created: {path}")

if __name__ == "__main__":
    create_structure(base_path, structure)
    print("\nProject files created successfully inside your existing folder!")
