from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import serial

ser = serial.Serial('COM3', 9600)

input_password = ''
password = ''


while True:
    cc=str(ser.readline())

    input_password = cc[2:][:-5].split("/")[0]
    light_sensor = cc[2:][:-5].split("/")[1]

    password += input_password[-1]

    if password[-1] == '*':
        password = password[:len(password)-2]    


    elif password[-1] == '#' and int(light_sensor) >= 300:
        password = password[:len(password)-1]
                
        # Initiate the browser
        email = 'dvic@gmail.com'
        browser  = webdriver.Chrome(ChromeDriverManager().install())

        browser.get('https://lg-double.netlify.app')

        time.sleep(2)

        browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]/form/div[1]/div/input').send_keys(email)
        browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]/form/div[2]/div/input').send_keys(password)
        browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]/form/button').click()
        time.sleep(50) 

    elif password[-1] == '#' and int(light_sensor) < 300:

        print(cc[2:][:-5])



    print(password, light_sensor)

