while True:

    print("Hola. En este programa, usted podrá calcular el salario que obtiene por día, hora y semana")
    Salario = int(input ("Ingrese el salario que usted obtiene mensualmente :"))
    Dias_que_labora = int (input ("Ingrese la cantidad de días que usted labora semanalmente :"))
    Horas_por_dia = int (input ("Ingrese la cantidad de horas por día que labora :"))
    Dias_en_mes = Dias_que_labora * 4
    Total = True
    
    if Dias_que_labora > 7 or Horas_por_dia >12:
        print("La cantidad de horas que trabajo que ingresó, no son posibles")
        Total = False    

    Salario_que_recibe_por_dia = Salario / Dias_en_mes
    Salario_que_recibe_por_hora = Salario_que_recibe_por_dia / Horas_por_dia
    Salario_que_recibe_semanalmente = Salario_que_recibe_por_dia * Dias_que_labora 


    if Total:
        print (f"El salario que recibe mensualmente es : ${Salario}")
        print (f"El salario que recibe semanalmente es : ${Salario_que_recibe_semanalmente}")
        print (f"El salario que recibe diariamente es : ${Salario_que_recibe_por_dia}")
        print (f"El salario que recibe por cada hora trabajada es: ${Salario_que_recibe_por_hora}")

    
