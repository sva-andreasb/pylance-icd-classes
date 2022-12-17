def ():
    '''returns MapProperty\n\n
    (final TypeSerializer typeSer, final BeanProperty prop)\n
    '''
def reset():
    '''returns None\n\n
    reset(final Object key, final Object value, final JsonSerializer<Object> keySer, final JsonSerializer<Object> valueSer)\n
    reset(final Object key, final JsonSerializer<Object> keySer, final JsonSerializer<Object> valueSer)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getValue():
    '''returns Object\n\n
    getValue()\n
    '''
def setValue():
    '''returns None\n\n
    setValue(final Object v)\n
    '''
def getFullName():
    '''returns PropertyName\n\n
    getFullName()\n
    '''
def serializeAsField():
    '''returns None\n\n
    serializeAsField(final Object map, final JsonGenerator gen, final SerializerProvider provider)\n
    '''
def serializeAsOmittedField():
    '''returns None\n\n
    serializeAsOmittedField(final Object map, final JsonGenerator gen, final SerializerProvider provider)\n
    '''
def serializeAsElement():
    '''returns None\n\n
    serializeAsElement(final Object map, final JsonGenerator gen, final SerializerProvider provider)\n
    '''
def serializeAsPlaceholder():
    '''returns None\n\n
    serializeAsPlaceholder(final Object value, final JsonGenerator gen, final SerializerProvider provider)\n
    '''
def depositSchemaProperty():
    '''returns None\n\n
    depositSchemaProperty(final JsonObjectFormatVisitor objectVisitor, final SerializerProvider provider)\n
    depositSchemaProperty(final ObjectNode propertiesNode, final SerializerProvider provider)\n
    '''
def getType():
    '''returns JavaType\n\n
    getType()\n
    '''
def getWrapperName():
    '''returns PropertyName\n\n
    getWrapperName()\n
    '''
def getMember():
    '''returns AnnotatedMember\n\n
    getMember()\n
    '''
