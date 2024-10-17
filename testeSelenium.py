from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui #Biblioteca para simular click (teclado ou mouse)
import time
from selenium.webdriver.common.by import By

#Inicializar o Selenium Web Driver
driver = webdriver.Chrome()


#Fazer a pesquisa para SUAP
driver.get("https://suap.uepb.edu.br/accounts/login/?next=/")


procura_login = driver.find_element(By.NAME, "username")
#name = "username" | id="id_username"
procura_senha = driver.find_element(By.NAME, "password")
#class = "password-input" | name="password" | id="id-password"


#Preencher login e senha
procura_login.send_keys("212080270")
procura_senha.send_keys("16111999")
login_button = driver.find_element(By.CSS_SELECTOR, ".btn")
login_button.click()
time.sleep(5)


#Colocar o link do documento a ser baixado
driver.get("https://suap.uepb.edu.br/edu/declaracaovinculo_pdf/61382/")
time.sleep(5)
#driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + 's')
pyautogui.hotkey('ctrl', 's')
time.sleep(5)
pyautogui.press('enter')
time.sleep(5)
driver.quit()
