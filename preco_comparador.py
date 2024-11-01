from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time

# Configuração do arquivo de log
logging.basicConfig(filename="automation.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Função para configurar o driver
def configurar_driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    return driver

# Função para buscar o preço na Amazon
def buscar_preco_amazon(driver, produto):
    url = f"https://www.amazon.com.br/s?k={produto}"
    driver.get(url)
    try:
        # Aguardando o elemento que contém a parte inteira do preço
        price_elements = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".a-price-whole"))
        )

        # Extraindo o preço da primeira aparição
        if price_elements:
            preco_inteiro = price_elements[0].text.replace('.', '').replace(',', '.')  # Formatação do preço
            
            logging.info(f"Preço encontrado na Amazon: R$ {preco_inteiro}")
            return float(preco_inteiro)
        else:
            logging.warning("Nenhum preço encontrado na Amazon.")
            return None
    except Exception as e:
        logging.error(f"Erro ao buscar preço na Amazon: {e}")
        return None

# Função para buscar o preço na Magazine Luiza
def buscar_preco_magalu(driver, produto):
    url = f"https://www.magazineluiza.com.br/busca/{produto}"
    driver.get(url)
    try:
        # Ajustando o seletor para capturar o preço corretamente
        price_elements = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[data-testid='price-value']"))
        )

        # Extraindo o preço da primeira aparição
        if price_elements:
            preco_texto = price_elements[0].text
            
            # Remover "ou " e formatar o preço
            preco = preco_texto.replace('R$', '').replace('ou', '').strip().replace('.', '').replace(',', '.')
            
            logging.info(f"Preço encontrado na Magazine Luiza: R$ {preco}")
            return float(preco)
        else:
            logging.warning("Nenhum preço encontrado na Magazine Luiza.")
            return None
    except Exception as e:
        logging.error(f"Erro ao buscar preço na Magazine Luiza: {e}")
        return None

# Função principal para iniciar a busca em ambos os sites
def comparar_precos(produto):
    driver = configurar_driver()
    start_time = time.time()  # Inicia o temporizador
    try:
        preco_amazon = buscar_preco_amazon(driver, produto)
        preco_magalu = buscar_preco_magalu(driver, produto)
        
        # Exibir preços ao usuário e comparar
        if preco_amazon is not None and preco_magalu is not None:
            print(f"Preço na Amazon: R$ {preco_amazon:.2f}")
            print(f"Preço na Magazine Luiza: R$ {preco_magalu:.2f}")

            menor_preco = min(preco_amazon, preco_magalu)
            if menor_preco == preco_amazon:
                print("O menor preço é na Amazon.")
            else:
                print("O menor preço é na Magazine Luiza.")
            
            logging.info("Comparação concluída com sucesso")
        else:
            logging.warning("Não foi possível obter o preço de um dos sites")
    
    finally:
        # Fecha o driver
        driver.quit()
        tempo_execucao = time.time() - start_time  # Calcula o tempo de execução
        logging.info(f"Navegador fechado. Tempo de execução: {tempo_execucao:.2f} segundos.")
        print(f"Tempo total de execução: {tempo_execucao:.2f} segundos.")

# Executa a função principal
if __name__ == "__main__":
    produto = "iPhone 15"
    comparar_precos(produto)