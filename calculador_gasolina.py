kmPercorridos = float(
    input("Entre com o valor de Quilômetros percorridos pelo carro:"))
gasolina = float(
    input("Entre com a quantidade, em litros, de gasolina consumida:"))

consumo = kmPercorridos / gasolina
precoGasolina = 8.10
valorConsumo = precoGasolina / consumo

print("Seu veículo faz uma média de: {:.2f}".format(consumo), "Km por litro."
      "\nE o valor gasto por km foi de: R$ {:.2f}".format(valorConsumo), ",00.")
