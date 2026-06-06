# album.py
# Album de figurinhas implementado com lista encadeada propria (NodoLista)
# Proibido usar list, deque ou qualquer estrutura pronta do Python na lista

from figurinha import Figurinha
from nodos import NodoLista

class Album:
    def __init__(self, total_figurinhas: int = 670):
        if not isinstance(total_figurinhas, int) or total_figurinhas <= 0:
            raise ValueError("Total de figurinhas do album deve ser um inteiro positivo.")
        self._cabeca: NodoLista | None = None
        self._tamanho: int = 0
        self.total_figurinhas: int = total_figurinhas

    # ------------------------------------------------------------------ inserir

    def adicionar(self, figurinha: Figurinha) -> None:
        """Insere figurinha no album. Nao permite ID duplicado."""
        if self.buscar_por_id(figurinha.id) is not None:
            raise ValueError(
                f"Figurinha {figurinha.id} ja esta no album. "
                "Use o repositorio de repetidas para guarda-la."
            )
        novo = NodoLista(figurinha)
        # Insere em ordem crescente de ID
        if self._cabeca is None or figurinha.id < self._cabeca.figurinha.id:
            novo.proximo = self._cabeca
            self._cabeca = novo
        else:
            atual = self._cabeca
            while atual.proximo is not None and atual.proximo.figurinha.id < figurinha.id:
                atual = atual.proximo
            novo.proximo = atual.proximo
            atual.proximo = novo
        self._tamanho += 1

    # ------------------------------------------------------------------ remover

    def remover(self, id: int) -> Figurinha:
        """Remove e retorna a figurinha com o ID informado."""
        anterior = None
        atual = self._cabeca
        while atual is not None:
            if atual.figurinha.id == id:
                if anterior is None:
                    self._cabeca = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                self._tamanho -= 1
                return atual.figurinha
            anterior = atual
            atual = atual.proximo
        raise KeyError(f"Figurinha {id} nao encontrada no album.")

    # ------------------------------------------------------------------ buscas

    def buscar_por_id(self, id: int) -> Figurinha | None:
        """Retorna a figurinha com o ID informado ou None."""
        atual = self._cabeca
        while atual is not None:
            if atual.figurinha.id == id:
                return atual.figurinha
            atual = atual.proximo
        return None

    def buscar_por_jogador(self, nome: str) -> list:
        """Retorna lista de figurinhas cujo nome contem o termo buscado."""
        termo = nome.strip().lower()
        resultado = []
        atual = self._cabeca
        while atual is not None:
            if termo in atual.figurinha.nome.lower():
                resultado.append(atual.figurinha)
            atual = atual.proximo
        return resultado

    def buscar_por_selecao(self, pais: str) -> list:
        """Retorna todas as figurinhas de um pais."""
        termo = pais.strip().lower()
        resultado = []
        atual = self._cabeca
        while atual is not None:
            if termo in atual.figurinha.pais.lower():
                resultado.append(atual.figurinha)
            atual = atual.proximo
        return resultado

    # ------------------------------------------------------------------ exibir

    def listar_todas(self) -> list:
        """Retorna lista Python com todas as figurinhas (somente para exibicao)."""
        resultado = []
        atual = self._cabeca
        while atual is not None:
            resultado.append(atual.figurinha)
            atual = atual.proximo
        return resultado

    def porcentagem_concluida(self) -> float:
        """Retorna o percentual do album preenchido."""
        return round((self._tamanho / self.total_figurinhas) * 100, 2)

    def tamanho(self) -> int:
        return self._tamanho

    def esta_vazio(self) -> bool:
        return self._tamanho == 0
