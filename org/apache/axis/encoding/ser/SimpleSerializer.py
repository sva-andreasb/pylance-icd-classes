VALUE_PROPERTY = "String  \"_value\""
def ():
    '''returns SimpleSerializer\n\n
    (final Class javaType, final QName xmlType)\n
    (final Class javaType, final QName xmlType, final TypeDesc typeDesc)\n
    '''
def serialize():
    '''returns None\n\n
    serialize(final QName name, Attributes attributes, final Object value, final SerializationContext context)\n
    '''
def getValueAsString():
    '''returns String\n\n
    getValueAsString(final Object value, final SerializationContext context)\n
    '''
def getMechanismType():
    '''returns String\n\n
    getMechanismType()\n
    '''
def writeSchema():
    '''returns Element\n\n
    writeSchema(final Class javaType, final Types types)\n
    '''
