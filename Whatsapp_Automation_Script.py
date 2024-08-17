import time
from selenium import webdriver
try:
    driver = webdriver.Chrome()
    driver.get('https://web.whatsapp.com/')
    name = str(input("Enter the name of user or group: "))
    msg = input("Enter your message: ")
    count = int(input("Enter the Count: "))
    input("Enter anything after QR Code")
    user = driver.find_element_by_xpath(f'//span[@title="{name}"]')
    user.click()
    msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]')
    for i in range(count):
        print(i)
        msg_box.send_keys(msg)
        # time.sleep(10)
        button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[2]/button')
        # time.sleep(5)
        button.click()

except Exception as e:
    print(e)