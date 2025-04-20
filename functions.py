def compuerta_and(numeroA, numeroB):
  numeroA, numeroB = emparejar_largos(numeroA, numeroB)
  resultado = ""
  for i in range(len(numeroA)):
    if numeroA[i] == "1" and numeroB[i] == "1":
      resultado += "1"
    else:
      resultado += "0"
  return resultado

def compuerta_or(numeroA, numeroB):
  numeroA, numeroB = emparejar_largos(numeroA, numeroB)
  resultado = ""
  for i in range(len(numeroA)):
    if numeroA[i] == "1" or numeroB[i] == "1":
      resultado += "1"
    else:
      resultado += "0"
  return resultado

def compuerta_not(numeroA):
  resultado = ""
  for i in range(len(numeroA)):
    if numeroA[i] == "1":
      resultado += "0"
    else:
      resultado += "1"
  return resultado

def compuerta_xor(numeroA, numeroB):
  numeroA, numeroB = emparejar_largos(numeroA, numeroB)
  resultado = ""
  for i in range(len(numeroA)):
    if numeroA[i] != numeroB[i]:
      resultado += "1"
    else:
      resultado += "0"
  return resultado

def convertir_a_binario(numero):
  resultado = ""
  while numero > 1:
    if numero % 2 > 0:
      resultado += "1"
    else:
      resultado += "0"
    numero = numero // 2
  resultado += "1"
  return resultado[:: -1]

def convertir_a_decimal(numero):
  numero = numero[:: -1]
  resultado = 0
  for i in range(len(numero)):
    if numero[i] == "1":
      resultado += 2 ** i
  return resultado

def emparejar_largos(numeroA, numeroB):
  largoA = len(numeroA)
  largoB = len(numeroB)
  if largoA != largoB:
    if largoA > largoB:
      numeroB = numeroB.zfill(largoA)
    else:
      numeroA = numeroA.zfill(largoB)
  return numeroA, numeroB
