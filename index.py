from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://cran.enlitic.work/login")

username = input('Enter username : ')
password = input('Enter password : ')

driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/div[2]/form/div[1]/div[1]/input').send_keys(username)

driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/div[2]/form/div[1]/div[2]/input').send_keys(password)

loginBtn = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/div[2]/form/div[2]/button')

loginBtn.send_keys(Keys.RETURN)

while True:
    reportNum = driver.find_element_by_xpath('/html/body/div/div[1]/div/div[4]/form/div[1]/div[1]/select')
    rNum = input ('10, 20, 50, 100, 200 : ')
    reportNum.click()
    reportNum.send_keys(rNum)

    reportProject = driver.find_element_by_xpath('/html/body/div/div[1]/div/div[4]/form/div[1]/div[2]/select')
    rPro = int(input ('Full Body -- Chest == 1 \nFull Body -- Spine == 2\nChoose menu : '))

    if rPro is 1:
        driver.find_element_by_xpath('/html/body/div/div[1]/div/div[4]/form/div[1]/div[2]/select/option[10]').click()
    elif rPro is 2:
        driver.find_element_by_xpath('/html/body/div/div[1]/div/div[4]/form/div[1]/div[2]/select/option[13]').click()

    driver.find_element_by_xpath('/html/body/div/div[1]/div/div[4]/form/div[3]/div/button').send_keys(Keys.RETURN)
    
    rValue = int(input('Select from 1 to 4 : '))

    slider = driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div/div[1]/div[2]/div/input')
    move = ActionChains(driver)
    
    temp = 0

    while True:             
        if rValue is 1:
            temp = int(25)
        elif rValue is 2:
            temp = int(50)
        elif rValue is 3: 
            temp = int(75)
        elif rValue is 4:
            temp = int(100)
        else:
            print('Please select from 1 to 4')
            pass

        move.click_and_hold(slider).move_by_offset(temp, 3).release().perform()

        driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div/div[4]/button').send_keys(Keys.RETURN)