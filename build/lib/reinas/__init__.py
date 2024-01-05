def es_seguro(tablero, fila, columna):
    for i in range(fila):
        if tablero[i] == columna or \
           tablero[i] - i == columna - fila or \
           tablero[i] + i == columna + fila:
            return False
    return True
#Si tablero[i] == columna, significa que hay una reina en la misma columna.
#tablero[i] - i: Representa la posición de la reina en la diagonal superior izquierda.Cuando tablero[i] - i == columna - fila, significa que hay una reina en la misma diagonal.
#tablero[i] + i: Representa la posición de la reina en la diagonal superior derecha.Cuando tablero[i] + i == columna + fila, significa que hay una reina en la misma diagonal.

def resolver_n_reinas_util(tablero, fila, n):
    if fila == n:
        return [list(tablero)]

    soluciones = []
    for columna in range(n):
        if es_seguro(tablero, fila, columna):
            tablero[fila] = columna
            soluciones.extend(resolver_n_reinas_util(tablero, fila + 1, n))

    return soluciones

  # Esta función es una  recursiva que se utiliza para encontrar todas las soluciones al problema de las N reinas.

 # La función contiene una condición de parada que verifica si todas las reinas han sido colocadas (fila == n). Si esto pasa ,la función retorna una lista que representa una solución válida del tablero.

# (soluciones = []) Se inicializa una lista llamada soluciones para almacenar todas las soluciones encontradas.

#(for columna in range(n):) aca la  función utiliza un bucle for para iterar a través de todas las columnas en la fila actual (range(n)).

#(if es_seguro(tablero, fila, columna):)Para cada columna, se verifica si es seguro colocar una reina en esa posición utilizando la función es_seguro. Si es seguro, se procede.
# Se actualiza el tablero colocando una reina en la posición (fila, columna).Se realiza una llamada recursiva a resolver_n_reinas_util para continuar con la siguiente fila (fila + 1).

#(soluciones.extend(...)): Las soluciones encontradas en la llamada recursiva se extienden a la lista de soluciones actual. Esto se hace para acumular todas las soluciones válidas.

#Retorno de Soluciones (return soluciones) Finalmente, la función retorna la lista de soluciones encontradas.

def resolver_n_reinas(n):
    tablero = [-1] * n
    return resolver_n_reinas_util(tablero, 0, n)

 #Esta función es la función principal que inicializa el tablero y llama a la función resolver_n_reinas_util con los parámetros iniciales.
 #Se inicializa una lista llamada tablero con valores -1, indicando que inicialmente no hay reinas colocadas en el tablero.
 #La función llama a resolver_n_reinas_util con el tablero inicializado, comenzando desde la fila 0 y especificando el tamaño del tablero.
 #La función retorna el resultado de la llamada a resolver_n_reinas_util, que es una lista de todas las soluciones encontradas.

