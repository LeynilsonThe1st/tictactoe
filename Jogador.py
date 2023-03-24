class Jogador:
    nome: str
    simbolo: str
    
    def __str__(self) -> str:
        return f"{self.nome} ({self.simbolo})"
    
    def __repr__(self) -> str:
        return f"{self.nome} ({self.simbolo})"