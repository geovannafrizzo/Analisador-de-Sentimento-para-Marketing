"""
Analisador de Sentimento - Versão com IA
-------------------------------------------
Classifica comentários usando a API da Anthropic (Claude), com
mais precisão que a versão baseada em palavras-chave — entende
ironia, contexto e frases mais complexas.

Requer:
    pip install anthropic
    Uma chave de API da Anthropic (console.anthropic.com)

Como usar:
    export ANTHROPIC_API_KEY="sua-chave-aqui"
    python analisador_ia.py
"""

import csv
import json
import os
import time

import anthropic

client = anthropic.Anthropic()  # lê a chave da variável ANTHROPIC_API_KEY

PROMPT_SISTEMA = """Você é um analista de sentimento especializado em marketing.
Classifique o comentário abaixo em uma das categorias: Positivo, Negativo ou Neutro.

Responda APENAS em formato JSON, sem nenhum texto adicional, no formato:
{"sentimento": "Positivo", "motivo": "breve explicação em até 10 palavras"}
"""


def classificar_com_ia(comentario):
    """Envia o comentário para o Claude e retorna a classificação."""
    resposta = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=100,
        system=PROMPT_SISTEMA,
        messages=[{"role": "user", "content": comentario}],
    )

    texto = resposta.content[0].text.strip()

    try:
        dados = json.loads(texto)
        return dados["sentimento"], dados.get("motivo", "")
    except (json.JSONDecodeError, KeyError):
        return "Erro", "não foi possível interpretar a resposta"


def analisar_csv(caminho_arquivo):
    """Lê um CSV com comentários e classifica cada um usando IA."""
    resultados = []

    with open(caminho_arquivo, encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            comentario = linha["comentario"]
            sentimento, motivo = classificar_com_ia(comentario)
            resultados.append((comentario, sentimento, motivo))
            time.sleep(0.3)  # evita ultrapassar limites de requisição

    return resultados


def exibir_resumo(resultados):
    """Mostra os resultados individuais e um resumo geral."""
    print("=" * 70)
    print("RESULTADO DA ANÁLISE (via Claude)")
    print("=" * 70)

    for comentario, sentimento, motivo in resultados:
        emoji = {"Positivo": "🟢", "Negativo": "🔴", "Neutro": "🟡"}.get(sentimento, "⚪")
        print(f"{emoji} [{sentimento}] {comentario}")
        if motivo:
            print(f"   → {motivo}")

    print("\n" + "=" * 70)
    print("RESUMO GERAL")
    print("=" * 70)

    from collections import Counter
    contagem = Counter(sentimento for _, sentimento, _ in resultados)
    total = len(resultados)

    for sentimento in ["Positivo", "Negativo", "Neutro"]:
        qtd = contagem.get(sentimento, 0)
        porcentagem = (qtd / total * 100) if total else 0
        print(f"{sentimento}: {qtd} ({porcentagem:.1f}%)")


if __name__ == "__main__":
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("⚠️  Defina a variável ANTHROPIC_API_KEY antes de rodar este script.")
        print('   Exemplo: export ANTHROPIC_API_KEY="sua-chave-aqui"')
    else:
        resultados = analisar_csv("dados/comentarios_exemplo.csv")
        exibir_resumo(resultados)
