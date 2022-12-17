def ():
    '''returns SerializerProvider\n\n
    ()\n
    '''
def setDefaultKeySerializer():
    '''returns None\n\n
    setDefaultKeySerializer(final JsonSerializer<Object> ks)\n
    '''
def setNullValueSerializer():
    '''returns None\n\n
    setNullValueSerializer(final JsonSerializer<Object> nvs)\n
    '''
def setNullKeySerializer():
    '''returns None\n\n
    setNullKeySerializer(final JsonSerializer<Object> nks)\n
    '''
def getLocale():
    '''returns Locale\n\n
    getLocale()\n
    '''
def getTimeZone():
    '''returns TimeZone\n\n
    getTimeZone()\n
    '''
def getAttribute():
    '''returns Object\n\n
    getAttribute(final Object key)\n
    '''
def setAttribute():
    '''returns SerializerProvider\n\n
    setAttribute(final Object key, final Object value)\n
    '''
def getGenerator():
    '''returns JsonGenerator\n\n
    getGenerator()\n
    '''
def findValueSerializer():
    '''returns JsonSerializer<Object>\n\n
    findValueSerializer(final Class<?> valueType, final BeanProperty property)\n
    findValueSerializer(final JavaType valueType, final BeanProperty property)\n
    findValueSerializer(final Class<?> valueType)\n
    findValueSerializer(final JavaType valueType)\n
    '''
def findPrimaryPropertySerializer():
    '''returns JsonSerializer<Object>\n\n
    findPrimaryPropertySerializer(final JavaType valueType, final BeanProperty property)\n
    findPrimaryPropertySerializer(final Class<?> valueType, final BeanProperty property)\n
    '''
def findTypedValueSerializer():
    '''returns JsonSerializer<Object>\n\n
    findTypedValueSerializer(final Class<?> valueType, final boolean cache, final BeanProperty property)\n
    findTypedValueSerializer(final JavaType valueType, final boolean cache, final BeanProperty property)\n
    '''
def findTypeSerializer():
    '''returns TypeSerializer\n\n
    findTypeSerializer(final JavaType javaType)\n
    '''
def findKeySerializer():
    '''returns JsonSerializer<Object>\n\n
    findKeySerializer(final JavaType keyType, final BeanProperty property)\n
    findKeySerializer(final Class<?> rawKeyType, final BeanProperty property)\n
    '''
def getDefaultNullKeySerializer():
    '''returns JsonSerializer<Object>\n\n
    getDefaultNullKeySerializer()\n
    '''
def getDefaultNullValueSerializer():
    '''returns JsonSerializer<Object>\n\n
    getDefaultNullValueSerializer()\n
    '''
def findNullKeySerializer():
    '''returns JsonSerializer<Object>\n\n
    findNullKeySerializer(final JavaType serializationType, final BeanProperty property)\n
    '''
def findNullValueSerializer():
    '''returns JsonSerializer<Object>\n\n
    findNullValueSerializer(final BeanProperty property)\n
    '''
def getUnknownTypeSerializer():
    '''returns JsonSerializer<Object>\n\n
    getUnknownTypeSerializer(final Class<?> unknownType)\n
    '''
def isUnknownTypeSerializer():
    '''returns boolean\n\n
    isUnknownTypeSerializer(final JsonSerializer<?> ser)\n
    '''
def defaultSerializeDateKey():
    '''returns None\n\n
    defaultSerializeDateKey(final long timestamp, final JsonGenerator gen)\n
    defaultSerializeDateKey(final Date date, final JsonGenerator gen)\n
    '''
def reportMappingProblem():
    '''returns None\n\n
    reportMappingProblem(final String message, final Object... args)\n
    reportMappingProblem(final Throwable t, String message, final Object... msgArgs)\n
    '''
def invalidTypeIdException():
    '''returns JsonMappingException\n\n
    invalidTypeIdException(final JavaType baseType, final String typeId, final String extraDesc)\n
    '''
def mappingException():
    '''returns JsonMappingException\n\n
    mappingException(final String message, final Object... msgArgs)\n
    '''
