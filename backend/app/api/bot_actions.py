from config import MONGODB_URI, MONGODB_DB_NAME
from pymongo import MongoClient
import uuid


# Setting up the MongoDB client using the MONGODB_URI from config.
client = MongoClient(MONGODB_URI)

# Specifying the database and collection we'll be using.
# Assuming the database name is 'chatbot_database' but you can change this as necessary.
db = client[MONGODB_DB_NAME]
bot_collection = db['Bots']

class BotInstance:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def save_to_db(self):
        """
        Save the bot instance to the MongoDB.
        """
        if not self.bot_exists(self.name):
            bot_data = {
                "name": self.name,
                "description": self.description,
                "id": str(uuid.uuid4()),
                "status": 'Publishing'
            }
            bot_collection.insert_one(bot_data)
        else:
            print(f"Bot with name '{self.name}' already exists!")

    @staticmethod
    def bot_exists(name):
        """
        Check if a bot with the given name already exists in the database.
        """
        existing_bot = bot_collection.find_one({"name": name})
        return existing_bot is not None

    @staticmethod
    def get_bot(name):
        """
        Retrieve a bot instance from the database by its name.
        """
        return bot_collection.find_one({"name": name})

    @staticmethod
    def delete_bot(name):
        """
        Delete a bot instance from the database by its name.
        """
        bot_collection.delete_one({"name": name})

    @staticmethod
    def list_all_bots():
        """
        List all registered bots in the database.
        
        Returns:
            List[Dict]: A list of dictionaries where each dictionary contains details of a bot.
        """
        # Using the find() method without any arguments returns all documents in the collection.
        bots = bot_collection.find()
        
        # Convert the cursor object (returned by find()) to a list of dictionaries
        bot_list = [bot for bot in bots]
        
        # Optionally, you can strip out the MongoDB's '_id' from the returned data if you don't want to expose it
        for bot in bot_list:
            bot.pop('_id', None)
        
        return bot_list

    # find bot by id    
    @staticmethod
    def find_by_id(bot_id):
        """
        Find a bot instance from the database by its id.
        """
        return bot_collection.find_one({"id": bot_id})

    if __name__ == "__main__":
        """Main function to find bot by id."""
        bots = find_by_id("28ea87e3-e8e2-4f86-96bd-fe2c3f7e3051")

        print(bots)

