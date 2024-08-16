print("Hola. Aquí vas a poder calcular el área de un terreno")
Base = float(input("Ingrese la base del terreno:"))
Altura_del_Triangulo= float(input("Ingrese la altura del triangulo:"))
Altura_Del_Rectangulo = float(input("Ingrese la altura del rectangulo:"))
Area_Del_Triangulo = Base * Altura_del_Triangulo / 2
Area_Del_Rectangulo = Base * Altura_Del_Rectangulo
Area_Total = Area_Del_Rectangulo + Area_Del_Triangulo
print(f"El area del terreno es: {Area_Total} mts")