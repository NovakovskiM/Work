from dataclasses import dataclass
from typing import List

# ================= EXCEÇÕES PERSONALIZADAS =================

class MoradorNaoEncontrado(Exception):
    pass

class PagamentoJaRealizado(Exception):
    pass


# ================= DATACLASS =================

@dataclass
class Endereco:
    rua: str
    numero: int


# ================= HERANÇA =================

class Pessoa:
    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.cpf = cpf

    def apresentar(self):
        return f"Pessoa: {self.nome}"


class Usuario(Pessoa):
    def __init__(self, nome: str, cpf: str, login: str):
        super().__init__(nome, cpf)
        self.login = login

    def apresentar(self):
        return f"Usuário: {self.nome}"


class Morador(Usuario):
    def __init__(self, nome: str, cpf: str, login: str, apartamento: str):
        super().__init__(nome, cpf, login)
        self.apartamento = apartamento

    def apresentar(self):
        return f"Morador: {self.nome} - Ap {self.apartamento}"


# ================= HERANÇA MÚLTIPLA =================

class Financeiro:
    def calcular_taxa(self):
        return 100.0


class MoradorFinanceiro(Morador, Financeiro):
    pass


# ================= PAGAMENTO =================

class Pagamento:
    def __init__(self, morador: Morador, valor: float):
        self.morador = morador
        self.valor = valor
        self.pago = False

    def pagar(self):
        if self.pago:
            raise PagamentoJaRealizado("Pagamento já foi feito!")
        self.pago = True

    def __str__(self):
        status = "Pago" if self.pago else "Pendente"
        return f"{self.morador.nome} - R${self.valor} - {status}"


# ================= SISTEMA =================

class Sistema:
    def __init__(self):
        self.moradores: List[Morador] = []
        self.pagamentos: List[Pagamento] = []

    def buscar_morador(self, cpf: str) -> Morador:
        lista = [m for m in self.moradores if m.cpf == cpf]

        if not lista:
            raise MoradorNaoEncontrado("Morador não encontrado!")

        return lista[0]

    def cadastrar_morador(self):
        try:
            nome = input("Nome: ")
            cpf = input("CPF: ")
            login = input("Login: ")
            ap = input("Apartamento: ")

            morador = Morador(nome, cpf, login, ap)
            self.moradores.append(morador)

            print("✅ Morador cadastrado!")

        except Exception as e:
            print("Erro:", e)

    def listar_moradores(self):
        for m in self.moradores:
            print(m.apresentar())

    def gerar_pagamento(self):
        try:
            cpf = input("CPF: ")
            valor = float(input("Valor: "))

            morador = self.buscar_morador(cpf)
            pagamento = Pagamento(morador, valor)

            self.pagamentos.append(pagamento)
            print("💰 Pagamento criado!")

        except Exception as e:
            print("Erro:", e)

    def pagar(self):
        try:
            cpf = input("CPF: ")
            morador = self.buscar_morador(cpf)

            for p in self.pagamentos:
                if p.morador == morador:
                    p.pagar()
                    print("✅ Pago!")
                    return

            print("Nenhum pagamento encontrado.")

        except Exception as e:
            print("Erro:", e)

    def listar_pagamentos(self):
        for p in self.pagamentos:
            print(p)


# ================= MENU =================

def menu():
    sistema = Sistema()

    while True:
        print("\n===== CONDOMÍNIO =====")
        print("1 - Cadastrar Morador")
        print("2 - Listar Moradores")
        print("3 - Gerar Pagamento")
        print("4 - Pagar")
        print("5 - Listar Pagamentos")
        print("0 - Sair")

        opcao = input("Opção: ")

        match opcao:
            case "1":
                sistema.cadastrar_morador()
            case "2":
                sistema.listar_moradores()
            case "3":
                sistema.gerar_pagamento()
            case "4":
                sistema.pagar()
            case "5":
                sistema.listar_pagamentos()
            case "0":
                break
            case _:
                print("❌ Opção inválida")


menu()
