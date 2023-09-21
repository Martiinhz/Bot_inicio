import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait #La tardanza del html
from selenium.webdriver.support import expected_conditions#Ayuda hacer la operacion de arriba
from selenium.webdriver.common.by import By#esperar que carge los elemenos bajos una condicion

options = webdriver.ChromeOptions()#todo desacctivado
options.add_argument('--Iniciar-maximizado')
options.add_argument('--desabilitar-extenciones')

driver_path = "C:\chromedriver"

driver = webdriver.Chrome()#para controlar la pagina

driver.get('https://www.riotgames.com/')

time.sleep(1)
element = driver.find_element(By.CSS_SELECTOR, 'a._2I66LI-wCuX47s2um7O7kh riotbar-anonymous-link _3qlG68WiAAf2HCeuzuwHXj riotbar-account-action _1SFUgr_Ul0xq7X3IdHVHrL theme-button'.replace(' ', '.'))
element.click()
time.sleep(1)

element = driver.find_element(By.CSS_SELECTOR, 'button.sc-eDDNvR ehkpbx'.replace(' ', '.'))
element.click()
time.sleep(1)

element = driver.find_element(By.CSS_SELECTOR, 'input.whsOnd zHQkBf'.replace(' ', '.'))
element.send_keys('grandejunior109@gmail.com')
time.sleep(1)

element = driver.find_element(By.CSS_SELECTOR, 'button.VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b'.replace(' ', '.'))
element.click()
time.sleep(3)

element = driver.find_element(By.CSS_SELECTOR, 'input.whsOnd zHQkBf'.replace(' ', '.'))
element.send_keys('1002592469')
time.sleep(1)

element = driver.find_element(By.CSS_SELECTOR, 'button.VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b'.replace(' ', '.'))
element.click()

time.sleep(120)