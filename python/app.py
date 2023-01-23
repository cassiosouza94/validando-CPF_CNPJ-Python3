from cpf import Cpf
from cnpj import Cnpj


validarCPF = Cpf()
print(validarCPF.valido('111.222.333-96'))

validarCNPJ = Cnpj()
print(validarCNPJ.valido('88.458.835/0001-30'))
