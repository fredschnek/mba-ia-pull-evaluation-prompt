# Screenshots — Evidências da avaliação no LangSmith

Capturas do dashboard LangSmith comprovando que o prompt otimizado
[`fredschnek/bug_to_user_story_v2`](https://smith.langchain.com/hub/fredschnek/bug_to_user_story_v2)
atinge ≥ 0.9 em todas as 5 métricas de avaliação.

| # | Arquivo | O que mostra |
|---|---|---|
| 01 | [`01-tracing-runs.png`](01-tracing-runs.png) | Projeto de tracing `prompt-optimization-challenge` no LangSmith com o histórico de runs de geração e dos juízes (F1, Clarity, Precision) executados durante `python src/evaluate.py`. |
| 02 | [`02-public-prompt.png`](02-public-prompt.png) | Página pública do prompt no LangSmith Hub (`fredschnek/bug_to_user_story_v2`), comprovando que está publicado e acessível sem autenticação. |
| 03 | [`03-dataset-examples.png`](03-dataset-examples.png) | Aba "Examples" do dataset `prompt-optimization-challenge-resolved-eval` mostrando os 15 bugs (5 simples, 7 médios, 3 complexos) usados na avaliação. |
| 04 | [`04-terminal-pass.png`](04-terminal-pass.png) | Saída do terminal de `python src/evaluate.py` com **STATUS: APROVADO** e as 5 métricas finais: Helpfulness 0.99, Correctness 1.00, F1-Score 1.00, Clarity 0.98, Precision 1.00 — média 0.994. |

## Links diretos

- Hub público: https://smith.langchain.com/hub/fredschnek/bug_to_user_story_v2
- Projeto de tracing: https://smith.langchain.com/o/a54d2e45-c09d-4951-a698-d49036b91bb3/projects/p/f88b26cf-234f-4c34-be79-c3e33917332c
- Dataset de avaliação: https://smith.langchain.com/o/a54d2e45-c09d-4951-a698-d49036b91bb3/datasets/1d4de0a3-c165-49e4-99aa-b3596edc2645
