"""
pip install selenium
"""

from selenium import webdriver # Responsável por controlar o navegador
from selenium.webdriver.common.keys import Keys # Simula digitação de teclas
from selenium.webdriver.common.by import By # Localiza elementos na página web

driver = webdriver.Chrome() # Iniciar o navegador Chrome

driver.get("https://www.google.com") # Leva o navegador para o site espeficiado

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("SUAP") # Simulação do que vai ser digitado na barra de busca
search_box.send_keys(Keys.RETURN) # Simulação da barra enter para finalizar a pesquisa

driver.implicitly_wait(10) # Espera para a página carregar
titles = driver.find_elements(By.TAG_NAME, "h3") # Retorna todos os elementos que usam H3 no HTML

# Loop para passar cada um dos elementos encontrados
for title in titles:
    print(title.text)

driver.quit() # Finalizar
