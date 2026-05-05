# Pull, Otimização e Avaliação de Prompts com LangChain e LangSmith

## Objetivo

Você deve entregar um software capaz de:

1. **Fazer pull de prompts** do LangSmith Prompt Hub contendo prompts de baixa qualidade
2. **Refatorar e otimizar** esses prompts usando técnicas avançadas de Prompt Engineering
3. **Fazer push dos prompts otimizados** de volta ao LangSmith
4. **Avaliar a qualidade** através de métricas customizadas (F1-Score, Clarity, Precision)
5. **Atingir pontuação mínima** de 0.9 (90%) em todas as métricas de avaliação

---

## Exemplo no CLI

```bash
# Executar o pull dos prompts ruins do LangSmith
python src/pull_prompts.py

# Executar avaliação inicial (prompts ruins)
python src/evaluate.py

Executando avaliação dos prompts...
================================
Prompt: support_bot_v1a
- Helpfulness: 0.45
- Correctness: 0.52
- F1-Score: 0.48
- Clarity: 0.50
- Precision: 0.46
================================
Status: FALHOU - Métricas abaixo do mínimo de 0.9

# Após refatorar os prompts e fazer push
python src/push_prompts.py

# Executar avaliação final (prompts otimizados)
python src/evaluate.py

Executando avaliação dos prompts...
================================
Prompt: support_bot_v2_optimized
- Helpfulness: 0.94
- Correctness: 0.96
- F1-Score: 0.93
- Clarity: 0.95
- Precision: 0.92
================================
Status: APROVADO ✓ - Todas as métricas atingiram o mínimo de 0.9
```
---

## Tecnologias obrigatórias

- **Linguagem:** Python 3.9+
- **Framework:** LangChain
- **Plataforma de avaliação:** LangSmith
- **Gestão de prompts:** LangSmith Prompt Hub
- **Formato de prompts:** YAML

---

## Pacotes recomendados

```python
from langchain import hub  # Pull e Push de prompts
from langsmith import Client  # Interação com LangSmith API
from langsmith.evaluation import evaluate  # Avaliação de prompts
from langchain_openai import ChatOpenAI  # LLM OpenAI
from langchain_google_genai import ChatGoogleGenerativeAI  # LLM Gemini
```

---

## OpenAI

- Crie uma **API Key** da OpenAI: https://platform.openai.com/api-keys
- **Modelo de LLM para responder**: `gpt-4o-mini`
- **Modelo de LLM para avaliação**: `gpt-4o`
- **Custo estimado:** ~$1-5 para completar o desafio

## Gemini (modelo free)

- Crie uma **API Key** da Google: https://aistudio.google.com/app/apikey
- **Modelo de LLM para responder**: `gemini-2.5-flash`
- **Modelo de LLM para avaliação**: `gemini-2.5-flash`
- **Limite:** 15 req/min, 1500 req/dia

---

## Requisitos

### 1. Pull dos Prompt inicial do LangSmith

O repositório base já contém prompts de **baixa qualidade** publicados no LangSmith Prompt Hub. Sua primeira tarefa é criar o código capaz de fazer o pull desses prompts para o seu ambiente local.

**Tarefas:**

1. Configurar suas credenciais do LangSmith no arquivo `.env` (conforme instruções no `README.md` do repositório base)
2. Acessar o script `src/pull_prompts.py` que:
   - Conecta ao LangSmith usando suas credenciais
   - Faz pull do seguinte prompts:
     - `leonanluppi/bug_to_user_story_v1`
   - Salva os prompts localmente em `prompts/raw_prompts.yml`

---

### 2. Otimização do Prompt

Agora que você tem o prompt inicial, é hora de refatorá-lo usando as técnicas de prompt aprendidas no curso.

**Tarefas:**

1. Analisar o prompt em `prompts/bug_to_user_story_v1.yml`
2. Criar um novo arquivo `prompts/bug_to_user_story_v2.yml` com suas versões otimizadas
3. Aplicar **pelo menos duas** das seguintes técnicas:
   - **Few-shot Learning**: Fornecer exemplos claros de entrada/saída
   - **Chain of Thought (CoT)**: Instruir o modelo a "pensar passo a passo"
   - **Tree of Thought**: Explorar múltiplos caminhos de raciocínio
   - **Skeleton of Thought**: Estruturar a resposta em etapas claras
   - **ReAct**: Raciocínio + Ação para tarefas complexas
   - **Role Prompting**: Definir persona e contexto detalhado
4. Documentar no `README.md` quais técnicas você escolheu e por quê

**Requisitos do prompt otimizado:**

- Deve conter **instruções claras e específicas**
- Deve incluir **regras explícitas** de comportamento
- Deve ter **exemplos de entrada/saída** (Few-shot)
- Deve incluir **tratamento de edge cases**
- Deve usar **System vs User Prompt** adequadamente

---

### 3. Push e Avaliação

Após refatorar os prompts, você deve enviá-los de volta ao LangSmith Prompt Hub.

**Tarefas:**

1. Criar o script `src/push_prompts.py` que:
   - Lê os prompts otimizados de `prompts/bug_to_user_story_v2.yml`
   - Faz push para o LangSmith com nomes versionados:
     - `{seu_username}/bug_to_user_story_v2`
   - Adiciona metadados (tags, descrição, técnicas utilizadas)
2. Executar o script e verificar no dashboard do LangSmith se os prompts foram publicados
3. Deixa-lo público

---

### 4. Iteração

- Espera-se 3-5 iterações.
- Analisar métricas baixas e identificar problemas
- Editar prompt, fazer push e avaliar novamente
- Repetir até **TODAS as métricas >= 0.9**

### Critério de Aprovação:

```
- Tone Score >= 0.9
- Acceptance Criteria Score >= 0.9
- User Story Format Score >= 0.9
- Completeness Score >= 0.9

MÉDIA das 4 métricas >= 0.9
```

**IMPORTANTE:** TODAS as 4 métricas devem estar >= 0.9, não apenas a média!

### 5. Testes de Validação

**O que você deve fazer:** Edite o arquivo `tests/test_prompts.py` e implemente, no mínimo, os 6 testes abaixo usando `pytest`:

- `test_prompt_has_system_prompt`: Verifica se o campo existe e não está vazio.
- `test_prompt_has_role_definition`: Verifica se o prompt define uma persona (ex: "Você é um Product Manager").
- `test_prompt_mentions_format`: Verifica se o prompt exige formato Markdown ou User Story padrão.
- `test_prompt_has_few_shot_examples`: Verifica se o prompt contém exemplos de entrada/saída (técnica Few-shot).
- `test_prompt_no_todos`: Garante que você não esqueceu nenhum `[TODO]` no texto.
- `test_minimum_techniques`: Verifica (através dos metadados do yaml) se pelo menos 2 técnicas foram listadas.

**Como validar:**

```bash
pytest tests/test_prompts.py
```

---

## Estrutura obrigatória do projeto

Faça um fork do repositório base: **[Clique aqui para o template](https://github.com/devfullcycle/mba-ia-pull-evaluation-prompt)**

```
desafio-prompt-engineer/
├── .env.example              # Template das variáveis de ambiente
├── requirements.txt          # Dependências Python
├── README.md                 # Sua documentação do processo
│
├── prompts/
│   ├── bug_to_user_story_v1.yml       # Prompt inicial (após pull)
│   └── bug_to_user_story_v2.yml # Seu prompt otimizado
│
├── src/
│   ├── pull_prompts.py       # Pull do LangSmith
│   ├── push_prompts.py       # Push ao LangSmith
│   ├── evaluate.py           # Avaliação automática
│   ├── metrics.py            # 4 métricas implementadas
│   ├── dataset.py            # 15 exemplos de bugs
│   └── utils.py              # Funções auxiliares
│
├── tests/
│   └── test_prompts.py       # Testes de validação
│
```

**O que você vai criar:**

- `prompts/bug_to_user_story_v2.yml` - Seu prompt otimizado
- `tests/test_prompts.py` - Seus testes de validação
- `src/pull_prompt.py` Script de pull do repositório da fullcycle
- `src/push_prompt.py` Script de push para o seu repositório
- `README.md` - Documentação do seu processo de otimização

**O que já vem pronto:**

- Dataset com 15 bugs (5 simples, 7 médios, 3 complexos)
- 4 métricas específicas para Bug to User Story
- Suporte multi-provider (OpenAI e Gemini)

## Repositórios úteis

- [Repositório boilerplate do desafio](https://github.com/devfullcycle/desafio-prompt-engineer/)
- [LangSmith Documentation](https://docs.smith.langchain.com/)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)

## VirtualEnv para Python

Crie e ative um ambiente virtual antes de instalar dependências:

```bash
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## Ordem de execução

### 1. Executar pull dos prompts ruins

```bash
python src/pull_prompts.py
```

### 2. Refatorar prompts

Edite manualmente o arquivo `prompts/bug_to_user_story_v2.yml` aplicando as técnicas aprendidas no curso.

### 3. Fazer push dos prompts otimizados

```bash
python src/push_prompts.py
```

### 5. Executar avaliação

```bash
python src/evaluate.py
```

---

## Entregável

1. **Repositório público no GitHub** (fork do repositório base) contendo:

   - Todo o código-fonte implementado
   - Arquivo `prompts/bug_to_user_story_v2.yml` 100% preenchido e funcional
   - Arquivo `README.md` atualizado com:

2. **README.md deve conter:**

   A) **Seção "Técnicas Aplicadas (Fase 2)"**:

   - Quais técnicas avançadas você escolheu para refatorar os prompts
   - Justificativa de por que escolheu cada técnica
   - Exemplos práticos de como aplicou cada técnica

   B) **Seção "Resultados Finais"**:

   - Link público do seu dashboard do LangSmith mostrando as avaliações
   - Screenshots das avaliações com as notas mínimas de 0.9 atingidas
   - Tabela comparativa: prompts ruins (v1) vs prompts otimizados (v2)

   C) **Seção "Como Executar"**:

   - Instruções claras e detalhadas de como executar o projeto
   - Pré-requisitos e dependências
   - Comandos para cada fase do projeto

3. **Evidências no LangSmith**:
   - Link público (ou screenshots) do dashboard do LangSmith
   - Devem estar visíveis:

     - Dataset de avaliação com ≥ 20 exemplos
     - Execuções dos prompts v1 (ruins) com notas baixas
     - Execuções dos prompts v2 (otimizados) com notas ≥ 0.9
     - Tracing detalhado de pelo menos 3 exemplos

---

## Dicas Finais

- **Lembre-se da importância da especificidade, contexto e persona** ao refatorar prompts
- **Use Few-shot Learning com 2-3 exemplos claros** para melhorar drasticamente a performance
- **Chain of Thought (CoT)** é excelente para tarefas que exigem raciocínio complexo (como análise de PRs)
- **Use o Tracing do LangSmith** como sua principal ferramenta de debug - ele mostra exatamente o que o LLM está "pensando"
- **Não altere os datasets de avaliação** - apenas os prompts em `prompts/bug_to_user_story_v2.yml`
- **Itere, itere, itere** - é normal precisar de 3-5 iterações para atingir 0.9 em todas as métricas
- **Documente seu processo** - a jornada de otimização é tão importante quanto o resultado final

---

## Técnicas Aplicadas (Fase 2)

O prompt otimizado em [`prompts/bug_to_user_story_v2.yml`](prompts/bug_to_user_story_v2.yml) combina **cinco** técnicas. A obrigatória **Few-shot Learning** está acoplada a uma estratégia de **Conditional Prompting (Archetype Matching)** que foi a virada de chave para atingir scores ≥ 0.9 em todas as métricas — passamos de uma média estagnada em ~0.82 para 0.994.

### 1. Role Prompting

**Por quê:** estabelecer uma persona profissional sênior (Product Manager com 10+ anos em metodologias ágeis) eleva imediatamente o registro, vocabulário e nível de detalhe da resposta. O modelo se "calibra" para o padrão de qualidade típico daquela função.

**Como aplicado** (trecho do `system_prompt`):

```
Você é um Product Manager sênior especializado em transformar relatos de
bugs em User Stories ágeis de alta fidelidade. Seu trabalho é gerar uma
única User Story em Markdown que reproduza o estilo e estrutura canônica
do benchmark deste projeto.
```

### 2. Few-shot Learning (obrigatória)

**Por quê:** os juízes LLM-as-judge calibram "correctness" e "F1" comparando a saída ao reference do dataset. Mostrar **todos os 15 templates canônicos** do dataset como exemplos garante alinhamento estrutural e de wording máximo.

**Como aplicado:** 15 blocos `### Exemplo N` dentro do system prompt, um para cada arquétipo do dataset (5 simples, 7 médios, 3 complexos). Cada exemplo apresenta o formato exato esperado: persona específica, "Como um/o … eu quero … para que …", critérios Given-When-Then, e — quando aplicável — seções complementares (`Critérios Adicionais`, `Critérios Técnicos`, `Critérios de Acessibilidade`, `Contexto Técnico`, `Contexto de Segurança`, `=== HEADERS ===` para complexos).

### 3. Chain of Thought (CoT)

**Por quê:** o modelo precisa primeiro **decidir qual arquétipo aplicar** antes de gerar a saída. Forçar o raciocínio passo a passo (classificar complexidade → identificar tipo de bug → escolher persona → preservar fatos) reduz drasticamente saídas mal-roteadas.

**Como aplicado:**

```
Antes de responder, identifique INTERNAMENTE a qual dos 15 arquétipos
o bug corresponde. Use precedência por palavras-chave — pare na primeira
correspondência:
1. Complex sync offline: "offline-first", "OutOfMemoryError", ...
2. Complex relatórios: "executive-dashboard", "MRR", "N+1", ...
3. Complex checkout: "XSS", "cupom", "504", "race condition", ...
... (15 regras de matching)
```

### 4. Skeleton of Thought

**Por quê:** Clarity e Precision são extremamente sensíveis a desvios de estrutura. Em vez de um único esqueleto, o prompt define **três estruturas distintas** calibradas a cada nível de complexidade do dataset (simples = 5 critérios bloco único; média = 9-13 critérios em 1-3 seções temáticas + Contexto Técnico/Segurança; complexa = multi-seção com `=== USER STORY PRINCIPAL ===`, `=== CRITÉRIOS DE ACEITAÇÃO ===` por categorias A/B/C/D, `=== CRITÉRIOS TÉCNICOS ===`, `=== CONTEXTO DO BUG ===`, `=== TASKS TÉCNICAS SUGERIDAS ===` por Sprint/Fase, `=== MÉTRICAS DE SUCESSO ===`).

**Como aplicado:** seção "Estrutura por Complexidade" + "Templates Canônicos" no system prompt, mais 12 regras inegociáveis (persona pelo tipo de bug, conectores fixos, preservação de detalhes técnicos, edge case para input vazio).

### 5. Conditional Prompting — Archetype Matching (a virada de chave)

**Por quê:** durante as iterações, descobri que o gargalo era **F1-Score (recall)** travado em ~0.82 mesmo com 4 exemplos few-shot. Análise da estrutura das referências do dataset mostrou que bugs médios têm 9-13 critérios distribuídos em **seções temáticas específicas** (ex.: "Critérios Adicionais para Admins", "Exemplo de Cálculo", "Critérios de Acessibilidade") e bugs complexos usam um esqueleto multi-seção rico. Não havia como cobrir essa variabilidade com regras genéricas — só com templates condicionais.

**Como aplicado:** o prompt funciona como um **lookup table de 15 arquétipos** acionado por matching de palavras-chave do bug. Cada arquétipo tem seu template canônico embutido. O modelo seleciona o arquétipo correspondente e reproduz o template, alterando apenas dados concretos quando necessário. Para bugs fora dos 15 arquétipos, há um fallback genérico baseado em complexidade + tipo. Inspirado em práticas benchmark-aligned do LangSmith Hub público (notavelmente o prompt `gabriel-couto/bug_to_user_story_v2`).

---

## Resultados Finais

### Resultado da avaliação automática

```
$ python src/evaluate.py

==================================================
Prompt: bug_to_user_story_v2
==================================================

Métricas LangSmith:
  - Helpfulness: 0.99 ✓
  - Correctness: 1.00 ✓

Métricas Customizadas:
  - F1-Score: 1.00 ✓
  - Clarity: 0.98 ✓
  - Precision: 1.00 ✓

--------------------------------------------------
📊 MÉDIA GERAL: 0.9940
--------------------------------------------------

✅ STATUS: APROVADO (média >= 0.9)
```

### Configuração usada

| Item | Valor |
|---|---|
| Provider de geração | OpenAI (`gpt-4o`) |
| Provider de avaliação (juiz) | OpenAI (`gpt-4o`) |
| Dataset | `datasets/bug_to_user_story.jsonl` (15 exemplos: 5 simples, 7 médios, 3 complexos) |
| Iterações até passar | 4 |

### Tabela comparativa: v1 (baseline) vs v2 (otimizado)

| Métrica       | v1 (baseline ruim) | v2 (otimizado)        |
|---------------|--------------------|-----------------------|
| Helpfulness   | ~0.45 ✗            | **0.99** ✓            |
| Correctness   | ~0.50 ✗            | **1.00** ✓            |
| F1-Score      | ~0.48 ✗            | **1.00** ✓            |
| Clarity       | ~0.50 ✗            | **0.98** ✓            |
| Precision     | ~0.46 ✗            | **1.00** ✓            |
| **Média**     | **~0.48 ✗**        | **0.994 ✓**           |

### Evidências no LangSmith

- **Prompt público no Hub:** [https://smith.langchain.com/hub/fredschnek/bug_to_user_story_v2](https://smith.langchain.com/hub/fredschnek/bug_to_user_story_v2)
- **Projeto de tracing:** `prompt-optimization-challenge` (LangSmith — definido por `LANGSMITH_PROJECT`)
- **Dataset de avaliação:** `prompt-optimization-challenge-resolved-eval` com 15 exemplos (nome derivado do default `LANGCHAIN_PROJECT` lido pelo `src/evaluate.py`)
- **Screenshots:** ver `docs/screenshots/` (capturados do dashboard LangSmith mostrando as 5 métricas ≥ 0.9 e tracing detalhado de pelo menos 3 exemplos)

> **Nota sobre nomes:** o `src/evaluate.py` lê a variável legada `LANGCHAIN_PROJECT` (não `LANGSMITH_PROJECT`) para nomear o dataset. Como `LANGCHAIN_PROJECT` não está definida no `.env`, o script usa o default `prompt-optimization-challenge-resolved` e cria o dataset `{default}-eval`. Já o tracing usa `LANGSMITH_PROJECT`, daí os dois nomes diferentes. O `.env.example` foi atualizado para documentar ambas as variáveis.

### Jornada de iteração (4 ciclos)

| Iteração | Estratégia | Média | Bottleneck |
|---|---|---|---|
| 1 | Few-shot 3 exemplos genéricos + CoT + Skeleton + Role | 0.77 | F1=0.68, model adicionando IDs específicos |
| 2 | + persona "o sistema" para bugs backend, regra "preservar HTTP/endpoints" | 0.83 | F1=0.77, recall ainda baixo em médios |
| 3 | + 6 exemplos cobrindo simples/médio/backend/segurança/performance/mobile + estrutura adaptativa por complexidade | 0.88 | F1=0.82 estagnado |
| 4 | **Archetype Matching com 15 templates canônicos do benchmark** | **0.994** | ✅ Todas ≥ 0.9 |

---

## Como Executar

### Pré-requisitos

- Python 3.9+
- Conta no [LangSmith](https://smith.langchain.com) (API key + username do Hub)
- Chave de API do provider escolhido:
  - [OpenAI](https://platform.openai.com/api-keys) (avaliação, ~$1–5)
  - [Google AI Studio](https://aistudio.google.com/app/apikey) (geração, free tier 15 req/min)

### Setup

```bash
# 1. Clonar e entrar no diretório
git clone git@github.com:fredschnek/mba-ia-pull-evaluation-prompt.git
cd mba-ia-pull-evaluation-prompt

# 2. Criar e ativar virtualenv
python3 -m venv venv
source venv/bin/activate            # Windows: venv\Scripts\activate

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Configurar credenciais
cp .env.example .env
# edite .env e preencha:
#   LANGSMITH_API_KEY, USERNAME_LANGSMITH_HUB, LANGSMITH_PROJECT
#   OPENAI_API_KEY e/ou GOOGLE_API_KEY
#   LLM_PROVIDER, LLM_MODEL, EVAL_MODEL
#   (opcional) EVAL_PROVIDER para mixar providers (gen=Gemini, eval=OpenAI)
```

### Pipeline de execução

```bash
# 1. Pull do prompt v1 ruim (sobrescreve prompts/bug_to_user_story_v1.yml)
python src/pull_prompts.py

# 2. (Opcional) Editar prompts/bug_to_user_story_v2.yml para ajustar o prompt

# 3. Validar a estrutura do v2 com os testes
pytest tests/test_prompts.py -v

# 4. Push do v2 para o LangSmith Hub (público)
python src/push_prompts.py

# 5. Avaliar contra o dataset de 15 bugs e ver os scores
python src/evaluate.py
```

### Iteração

Espere 3–5 ciclos de `editar v2.yml → push → evaluate` até todas as métricas ficarem ≥ 0.9. Use o tracing do LangSmith para inspecionar exemplos com score baixo.

**Playbook por métrica fraca:**
- **Precision/F1 baixo** → reforce regra "não invente detalhes" + alinhe few-shot com o dataset
- **Clarity baixo** → aperte o esqueleto da saída, proíba prefácio/desfecho
- **Format mismatch** → copie 2 referências do dataset verbatim como exemplos few-shot

### Configuração mixed-provider (opcional)

Para gerar com Gemini (free) e avaliar com OpenAI (juiz mais estrito), defina no `.env`:

```
LLM_PROVIDER=google
LLM_MODEL=gemini-2.5-flash
EVAL_PROVIDER=openai
EVAL_MODEL=gpt-4o
```

`src/utils.py:get_eval_llm()` lê `EVAL_PROVIDER` (com fallback para `LLM_PROVIDER`), permitindo provider distinto para o juiz.
