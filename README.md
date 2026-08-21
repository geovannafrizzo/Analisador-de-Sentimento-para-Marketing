# 📊 Analisador de Sentimento para Marketing

Projeto que classifica comentários de clientes (redes sociais, reviews, pesquisas de satisfação) em **Positivo**, **Negativo** ou **Neutro** — uma aplicação prática de análise de dados e IA para apoiar decisões de marketing e comunicação.

## 💡 Por que esse projeto?

Como profissional de marketing, entender rapidamente o que o público está falando sobre uma marca é essencial para social listening, gestão de crise e análise de campanhas. Este projeto simula esse processo de forma automatizada.

## 🚀 O que tem aqui

Duas versões do analisador:

| Versão | Como funciona | Requer API? |
|---|---|---|
| `analisador_simples.py` | Classificação por palavras-chave | ❌ Não |
| `analisador_ia.py` | Classificação via IA (Claude), entende contexto e ironia | ✅ Sim (paga) |

## 🛠️ Como usar

### Versão simples (recomendada para começar)

Roda direto, sem instalar nada além do Python:

```bash
python analisador_simples.py
```

### Versão com IA (opcional)

Essa versão usa a API da Anthropic, que é **paga por uso** (não tem plano gratuito) — é preciso criar uma conta em [platform.claude.com](https://platform.claude.com), cadastrar um cartão e gerar uma chave de API antes de rodar:

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY="sua-chave-aqui"
python analisador_ia.py
```

## 📁 Estrutura

```
analisador-sentimento-marketing/
├── analisador_simples.py     # versão sem API
├── analisador_ia.py          # versão com Claude
├── requirements.txt
├── dados/
│   └── comentarios_exemplo.csv
└── README.md
```

## 📈 Exemplo de saída

```
🟢 [Positivo] Adorei o atendimento, super rápido e atencioso!
🔴 [Negativo] Produto chegou quebrado, muito decepcionado com a compra.
🟡 [Neutro] Entrega dentro do prazo, sem problemas.

RESUMO GERAL
Positivo: 7 (46.7%)
Negativo: 5 (33.3%)
Neutro: 3 (20.0%)
```

## 🔮 Próximos passos

- [ ] Testar a versão com IA (`analisador_ia.py`) com uma conta de API
- [ ] Adicionar suporte para importar comentários direto do Instagram/Twitter via API
- [ ] Gerar gráfico de distribuição de sentimento
- [ ] Exportar resultados para um relatório em PDF

## 👩‍💻 Sobre

Projeto criado por [Geovanna Frizzo](https://www.linkedin.com/in/geovanna-frizzo-664000249/), estudante de Relações Públicas e profissional de marketing, explorando como IA pode apoiar o dia a dia de comunicação e marketing digital.
