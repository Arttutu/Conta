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

# Chegou o Natal a melhor época do Ano  amor !! , é quando a gente  come muito, da risada com a família, comemora o nascimento de jesus
#, e claro recebe presestes como esse kkkk "emoji",  mais do que isso é quando a gente para e pensa tudo que vivemos esse ano, todas as dificulades
# e provações e  eu simplismente amo como conseguimos enfrentar tudo isso e permanecer juntos até esse momento tão aguarado. Estou ansioso para
# o que vem no próximo ano e motivado para fazer acontencer coisas incríveis nas nossas vida, mas é claro só quero isso se for com vc, que tal, você aceita passar
# o próximo natal comigo ?

 # te amo minha gata, desejo que tenha uma noite abençoada
 # Marry Chritisman