from sentence_transformers import SentenceTransformer
from cs50 import SQL

db = SQL("sqlite:///Atmosphere_glossary.db")

model = SentenceTransformer("bert-base-nli-mean-tokens")

q_data = db.execute("SELECT question FROM Q_A;")

q_sentence = []
for row in q_data:
    q_sentence.append(row["question"])

sentence_vecs = model.encode(q_sentence)

### insert sentence vector into sql ###
for i in range(len(q_sentence)):
    db.execute("INSERT INTO sentence_vector(query, vector) VALUES (?, ?)",
                q_sentence[i], str(sentence_vecs[i]))