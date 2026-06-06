from figurinha import Figurinha
from nodos import NodoFila


class Fila:
    def __init__(self):
        self._inicio: NodoFila | None = None
        self._fim: NodoFila | None = None
        self._tamanho: int = 0

    def enqueue(self, figurinha: Figurinha) -> None:
        novo = NodoFila(figurinha)
        if self._fim is None:
            self._inicio = novo
            self._fim = novo
        else:
            self._fim.proximo = novo
            self._fim = novo
        self._tamanho += 1

    def dequeue(self) -> Figurinha:
        if self._inicio is None:
            raise IndexError("Fila vazia. Nenhuma figurinha para remover.")
        figurinha = self._inicio.figurinha
        self._inicio = self._inicio.proximo
        if self._inicio is None:
            self._fim = None
        self._tamanho -= 1
        return figurinha

    def peek(self) -> Figurinha:
        if self._inicio is None:
            raise IndexError("Fila vazia.")
        return self._inicio.figurinha

    def limpar(self) -> None:
        self._inicio = None
        self._fim = None
        self._tamanho = 0

    def esta_vazia(self) -> bool:
        return self._tamanho == 0

    def tamanho(self) -> int:
        return self._tamanho

    def listar(self) -> list:
        resultado = []
        atual = self._inicio
        while atual is not None:
            resultado.append(atual.figurinha)
            atual = atual.proximo
        return resultado

    def contem_id(self, id: int) -> bool:
        atual = self._inicio
        while atual is not None:
            if atual.figurinha.id == id:
                return True
            atual = atual.proximo
        return False

    def remover_por_id(self, id: int) -> Figurinha | None:
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
