from datetime import datetime
from flask import Flask, request, render_template
import json

# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")

application = Flask(__name__)  # Создаём Flask-приложение
DB_FILE = "./data/db.json"


# Функция чтения сообщений из файла
def load_mesages():
    with open(DB_FILE, "r") as json_file:
        data = json.load(json_file)
    return data["messages"]


all_messages = load_mesages()  # Список всех сообщений


# Фукция сохранения сообщений в файл
def save_messages():
    data = {
        "messages": all_messages
    }
    with open(DB_FILE, "w") as json_file:  # Открываем файл для записи
        # json_file = open(DB_FILE, "w")
        json.dump(data, json_file)


@application.route('/')
def index_page():
    return 'Hello, welcome to Chat'


@application.route("/get_messages")
def get_messages():
    return {"messages": all_messages}


@application.route("/send_message")
def send_message():
    sender = request.args["name"]
    text = request.args["text"]
    if len(sender) > 16 or not sender or not text:
        send_message()

    add_message(sender, text)

    save_messages()
    return 'OK'


@application.route("/chat")
def display_chat():
    # Показываем файл из папки templates
    return render_template("form.html")


def print_message(mess):
    print(f"[{mess['sender']}] / {mess['time']} >>>>> {mess['text']}")


def add_message(sender, text):
    new_message = {
        'sender': sender,
        'text': text,
        'time': datetime.now().strftime("%H:%M")
    }

    all_messages.append(new_message)


application.run()
