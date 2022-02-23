import os
from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys


def send_pic(chat, pic):
    """
    
    Doesn't work well with emojis
    """

    options = webdriver.ChromeOptions()
    options.add_argument('--user-data-dir=/home/guigo/Documentos/proj_dir/06-motionSnitcher/session')
    options.add_argument('--profile-directory=Default')

    time.sleep(3)

    browser = webdriver.Chrome(options=options)
    browser.get(f'https://web.whatsapp.com/')
    time.sleep(13)

    for pic in pics:
        search_box = browser.find_element(By.CLASS_NAME, "_13NKt")
        search_box.send_keys(chat)
        search_box.send_keys(Keys.ENTER)

        opt_but = browser.find_element(By.CLASS_NAME, '_2jitM')
        opt_but.click()
        pic_but = browser.find_element(By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
        pic_but.send_keys(pic)
        time.sleep(4)
        send_but = browser.find_element(By.CLASS_NAME, '_1w1m1')
        send_but.click()
        time.sleep(6)

    time.sleep(10)
    browser.close()


pics=[
    "/home/guigo/Documentos/proj_dir/06-motionSnitcher/gcp.png",
    "/home/guigo/Documentos/proj_dir/06-motionSnitcher/scoef_ic_gwr.png"
]

send_pic(chat = "..", pic = pics)
