from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import pyautogui as pag
from bs4 import BeautifulSoup
import requests
import time

def login(driver):
  
    # Getting the login element
    username = driver.find_element_by_id("username") 
  
    # Sending the keys for username      
    username.send_keys("7490876006")
  
    # Getting the password element                                  
    password = driver.find_element_by_id("password")
  
    # Sending the keys for password    
    password.send_keys("@HP1001hp@")      
  
    # Getting the tag for submit button                     
    driver.find_element_by_class_name("login__form_action_container").click()         
    goto_network(driver)
    
def goto_network(driver):
    driver.get("https://www.linkedin.com/mynetwork/invite-connect/connections/")
    time.sleep(3)
    for i in range(1,10):
        user = '/html/body/div[7]/div[3]/div/div/div/div/div/div/div/main/div/div/section/ul/li[{0}]/div[2]/div[1]/button'.format(i)
        driver.find_element_by_xpath(user).click()
        time.sleep(3)
        text = driver.find_element_by_xpath('/html/body/div[7]/aside/div[2]/div[1]/form/div[2]/div/div[1]/div[1]')
        text.send_keys('Automation testing')
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[7]/aside/div[2]/div[1]/form/footer/div[2]/div[1]/button').click()
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[7]/aside/div[2]/header/section[2]/button[2]').click()
        time.sleep(3)



    #content = driver.page_source
    #soup = BeautifulSoup(content,'html.parser')
    #for tag in soup.find_all("a",href=True,attrs={"class":"ember-view mn-connection-card__picture"}):
    #    print(tag['href'])
    
    
   
def main():
  
    url = "https://www.linkedin.com/login"  
  
    driver = webdriver.Chrome('C:\\Program Files\\Web Driver\\chromedriver.exe')     
    driver.get(url)

    login(driver)
  
# Driver's code 
if __name__ == "__main__":
    main()
