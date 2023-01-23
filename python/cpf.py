from documento_fiscal import DocumentoFiscal


class Cpf(DocumentoFiscal):
    def __init__(self):
        self.numeroDigitoVerificador1 = range(10, 0, -1)
        self.numeroDigitoVerificador2 = range(11, 0, -1)

    def calcularDigitoVerificador(self, cpf, digito=1):
        numeros = self.numeroDigitoVerificador1 if digito == 1 else self.numeroDigitoVerificador2
        resultado = (sum(int(digito) * numero for digito, numero in zip(cpf, numeros)))
        resultado = (resultado * 10) % 11
        return 0 if resultado == 10 else resultado
        