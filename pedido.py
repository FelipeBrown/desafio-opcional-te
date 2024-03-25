from te import Te


sabor =  int(input("Ingrese sabor del té: "))
formato = int(input("ingrese el formato del té: "))


te = Te(sabor, formato)

print(f"el sabor del té es: {te.obtener_sabor()}")
print(f"el formato es de {te.formato} gramos")
print(f"el precio de te es: {Te.obtener_precio(formato)} ")
tiempo, recomendacion = Te.obtener_tiempo_recomedacion(sabor)
print(f"el tiempo de preparación es: {tiempo} minutos")
print(f"se recomienda: {recomendacion}")
print(f"vence en: {Te.duracion}")