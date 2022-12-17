def unwrappingSerializer():
    '''returns JsonSerializer<T>\n\n
    unwrappingSerializer(final NameTransformer unwrapper)\n
    '''
def replaceDelegatee():
    '''returns JsonSerializer<T>\n\n
    replaceDelegatee(final JsonSerializer<?> delegatee)\n
    '''
def serializeWithType():
    '''returns None\n\n
    serializeWithType(final T value, final JsonGenerator gen, final SerializerProvider serializers, final TypeSerializer typeSer)\n
    '''
def handledType():
    '''returns Class<T>\n\n
    handledType()\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty(final T value)\n
    isEmpty(final SerializerProvider provider, final T value)\n
    '''
def usesObjectId():
    '''returns boolean\n\n
    usesObjectId()\n
    '''
def isUnwrappingSerializer():
    '''returns boolean\n\n
    isUnwrappingSerializer()\n
    '''
def properties():
    '''returns Iterator<PropertyWriter>\n\n
    properties()\n
    '''
def acceptJsonFormatVisitor():
    '''returns None\n\n
    acceptJsonFormatVisitor(final JsonFormatVisitorWrapper visitor, final JavaType type)\n
    '''
