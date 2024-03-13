def calcular_descuento(subtotal, descuento = 35):
    monto_descuento = (subtotal * descuento) / 1000
    return monto_descuento

valor_subtotal = 1000
porcentaje_descuento = 35

valor_descuento = calcular_descuento(valor_subtotal)
valor_total = valor_subtotal - valor_descuento
print(f'Total = {valor_total}. Luego de un descuento de {valor_descuento}. Aplicando el 35% al subtotal de {valor_subtotal}')


valor_subtotal = float(input('Ingrese el subtotal: '))
porcentaje_descuento = int(input('Ingreso el procentaje de descuento: '))

valor_descuento = calcular_descuento(valor_subtotal, porcentaje_descuento)
valor_total = valor_subtotal - valor_descuento
print(f'Total = {valor_total}. Luego de un descuento de {valor_descuento}. Aplicando el {porcentaje_descuento}% al subtotal de {valor_subtotal}.')
print(f'El valor a cancelar es:{valor_total}')