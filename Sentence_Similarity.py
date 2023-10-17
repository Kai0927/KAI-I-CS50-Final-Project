from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os
from cs50 import SQL

def Answer_AI(input_q):

    def Convert(string):
        li_new = []
        li = list(string.strip("]").strip("[").split(" "))
        for i in li:
            if (i != ""):
                li_new.append(float(i))
        li_new = np.asarray(li_new)
        #print(li_new.shape)
        return li_new

    db = SQL("sqlite:///Atmosphere_glossary.db")

    model = SentenceTransformer("bert-base-nli-mean-tokens")

    input_q = input_q
    sentence_input_vecs = model.encode(input_q)

    ### Import data vector from sql ###
    sentence_vecs_db = db.execute("SELECT vector FROM sentence_vector;")

    sentence_vecs = []
    for row in sentence_vecs_db:
        sentence_vecs.append(Convert(row["vector"]))

    similarity = cosine_similarity(
        [sentence_input_vecs],
        sentence_vecs
    )

    ### find the most similar question ###
    max_similar = np.max(similarity)
    max_index = np.where(similarity == max_similar)

    print(max_index)

    ### Answer from AI ###
    answer_db_AI = db.execute("SELECT answer FROM Q_A;")
    print(answer_db_AI[max_index[1][0]]["answer"])

    return answer_db_AI[max_index[1][0]]["answer"]