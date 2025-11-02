import math
hechos = (
    ('gastos', 'fijos', 'renta', 'alta'),
    ('gastos', 'fijos', 'electricidad', 'alta'),
    ('gastos', 'fijos', 'telefono/internet', 'media'),
    ('gastos', 'fijos', 'seguros', 'media'),
    ('gastos', 'variables', 'comida', 'alta'),
    ('gastos', 'variables', 'transporte', 'media'),
    ('gastos', 'variables', 'ropa', 'baja'),
    ('gastos', 'variables', 'entretenimiento', 'baja'),
    ('gastos', 'variables', 'intereses_deuda', 'alta')
)

ej_datos = {
    'ingresos': 1000,
    'gastos': {
        'fijos': [
            {'renta': 100},
            {'electricidad': 100},
            {'telefono/internet': 100},
            {'seguros': 100}
            ],
        'variables': [
            {'comida': 50},
            {'transporte': 50},
            {'ropa': 100},
            {'entretenimiento': 100}
        ]
    },
    'meta_ahorro': 10000
}

# funciones auxiliares
def sumar_gastos(gastos:dict, tipos=('fijos', 'variables'), tipo_index=0, gasto_index=0, total=0):
    # Caso base
    if tipo_index >= len(tipos):
        return total

    tipo_actual = tipos[tipo_index]
    lista_gastos = gastos[tipo_actual]

    # termino los gastos del tipo actual
    if gasto_index >= len(lista_gastos):
        return sumar_gastos(gastos, tipos, tipo_index + 1, 0, total)

    gasto = lista_gastos[gasto_index]
    nombre = list(gasto.keys())[0]
    monto = gasto[nombre]

    return sumar_gastos(gastos, tipos, tipo_index, gasto_index + 1, total + monto)

def sumar_prioridad(gastos: dict, hechos: tuple, prioridad_objetivo: str,
                    tipos=('fijos', 'variables'), tipo_index=0, gasto_index=0, total=0):
    # Caso base
    if tipo_index >= len(tipos):
        return total
    
    tipo_actual = tipos[tipo_index]
    lista_gastos = gastos[tipo_actual]

    # termino los gastos del tipo actual
    if gasto_index >= len(lista_gastos):
        return sumar_prioridad(gastos, hechos, prioridad_objetivo, tipos, tipo_index + 1, 0, total)

    gasto = lista_gastos[gasto_index]
    nombre = list(gasto.keys())[0]
    monto = gasto[nombre]

    # Buscar prioridad
    prioridad = obtener_prioridad(nombre, tipo_actual, hechos)
    if prioridad == prioridad_objetivo:
        total += monto

    return sumar_prioridad(gastos, hechos, prioridad_objetivo, tipos, tipo_index, gasto_index + 1, total)


def obtener_prioridad(nombre, tipo, hechos, index=0):
    # Caso base
    if index >= len(hechos):
        return None

    categoria, tipo_gasto, nombre_gasto, nivel = hechos[index]

    if categoria == 'gastos' and tipo_gasto == tipo and nombre_gasto == nombre:
        return nivel

    return obtener_prioridad(nombre, tipo, hechos, index + 1)

# Reglas 

def hay_ingreso(datos:dict):
    return datos.get("ingresos", 0) > 0

def regla_50_30_20(datos:dict, hechos):
    ingresos = datos["ingresos"]
    gastos = datos["gastos"]
    total_alta_media = sumar_prioridad(gastos, hechos, 'alta') + sumar_prioridad(gastos, hechos, 'media')
    total_baja = sumar_prioridad(gastos, hechos, 'baja')

    limite_alta_media = ingresos * 0.5
    limite_baja = ingresos * 0.3

    return total_alta_media <= limite_alta_media and total_baja <= limite_baja

def requiere_ajustes(datos:dict):
    if not datos: return "sin datos" 
    ingresos = datos["ingresos"]
    gastos_totales = sumar_gastos(datos["gastos"])
    
    return ingresos < gastos_totales

def tiempo_para_ahorrar(datos):
    ingresos = datos["ingresos"]
    meta_ahorro = datos["meta_ahorro"]
    gastos_totales = sumar_gastos(datos["gastos"])
    return math.ceil((meta_ahorro / (ingresos - gastos_totales)))

def puede_ahorrar(datos:dict):
    ingresos = datos["ingresos"]
    gastos_totales = sumar_gastos(datos["gastos"])
    return ingresos > gastos_totales

def existen_gastos_alta_media(gastos_dict, hechos, tipos=['fijos','variables'], tipo_index=0, gasto_index=0):
    # Caso base
    if tipo_index >= len(tipos):
        return False

    tipo_actual = tipos[tipo_index]
    lista_gastos = gastos_dict[tipo_actual]

    # Ya no hay gastos de ese tipo
    if gasto_index >= len(lista_gastos):
        return existen_gastos_alta_media(gastos_dict, hechos, tipos, tipo_index + 1, 0)

    gasto = lista_gastos[gasto_index]
    nombre = list(gasto.keys())[0]

    prioridad = obtener_prioridad(nombre, tipo_actual, hechos)

    if prioridad == 'alta' or prioridad == 'media':
        return True

    return existen_gastos_alta_media(gastos_dict, hechos, tipos, tipo_index, gasto_index + 1)

def calcular_deficit():
    return

def cumple_porcentaje_objetivo():
    return

def calcular_monto_recorte():
    return


# Consultas

def meses_para_ahorrar(datos:dict):
    if hay_ingreso(datos):
        if puede_ahorrar(datos):
            return tiempo_para_ahorrar(datos)
        else:
            return "No puede ahorrar, se requieren ajustes en el presupuesto."
    else:
        return "No hay ingresos registrados."
    
def gastos_requieren_ajuste(datos:dict):
    if hay_ingreso(datos):
        if requiere_ajustes(datos):
            return "Los gastos requieren ajustes."
        else:
            return "Los gastos están dentro del presupuesto."
    else:
        return "No es posible evaluar sin ingresos."
    
def ingresos_cumplen_regla_50_30_20(datos:dict):
    if hay_ingreso(datos):
        if regla_50_30_20():
            return "Cumple la regla 50-30-20."
        else:
            return "No cumple la regla 50-30-20."
    else:
        return "No es posible evaluar sin ingresos."

print(meses_para_ahorrar(ej_datos))
print(gastos_requieren_ajuste(ej_datos))
print(regla_50_30_20(ej_datos, hechos))