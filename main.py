from flask import Flask, request, render_template,flash,redirect
import os
import requests
import telebot


app = Flask(__name__)


@app.route('/', methods=['GET' , 'POST'])
def home():
    if request.method == "POST":
        if request.form.get("pass")=='123':
            #one input file
            file = request.files['file']
            path =(f'data/{file.filename}')
            file.save(path)

            #two input caption
            caption = request.form.get('caption')

            bot_token = '5271798021:AAE-gNrHHllFUuRN1i5RkDoQnDCCIFy8kUs'
            user_id = '861577423'
            bot = telebot.TeleBot(bot_token)

            
            doc = open(path,'rb')
            bot.send_document(user_id,document=doc,caption=caption)
            bot.stop_bot()
            doc.close()
            os.remove(path)
            #return('successfully Send Data')
            return redirect('/')
        else:
            return('Bad Password')
            
    return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True)
