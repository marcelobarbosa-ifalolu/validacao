# EMERGÊNCIA SINTRÓPICA COMO ATRATOR TERRITORIAL:
## o espaço de fases do modelo MIA–IRBI e suas bifurcações

**Marcelo Ramão da Silveira Barbosa**

> **Citação do repositório:**  
> O protocolo MIA–IRBI, os dados e os notebooks estão disponíveis em:  
> [https://github.com/marcelobarbosa-ifalolu/validacao](https://github.com/marcelobarbosa-ifalolu/validacao) (BARBOSA, 2026).

---

### Resumo

Este artigo desenvolve a fundamentação dinâmica do modelo MIA–IRBI, demonstrando que seus cinco regimes territoriais — Emergência Sintrópica, Homeostase Rígida, Entropia Potencial, Entropia Dispersiva e Colapso Exofágico — não são meras categorias descritivas, mas estados qualitativamente distintos de um sistema dinâmico territorial. Constrói-se o espaço de fases tridimensional definido por $S_m$ (entropia mediada), $X$ (estrutura) e $M$ (movimento), e identificam-se os atratores e as superfícies de bifurcação que governam as transições entre regimes. A Emergência Sintrópica é caracterizada como um atrator associado à condição $|\vec{Ph}| > |\vec{PH}|$, enquanto o Colapso Exofágico emerge como bacia de captura quando a estrutura se torna rígida e o movimento cessa. Conecta-se o MIA‑IRBI à literatura de criticalidade auto-organizada (Bak, 1996), estruturas dissipativas (Prigogine, 1984) e resiliência ecológica (Holling, 1973), oferecendo uma formalização matemática original para a análise territorial.

**Palavras-chave:** espaço de fases; atratores; bifurcação; sistemas complexos; resiliência territorial; MIA–IRBI.

---

### 1. Introdução

O modelo MIA‑IRBI (Barbosa, 2026) propôs uma classificação de territórios em cinco regimes a partir da interação entre pressões exógenas ($\vec{PH}$), capacidade adaptativa endógena ($\vec{Ph}$), energia ($E$), estrutura ($X$) e movimento ($M$). Embora a validação empírica preliminar tenha demonstrado coerência entre a classificação e as trajetórias observadas de cinco territórios (São Gabriel do Oeste, Romagna, Zouping, Nova Nazaré e McDowell), o modelo carecia de uma formalização dinâmica que:

1. demonstrasse que os regimes são estados de um mesmo sistema, e não tipos isolados;
2. identificasse as condições sob as quais um território transita de um regime a outro;
3. conectasse o MIA‑IRBI à teoria dos sistemas dinâmicos não lineares e às discussões contemporâneas sobre criticalidade e resiliência.

Este artigo preenche essas lacunas. A seção 2 constrói o espaço de fases, definindo as variáveis de estado e o campo vetorial. A seção 3 identifica os atratores e as superfícies de bifurcação. A seção 4 conecta o modelo à literatura de sistemas complexos. A seção 5 deriva implicações para políticas territoriais.

---

### 2. O espaço de fases do MIA–IRBI

#### 2.1 Variáveis de estado

O estado de um território no instante $t$ é descrito pelo vetor:

\[
\mathbf{S}(t) = (S_m(t), X(t), M(t)) \in [0,1]^3
\]

onde:
- $S_m = 1 - \Theta$ é a entropia mediada, que expressa o grau de fluidez e potencial reorganizador do sistema;
- $X$ é a estrutura, refletindo a consolidação institucional e organizacional;
- $M$ é o movimento, capturando a taxa de inovação e reorganização ativa.

A energia $E$ é tratada como parâmetro de controle exógeno, variando mais lentamente que as variáveis de estado. Os vetores $\vec{PH} = (PH_x, PH_y)$ e $\vec{Ph} = (Ph_x, Ph_y)$ determinam a direção do fluxo no espaço de fases.

#### 2.2 Campo vetorial

Propõe-se o seguinte sistema de equações diferenciais para a dinâmica temporal:

\[
\begin{aligned}
\frac{dS_m}{dt} &= \alpha (|\vec{Ph}| - |\vec{PH}|) - \beta S_m (1 - M) \\
\frac{dX}{dt} &= \gamma S_m (1 - X) - \delta (1 - M) X \\
\frac{dM}{dt} &= \eta S_m X (1 - M) - \zeta (|\vec{PH}| - |\vec{Ph}|)_+ M
\end{aligned}
\]

com $\alpha, \beta, \gamma, \delta, \eta, \zeta > 0$ e $(x)_+ = \max(x, 0)$.

**Interpretação das equações:**

- **Equação de $S_m$:** A entropia mediada cresce proporcionalmente à vantagem da capacidade adaptativa sobre a pressão ($|\vec{Ph}| - |\vec{PH}|$) e decai quando o movimento é baixo, pois a estagnação impede a transformação da entropia em reorganização.
- **Equação de $X$:** A estrutura se consolida na presença de entropia mediada — é preciso haver potencial reorganizador ($S_m$) para que novas instituições se formem. A estrutura é erodida pela falta de movimento ($1-M$), que representa rigidez e obsolescência.
- **Equação de $M$:** O movimento é impulsionado pelo produto $S_m X$: é necessário tanto fluidez quanto estrutura para canalizar a inovação. O movimento é inibido pelo excesso de pressão externa ($|\vec{PH}| \gg |\vec{Ph}|$), que drena a energia para funções defensivas.

#### 2.3 Pontos fixos

O sistema possui até cinco pontos fixos, correspondentes aos regimes do MIA‑IRBI:

| Ponto fixo | $S_m$ | $X$ | $M$ | Condição | Regime |
|------------|-------|-----|-----|-----------|--------|
| $P_1$ | 1 | 1 | 1 | $|\vec{Ph}| \gg |\vec{PH}|$ | Emergência Sintrópica |
| $P_2$ | $S_m^* \in (0,35; 0,5)$ | $X^* \in (0,5; 0,8)$ | $M^* < 0,4$ | $|\vec{PH}| \approx |\vec{Ph}|$ | Homeostase Rígida |
| $P_3$ | $>0,5$ | $<0,5$ | $<0,5$ | $|\vec{Ph}| > |\vec{PH}|$, $X$ baixo | Entropia Potencial |
| $P_4$ | $>0,5$ | $<0,5$ | $<0,5$ | $|\vec{Ph}| > |\vec{PH}|$, $M$ baixo | Entropia Dispersiva |
| $P_5$ | 0 | 0 | 0 | $|\vec{PH}| \gg |\vec{Ph}|$, $E$ baixo | Colapso Exofágico |

A distinção entre $P_3$ e $P_4$ depende da componente dominante da entropia: se $X$ for maior que $0,5$, a entropia é potencial (há estrutura para canalizá-la); se $X$ for menor, é dispersiva.

---

### 3. Atratores e bifurcações

#### 3.1 Análise de estabilidade local

A matriz jacobiana do sistema em um ponto genérico $(S_m, X, M)$ é:

\[
J = \begin{bmatrix}
-\beta(1-M) & 0 & \beta S_m \\
\gamma(1-X) & -\gamma S_m - \delta(1-M) & \delta X \\
\eta X(1-M) & \eta S_m(1-M) & -\eta S_m X - \zeta(|\vec{PH}| - |\vec{Ph}|)_+
\end{bmatrix}
\]

**No atrator sintrópico $P_1 = (1,1,1)$:**

\[
J(P_1) = \begin{bmatrix}
0 & 0 & \beta \\
0 & -\gamma - \delta & \delta \\
0 & 0 & -\eta
\end{bmatrix}
\]

Os autovalores são $\lambda_1 = 0$, $\lambda_2 = -(\gamma + \delta) < 0$, $\lambda_3 = -\eta < 0$. O autovalor nulo reflete a neutralidade de $S_m$ quando $M=1$ (a entropia é plenamente canalizada). O ponto é marginalmente estável na direção de $S_m$, mas atrai trajetórias para $(1,1,1)$ desde que $|\vec{Ph}| > |\vec{PH}|$.

**No atrator de colapso $P_5 = (0,0,0)$:**

\[
J(P_5) = \begin{bmatrix}
-\beta & 0 & 0 \\
\gamma & -\delta & 0 \\
0 & 0 & -\zeta(|\vec{PH}| - |\vec{Ph}|)_+
\end{bmatrix}
\]

Os autovalores são todos negativos: $\lambda_1 = -\beta$, $\lambda_2 = -\delta$, $\lambda_3 = -\zeta(|\vec{PH}| - |\vec{Ph}|)_+$. $P_5$ é um **sumidouro**: uma vez que o sistema entra em sua bacia, não há saída espontânea.

#### 3.2 Superfícies de bifurcação

As transições críticas ocorrem quando o sistema cruza superfícies de bifurcação no espaço de parâmetros $(\alpha, \beta, \gamma, \delta, \eta, \zeta, |\vec{PH}|, |\vec{Ph}|)$.

**Bifurcação $B_1$ — Homeostase para Emergência (transcrítica):**

Definida pela condição $|\vec{Ph}| = |\vec{PH}|$ com $X > 0,5$. Quando a capacidade adaptativa iguala e depois supera a pressão, o ponto fixo de homeostase ($P_2$) perde estabilidade e o sistema é atraído para $P_1$. Esta é uma **bifurcação transcrítica**: há troca de estabilidade entre dois pontos fixos.

**Bifurcação $B_2$ — Homeostase para Colapso (sela-nó):**

Definida por $M = M_{crit} \approx 0,3$ e $X < 0,4$. Quando o movimento cai abaixo de um limiar crítico e a estrutura já está fragilizada, o ponto fixo de homeostase colide com um ponto de sela e desaparece — uma **bifurcação sela‑nó**. O sistema é então inevitavelmente arrastado para $P_5$.

**Bifurcação $B_3$ — Emergência para Entropia Dispersiva (Hopf degenerada):**

Definida por $X = 0,5$ com $S_m$ elevado. Quando a estrutura é insuficiente para canalizar a alta entropia, o sistema oscila entre potencial reorganizador e fragmentação, podendo estabilizar-se em $P_4$. Corresponde a uma transição de fase desorganizada, análoga a uma bifurcação de Hopf degenerada onde o ciclo limite colapsa em um ponto dispersivo.

#### 3.3 Diagrama de bifurcação esquemático

(No artigo final, incluir um diagrama qualitativo com $|\vec{Ph}| - |\vec{PH}|$ no eixo horizontal e $X$ no eixo vertical, mostrando as bacias de atração dos três atratores principais e as superfícies de bifurcação.)

---

### 4. Conexão com a literatura de sistemas complexos

#### 4.1 Prigogine e as estruturas dissipativas

A Emergência Sintrópica é formalmente análoga ao conceito de **estrutura dissipativa** de Prigogine (1984): um estado longe do equilíbrio termodinâmico, mantido por fluxos contínuos de energia ($E$) e matéria/informação ($M$), que gera ordem a partir de flutuações. No MIA‑IRBI, a condição $|\vec{Ph}| > |\vec{PH}|$ expressa exatamente a capacidade do sistema de exportar entropia para o ambiente, mantendo baixa a entropia interna apesar dos fluxos intensos. O parâmetro $\alpha$ na equação de $S_m$ quantifica a eficiência dessa exportação.

#### 4.2 Holling e o ciclo adaptativo

O ciclo adaptativo de Holling (1973, 2001) — com suas quatro fases: exploração ($r$), conservação ($K$), liberação ($\Omega$) e reorganização ($\alpha$) — encontra correspondência precisa no espaço de fases do MIA‑IRBI:

| Fase de Holling | Estado no MIA‑IRBI | Características |
|-----------------|-------------------|-----------------|
| $r$ (exploração) | Entropia Potencial | $S_m$ alto, $X$ baixo, $M$ moderado — recursos abundantes, instituições incipientes |
| $K$ (conservação) | Homeostase Rígida | $S_m$ moderado, $X$ alto, $M$ baixo — instituições consolidadas, eficiência máxima, resiliência mínima |
| $\Omega$ (liberação) | Colapso Exofágico | $S_m$ e $X$ colapsam, $M \to 0$ — ruptura, liberação de recursos |
| $\alpha$ (reorganização) | **Emergência Sintrópica** (sucesso) ou Entropia Dispersiva (fracasso) | Depende da capacidade de recombinar recursos com nova estrutura |

A contribuição do MIA‑IRBI é fornecer métricas quantitativas ($S_m, X, M$) para identificar a fase do ciclo adaptativo em tempo real.

#### 4.3 Bak e a criticalidade auto-organizada

A proximidade do sistema à superfície de bifurcação $B_2$ pode ser interpretada como um estado de **criticalidade auto-organizada** (Bak, 1996). Nesse estado, pequenas perturbações — uma queda marginal em $M$, por exemplo — podem desencadear avalanches de colapso que redesenham toda a paisagem territorial. Isso explica por que territórios aparentemente estáveis (homeostáticos) podem ruir abruptamente após choques que, isoladamente, pareceriam administráveis. A distribuição dos tamanhos de "avalanches territoriais" (número de municípios que colapsam em um dado período) deveria seguir uma lei de potência, hipótese testável empiricamente.

---

### 5. Implicações para políticas territoriais

#### 5.1 Indicadores de alerta precoce

A identificação das superfícies de bifurcação permite construir indicadores de proximidade ao colapso ou de potencial de emergência:

1. **Índice de Vulnerabilidade à Rigidez ($V_R$):**

\[
V_R = (1 - S_m) \cdot (1 - M)
\]

Quando $V_R > 0,5$, o sistema está na bacia de atração da Homeostase Rígida e é vulnerável a choques.

2. **Índice de Proximidade ao Colapso ($V_C$):**

\[
V_C = \frac{|\vec{PH}|}{|\vec{PH}| + |\vec{Ph}|} \cdot (1 - X)
\]

Quando $V_C > 0,75$, o sistema está próximo da superfície de bifurcação $B_2$ e requer intervenção urgente.

3. **Índice de Potencial Sintrópico ($V_S$):**

\[
V_S = S_m \cdot X \cdot M
\]

Quando $V_S > 0,5$, o sistema está na bacia de atração da Emergência Sintrópica. Políticas devem focar em manter e ampliar essa condição.

#### 5.2 Estratégias de intervenção

A análise dinâmica sugere três alavancas de política pública:

- **Aumentar $M$ (movimento):** Fomento à inovação, educação, mobilidade, conexões interterritoriais. É a alavanca mais efetiva para afastar o sistema de $B_2$.
- **Reduzir $|\vec{PH}|$ (pressão exógena):** Diversificação econômica para diminuir a concentração setorial ($PH_y$) e aumento da autonomia fiscal para reduzir a dependência de transferências ($PH_x$).
- **Aumentar $|\vec{Ph}|$ (capacidade adaptativa):** Fortalecimento de organizações da sociedade civil, cooperativas, empreendedorismo local.

A combinação ótima depende da posição atual do território no espaço de fases. O protocolo MIA‑IRBI fornece o diagnóstico; a análise dinâmica aqui apresentada fornece a prescrição.

---

### 6. Conclusão

Este artigo demonstrou que os cinco regimes do MIA‑IRBI emergem naturalmente da dinâmica de três variáveis de estado ($S_m, X, M$) governadas por um campo vetorial com três atratores e três superfícies de bifurcação. A Emergência Sintrópica não é um acidente histórico ou uma idiossincrasia cultural — é um **atrator dinâmico** acessível a qualquer território que consiga, simultaneamente, manter sua capacidade adaptativa acima da pressão estrutural ($|\vec{Ph}| > |\vec{PH}|$) e possuir estrutura suficiente ($X > 0,5$) para canalizar a entropia em reorganização.

As implicações são profundas: o desenvolvimento territorial deixa de ser pensado como acúmulo linear de fatores (mais PIB, mais infraestrutura) e passa a ser concebido como a **navegação em um espaço de fases com bifurcações**, exigindo monitoramento contínuo e intervenções precisas nos momentos críticos.

Trabalhos futuros incluirão a estimação dos parâmetros ($\alpha, \beta, \gamma, \delta, \eta, \zeta$) a partir de séries temporais de indicadores municipais, a simulação numérica do campo vetorial para gerar previsões testáveis e a validação empírica da hipótese de criticalidade auto-organizada na distribuição de colapsos territoriais.

---

### Referências

BAK, P. *How Nature Works: The Science of Self-Organized Criticality*. New York: Copernicus, 1996.

BARBOSA, M. R. S. MIA–IRBI e a reorganização territorial: validação empírica preliminar dos regimes de emergência sintrópica, captura estrutural e colapso exofágico. 2026. Pré‑print. Disponível em: [https://github.com/marcelobarbosa-ifalolu/validacao](https://github.com/marcelobarbosa-ifalolu/validacao).

HOLLING, C. S. Resilience and stability of ecological systems. *Annual Review of Ecology and Systematics*, v. 4, p. 1‑23, 1973.

HOLLING, C. S. Understanding the complexity of economic, ecological, and social systems. *Ecosystems*, v. 4, n. 5, p. 390‑405, 2001.

PRIGOGINE, I.; STENGERS, I. *Order out of Chaos: Man’s New Dialogue with Nature*. New York: Bantam Books, 1984.
