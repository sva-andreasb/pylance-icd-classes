def copy():
    '''returns DefaultSerializerProvider\n\n
    copy()\n
    copy()\n
    '''
def serializerInstance():
    '''returns JsonSerializer<Object>\n\n
    serializerInstance(final Annotated annotated, final Object serDef)\n
    '''
def includeFilterInstance():
    '''returns Object\n\n
    includeFilterInstance(final BeanPropertyDefinition forProperty, final Class<?> filterClass)\n
    '''
def includeFilterSuppressNulls():
    '''returns boolean\n\n
    includeFilterSuppressNulls(final Object filter)\n
    '''
def findObjectId():
    '''returns WritableObjectId\n\n
    findObjectId(final Object forPojo, final ObjectIdGenerator<?> generatorType)\n
    '''
def hasSerializerFor():
    '''returns boolean\n\n
    hasSerializerFor(final Class<?> cls, final AtomicReference<Throwable> cause)\n
    '''
def getGenerator():
    '''returns JsonGenerator\n\n
    getGenerator()\n
    '''
def serializeValue():
    '''returns None\n\n
    serializeValue(final JsonGenerator gen, final Object value)\n
    serializeValue(final JsonGenerator gen, final Object value, final JavaType rootType)\n
    serializeValue(final JsonGenerator gen, final Object value, final JavaType rootType, JsonSerializer<Object> ser)\n
    '''
def serializePolymorphic():
    '''returns None\n\n
    serializePolymorphic(final JsonGenerator gen, final Object value, final JavaType rootType, JsonSerializer<Object> valueSer, final TypeSerializer typeSer)\n
    '''
def cachedSerializersCount():
    '''returns int\n\n
    cachedSerializersCount()\n
    '''
def flushCachedSerializers():
    '''returns None\n\n
    flushCachedSerializers()\n
    '''
def acceptJsonFormatVisitor():
    '''returns None\n\n
    acceptJsonFormatVisitor(final JavaType javaType, final JsonFormatVisitorWrapper visitor)\n
    '''
def generateJsonSchema():
    '''returns JsonSchema\n\n
    generateJsonSchema(final Class<?> type)\n
    '''
def ():
    '''returns Impl\n\n
    ()\n
    (final Impl src)\n
    '''
def createInstance():
    '''returns Impl\n\n
    createInstance(final SerializationConfig config, final SerializerFactory jsf)\n
    '''
