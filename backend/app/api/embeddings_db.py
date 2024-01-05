from pymongo import MongoClient, collection
from typing import List, Dict

mongodb_connection_string = ""

class embeddings_db:
    def __init__(self, mongodb_connection_string: str):
        client = MongoClient(mongodb_connection_string)
        self.db = client["PRISM-tiw"]

    def execute_search_query(self, embeddings: List[float], team_id: str, custom_k_int: int = 3) -> List[Dict]:
        pipeline = self.make_pipeline(embeddings, custom_k_int)
        collection = self.get_team_collection(team_id)
        # Mongo's aggregate is a blocking operation
        mongodb_results = list(collection.aggregate(pipeline))
        return mongodb_results

    def get_team_collection(self, team_collection_id: str) -> collection:
        return self.db[team_collection_id]

    def make_pipeline(self, embeddings: List[float], k: int):
        return [
            {
                "$search": {
                    "cosmosSearch": {
                        "vector": embeddings,
                        "path": "Embeddings",
                        "k": k
                    },
                    "returnStoredSource": True
                }
            }
        ]

vectorDb = embeddings_db(mongodb_connection_string)

# Sample data for testing
sample_embeddings = [0.1, 0.2, 0.3, ...]  # Fill with your placeholder data
sample_team_id = "64b326adae8"

# Call the search function and print results
results = vectorDb.execute_search_query(sample_embeddings, sample_team_id, 3)
for result in results:
    print(result)