from flask import Flask, Blueprint, request
from api.bot_actions import BotInstance

app = Flask(__name__)

api = Blueprint('api', __name__, url_prefix='/api')

@app.route('/api/test')
def hello_world():
    return 'Hello, World!'

@api.route('/bot/create/', methods=['POST'])
def create_bot():
    bot_name = request.form.get('botName')
    bot_description = request.form.get('botDescription')
    file = request.files.get('file')

    if not bot_name:
        return {"message": "Bot name is required"}, 400
    
    if not bot_description:
        return {"message": "Bot description is required"}, 400
    
    if not file:
        return {"message": "Info file is required"}, 400
    
    NewBot = BotInstance(bot_name, bot_description)
    NewBot.save_to_db()

    return {"message": "Bot created successfully!"}

app.register_blueprint(api)