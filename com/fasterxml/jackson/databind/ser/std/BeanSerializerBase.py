def ():
    '''returns BeanSerializerBase\n\n
    (final BeanSerializerBase src, final BeanPropertyWriter[] properties, final BeanPropertyWriter[] filteredProperties)\n
    '''
def resolve():
    '''returns None\n\n
    resolve(final SerializerProvider provider)\n
    '''
def properties():
    '''returns Iterator<PropertyWriter>\n\n
    properties()\n
    '''
def usesObjectId():
    '''returns boolean\n\n
    usesObjectId()\n
    '''
def serializeWithType():
    '''returns None\n\n
    serializeWithType(final Object bean, final JsonGenerator gen, final SerializerProvider provider, final TypeSerializer typeSer)\n
    '''
def getSchema():
    '''returns JsonNode\n\n
    getSchema(final SerializerProvider provider, final Type typeHint)\n
    '''
def acceptJsonFormatVisitor():
    '''returns None\n\n
    acceptJsonFormatVisitor(final JsonFormatVisitorWrapper visitor, final JavaType typeHint)\n
    '''
