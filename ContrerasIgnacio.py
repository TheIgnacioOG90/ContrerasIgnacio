# Trabajo de Evaluacion 3
import csv
import random
import statistics

def generacion_de_saldos_aleatorios():
    return [random.randint(10000, 100000) for _ in range(10)]

def clasificar_saldos(saldos):
    rangos = {"Saldo Bajo": (10000, 40000), "Saldo Medio": (40001, 70000), "Saldo Alto": (70001, 100000)}
    clasificacion = { "Saldos Bajos": [], "Saldos Medios": [], "Saldos Altos": []}
    for saldo in saldos:
        for rango in rangos:
            if rangos[rango][0] <= saldo <= rangos[rango][1]:
                clasificacion[rango].append(saldo)
                break


