import telebot
import AI
import test1

bot = telebot.TeleBot('7383394195:AAHG6dGM-qNGolAQS3YBFqcR5Iq4T2L-Syk')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Здравствуйте! Отправьте мне изображение и мои модели tf-gpu и yolo8 скажут вам что они видят на изображении!')

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    photo = message.photo[-1]
    file_info = bot.get_file(photo.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    save_path = 'photo.jpg'
    with open(save_path, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.reply_to(message, 'Замечательно! Пожалуйста, немного подождите.')
    bot.send_message(message.chat.id, AI.Detection())

    test1.Detection()
    bot.reply_to(message, 'Ответ yolo.')
    file = open('output.jpg', 'rb')
    bot.send_photo(message.chat.id, file)

bot.polling()