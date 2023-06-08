# -- coding: UTF-8 -- 
from PyQt6 import QtWidgets, uic
from threading import *
from gtts import gTTS, lang
import json
app = QtWidgets.QApplication([])
ui = uic.loadUi('main.ui')
langs = lang.tts_langs()
def translate(index):
    if index == 0:
        target_lang = 'English'
    if index == 1:
        target_lang = 'Ukrainian'
    with open('interface.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    ui.Startbtn.setText(data[target_lang]['Convert'])
    ui.inputText.setPlaceholderText(data[target_lang]['Placeholder_text'])
    ui.groupBox.setTitle(data[target_lang]['Text'])
    ui.langtxt.setText(data[target_lang]['Interface language'])
for i in langs.values():
    ui.Language.addItem(i)
def process():
    currentlang = list(langs.keys())[list(langs.values()).index(ui.Language.currentText())]
    text = ui.inputText.toPlainText()
    gTTS(text=text, lang=currentlang, slow=False).save('result.mp3')
    
def thread():
    t1=Thread(target=process)
    t1.start()
ui.Startbtn.pressed.connect(thread)
ui.langbox.activated.connect(lambda: translate(ui.langbox.currentIndex()))
ui.show()
app.exec()