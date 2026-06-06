from figurinha import Figurinha


class NodoLista:
    def __init__(self, figurinha: Figurinha):
        self.figurinha: Figurinha = figurinha
        self.proximo: "NodoLista | None" = None


class NodoFila:
    def __init__(self, figurinha: Figurinha):
        self.figurinha: Figurinha = figurinha
        self.proximo: "NodoFila | None" = None
