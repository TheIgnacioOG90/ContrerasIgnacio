# Trabajo de Evaluacion 3
import csv
import random
import statistics

def Generacion_De_Saldos_Aleatorios():
    return [random.randint(10000, 100000) for _ in range(10)]

def Clasificar_Saldos(saldos):
    rangos = {"Saldo Bajo": (10000, 40000), "Saldo Medio": (40001, 70000), "Saldo Alto": (70001, 100000)}
    clasificacion = { "Saldos Bajos": [], "Saldos Medios": [], "Saldos Altos": []}
    for saldo in saldos:
        for rango in rangos:
            if rangos[rango][0] <= saldo <= rangos[rango][1]:
                clasificacion[rango].append(saldo)
                break
    return clasificacion

def Media_Geometrica(saldos):
    producto = 1
    for saldo in saldos:
        producto += saldo
    return producto ** (1/len(saldos))

def Mostrar_Estadisticas(saldos):
    saldo_max = max(saldos)
    saldo_min = min(saldos)
    saldo_promedio = statistics.mean(saldos)
    media_geometrica = Media_Geometrica(saldos)
    print(f"Saldo Mas Alto: {saldo_max}\nSaldo Mas Bajo: {saldo_min}\nSaldo Promedio: {saldo_promedio}\nMedia Geometrica: {media_geometrica}")
    
def Generar_Reporte_csv(saldos):
    with open("Reporte.csv", "w" ,newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Clientes", "Saldos Brutos", "Deducciones", "Saldos Netos"])
        for i, saldo in enumerate(saldos, start=1):
            deduccion = saldo * 0.1  # Deduccion del 10%
            saldo_neto = saldo - deduccion
            writer.writerow([f"Cliente {i}" , saldo , deduccion, saldo_neto])

def main():
         
        

