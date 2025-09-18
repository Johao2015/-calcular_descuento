


def calcular_descuento(monto_total, porcentaje_descuento=10):
    """Calcula el monto del descuento en base al monto total y el porcentaje."""
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Programa principal
if __name__ == "__main__":
    monto1 = 200
    descuento1 = calcular_descuento(monto1)
    monto_final1 = monto1 - descuento1

    print(f"Compra 1:")
    print(f"Monto total: ${monto1:.2f}")
    print(f"Descuento aplicado: ${descuento1:.2f}")
    print(f"Monto final a pagar: ${monto_final1:.2f}\\n")

    monto2 = 500
    porcentaje2 = 20
    descuento2 = calcular_descuento(monto2, porcentaje2)
    monto_final2 = monto2 - descuento2

    print(f"Compra 2:")
    print(f"Monto total: ${monto2:.2f}")
    print(f"Descuento aplicado ({porcentaje2}%): ${descuento2:.2f}")
    print(f"Monto final a pagar: ${monto_final2:.2f}")
