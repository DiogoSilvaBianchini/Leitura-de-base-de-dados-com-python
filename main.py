# Importação
from os import path
import pandas as pd;
from twilio.rest import Client
from pathlib import Path
# Authenticação
account_sid = "AC4b6814662ce7f1e0788d25f91d08c5de"
auth_token  = "0d4a97a553932759c7f0ce9b7e6d88ad"
client = Client(account_sid, auth_token)

# Montagem da lógica
tabelas = ['janeiro','fevereiro','março','abril','maio','junho']
filePath = './base/'
cont = 0
valor = 28546

# Montagem da leitura da base de dados em Excel
for mes in tabelas:
    tabela_de_vendas = pd.read_excel(Path(f'{filePath}{mes}.xlsx'))
    # Condição que aborda a coluna 'Vendas' da base de dados, e compara com o valor
    if(tabela_de_vendas['Vendas'] > valor).any():
        # Variavel que armazena o vendedor e o quanto ele vendeu
        vendedor = tabela_de_vendas.loc[tabela_de_vendas['Vendas'] > valor, 'Vendedor'].values[0]
        venda = tabela_de_vendas.loc[tabela_de_vendas['Vendas'] > valor, 'Vendas'].values[0]
        
        # Envio da msg por SMS, onde to recebe o numero alvo e from_ recebe o seu numero
        message = client.messages.create(
            to="+5515997516834", 
            from_="+19154659571",
            body=f"No mês de {mes}, O vendedor {vendedor} vendeu {venda}")
        
        # Protocolo de atencimento
        print(message.sid)