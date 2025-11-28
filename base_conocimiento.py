hechos = (
    ('gastos', 'fijos', 'renta', 'alta'),
    ('gastos', 'fijos', 'agua', 'alta'),
    ('gastos', 'fijos', 'electricidad', 'alta'),
    ('gastos', 'fijos', 'telefono/internet', 'media'),
    ('gastos', 'fijos', 'seguros', 'media'),
    ('gastos', 'variables', 'comida', 'alta'),
    ('gastos', 'variables', 'transporte', 'media'),
    ('gastos', 'variables', 'ropa', 'baja'),
    ('gastos', 'variables', 'entretenimiento', 'baja'),
    ('gastos', 'variables', 'intereses deuda', 'alta'),
    ('objetivo', .50, ('alta', 'media')),
    ('objetivo', .30, ('baja',))
)

'''
ej_datos = {
    'ingresos': 1000,
    'gastos': {
        'fijos': [
            {'renta': 200},
            {'electricidad': 100},
            {'telefono/internet': 100},
            {'seguros': 100}
            ],
        'variables': [
            {'comida': 50},
            {'transporte': 50},
            {'ropa': 250},
            {'entretenimiento': 100}
        ]
    },
    'meta_ahorro': 10000
}
'''