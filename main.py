from datetime import datetime
from flask import Flask, request, render_template

# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")

application = Flask(__name__)


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

    add_message(sender, text)
    return 'OK'

@application.route("/chat")
def display_chat():
    return render_template("form.html")

all_messages = [
    {
        'sender': 'Dima',
        'text': 'Привет друзья!',
        'time': '14:58'
    }, {
        'sender': 'Vanya',
        'text': 'Я тоже тут!',
        'time': '15:00',
    }, {
        'sender': 'Denis',
        'text': 'Привет Дима!',
        'time': '15:08'
    }
]


def print_message(mess):
    print(f"[{mess['sender']}] / {mess['time']} >>>>> {mess['text']}")


def add_message(sender, text):
    new_message = {
        'sender': sender,
        'text': text,
        'time': datetime.now().strftime("%H:%M:%S")
    }
    all_messages.append(new_message)


# while True:
#     for message in all_messages:
#         print_message(message)
#
#     add_message(input(), input())

application.run()
