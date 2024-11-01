# Projeto de Automação de Preços

## Descrição
Este projeto utiliza Python e Selenium para buscar e comparar preços de um produto, atualmente configurado para o "iPhone 15", nos sites da Amazon e Magazine Luiza. A automação realiza a busca, captura os preços e armazena o resultado em um arquivo de log.

## Requisitos
- **Python** 3.7 ou superior
- **Selenium** (para automação)
- **GeckoDriver** (para Firefox) ou **ChromeDriver** (para Chrome)

## Configuração do Ambiente

### 1. Instalar Dependências
Instale as dependências usando o comando:
```bash
pip install -r requirements.txt
```

### 3. Alterar entre Firefox e Chrome
Para trocar de Firefox para Chrome, faça as seguintes alterações no código:

1. Substitua `webdriver.Firefox()` por `webdriver.Chrome()` na função de configuração do driver.
   ```python
   driver = webdriver.Chrome()
   ```

## Como Executar
1. No terminal ou prompt de comando, navegue até a pasta do projeto.
2. Execute o script com:
   ```bash
   python preco_comparador.py
   ```

O script buscará o preço do produto nos sites e exibirá o resultado no terminal com uma comparação e com o tempo total de execução.

## Logs
Durante a execução, o script cria automaticamente um arquivo de log (`automation.log`). Este arquivo armazena informações sobre os preços encontrados, a comparação, o tempo de execução e qualquer erro ocorrido durante o processo de busca.

## Estrutura do Projeto

- **`preco_comparador.py`**: Script principal que realiza a busca e comparação de preços.
- **`automation.log`**: Arquivo de log gerado automaticamente contendo informações de execução.
- **`requirements.txt`**: Arquivo contendo as dependências do projeto para facil instalação.