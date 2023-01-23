class DocumentoFiscal:
    def __init__(self):
        self.numeroDigitoVerificador1 = []
        self.numeroDigitoVerificador2 = []

    def calcularDigitoVerificador(self, documento, digito=1):
        pass

    def valido(self, documento):

        documento = documento.replace('.', '').replace('/', '').replace('-', '')

        if (not documento.isnumeric()):
            return False

        digitos = None

        if (len(documento) == 11):
            digitos = documento[:9]
        elif (len(documento) == 14):
            digitos = documento[:12]
        else:
            return False

        digitoVerificador1 = self.calcularDigitoVerificador(digitos, 1)
        digitoVerificador2 = self.calcularDigitoVerificador(digitos + str(digitoVerificador1), 2)

        return documento == digitos + str(digitoVerificador1) + str(digitoVerificador2)
        