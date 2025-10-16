velocidad = float(input("indique la velocidad:"))
altura = float(input("indique la altura:"))
gravedad = 9.8 
import math

if ((velocidad*velocidad)-(2*gravedad)*altura) < 0:
    print("no se puede sacar raiz negativa ")
else:
    resultado = velocidad + math.sqrt((velocidad*velocidad)-(2*gravedad)*altura)/gravedad
    print(f"tu resultado es:{resultado}")