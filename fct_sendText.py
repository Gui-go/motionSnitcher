import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

def send_text(dfmensagens="dfmensagens.csv"):
    """
    
    Works fine with emojis 🤖🤖🤖
    """

    # Read messages data
    dfm = pd.read_csv(dfmensagens, sep=";")

    # add options and arguments to avoid QR session pass
    options = webdriver.ChromeOptions()
    options.add_argument('--user-data-dir=/home/guigo/Documentos/proj_dir/06-motionSnitcher/session')
    options.add_argument('--profile-directory=Default')
    time.sleep(2)

    # Initiate browser
    browser = webdriver.Chrome(options=options)
    browser.get(f'https://web.whatsapp.com/')
    
    # Send each message in a loop
    for i, m in enumerate(dfm['message']):
        p = dfm.loc[i, "person"]
        m = dfm.loc[i, "message"]
        n = dfm.loc[i, "number"]
        # print(f"Sending {m} to {p} at {n}")
        browser.get(f'https://web.whatsapp.com/send?phone={n}&text={m}')
        time.sleep(8)

        # Click send button to send text
        browser.find_element(By.CLASS_NAME, "_4sWnG").click()

        time.sleep(10)

    browser.close()


send_text()