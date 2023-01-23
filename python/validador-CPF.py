cpf = '11122233396'
numeroDigitoVerificador1 = 0
numeroDigitoVerificador2 = 0
checagemDigitoVerificador1 = 0
checagemDigitoVerificador2 = 0
i = 1

if len(cpf) < 11:
    diferencaNumericaCPF = 11 - len(cpf)
    cpf = '0' * diferencaNumericaCPF + cpf

checagemDigitoVerificador1 = int(cpf[9:10])
checagemDigitoVerificador2 = int(cpf[10:11])

for i in range(1, 10):
    numeroDigitoVerificador1 = numeroDigitoVerificador1 + int(cpf[i-1:i]) * i

numeroDigitoVerificador1 = numeroDigitoVerificador1 % 11

if (numeroDigitoVerificador1 == 10):
    numeroDigitoVerificador1 = 0

if numeroDigitoVerificador1 != checagemDigitoVerificador1:
    print('1º Digíto verificador do CPF informado inválido! ❌')

for i in range(2, 11):
    numeroDigitoVerificador2 = numeroDigitoVerificador2 + int(cpf[i-1:i]) * (i - 1)

numeroDigitoVerificador2 = numeroDigitoVerificador2 % 11

if (numeroDigitoVerificador2 == 10):
    numeroDigitoVerificador2 = 0

if numeroDigitoVerificador2 != checagemDigitoVerificador2:
    print('2º Digíto verificador do CPF informado inválido! ❌')

if (numeroDigitoVerificador1 == checagemDigitoVerificador1 and numeroDigitoVerificador2 == checagemDigitoVerificador2):
    print('CPF válido! ✅')
    