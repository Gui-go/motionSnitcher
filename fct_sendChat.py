import os
from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys


def send_chat(chat, text):
    """
    
    Doesn't work well with emojis
    """

    options = webdriver.ChromeOptions()
    options.add_argument('--user-data-dir=/home/guigo/Documentos/proj_dir/06-motionSnitcher/session')
    options.add_argument('--profile-directory=Default')

    time.sleep(3)

    browser = webdriver.Chrome(options=options)
    browser.get(f'https://web.whatsapp.com/')
    time.sleep(8)

    search_box = browser.find_element(By.CLASS_NAME, "_13NKt")
    search_box.send_keys(chat)
    search_box.send_keys(Keys.ENTER)

    txt_box = browser.find_element(By.CLASS_NAME, "_2cYbV").find_element(By.CLASS_NAME, "_13NKt")
    txt_box.send_keys(text)
    browser.find_element(By.CLASS_NAME, "_4sWnG").click()

    time.sleep(16)
    browser.close()


send_chat(chat = "..", text = "Bip bot")
