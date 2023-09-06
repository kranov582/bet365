from seleniumbase import Driver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from a_selenium2df import get_df
from PrettyColorPrinter import add_printer

add_printer(1)
driver = Driver(uc=True)
driver.get("https://www.bet365.com/bpa?affiliate=365_02495779&gclid=Cj0KCQjwgNanBhDUARIsAAeIcAsJWb6uKuMKI0Vncng7NfW_a2sl0OKK7BL9MWrhApMfv3oNhi6OAKsaAmA6EALw_wcB#/IP/B1")
df = pd.DataFrame()

while df.empty:
    df = get_df(
        driver,
        By,
        WebDriverWait,
        expected_conditions,
        queryselector="*",
        with_methods=True,
    )
df.loc[df.aa_textContent.str.contains("^Aceitar$", regex=True, na=False)].iloc[
    0
].se_click()


dfteams = df.loc[(df['aa_classList'].str.contains("ovm-Competition ovm-Competition-open", na=False))]

print(dfteams)

lista = list(dfteams['aa_innerText'])
lista_nova = []

df.to_excel('dados.xlsx', engine='xlsxwriter')
dfteams.to_excel('dados_teams.xlsx', engine='xlsxwriter')

for x in range(len(lista)):
    z = lista[x].splitlines()
    lista_nova.append(z)

dados_finais = pd.DataFrame(lista_nova, columns = ['Time 1', 'Time 2', 'Tempo de jogo','numero', 'Gols time 1', 'Gols time 2', '1', 'x', '2'])


dados_finais.to_excel('dados_finais.xlsx', engine='xlsxwriter')