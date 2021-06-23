from selenium import webdriver
from time import sleep
driver = webdriver.Chrome(executable_path="./chromedriver")
driver.get("https://10fastfingers.com/advanced-typing-test/english")
sleep(5)
word_list = driver.execute_script("return document.getElementById('wordlist').innerHTML")
words = word_list.split("|")
for i in range(len(words)):
    driver.find_element_by_id("inputfield").send_keys(words[i] + " ")
    sleep(0.05)