def SerializerProvider():
'''public SerializerProvider()
'''
pass
def setDefaultKeySerializer():
'''public void setDefaultKeySerializer(final JsonSerializer<Object> ks)
'''
pass
def setNullValueSerializer():
'''public void setNullValueSerializer(final JsonSerializer<Object> nvs)
'''
pass
def setNullKeySerializer():
'''public void setNullKeySerializer(final JsonSerializer<Object> nks)
'''
pass
def getConfig():
'''public final SerializationConfig getConfig()
'''
pass
def getAnnotationIntrospector():
'''public final AnnotationIntrospector getAnnotationIntrospector()
'''
pass
def getTypeFactory():
'''public final TypeFactory getTypeFactory()
'''
pass
def canOverrideAccessModifiers():
'''public final boolean canOverrideAccessModifiers()
'''
pass
def isEnabled():
'''public final boolean isEnabled(final MapperFeature feature)
public final boolean isEnabled(final SerializationFeature feature)
'''
pass
def getLocale():
'''public Locale getLocale()
'''
pass
def getTimeZone():
'''public TimeZone getTimeZone()
'''
pass
def getAttribute():
'''public Object getAttribute(final Object key)
'''
pass
def setAttribute():
'''public SerializerProvider setAttribute(final Object key, final Object value)
'''
pass
def hasSerializationFeatures():
'''public final boolean hasSerializationFeatures(final int featureMask)
'''
pass
def getFilterProvider():
'''public final FilterProvider getFilterProvider()
'''
pass
def getGenerator():
'''public JsonGenerator getGenerator()
'''
pass
def findValueSerializer():
'''public JsonSerializer<Object> findValueSerializer(final Class<?> valueType, final BeanProperty property)
public JsonSerializer<Object> findValueSerializer(final JavaType valueType, final BeanProperty property)
public JsonSerializer<Object> findValueSerializer(final Class<?> valueType)
public JsonSerializer<Object> findValueSerializer(final JavaType valueType)
'''
pass
def findPrimaryPropertySerializer():
'''public JsonSerializer<Object> findPrimaryPropertySerializer(final JavaType valueType, final BeanProperty property)
public JsonSerializer<Object> findPrimaryPropertySerializer(final Class<?> valueType, final BeanProperty property)
'''
pass
def findTypedValueSerializer():
'''public JsonSerializer<Object> findTypedValueSerializer(final Class<?> valueType, final boolean cache, final BeanProperty property)
public JsonSerializer<Object> findTypedValueSerializer(final JavaType valueType, final boolean cache, final BeanProperty property)
'''
pass
def findTypeSerializer():
'''public TypeSerializer findTypeSerializer(final JavaType javaType)
'''
pass
def findKeySerializer():
'''public JsonSerializer<Object> findKeySerializer(final JavaType keyType, final BeanProperty property)
public JsonSerializer<Object> findKeySerializer(final Class<?> rawKeyType, final BeanProperty property)
'''
pass
def getDefaultNullKeySerializer():
'''public JsonSerializer<Object> getDefaultNullKeySerializer()
'''
pass
def getDefaultNullValueSerializer():
'''public JsonSerializer<Object> getDefaultNullValueSerializer()
'''
pass
def findNullKeySerializer():
'''public JsonSerializer<Object> findNullKeySerializer(final JavaType serializationType, final BeanProperty property)
'''
pass
def findNullValueSerializer():
'''public JsonSerializer<Object> findNullValueSerializer(final BeanProperty property)
'''
pass
def getUnknownTypeSerializer():
'''public JsonSerializer<Object> getUnknownTypeSerializer(final Class<?> unknownType)
'''
pass
def isUnknownTypeSerializer():
'''public boolean isUnknownTypeSerializer(final JsonSerializer<?> ser)
'''
pass
def defaultSerializeValue():
'''public final void defaultSerializeValue(final Object value, final JsonGenerator gen)
'''
pass
def defaultSerializeField():
'''public final void defaultSerializeField(final String fieldName, final Object value, final JsonGenerator gen)
'''
pass
def defaultSerializeDateValue():
'''public final void defaultSerializeDateValue(final long timestamp, final JsonGenerator gen)
public final void defaultSerializeDateValue(final Date date, final JsonGenerator gen)
'''
pass
def defaultSerializeDateKey():
'''public void defaultSerializeDateKey(final long timestamp, final JsonGenerator gen)
public void defaultSerializeDateKey(final Date date, final JsonGenerator gen)
'''
pass
def defaultSerializeNull():
'''public final void defaultSerializeNull(final JsonGenerator gen)
'''
pass
def reportMappingProblem():
'''public void reportMappingProblem(final String message, final Object... args)
public void reportMappingProblem(final Throwable t, String message, final Object... msgArgs)
'''
pass
def reportBadTypeDefinition():
'''public <T> T reportBadTypeDefinition(final BeanDescription bean, String msg, final Object... msgArgs)
'''
pass
def reportBadPropertyDefinition():
'''public <T> T reportBadPropertyDefinition(final BeanDescription bean, final BeanPropertyDefinition prop, String message, final Object... msgArgs)
'''
pass
def reportBadDefinition():
'''public <T> T reportBadDefinition(final JavaType type, final String msg)
public <T> T reportBadDefinition(final JavaType type, final String msg, final Throwable cause)
public <T> T reportBadDefinition(final Class<?> raw, final String msg, final Throwable cause)
'''
pass
def invalidTypeIdException():
'''public JsonMappingException invalidTypeIdException(final JavaType baseType, final String typeId, final String extraDesc)
'''
pass
def mappingException():
'''public JsonMappingException mappingException(final String message, final Object... msgArgs)
'''
pass
