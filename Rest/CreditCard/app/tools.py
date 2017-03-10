
def translate(serializer, data):
    """Herramienta para traducir de nombre comun a base de datos"""

    newDict = {}

    for key in data:
        newDict[ serializer().get_fields()[ key ].source ] = data[key]

    return newDict


