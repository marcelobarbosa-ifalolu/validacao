# ================================================
# 01_empresas_cnpj_basedosdados.py
# Contagem de Empresas Ativas por Município
# Fonte: Base dos Dados - br_me_cnpj
# ================================================

import basedosdados as bd
import pandas as pd
from datetime import datetime

# ================== CONFIGURAÇÕES ==================
# Substitua pelo seu billing project ID (crie um gratuito no Google Cloud)
PROJECT_ID = "seu-projeto-basedosdados"   # ← MUDE AQUI

# Configurar billing project
bd.config.billing_project_id = PROJECT_ID

print("🔄 Iniciando consulta de empresas ativas por município...")

# ================== CONSULTA SQL ==================
query = """
SELECT 
    e.id_municipio,
    m.nome AS nome_municipio,
    m.sigla_uf,
    COUNT(*) AS total_empresas_ativas,
    COUNT(CASE WHEN e.situacao_cadastral = '2' THEN 1 END) AS empresas_ativas,  -- Situação 2 = Ativa
    COUNT(DISTINCT e.cnae_fiscal_principal) AS diversidade_cnae
FROM `basedosdados.br_me_cnpj.estabelecimentos` e
JOIN `basedosdados.br_bd_diretorios_brasil.municipio` m 
    ON e.id_municipio = m.id_municipio
WHERE e.situacao_cadastral = '2'  -- Apenas empresas ATIVAS
GROUP BY e.id_municipio, m.nome, m.sigla_uf
ORDER BY total_empresas_ativas DESC
"""

# ================== EXECUTAR CONSULTA ==================
df_empresas = bd.read_sql(query, billing_project_id=PROJECT_ID)

print(f"✅ Consulta concluída! {len(df_empresas)} municípios encontrados.")

# ================== CÁLCULOS ADICIONAIS ==================
# Densidade aproximada (empresas por 10 mil habitantes) - vamos cruzar com população depois
# Por enquanto salvamos o básico

df_empresas['data_extracao'] = datetime.now().strftime("%Y-%m-%d")

# ================== SALVAR ARQUIVOS ==================
output_path = "data/empresas_ativas_por_municipio.csv"

df_empresas.to_csv(output_path, index=False, encoding='utf-8')

print(f"💾 Arquivo salvo em: {output_path}")
print(f"   Total de registros: {len(df_empresas):,}")
print(f"   Top 5 municípios:\n{df_empresas.head(5)[['nome_municipio', 'sigla_uf', 'empresas_ativas']]}")

# Salvar também versão compacta (parquet - mais eficiente)
df_empresas.to_parquet("data/empresas_ativas_por_municipio.parquet", index=False)
print("📦 Versão Parquet também salva.")
