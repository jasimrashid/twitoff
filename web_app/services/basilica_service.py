

from basilica import Connection
import os
from dotenv import load_dotenv

API_KEY = os.getenv("BASILICA_API_KEY")

connection = Connection(API_KEY)
print("CONNECTION", type(Connection))


if __name__ == "__main__":
# "4e7b4faa-bd84-9e9d-a8bb-61f546fed095" #TODO use env variable
    sentences = [
        "This is a sentence!",
        "This is a similar sentence!",
        "I don't think this sentence is very similar at all...",
    ]

    embeddings = list(connection.embed_sentences(sentences))

    embedding = connection.embed_sentence("hello world", model="twitter")
    print(type(embedding))
    print(type(embedding[0]))
    print(len(embedding))


    print(embeddings)
    

# [[0.8556405305862427, ...], ...]