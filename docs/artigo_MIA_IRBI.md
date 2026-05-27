# MIA–IRBI E A REORGANIZAÇÃO TERRITORIAL:
## validação empírica preliminar dos regimes de emergência sintrópica, captura estrutural e colapso exofágico

**Marcelo Ramão da Silveira Barbosa**

> **Citação do protocolo e dados:**  
> O protocolo computacional MIA–IRBI, os dados normalizados e os gráficos estão publicamente disponíveis no repositório GitHub:  
> [https://github.com/marcelobarbosa-ifalolu/validacao](https://github.com/marcelobarbosa-ifalolu/validacao) (BARBOSA, 2026).

---

### RESUMO

O presente artigo apresenta a validação empírica preliminar do modelo MIA–IRBI (Método Integral de Análise e Índice de Resiliência Baseado em Ifá), ferramenta de diagnóstico territorial voltada a sistemas complexos. A hipótese central é a de que os territórios não entram em crise por excesso de entropia, mas pela incapacidade de reorganizar as tensões entre forças exógenas e capacidades adaptativas internas. O trabalho propõe uma inversão conceitual: a entropia é redefinida como baixa articulação entre sistemas, e a homeostase, como mecanismo de estabilização que pode resultar em captura estrutural. Metodologicamente, operacionalizam-se as variáveis Energia ($E$), Estrutura ($X$) e Movimento ($M$), conjugadas às pressões estruturais externas ($PH$) e à capacidade adaptativa endógena ($Ph$). Foram analisados cinco territórios em contextos distintos: São Gabriel do Oeste (Brasil), Romagna (Itália), Zouping (China), Nova Nazaré (Brasil) e McDowell (Estados Unidos). Os resultados, atualizados com dados recentes (2022–2025), mostram convergência entre sistemas territorializados resilientes, classificados no regime de Emergência Sintrópica, e permitem distinguir estruturas submetidas à captura estrutural e ao colapso exofágico. Conclui-se que a resiliência territorial não depende da intensidade das forças atuantes, mas da capacidade de converter entropia em reorganização adaptativa. O modelo revela potencial para análises prospectivas, governança territorial e estudos comparados multiescalares.

**Palavras-chave:** território; entropia; homeostase; resiliência territorial; sistemas complexos; MIA–IRBI.

---

### 1 INTRODUÇÃO

A intensificação das dinâmicas globais de circulação de capital, informação e poder impôs novos desafios à análise territorial. Modelos clássicos de desenvolvimento regional têm dificuldade crescente para explicar por que certos territórios, mesmo sob intensas pressões estruturais, conseguem reorganizar-se e produzir trajetórias adaptativas, enquanto outros colapsam apesar de exibirem elevada eficiência funcional.

A hipótese central deste trabalho é a de que os territórios não entram em crise por excesso de entropia, mas pela incapacidade de reorganização diante das tensões entre captura estrutural e adaptação endógena. Propõe-se, assim, uma inversão analítica da relação entre entropia e homeostase.

Tradicionalmente, homeostase é interpretada como condição de equilíbrio e estabilidade, e entropia, como desordem e degradação sistêmica. O modelo MIA–IRBI oferece leitura distinta: a homeostase representa estabilização estrutural, podendo conduzir à captura das possibilidades territoriais; a entropia, por sua vez, corresponde ao conjunto de relações, fluxos e potencialidades ainda não articuladas pelo sistema dominante.

O território passa a ser compreendido como campo dinâmico de forças, no qual pressões exógenas e capacidades internas interagem continuamente. Tal formulação dialoga com:

* A noção de meio inovador de Maillat (1991; 2002);
* A lógica espacial do capital desenvolvida por Méndez (1997);
* As interpretações territoriais de Milton Santos (1996);
* A teoria dos sistemas complexos aplicada às dinâmicas espaciais.

A partir desse arcabouço, este artigo apresenta a validação empírica preliminar do protocolo computacional MIA–IRBI, aplicado a cinco territórios localizados em contextos geopolíticos distintos.

---

### 2 FUNDAMENTAÇÃO TEÓRICA

#### 2.1 Entropia e homeostase territorial

O modelo MIA–IRBI redefine a entropia territorial não como ausência de ordem, mas como baixa articulação entre sistemas coexistentes. Formalmente:

$$ S = 1 - \Theta $$

onde:
* $S$ representa a entropia territorial;
* $\Theta$ representa o grau de captura estrutural.

Diferentemente das interpretações termodinâmicas clássicas, a entropia territorial corresponde à parcela do sistema que ainda não foi rigidamente estabilizada por estruturas dominantes. A homeostase, portanto, não elimina a entropia; ela organiza parte dela em estruturas relativamente estáveis.

O grau de captura estrutural é definido como:

$$ \Theta = \frac{|\vec{PH}|}{|\vec{PH}| + |\vec{Ph}|} $$

em que:
* $\vec{PH} = (PH_x, PH_y)$ é o vetor de pressão estrutural exógena;
* $\vec{Ph} = (Ph_x, Ph_y)$ é o vetor de capacidade adaptativa endógena.

A relação entre esses vetores determina o regime territorial predominante.

#### 2.2 Pressão estrutural e capacidade adaptativa

A dinâmica territorial emerge da tensão entre:

$$ \vec{PH} \rightarrow \text{captura estrutural} $$

e

$$ \vec{Ph} \rightarrow \text{reorganização adaptativa} $$

Quando $|\vec{PH}| > |\vec{Ph}|$, predomina a dependência estrutural e a captura territorial. Quando $|\vec{Ph}| > |\vec{PH}|$, abre-se espaço para reorganização endógena, inovação territorial e emergência adaptativa.

Essa formulação aproxima-se das leituras de Maillat sobre meios inovadores e das análises de Méndez acerca das reorganizações espaciais do capitalismo global.

#### 2.3 O Índice de Resiliência Baseado em Ifá (IRBI)

O IRBI sintetiza a capacidade territorial de reorganização adaptativa a partir de três dimensões fundamentais:

$$ IRBI = 0{,}40E + 0{,}35X + 0{,}25M $$

onde:
* $E$ = Energia territorial (densidade de fluxos econômicos e infraestrutura);
* $X$ = Estrutura territorial (consolidação institucional e organizacional);
* $M$ = Movimento territorial (mobilidade e diversidade de trajetórias).

As variáveis são operacionalizadas mediante proxies empíricas derivadas de indicadores socioeconômicos, institucionais e relacionais, normalizados no intervalo $[0,1]$. Nesta versão atualizada, os escores de $E$, $X$ e $M$ foram recalculados com dados recentes (2022–2025) provenientes de fontes oficiais (IBGE, US Census, Eurostat, NBS China etc.), conforme detalhado no Apêndice Metodológico.

---

### 3 METODOLOGIA

#### 3.1 Procedimento metodológico

A pesquisa estruturou-se em quatro etapas:
1. Definição das variáveis e construção das proxies territoriais;
2. Operacionalização computacional do protocolo MIA–IRBI;
3. Aplicação empírica a cinco territórios;
4. Classificação dos regimes territoriais.

Os indicadores foram normalizados pelo método Min‑Máx. O protocolo computacional, incluindo os dados e gráficos, está disponível no repositório GitHub do autor (BARBOSA, 2026).

#### 3.2 Regimes territoriais

O modelo classifica os territórios em cinco regimes:

| Regime | Característica predominante |
| :--- | :--- |
| **Emergência Sintrópica** | Reorganização adaptativa |
| **Homeostase rígida** | Estabilidade dependente |
| **Entropia potencial** | Reorganização latente |
| **Entropia dispersiva** | Fragmentação estrutural |
| **Colapso exofágico** | Captura extrema e erosão territorial |

A classificação é obtida a partir das relações entre $\Theta$, $S_m$ (entropia mediada), $M$, as componentes do vetor resultante $\vec{R} = \vec{PH} - \vec{Ph}$, $E$ e $X$. Os limiares exatos encontram‑se implementados no código do protocolo.

#### 3.3 Casos analisados

Foram analisados cinco territórios:
* São Gabriel do Oeste (Brasil);
* Romagna / Emilia‑Romagna (Itália);
* Zouping (China);
* Nova Nazaré (Brasil);
* McDowell (Estados Unidos).

A seleção buscou contemplar diferentes escalas, regimes políticos, formas de inserção econômica e capacidades adaptativas.

---

### 4 RESULTADOS

#### Tabela 1 – Escores normalizados e IRBI calculado (valores atualizados 2022–2025)

| Território | E | X | M | IRBI |
| :--- | :---: | :---: | :---: | :---: |
| **São Gabriel do Oeste (BR)** | 0.85 | 0.82 | 0.78 | **0.82** |
| **Romagna (IT)** | 0.95 | 0.95 | 0.92 | **0.94** |
| **Zouping (CN)** | 0.75 | 0.85 | 0.85 | **0.81** |
| **Nova Nazaré (BR)** | 0.35 | 0.40 | 0.32 | **0.36** |
| **McDowell (EUA)** | 0.25 | 0.28 | 0.20 | **0.25** |

*Fonte: IBGE, US Census/FRED, Eurostat/ISTAT, NBS China. Normalização Min‑Máx entre os cinco casos.*

#### 4.1 Emergência Sintrópica

São Gabriel do Oeste (IRBI = 0,82), Romagna (0,94) e Zouping (0,81) exibem valores elevados de IRBI, indicando alta capacidade de reorganização adaptativa. Em todos os três, verifica-se $|\vec{Ph}| > |\vec{PH}|$ nas componentes vetoriais, resultando em $\Theta$ moderado e entropia mediada ($S_m$) predominantemente canalizada para reorganização ($S_{pot} > S_{disp}$). As três localidades apresentam:
* Elevada densidade relacional (distritos industriais na Romagna, clusters agroindustriais em SGO, parques estatais em Zouping);
* Forte capacidade adaptativa (inovação setorial, diversificação produtiva);
* Baixa captura estrutural (dependência fiscal controlada, governança multinível);
* Elevada articulação institucional.

A convergência de contextos tão díspares (economia de mercado italiana, agronegócio brasileiro e industrialização planificada chinesa) reforça a hipótese de que a Emergência Sintrópica é um atrator independente do regime político, ancorado na capacidade endógena de reorganização.

#### 4.2 Homeostase rígida e dependência funcional

Nova Nazaré (IRBI = 0,36) apresenta escores baixos em todas as dimensões, com $E$ e $M$ particularmente limitados. A dependência de transferências governamentais e a monocultura da soja configuram um quadro de homeostase funcional dependente, no qual a estrutura territorial ($X$) estabiliza o território sem gerar trajetórias de inovação. O vetor resultante $\vec{R}$ aponta para fora ($|\vec{PH}| \gg |\vec{Ph}|$), e $\Theta$ é elevado, confirmando a captura estrutural.

#### 4.3 Colapso exofágico

McDowell (IRBI = 0,25) ilustra o caso extremo de captura exofágica. Apesar de uma renda per capita ainda moderada, a degradação da infraestrutura ($X=0,28$) e a paralisia do movimento ($M=0,20$) revelam um território onde a entropia é inteiramente dispersiva ($S_{disp} \gg S_{pot}$). O colapso da indústria carbonífera deixou um vácuo institucional e relacional, com $\Theta \geq 0,75$, baixíssima densidade de organizações civis e emigração acentuada. O caso demonstra que mesmo fluxos econômicos passados significativos não garantem resiliência se não houver capacidade endógena de reorganização.

---

### 5 DISCUSSÃO

Os resultados atualizados corroboram a premissa central do modelo: a resiliência territorial não é função direta da riqueza ou do tamanho do PIB, mas da articulação entre energia, estrutura e movimento. Romagna, com o maior IRBI (0,94), é também o território com maior densidade relacional e inovação, enquanto McDowell, com o menor índice (0,25), sofre de colapso exofágico mesmo com renda per capita comparável à de algumas regiões brasileiras intermediárias.

A convergência entre Romagna, Zouping e São Gabriel do Oeste em torno do regime de Emergência Sintrópica sugiro a existência de um atrator territorial definido por:
* Densidade relacional;
* Capacidade adaptativa superior à pressão estrutural;
* Redução da captura via diversificação institucional e econômica;
* Sincronização entre inovação ($M$) e organização ($X$).

O caso de Nova Nazaré alerta para os riscos da stability funcional: uma estrutura que se mantém apenas por transferências externas pode ocultar fragilidades profundas, prontas para se manifestarem diante de choques. Já McDowell representa o estágio terminal desse processo — um território onde a homeostase se quebrou e a entropia se tornou puramente dispersiva, sem capacidade de reorganização.

A atualização dos dados reforça a validade do protocolo MIA–IRBI como ferramenta de diagnóstico capaz de capturar essas nuances com indicadores relativamente simples e acessíveis.

---

### 6 CONSIDERAÇÕES FINAIS

O protocolo MIA–IRBI apresentou consistência teórica, operacional e classificatória na análise comparada dos territórios investigados, mesmo após a recalibração com dados recentes. Sua principal contribuição é reinterpretar a resiliência territorial não como estabilidade, mas como capacidade adaptativa de reorganização.

A pesquisa demonstrou que:
* A entropia territorial pode assumir caráter reorganizador;
* A homeostase pode produzir rigidez estrutural;
* A captura territorial depende da relação entre forças externas e capacidade adaptativa interna.

O modelo oferece potencial para:
* Análise prospectiva;
* Governança territorial;
* Geografia computacional;
* Monitoramento regional;
* Estudos comparados multiescalares.

Os próximos passos da pesquisa incluem a ampliação da base empírica para centenas de municípios, a aplicação longitudinal do protocolo em cortes temporais sucessivos e a validação estatística por meio de modelos econométricos para dados em painel.

---

### REFERÊNCIAS

BARBOSA, M. R. S. *A ordem da entropia e a desordem da homeostase: uma leitura territorial dos sistemas complexos*. Cuiabá, 2026. No prelo.

BARBOSA, M. R. S. **MIA–IRBI: validação empírica preliminar** — protocolo computacional e dados. 2026. Repositório GitHub. Disponível em: [https://github.com/marcelobarbosa-ifalolu/validacao](https://github.com/marcelobarbosa-ifalolu/validacao). Acesso em: 26 maio 2026.

MAILLAT, D. *Milieux innovateurs et dynamique territoriale*. Paris: GREMI, 1991.

MAILLAT, D. *Globalização, meio inovador e sistemas territoriais de produção*. Porto Alegre: Editora da UFRGS, 2002.

MÉNDEZ, R. *Geografía económica: la lógica espacial del capitalismo global*. Barcelona: Ariel, 1997.

SANTOS, M. *A natureza do espaço*. São Paulo: Hucitec, 1996.

PRIGOGINE, I. *Order out of chaos*. New York: Bantam Books, 1984.

MORIN, E. *Introdução ao pensamento complexo*. Porto Alegre: Sulina, 2005.

ARRIGHI, G. *O longo século XX*. Rio de Janeiro: Contraponto, 1996.

---


ARRIGHI, Giovanni. *O longo século XX*. Rio de Janeiro: Contraponto, 1996.
