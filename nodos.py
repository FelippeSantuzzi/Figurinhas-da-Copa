# nodos.py
# Nos encadeados usados pelo Album (lista) e pela Fila FIFO
# Nenhuma estrutura pronta do Python e usada aqui

from figurinha import Figurinha


class NodoLista:
    """No da lista encadeada simples usada pelo Album."""

    def __init__(self, figurinha: Figurinha):
        self.figurinha: Figurinha = figurinha
        self.proximo: "NodoLista | None" = None


class NodoFila:
    """No da fila FIFO usada pelo Historico e Repositorio."""

    def __init__(self, figurinha: Figurinha):
        self.figurinha: Figurinha = figurinha
        self.proximo: "NodoFila | None" = None
