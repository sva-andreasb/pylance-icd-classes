def ():
    '''returns BeanPropertyWriter\n\n
    (final BeanPropertyDefinition propDef, final AnnotatedMember member, final Annotations contextAnnotations, final JavaType declaredType, final JsonSerializer<?> ser, final TypeSerializer typeSer, final JavaType serType, final boolean suppressNulls, final Object suppressableValue, final Class<?>[] includeInViews)\n
    (final BeanPropertyDefinition propDef, final AnnotatedMember member, final Annotations contextAnnotations, final JavaType declaredType, final JsonSerializer<?> ser, final TypeSerializer typeSer, final JavaType serType, final boolean suppressNulls, final Object suppressableValue)\n
    '''
def rename():
    '''returns BeanPropertyWriter\n\n
    rename(final NameTransformer transformer)\n
    '''
def assignTypeSerializer():
    '''returns None\n\n
    assignTypeSerializer(final TypeSerializer typeSer)\n
    '''
def assignSerializer():
    '''returns None\n\n
    assignSerializer(final JsonSerializer<Object> ser)\n
    '''
def assignNullSerializer():
    '''returns None\n\n
    assignNullSerializer(final JsonSerializer<Object> nullSer)\n
    '''
def unwrappingWriter():
    '''returns BeanPropertyWriter\n\n
    unwrappingWriter(final NameTransformer unwrapper)\n
    '''
def setNonTrivialBaseType():
    '''returns None\n\n
    setNonTrivialBaseType(final JavaType t)\n
    '''
def fixAccess():
    '''returns None\n\n
    fixAccess(final SerializationConfig config)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getFullName():
    '''returns PropertyName\n\n
    getFullName()\n
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
def getInternalSetting():
    '''returns Object\n\n
    getInternalSetting(final Object key)\n
    '''
def setInternalSetting():
    '''returns Object\n\n
    setInternalSetting(final Object key, final Object value)\n
    '''
def removeInternalSetting():
    '''returns Object\n\n
    removeInternalSetting(final Object key)\n
    '''
def getSerializedName():
    '''returns SerializableString\n\n
    getSerializedName()\n
    '''
def hasSerializer():
    '''returns boolean\n\n
    hasSerializer()\n
    '''
def hasNullSerializer():
    '''returns boolean\n\n
    hasNullSerializer()\n
    '''
def getTypeSerializer():
    '''returns TypeSerializer\n\n
    getTypeSerializer()\n
    '''
def isUnwrapping():
    '''returns boolean\n\n
    isUnwrapping()\n
    '''
def willSuppressNulls():
    '''returns boolean\n\n
    willSuppressNulls()\n
    '''
def wouldConflictWithName():
    '''returns boolean\n\n
    wouldConflictWithName(final PropertyName name)\n
    '''
def getSerializer():
    '''returns JsonSerializer<Object>\n\n
    getSerializer()\n
    '''
def getSerializationType():
    '''returns JavaType\n\n
    getSerializationType()\n
    '''
def getGenericPropertyType():
    '''returns Type\n\n
    getGenericPropertyType()\n
    '''
def serializeAsField():
    '''returns None\n\n
    serializeAsField(final Object bean, final JsonGenerator gen, final SerializerProvider prov)\n
    '''
def serializeAsOmittedField():
    '''returns None\n\n
    serializeAsOmittedField(final Object bean, final JsonGenerator gen, final SerializerProvider prov)\n
    '''
def serializeAsElement():
    '''returns None\n\n
    serializeAsElement(final Object bean, final JsonGenerator gen, final SerializerProvider prov)\n
    '''
def serializeAsPlaceholder():
    '''returns None\n\n
    serializeAsPlaceholder(final Object bean, final JsonGenerator gen, final SerializerProvider prov)\n
    '''
def depositSchemaProperty():
    '''returns None\n\n
    depositSchemaProperty(final JsonObjectFormatVisitor v, final SerializerProvider provider)\n
    depositSchemaProperty(final ObjectNode propertiesNode, final SerializerProvider provider)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
