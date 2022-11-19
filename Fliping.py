print ("Vamos a calcular tu flipping ")                                                                                  #programa para calcular la utilidad de el flipping

Valor_del_dueño = int(input("¿Cuanto quiere el dueño?: "))                                                               #¿cuanto quiere el dueño?                                                               
Remodelacion = Valor_del_dueño * 0.1                                                                                     #Procedimiento del porcentaje de remodelacion 10%                                                                                      
TotalEnInmueble = Remodelacion + Valor_del_dueño                                                                         #TOTAL DEL DUEÑO MAS LA REMODELACION 

Precio_de_venta = int(input("¿En cuanto la quieres vender? "))                                                           #EN ESTO LA VOY A VENDER 
Utilidad_bruta_SIN_inmobiliara = Precio_de_venta - TotalEnInmueble                                                       #RESTA DEL VALOR EN INMUEBLE Y EL PRECIO DE VENTA 

Porcentaje_de_la_inmobiliaria = float(input("Recuerda poner 0.0 ¿Cuanto tiene la inmobiliaria?: "))                      #¿Cuanto tiene la inmobiliaria?
Menos_la_inmobiliaria = Porcentaje_de_la_inmobiliaria * Precio_de_venta                                                  #LO QUE TIENE LA INMOBILIARIA EN UNA VARIABLE

Porcentaje_del_inversionista = float(input("Recuerda poner 0. ¿Cuanto de rendimiento le das al inversionista?: "))       #¿Cuanto le doy al inversionista?
Menos_el_inversionista = Porcentaje_del_inversionista * Remodelacion                                                     #GUARDADO EN UNA VARIABLE 

Utilidad_menos_la_inmobiliaria = Utilidad_bruta_SIN_inmobiliara - Menos_la_inmobiliaria                                  #UTILIDAD BRUTA MENOS LA COMICION DE LA IBNOBILIARIA

Porcentaje_del_dueño = float(input("Recuerda poner 0. ¿Cuanto le vas a dar al dueño?: "))                                #¿Cuanto de doy al dueño?
Menos_el_dueño = Porcentaje_del_dueño * Utilidad_menos_la_inmobiliaria                                                   #GUARDADO EN UNA VARIABLE 

Utilidad_Neta = Utilidad_menos_la_inmobiliaria - Menos_el_inversionista - Menos_el_dueño                                 #UTILIDAD PARA NOSOTROS

print(f"Le tienes que meter a la remodelación: {Remodelacion}")         
print(f"Este es el total del lo que pide el dueño más la remodelación: {TotalEnInmueble}")
print(f"Si la vas a vender en {Precio_de_venta} Entonces esta es la utilidad bruta {Utilidad_bruta_SIN_inmobiliara}")
print(f"Y esto es menos la comisión de la inmobiliaria {Utilidad_menos_la_inmobiliaria}")
print(f"La inmobiliaria tiene de comisión: {Menos_la_inmobiliaria}")
print(f"Esto le darás al inversionista: {Menos_el_inversionista}")
print(f"Esto le darás al dueño: {Menos_el_dueño}")
print(f"Esta es la utilidad neta (PA MIGUELON): {Utilidad_Neta}")