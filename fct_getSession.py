from selenium import webdriver
import time


def get_session(sec=10):
    """
    Function to get session data and pass QR session by
    """
    options = webdriver.ChromeOptions()
    options.add_argument('--user-data-dir=/home/guigo/Documentos/proj_dir/06-motionSnitcher/session')
    # options.add_argument('--profile-directory=Default')
    browser = webdriver.Chrome(options=options)
    browser.get('https://web.whatsapp.com/')
    time.sleep(sec)
    browser.close() # Colocar try except key hit

# get_session(sec=10)