from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

all_messege = [
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

def print_messege(mess):
    print(f"[{mess['sender']}] / {mess['time']} >>>>> {mess['text']}")


def add_messege(sender, text):
    new_message = {
        'sender': sender,
        'text': text,
        'time': datetime.now().strftime("%H:%M:%S")
    }
    all_messege.append(new_message)

while True:
    for messege in all_messege:
        print_messege(messege)

    add_messege(input(), input())


