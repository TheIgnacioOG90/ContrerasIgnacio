# Trabajo Evualuacion 3
import random
import csv
import statistics 

def generar_saldos_aleatorios():
    
    return [random.randint(10000, 100000) for _ in range(10)]

def clasificar_saldos(saldos):
    rangos = {"Bajo": (10000, 40000), "Medio": (40001, 70000), "Alto": (70001, 100000)}
    clasificacion = {"Bajo": [], "Medio": [], "Alto": []}
    for saldo in saldos:
        for rango in rangos:
            if rangos[rango][0] <= saldo <= rangos[rango][1]:
                clasificacion[rango].append(saldo)
                break
    return clasificacion

def media_geometrica(saldos):
    producto = 1
    for saldo in saldos:
        producto *= saldo
    return producto ** (1/len(saldos))

def mostrar_estadisticas(saldos):
    saldo_max = max(saldos)
    saldo_min = min(saldos)
    saldo_prom = statistics.mean(saldos)
    media_geom = media_geometrica(saldos)
    print(f"Saldo Más alto: {saldo_max}\nSaldo Más bajo: {saldo_min}\nSaldo Promedio: {saldo_prom}\nMedia Geométrica: {media_geom}")

def generar_reporte_csv(saldos):
    with open('reporte_saldos.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Clientes", "Saldo Brutos", "Deducciones", "Saldo Netos"])
        for i, saldo in enumerate(saldos, start=1):
            deduccion = saldo * 0.1  # Deducción del 10%
            saldo_neto = saldo - deduccion
            writer.writerow([f"Cliente {i}", saldo, deduccion, saldo_neto])

def main():
    saldos = []
    while True:
        print("\n1. Generar Saldos Aleatorios\n2. Clasificar Saldos\n3. Ver Estadísticas\n4. Reporte de Saldos\n5. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            saldos = generar_saldos_aleatorios()
            print("Saldos generados.")
        elif opcion == "2":
            if saldos:
                clasificacion = clasificar_saldos(saldos)
                print("Clasificación de saldos:", clasificacion)
            else:
                print("Primero debe generar los saldos.")
        elif opcion == "3":
            if saldos:
                mostrar_estadisticas(saldos)
            else:
                print("Primero debe generar los saldos.")
        elif opcion == "4":
            if saldos:
                generar_reporte_csv(saldos)
                print("Reporte generado.")
            else:
                print("Primero debe generar los saldos.")
        elif opcion == "5":
            print("Gracias por usar nuestro programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()