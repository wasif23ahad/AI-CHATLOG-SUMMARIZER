import os

# Base path  of this project
base_path = r"F:\my_AI_Projects\JobAssesments\QtecSolutionLimited\AI_ChatLog_Summarizer"

# Defining internal folder and file structure
structure = {
    "chat_logs": {
        "sample_chat.txt": """User: Hi, can you tell me about Python?
AI: Sure! Python is a popular programming language known for its readability.
User: What can I use it for?
AI: You can use Python for web development, data analysis, AI, and more.
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
