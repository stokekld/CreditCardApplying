
def translate(serializer, data):

    newDict = {}

    for key in data:
        newDict[ serializer().get_fields()[ key ].source ] = data[key]

    return newDict


