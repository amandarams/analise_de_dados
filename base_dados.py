#
import os
import pandas as pd
from fpdf import FPDF

# Carregar a base de dados a partir de um arquivo CSV local
arquivo_csv = r"C:\Users\Amanda\Desktop\analise-de-dados-covid\base_de_dados.csv"
data = pd.read_csv(arquivo_csv, low_memory=False)

variaveis = data.columns
tipos_variaveis = data.dtypes
info_variaveis = pd.DataFrame({'Variável': variaveis, 'Tipo': tipos_variaveis})

info_variaveis.to_csv('info_variaveis.csv', index=False)

descricao_variaveis = data.describe().T

# Salvando análise de dados no caminho informado abaixo
descricao_variaveis.to_csv(r'C:\Users\Amanda\Desktop\analise-de-dados-covid\analise_dados.csv')

print("Arquivos CSV e PDF foram criados com sucesso.")


