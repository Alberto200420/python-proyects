def dividendos(inversionista, porcentaje):
    rendimiento = inversionista * porcentaje
    ganancia = inversionista + rendimiento
    print(f"TOTAL ---- {ganancia} ---- GANO ---- {rendimiento} --- LE METIO ---- {inversionista}")
    rendimiento_total.append(rendimiento)
    inversionistas.append(inversionista)

rendimiento_total = []
inversionistas = []

dividendos(3500, 0.15)
dividendos(500 , 0.15)
dividendos(8000, 0.15)
dividendos(100000, 0.15)
dividendos(36 , 0.15)
dividendos(75, 0.15)
dividendos(999, 0.15)
dividendos(90 , 0.15)
dividendos(800 , 0.15)
dividendos(16000 , 0.15)
dividendos(80000 , 0.15)
dividendos(500 , 0.15)
dividendos(1000, 0.15)
dividendos(5500 , 0.15)
dividendos(17000, 0.15)
dividendos(84000, 0.15)
dividendos(2000, 0.15)
dividendos(400, 0.15)
dividendos(700, 0.15)
dividendos(300000, 0.15)
dividendos(900, 0.15)
dividendos(10, 0.15)
dividendos(500, 0.15)
dividendos(900, 0.15)
dividendos(9000, 0.15)
dividendos(90000, 0.15)
dividendos(1000, 0.15)
dividendos(10000, 0.15)
dividendos(100, 0.15)
dividendos(200, 0.15)
dividendos(200, 0.15)
dividendos(300, 0.15)
dividendos(400, 0.15)
dividendos(500, 0.15)
dividendos(600, 0.15)
dividendos(9700, 0.15)
dividendos(700, 0.15)
dividendos(800, 0.15)
dividendos(900, 0.15)
dividendos(1000, 0.15)
dividendos(500000, 0.15)
dividendos(500, 0.15)
dividendos(1000, 0.15)
dividendos(1000, 0.15)
dividendos(1000, 0.15)
dividendos(1000, 0.15)
dividendos(1000, 0.15)
dividendos(1000, 0.15)
dividendos(1000, 0.15)
dividendos(90, 0.15)
dividendos(300, 0.15)
dividendos(44000, 0.15)
dividendos(88000, 0.15)
dividendos(24000, 0.15)
dividendos(10, 0.15)
dividendos(500, 0.15)
dividendos(900, 0.15)
dividendos(9000, 0.15)
dividendos(90000, 0.15)
dividendos(1000, 0.15)
dividendos(10000, 0.15)
dividendos(100, 0.15)
dividendos(200, 0.15)
dividendos(200, 0.15)
dividendos(300, 0.15)
dividendos(400, 0.15)
dividendos(500, 0.15)
dividendos(600, 0.15)
dividendos(9700, 0.15)
dividendos(700, 0.15)
dividendos(800, 0.15)
dividendos(900, 0.15)
dividendos(1000, 0.15)
dividendos(500000, 0.15)
dividendos(500, 0.15)
dividendos(1000, 0.15)
dividendos(1000, 0.15)
dividendos(1000, 0.15)
dividendos(1000, 0.15)
dividendos(1000, 0.15)
dividendos(1000, 0.15)
dividendos(1000, 0.15)
dividendos(90, 0.15)
dividendos(300, 0.15)
dividendos(44000, 0.15)
dividendos(88000, 0.15)
dividendos(24000, 0.15)
dividendos(200, 0.15)
dividendos(78000, 0.15)
dividendos(44000, 0.15)
dividendos(250000, 0.15)
dividendos(250000, 0.15)
dividendos(400, 0.15)
dividendos(174000, 0.15)

i = 0
for numero in rendimiento_total:
    i += numero

f = 0
for array in inversionistas:
    f += array


print(f"Suma total de todos los rendimientos:{i} Suma totoal de todos los inversionistas:{f}")