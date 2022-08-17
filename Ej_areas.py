Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def areatriangulo(altura, base):
    area = (base * altura) / 2
    return area

def areacirculo(radio):
    area = 3.14 *(radio * radio)
    return area

print("El area del triangulo es = ", areatriangulo(12,2))
El area del triangulo es =  12.0
print("El area del circulo es = ", areacirculo(3.0))
El area del circulo es =  28.26
