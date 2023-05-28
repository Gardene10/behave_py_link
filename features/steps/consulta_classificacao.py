import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

base_url = 'https://ge.globo.com/'
element_menu = 'burger'
element_brasileirao = '//*[@id="menu-1-brasileirao"]/a/span[1]'
get_primeiro = '//*[@id="classificacao__wrapper"]/article/section[1]/div/table[1]/tbody/tr[1]/td[2]/strong'
@given(u'acesso a pagina inicial do globo esporte')
def step_impl(context):
    """
    Abre a página inicial do Globo Esporte.
    """
    context.web = Chrome()  # Inicializa o driver do Chrome
    context.web.get(base_url)
    time.sleep(2)  # Aguarda 2 segundos

    context.element_menu = context.web.find_element(By.CLASS_NAME, element_menu)
    context.element_menu.click()


@when(u'clico no menu do brasileirao')
def step_impl(context):
    wait = WebDriverWait(context.web, 10)


    context.element_brasileirao = context.web.find_element(By.XPATH, element_brasileirao)
    context.element_brasileirao.click()


@when(u'a classificacao e exibida')
def step_impl(context):
    context.get_primeiro = context.web.find_element(By.XPATH, get_primeiro)



@then(u'devo saber quem e o primeiro colocado')
def step_impl(context):
    primeiro = context.get_primeiro.text
    print(primeiro)

    # Salva o resultado da variável primeiro em um arquivo txt
    file = open("features/results/results.txt", 'r')
    content = file.readlines()
    content.append("\n" + primeiro)
    file = open("features/results/results.txt", 'w')
    file.writelines(content)
