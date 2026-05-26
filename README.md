# validacao
MIA-IRBI: computational protocol for territorial diagnosis, classifying resilience into five regimes (syntropic emergence, rigid homeostasis, potential entropy, dispersive entropy, exophagic collapse). Based on Ifá. Includes empirical validation with 5 municipalities.
# MIA–IRBI: Diagnóstico Territorial e Regimes de Resiliência

**Método Integral de Análise & Índice de Resiliência Baseado em Ifá**

Este repositório contém o protocolo computacional, os dados de validação e a documentação do modelo MIA–IRBI, ferramenta de diagnóstico territorial para sistemas complexos.

## 📌 Resumo

O modelo MIA–IRBI propõe uma reinterpretação da entropia e da homeostase em territórios, classificando-os em cinco regimes:
1. **Emergência Sintrópica**
2. **Homeostase Rígida**
3. **Entropia Potencial**
4. **Entropia Dispersiva**
5. **Colapso Exofágico**

A validação empírica preliminar foi realizada com cinco territórios (São Gabriel do Oeste, Romagna, Zouping, Nova Nazaré, McDowell).

## 📂 Estrutura

- `data/proxies_territoriais.csv`: indicadores normalizados usados na calibração.
- `notebook/MIA_IRBI_validacao_cinco_regimes.ipynb`: pipeline de diagnóstico completo (executável no Google Colab).
- `docs/artigo_MIA_IRBI.md`: versão integral do artigo (pré-print).

## 🚀 Como usar

1. Acesse o notebook diretamente no [Google Colab](https://colab.research.google.com/) (link para o arquivo .ipynb no repositório).
2. Execute as células sequencialmente para gerar a tabela de diagnóstico, o círculo azimutal e o gráfico de entropias.
3. Para novos territórios, edite o dataframe `dados` com seus próprios indicadores normalizados.

## 📊 Dados

A tabela de proxies (`proxies_territoriais.csv`) contém:
- Identificação do território
- Dimensões E, X, M
- Componentes vetoriais PH_x, PH_y, Ph_x, Ph_y
- Indicadores originais e fontes sugeridas

## 📖 Referência

Barbosa, M. R. S. *MIA–IRBI e a Reorganização Territorial: validação empírica preliminar dos regimes de emergência sintrópica, captura estrutural e colapso exofágico* (2026).

## 📝 Licença

Este projeto está licenciado sob a licença MIT – veja o arquivo `LICENSE` para detalhes.
