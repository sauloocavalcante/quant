# Quant

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)

Ferramenta para análise quantitativa de ativos financeiros, desenvolvida em Python com interface interativa via Streamlit. O projeto permite calcular indicadores técnicos (como RSI), visualizar sinais de compra/venda e executar backtesting de estratégias.

---

## 📋 Funcionalidades

- **Download de dados históricos** – Obtém cotações de ativos via Yahoo Finance (`yfinance`).
- **Cálculo do RSI (Índice de Força Relativa)** – Com períodos personalizáveis.
- **Sinais de trading baseados em RSI** – Geração automática de sinais **BUY**, **SELL** ou **HOLD** com base nos níveis de sobrecompra/sobrevenda.
- **Dashboard interativo** – Interface com duas abas:
  - **RSI**: Exibe uma tabela com os sinais atuais para uma lista de ativos.
