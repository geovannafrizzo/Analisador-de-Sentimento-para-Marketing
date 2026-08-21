"""
Analisador de Sentimento - Versão Simples
-------------------------------------------
Classifica comentários em positivo, negativo ou neutro usando
uma lista de palavras-chave. Não precisa de API nem de internet.

Ideal para: social listening básico, triagem rápida de comentários
de redes sociais, reviews de produtos, pesquisas de satisfação.

Como usar:
    python analisador_simples.py
"""

import csv
from collections import Counter

# Palavras que indicam sentimento positivo ou negativo
PALAVRAS_POSITIVAS = [
    "adorei", "ótimo", "ótima", "excelente", "recomendo", "perfeito",
    "perfeita", "maravilhoso", "maravilhosa", "gostei", "bom", "boa",
    "rápido", "rápida", "atencioso", "atenciosa", "superou", "nota 10",
    "sem problemas", "certinho", "voltarei"
]

PALAVRAS_NEGATIVAS = [
    "péssimo", "péssima", "decepcionado", "decepcionada", "quebrado",
    "defeito", "horrível", "insatisfeito", "insatisfeita", "demorou",
    "não gostei", "nunca mais", "ruim", "atrasado", "problema"
]


def classificar_comentario(texto):
    """Classifica um comentário como positivo, negativo ou neutro."""
    texto_lower = texto.lower()

    pontos_positivos = sum(1 for palavra in PALAVRAS_POSITIVAS if palavra in texto_lower)
    pontos_negativos = sum(1 for palavra in PALAVRAS_NEGATIVAS if palavra in texto_lower)

    if pontos_positivos > pontos_negativos:
        return "Positivo"
    elif pontos_negativos > pontos_positivos:
        return "Negativo"
    else:
        return "Neutro"


def analisar_csv(caminho_arquivo):
    """Lê um CSV com comentários e retorna a classificação de cada um."""
    resultados = []

    with open(caminho_arquivo, encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            comentario = linha["comentario"]
            sentimento = classificar_comentario(comentario)
            resultados.append((comentario, sentimento))

    return resultados


def exibir_resumo(resultados):
    """Mostra os resultados individuais e um resumo geral."""
    print("=" * 60)
    print("RESULTADO DA ANÁLISE")
    print("=" * 60)

    for comentario, sentimento in resultados:
        emoji = {"Positivo": "🟢", "Negativo": "🔴", "Neutro": "🟡"}[sentimento]
        print(f"{emoji} [{sentimento}] {comentario}")

    print("\n" + "=" * 60)
    print("RESUMO GERAL")
    print("=" * 60)

    contagem = Counter(sentimento for _, sentimento in resultados)
    total = len(resultados)

    for sentimento in ["Positivo", "Negativo", "Neutro"]:
        qtd = contagem.get(sentimento, 0)
        porcentagem = (qtd / total * 100) if total else 0
        print(f"{sentimento}: {qtd} ({porcentagem:.1f}%)")


if __name__ == "__main__":
    resultados = analisar_csv("dados/comentarios_exemplo.csv")
    exibir_resumo(resultados)
