from typing import Type

class Cidade:
    # Constructor
    def __init__(self, id: Type[int], nome: Type[str], pais: Type[str]) -> Type[None]:
        self._id = id
        self._nome = nome
        self._pais = pais

    # Getter para id
    @property
    def id(self):
        return self._id

    # Getter para nome
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    # Getter para pais
    @property
    def pais(self):
        return self._pais

    # Setter para pais
    @pais.setter
    def pais(self, novo_pais):
        self._pais = novo_pais

    def __str__(self):
        return f"Cidade(id={self._id}, nome='{self._nome}', pais='{self._pais}')"
