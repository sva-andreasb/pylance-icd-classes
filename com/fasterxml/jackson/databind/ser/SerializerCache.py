def ():
    '''returns SerializerCache\n\n
    ()\n
    '''
def getReadOnlyLookupMap():
    '''returns ReadOnlyClassToSerializerMap\n\n
    getReadOnlyLookupMap()\n
    '''
def untypedValueSerializer():
    '''returns JsonSerializer<Object>\n\n
    untypedValueSerializer(final Class<?> type)\n
    untypedValueSerializer(final JavaType type)\n
    '''
def typedValueSerializer():
    '''returns JsonSerializer<Object>\n\n
    typedValueSerializer(final JavaType type)\n
    typedValueSerializer(final Class<?> cls)\n
    '''
def addTypedSerializer():
    '''returns None\n\n
    addTypedSerializer(final JavaType type, final JsonSerializer<Object> ser)\n
    addTypedSerializer(final Class<?> cls, final JsonSerializer<Object> ser)\n
    '''
def addAndResolveNonTypedSerializer():
    '''returns None\n\n
    addAndResolveNonTypedSerializer(final Class<?> type, final JsonSerializer<Object> ser, final SerializerProvider provider)\n
    addAndResolveNonTypedSerializer(final JavaType type, final JsonSerializer<Object> ser, final SerializerProvider provider)\n
    addAndResolveNonTypedSerializer(final Class<?> rawType, final JavaType fullType, final JsonSerializer<Object> ser, final SerializerProvider provider)\n
    '''
