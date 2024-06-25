#Trabajo Evaluacion 3
import random
import statistics
import csv

# Funcion para generar y clasificar saldos

def generar_y_clasificar_saldos():
    saldos = [random.randint(1, 10000) for _ in range(10)]
    rangos = {"Saldo Bajo": [], "Saldo Medio": [], "Saldo Alto": []}
    for saldo in saldos:
        if saldos < 3000:
            rangos["Saldo Bajo"].append(saldo)
        elif saldo < 6000:
            rangos["Saldo Medio"].append(saldo)
        else:
            rangos["Saldo Alto"].append(saldo)
    return saldos, rangos

# Funcion para generar estadisticas y reporte de saldos

def estadisticas_y_reporte(saldos):
    print(f"Saldo Mas Alto: {max(saldos)}")
    print(f"Saldo Mas Bajo: {min(saldos)}")
    print(f"Saldo Promedio: {statistics.mean(saldos)}")
    print(f"Media Geométrica: {statistics.geometric_mean(saldos)}")
    

