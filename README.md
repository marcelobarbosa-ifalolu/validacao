# MIA–IRBI: Diagnóstico Territorial e Regimes de Resiliência

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20413293.svg)](https://doi.org/10.5281/zenodo.20413293)

**Método Integral de Análise & Índice de Resiliência Baseado em Ifá**

Este repositório contém o protocolo computacional, os dados de validação e a documentação do modelo MIA–IRBI, ferramenta de diagnóstico territorial para sistemas complexos.

## 📌 Resumo

O modelo MIA–IRBI propõe uma reinterpretação da entropia e da homeostase em territórios, classificando-os em cinco regimes:
1. **Emergência Sintrópica**
2. **Homeostase Rígida**
3. **Entropia Potencial**
4. **Entropia Dispersiva**
5. **Colapso Exofágico**

A validação empírica preliminar foi realizada com cinco territórios (São Gabriel do Oeste, Romagna, Zouping, Nova Nazaré, McDowell) e expandida para os 5.570 municípios brasileiros.

## 📂 Estrutura

- `data/`: dados brutos, proxies normalizadas e resultados completos para o Brasil.
- `notebook/`: pipeline de diagnóstico executável no Google Colab.
- `docs/`: artigo empírico (validação) e artigo teórico (espaço de fases e atratores).
- `scripts/`: código-fonte Python do protocolo.

## 🚀 Como usar

1. Acesse o notebook no Google Colab: [MIA-IRBI Pipeline](https://colab.research.google.com/drive/1EJpZGb3oAjveo0KvtjdRfzpSj2shbwYA)
2. Execute as células sequencialmente para gerar o diagnóstico e os gráficos.
3. Para novos territórios, edite o dataframe `dados` com seus próprios indicadores normalizados.

## 📖 Referência

BARBOSA, M. R. S. **MIA–IRBI: validação empírica preliminar** — protocolo computacional e dados. 2026. Zenodo. DOI: [10.5281/zenodo.20413293](https://doi.org/10.5281/zenodo.20413293).

## 📝 Licença

Este projeto está licenciado sob a licença MIT — veja o arquivo `LICENSE` para detalhes.
