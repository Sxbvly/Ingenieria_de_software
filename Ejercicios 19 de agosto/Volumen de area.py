print("Hola. En este programa usted podrá calcular el volumen de un área")
ancho = float (input("Por favor, ingrese el ancho que tiene la alberca en metros :"))
largo_del_rectangulo = float (input("Por favor, ingrese el largo del rectángulo en metros :"))
largo_del_triangulo = float (input("Por favor, ingrese el largo del triángulo en metros :"))
profundidad = float (input("Por favor ingrese la profundidad del área en metros :"))
area_del_rectangulo = ancho * largo_del_rectangulo
area_del_triangulo = ancho * largo_del_triangulo / 2
volumen_de_area = (area_del_rectangulo * profundidad) + (area_del_triangulo * profundidad)
print ("El volúmen total del área es ", volumen_de_area, "mts")