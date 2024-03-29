#! python3

# browser.py - Handles running a selenium browser

from pyperclip import paste
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from automating_anki.listener import listenForCopy, listenForCopyAndNext, listenForNext, getCopyOccured, setCopyOccured
from urllib.request import urlretrieve
# from pyautogui import click, press

WORD_REFERENCE = 'https://www.wordreference.com/deen/'
GOOGLE_TRANSLATE = 'https://translate.google.ca/#view=home&op=translate&sl=de&tl=en&text='

def getDriver():
    capa = DesiredCapabilities.FIREFOX
    capa["pageLoadStrategy"] = "none"
    driver = webdriver.Firefox(desired_capabilities=capa)
    driver.maximize_window()
    return(driver)

def loadWordReference(driver, word):
    wordReferenceSite = WORD_REFERENCE + word
    wait = WebDriverWait(driver, 5)
    driver.get(wordReferenceSite)
    wait.until(EC.presence_of_element_located((By.ID, 'articleWRD')))
    driver.execute_script("window.stop();")
    listenForNext()

def saveImage(image_link, filename):
    urlretrieve(image_link, filename)
    return 1

def getImage(driver, sentence, filename):
    imagesSite = 'https://www.google.com/search?q=' + sentence + '&sout=1&hl=en&tbm=isch&oq=v&gs_l=img.3..35i39l2j0l8.4861.6646.0.7238.1.1.0.0.0.0.90.90.1.1.0....0...1ac.1.34.img..0.1.90.SKWUGDKJMsg'
    driver.get(imagesSite)
    # print("Press 'enter' when mouse is hovering over the image.\n")
    print("Copy image filepath.\n")
    result = None
    while result is None:
        try:
            listenForNext()
            image_link = paste()
            result = saveImage(image_link, filename)
        except:
             pass


def getTranslation(driver, sentence):
    googleTranslateSite = GOOGLE_TRANSLATE + sentence
    driver.get(googleTranslateSite)
    print("Read translation, press 'enter' to continue.\n")
    listenForNext()

def getSentence(driver, sites):
    object = "an example sentence"
    sentence = copyFromSite(driver, sites, object)
    return(sentence)

def getDefinition(driver, sites):
    object = "a definition"
    definition = copyFromSite(driver, sites, object)
    return(definition)

def copyFromSite(driver, sites, object):
    print("Copy ", object)
    print("Or press the 'enter' key for the next site.")
    for site in sites:
        if (not getCopyOccured()):
            driver.get(site)
            listenForCopyAndNext()
        else:
            break
    setCopyOccured(False)
    clipboard = paste()
    return(clipboard)
