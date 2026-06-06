# fila.py
# Implementacao propria de fila FIFO usando NodoFila encadeado
# Proibido usar list, deque ou qualquer estrutura pronta do Python

from figurinha import Figurinha
from nodos import NodoFila


class Fila:
    def __init__(self):
        self._inicio: NodoFila | None = None
        self._fim: NodoFila | None = None
        self._tamanho: int = 0

    def enqueue(self, figurinha: Figurinha) -> None:
        """Insere figurinha no fim da fila."""
        novo = NodoFila(figurinha)
        if self._fim is None:
            self._inicio = novo
            self._fim = novo
        else:
            self._fim.proximo = novo
            self._fim = novo
        self._tamanho += 1

    def dequeue(self) -> Figurinha:
        """Remove e retorna a figurinha do inicio da fila."""
        if self._inicio is None:
            raise IndexError("Fila vazia. Nenhuma figurinha para remover.")
        figurinha = self._inicio.figurinha
        self._inicio = self._inicio.proximo
        if self._inicio is None:
            self._fim = None
        self._tamanho -= 1
        return figurinha

    def peek(self) -> Figurinha:
        """Retorna a figurinha do inicio sem remover."""
        if self._inicio is None:
            raise IndexError("Fila vazia.")
        return self._inicio.figurinha

    def limpar(self) -> None:
        """Esvazia a fila."""
        self._inicio = None
        self._fim = None
        self._tamanho = 0

    def esta_vazia(self) -> bool:
        return self._tamanho == 0

    def tamanho(self) -> int:
        return self._tamanho

    def listar(self) -> list:
        """Retorna lista Python com todas as figurinhas (apenas para exibicao)."""
        resultado = []
        atual = self._inicio
        while atual is not None:
            resultado.append(atual.figurinha)
            atual = atual.proximo
        return resultado

    def contem_id(self, id: int) -> bool:
        """Verifica se existe figurinha com o id informado."""
        atual = self._inicio
        while atual is not None:
            if atual.figurinha.id == id:
                return True
            atual = atual.proximo
        return False

    def remover_por_id(self, id: int) -> Figurinha | None:
        """Remove e retorna a primeira figurinha com o id informado."""
        anterior = None
        atual = self._inicio
        while atual is not None:
            if atual.figurinha.id == id:
                if anterior is None:
                    self._inicio = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                if atual == self._fim:
                    self._fim = anterior
                self._tamanho -= 1
                return atual.figurinha
            anterior = atual
            atual = atual.proximo
        return None
