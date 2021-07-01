#import secrets
from secrets import user, passwrd, driver
#Importing packages
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




import pandas as pd
f = open('problems.txt', 'a')
driver = webdriver.Chrome(driver)

driver.get('https://www.moonboard.com')
driver.find_element_by_id("loginDropdown").click()


username=driver.find_element_by_id("Login_Username")

password = driver.find_element_by_id("Login_Password")


username.send_keys(user)

password.send_keys(passwrd)

driver.find_element_by_id("navlogin").click()

driver.get('https://www.moonboard.com/Account/Index')
users = [u.get_attribute('data-uid') for u in driver.find_elements_by_xpath('//table/tbody/tr')]



driver.get('https://www.moonboard.com/Account/Profile/'+users[0])

# problems
driver.get('https://www.moonboard.com/Account/Profile/a0275379-a251-47ab-8904-4b3c5ea1710a')
#driver.get('https://www.moonboard.com/Account/Profile/987158ee-6675-4261-aa1e-94f78b2f651a')
def get_problems():
    """Gets created problems"""
    # get last page of user's problems
    last_page = driver.find_elements_by_xpath("//*[@class='k-link k-pager-nav k-pager-last']" )

    lastpage= int(last_page[-1].get_attribute('data-page'))
    print('this last page ' + str(lastpage))
    n=0

    while n < int(lastpage)+1:

        #prob_table = driver.find_elements_by_id("grdUserProblems")[0].find_elements_by_xpath("//a[starts-with(@href, '/Problems')]")
        driver.implicitly_wait(5)

        wait = WebDriverWait(driver, 20)


        prob_table = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='grdUserProblems']/div[2]/table/tbody")))
        z = True
        while z == True:
            try:
                problems = [p.get_attribute('href') for p in prob_table.find_elements_by_tag_name('a')]
                z = False
            except:
                prob_table = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='grdUserProblems']/div[2]/table/tbody")))

        buttons=driver.find_elements_by_xpath('//*[@class="k-icon k-i-arrow-60-right"]' )

        print('this is n ' + str(n))
        for problem in range(len(problems)):
            f.write(problems.pop()+'\n')
        prob_table2 = driver.find_element_by_xpath("//*[@id='grdUserProblems']/div[2]/table/tbody")


        buttons[1].click()
        n +=1





# select by visible text
f = open('problems.txt', 'w')
moonboard = 19
for moonboard in moonboards:
    select = Select(driver.find_element_by_id('Holdsetup'))
    select.select_by_value(str(moonboard))
    try:
        get_problems()
    except:
        pass

    if moonboard == 19 ^ moonboard == 15:
        driver.find_element_by_id('divConfig').find_elements_by_xpath('//*[@class="btnConfig"]')[0].click()
        try:
            get_problems()
        except:
            pass
f.close()





rows = table_id.find_elements(By.TAG_NAME, "tr")
rows
rows[1].text



driver.find_element_by_xpath("//select[id='fruits']").click()


'Go to the next page'
buttons=driver.find_elements_by_xpath('//*[@class="k-icon k-i-arrow-60-right"]' )
buttons[1].click()

last_button=driver.find_elements_by_xpath('//*[@class="k-link k-pager-nav k-pager-last"]' )
last_button[1].get_attribute('dat
a-page')



users2=driver.find_elements_by_xpath('//table/tbody/tr/td')
users2[0].text

a
users[0].data-uid
elems[0].getText()


driver.get('https://www.moonboard.com/Account/Profile/'+element)
users[0]

temp=driver.find_elements_by_xpath('//tr/..')
temp[1].text

temp[2].get_attribute('href')
temp[0].link
for t in temp:
    print(t)

    t.getAttribute()
element = users[1]
element
help(users[0])
elems = driver.find_elements_by_xpath("//a[@href]")
users[0].tag_name
element
element
help(users[1])
