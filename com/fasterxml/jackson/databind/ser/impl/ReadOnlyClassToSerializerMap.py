def ():
    '''returns Bucket\n\n
    (final Map<TypeKey, JsonSerializer<Object>> serializers)\n
    (final Bucket next, final TypeKey key, final JsonSerializer<Object> value)\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def typedValueSerializer():
    '''returns JsonSerializer<Object>\n\n
    typedValueSerializer(final JavaType type)\n
    typedValueSerializer(final Class<?> type)\n
    '''
def untypedValueSerializer():
    '''returns JsonSerializer<Object>\n\n
    untypedValueSerializer(final JavaType type)\n
    untypedValueSerializer(final Class<?> type)\n
    '''
def matchesTyped():
    '''returns boolean\n\n
    matchesTyped(final Class<?> key)\n
    matchesTyped(final JavaType key)\n
    '''
def matchesUntyped():
    '''returns boolean\n\n
    matchesUntyped(final Class<?> key)\n
    matchesUntyped(final JavaType key)\n
    '''
