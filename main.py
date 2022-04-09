from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, UnexpectedAlertPresentException
from selenium.webdriver.common.by import By
import time
import PIL.Image as i
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "tesseract-ocr/tesseract.exe "
path = 'msedgedriver.exe'
driver = webdriver.Edge(path)
# 清除浏览器cookies
'''cookies = driver.get_cookies()
print(f"main: cookies = {cookies}")
driver.delete_all_cookies()'''
# for it in range(0, 10):
# for i in range(0, 10):
it = 0
while 1:
    try:
        driver.get('http://smst.hhu.edu.cn/login.aspx')

        user = driver.find_element(By.ID, 'userbh')
        user.send_keys('1862410235')
        passwd = driver.find_element(By.ID, 'pas1s')
        passwd.send_keys('112233abcD')
        cap = driver.find_element(By.ID, 'Image1')
        # cap.screenshot('cap/cap_' + str(i) + '.png')
        cap.screenshot('run_cap/cap_' + str(it) + '.png')
        time.sleep(2)
        # raw = i.open('cap/cap_' + str(i) + '.png')
        raw = i.open('run_cap/cap_' + str(it) + '.png')

        # num = pytesseract.image_to_string(raw, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
        num = pytesseract.image_to_string(raw, lang='num')

        print(num)
        cap_in = driver.find_element(By.ID, 'vcode')
        cap_in.send_keys(num)
        cap_in.submit()

        time.sleep(6)
        driver.quit()
        break

    except StaleElementReferenceException:
        it = it + 1
        break

    except UnexpectedAlertPresentException:
        it = it + 1
        print("验证码错误")
        continue

mainWindow = driver.current_window_handle
driver.switch_to_window(mainWindow)
driver.get('http://smst.hhu.edu.cn/txxm/default.aspx?dfldm=02')

mainWindow = driver.current_window_handle
driver.switch_to_window(mainWindow)

f = driver.find_element_by_xpath(
    '/html/body/form/table/tbody/tr/td[2]/table[3]/tbody/tr/td/table/tbody/tr[2]/td[1]/span/div/div/a[1]')
f.click()

driver.switch_to_frame('r_3_3')
send = driver.find_element_by_xpath('/html/body/form/div/table/tbody/tr/td/table[3]/tbody/tr[1]/td/input[2]')
send.click()
print('打卡成功！')
time.sleep(2)
driver.quit()
