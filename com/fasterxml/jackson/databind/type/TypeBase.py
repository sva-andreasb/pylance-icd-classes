def toCanonical():
    '''returns String\n\n
    toCanonical()\n
    '''
def getBindings():
    '''returns TypeBindings\n\n
    getBindings()\n
    '''
def containedTypeCount():
    '''returns int\n\n
    containedTypeCount()\n
    '''
def containedType():
    '''returns JavaType\n\n
    containedType(final int index)\n
    '''
def containedTypeName():
    '''returns String\n\n
    containedTypeName(final int index)\n
    '''
def getSuperClass():
    '''returns JavaType\n\n
    getSuperClass()\n
    '''
def getInterfaces():
    '''returns List<JavaType>\n\n
    getInterfaces()\n
    '''
def findTypeParameters():
    '''returns JavaType[]\n\n
    findTypeParameters(final Class<?> expType)\n
    '''
def serializeWithType():
    '''returns None\n\n
    serializeWithType(final JsonGenerator g, final SerializerProvider provider, final TypeSerializer typeSer)\n
    '''
def serialize():
    '''returns None\n\n
    serialize(final JsonGenerator gen, final SerializerProvider provider)\n
    '''
