# figurinha.py
# Entidade base do sistema de album de figurinhas Copa 2026

RARIDADES_VALIDAS = ("comum", "rara", "lendaria")

POSICOES_VALIDAS = (
    "goleiro", "zagueiro", "lateral", "volante",
    "meia", "atacante", "ponta"
)

class Figurinha:
    def __init__(self, id: int, nome: str, pais: str, posicao: str, raridade: str):
        if not isinstance(id, int) or id <= 0:
            raise ValueError(f"ID invalido: '{id}'. Deve ser um inteiro positivo.")

        nome = nome.strip()
        pais = pais.strip()
        posicao = posicao.strip().lower()
        raridade = raridade.strip().lower()

        if not nome:
            raise ValueError("Nome do jogador nao pode ser vazio.")
        if not pais:
            raise ValueError("Pais nao pode ser vazio.")
        if posicao not in POSICOES_VALIDAS:
            raise ValueError(
                f"Posicao invalida: '{posicao}'. "
                f"Validas: {', '.join(POSICOES_VALIDAS)}"
            )
        if raridade not in RARIDADES_VALIDAS:
            raise ValueError(
                f"Raridade invalida: '{raridade}'. "
                f"Validas: {', '.join(RARIDADES_VALIDAS)}"
            )

        self.id = id
        self.nome = nome
        self.pais = pais
        self.posicao = posicao
        self.raridade = raridade

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "nome": self.nome,
            "pais": self.pais,
            "posicao": self.posicao,
            "raridade": self.raridade
        }

    @staticmethod
    def from_dict(dados: dict) -> "Figurinha":
        return Figurinha(
            id=int(dados["id"]),
            nome=dados["nome"],
            pais=dados["pais"],
            posicao=dados["posicao"],
            raridade=dados["raridade"]
        )

    def __str__(self) -> str:
        return (
            f"[{self.id:03d}] {self.nome} | {self.pais} | "
            f"{self.posicao.capitalize()} | {self.raridade.capitalize()}"
        )

    def __repr__(self) -> str:
        return f"Figurinha(id={self.id}, nome='{self.nome}', pais='{self.pais}')"
