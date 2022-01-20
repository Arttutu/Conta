class Conta:

    def __init__(self, numero, saldo, titular, limite):
        print("contruindo...")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite


    def extrato(self):
        print("O titular {} tem {} de saldo na conta".format(self.__titular, self.__saldo))

    def sacar(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
            print("Saque Efetuado")
        else:
            print("Não é possível sacar o valor {}".format(valor))
            print("saque falhou")

    def __pode_sacar(self, valor_de_saque):
        disponivel_para_saque = self.__limite + self.__saldo
        return valor_de_saque <= disponivel_para_saque

    def depositar(self, valor):
        self.saldo += valor

    def transfere(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self, limite):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        self.__limite = valor

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigo_bancos():
        return {"bb":'001', "Bradesco":'237'}

