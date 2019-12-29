from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://cran.enlitic.work/login")

username = input('Enter username : ')
password = input('Enter password : ')

driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/div[2]/form/div[1]/div[1]/input').send_keys(username)

driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/div[2]/form/div[1]/div[2]/input').send_keys(password)

loginBtn = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/div[2]/form/div[2]/button')

loginBtn.send_keys(Keys.RETURN)

reportNum = driver.find_element_by_xpath('/html/body/div/div[1]/div/div[4]/form/div[1]/div[1]/select')
rNum = input ('20, 50, 100, 200 : ') #If you want 10, jsut go click it with your finger >:p
reportNum.click()
reportNum.send_keys(rNum)

reportProject = driver.find_element_by_xpath('/html/body/div/div[1]/div/div[4]/form/div[1]/div[2]/select')
rPro = int(input ('Full Body -- Chest == 1 \nFull Body -- Spine == 2\nChoose menu : '))

if rPro is 1:
    driver.find_element_by_xpath('/html/body/div/div[1]/div/div[4]/form/div[1]/div[2]/select/option[10]').click()
elif rPro is 2:
    driver.find_element_by_xpath('/html/body/div/div[1]/div/div[4]/form/div[1]/div[2]/select/option[13]').click()

driver.find_element_by_xpath('/html/body/div/div[1]/div/div[4]/form/div[3]/div/button').send_keys(Keys.RETURN)


while True: 
    rValue = int(input('Select from 0 to 3 : '))
    driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div/div[1]/div[2]/div/input').__setattr__("value", rValue)
    driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div/div[4]/button').send_keys(Keys.RETURN)
