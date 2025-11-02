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
    'ingresos': 3000,
    'gastos': {
        'fijos': [
            {'renta': 1000},
            {'electricidad': 150},
            {'telefono/internet': 100},
            {'seguros': 200}
            ],
        'variables': [
            {'comida': 400},
            {'transporte': 150},
            {'ropa': 100},
            {'entretenimiento': 200},
            {'intereses_deuda': 250}
        ]
    }
}


# Reglas 

def hay_ingreso():
    return

def cumple_regla_50_30_20():
    return

def requieres_ajuste(datos:dict):
    if not datos: return "sin datos" 
    ingresos = datos["ingresos"]
    gastos_totales = sum(list(gasto.values())[0] for categoria in datos["gastos"].values() for gasto in categoria)
    
    return ingresos < gastos_totales

def tiempo_para_ahorrar():
    return

def puede_ahorrar():
    return

def existen_gastos_prioridad_alta():
    return

def calcular_deficit():
    return

def cumple_porcentaje_objetivo():
    return

def calcular_monto_recorte():
    return


print(requieres_ajuste(ej_datos)) 