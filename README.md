# analise_de_dados
Analise de Dados da Covid-19 

# Análise de Dados COVID-19

Este repositório contém uma análise detalhada dos dados de COVID-19, utilizando a base de dados pública fornecida pela [Kaggle - COVID-19 Data](https://www.kaggle.com/datasets/vmahawar/coronavirus-covid-19-cases/data). O objetivo deste estudo é entender a evolução dos casos e mortes por COVID-19, bem como o impacto das vacinações e taxas de reprodução.

## Objetivo

O objetivo deste estudo é realizar uma análise estatística sobre os casos de COVID-19 globalmente, explorando variáveis como número de casos totais, novos casos, mortes totais, vacinas aplicadas, entre outros. A análise utiliza medidas de tendência central (média, mediana) e dispersão (desvio padrão).

## Estrutura dos Dados

A base de dados contém as seguintes variáveis:

- `total_cases`: Casos totais registrados.
- `new_cases`: Novos casos registrados.
- `total_deaths`: Total de mortes registradas.
- `new_deaths`: Novas mortes registradas.
- `total_vaccinations`: Total de vacinações realizadas.
- `people_vaccinated`: Pessoas vacinadas.
- `reproduction_rate`: Taxa de reprodução do vírus.
- `icu_patients`: Pacientes em UTI.

## Análise Realizada

Utilizando a base de dados CSV, foram feitas as seguintes etapas:

1. **Carregamento dos Dados**: O arquivo CSV foi carregado usando a biblioteca `pandas`.
2. **Análise Descritiva**: Foram calculadas as estatísticas descritivas, como a média, desvio padrão e valores máximos para várias variáveis (casos, mortes, vacinações, etc).
3. **Criação de Relatórios**: As análises detalhadas foram exportadas para arquivos CSV e PDF.
