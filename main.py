import os
import re
from collections import Counter
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# ===== 1. Read & Parse the Chat Log =====
def read_chat_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    user_msgs = []
    ai_msgs = []

    for line in lines:
        line = line.strip()
        if line.startswith("User:"):
            user_msgs.append(line[5:].strip())
        elif line.startswith("AI:"):
            ai_msgs.append(line[3:].strip())

    return user_msgs, ai_msgs

# ===== 2. Message Statistics =====
def count_messages(user_msgs, ai_msgs):
    return {
        "total": len(user_msgs) + len(ai_msgs),
        "user": len(user_msgs),
        "ai": len(ai_msgs)
    }

# ===== 3. Keyword Analysis with TF-IDF =====
def extract_keywords(messages, top_n=5):
    combined_text = " ".join(messages)
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform([combined_text])
    scores = tfidf_matrix.toarray()[0]
    feature_names = vectorizer.get_feature_names_out()
    sorted_keywords = sorted(zip(feature_names, scores), key=lambda x: x[1], reverse=True)
    return [word for word, _ in sorted_keywords[:top_n]]

# ===== 4. Generate Summary =====
def generate_summary(file_path):
    user_msgs, ai_msgs = read_chat_file(file_path)
    all_msgs = user_msgs + ai_msgs
    stats = count_messages(user_msgs, ai_msgs)
    keywords = extract_keywords(all_msgs)

    print("\n📄 Summary Report")
    print(f"- Total messages: {stats['total']}")
    print(f"- User messages: {stats['user']}, AI messages: {stats['ai']}")
    print(f"- Most common keywords: {', '.join(keywords)}")

# ===== 5. Run Summary on Specific File =====
if __name__ == "__main__":
    chat_file_path = r"F:\my_AI_Projects\JobAssesments\QtecSolutionLimited\AI_ChatLog_Summarizer\sampleChatLog\chat.txt"
    if os.path.exists(chat_file_path):
        generate_summary(chat_file_path)
    else:
        print(f"File not found: {chat_file_path}")
