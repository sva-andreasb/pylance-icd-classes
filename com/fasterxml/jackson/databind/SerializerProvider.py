def SerializerProvider():
    '''    public SerializerProvider()
    '''
def setDefaultKeySerializer():
    '''    public void setDefaultKeySerializer(final JsonSerializer<Object> ks)
    '''
def setNullValueSerializer():
    '''    public void setNullValueSerializer(final JsonSerializer<Object> nvs)
    '''
def setNullKeySerializer():
    '''    public void setNullKeySerializer(final JsonSerializer<Object> nks)
    '''
def getConfig():
    '''    public final SerializationConfig getConfig()
    '''
def getAnnotationIntrospector():
    '''    public final AnnotationIntrospector getAnnotationIntrospector()
    '''
def getTypeFactory():
    '''    public final TypeFactory getTypeFactory()
    '''
def canOverrideAccessModifiers():
    '''    public final boolean canOverrideAccessModifiers()
    '''
def isEnabled():
    '''    public final boolean isEnabled(final MapperFeature feature)
    public final boolean isEnabled(final SerializationFeature feature)
    '''
def getLocale():
    '''    public Locale getLocale()
    '''
def getTimeZone():
    '''    public TimeZone getTimeZone()
    '''
def getAttribute():
    '''    public Object getAttribute(final Object key)
    '''
def setAttribute():
    '''    public SerializerProvider setAttribute(final Object key, final Object value)
    '''
def hasSerializationFeatures():
    '''    public final boolean hasSerializationFeatures(final int featureMask)
    '''
def getFilterProvider():
    '''    public final FilterProvider getFilterProvider()
    '''
def getGenerator():
    '''    public JsonGenerator getGenerator()
    '''
def findValueSerializer():
    '''    public JsonSerializer<Object> findValueSerializer(final Class<?> valueType, final BeanProperty property)
    public JsonSerializer<Object> findValueSerializer(final JavaType valueType, final BeanProperty property)
    public JsonSerializer<Object> findValueSerializer(final Class<?> valueType)
    public JsonSerializer<Object> findValueSerializer(final JavaType valueType)
    '''
def findPrimaryPropertySerializer():
    '''    public JsonSerializer<Object> findPrimaryPropertySerializer(final JavaType valueType, final BeanProperty property)
    public JsonSerializer<Object> findPrimaryPropertySerializer(final Class<?> valueType, final BeanProperty property)
    '''
def findTypedValueSerializer():
    '''    public JsonSerializer<Object> findTypedValueSerializer(final Class<?> valueType, final boolean cache, final BeanProperty property)
    public JsonSerializer<Object> findTypedValueSerializer(final JavaType valueType, final boolean cache, final BeanProperty property)
    '''
def findTypeSerializer():
    '''    public TypeSerializer findTypeSerializer(final JavaType javaType)
    '''
def findKeySerializer():
    '''    public JsonSerializer<Object> findKeySerializer(final JavaType keyType, final BeanProperty property)
    public JsonSerializer<Object> findKeySerializer(final Class<?> rawKeyType, final BeanProperty property)
    '''
def getDefaultNullKeySerializer():
    '''    public JsonSerializer<Object> getDefaultNullKeySerializer()
    '''
def getDefaultNullValueSerializer():
    '''    public JsonSerializer<Object> getDefaultNullValueSerializer()
    '''
def findNullKeySerializer():
    '''    public JsonSerializer<Object> findNullKeySerializer(final JavaType serializationType, final BeanProperty property)
    '''
def findNullValueSerializer():
    '''    public JsonSerializer<Object> findNullValueSerializer(final BeanProperty property)
    '''
def getUnknownTypeSerializer():
    '''    public JsonSerializer<Object> getUnknownTypeSerializer(final Class<?> unknownType)
    '''
def isUnknownTypeSerializer():
    '''    public boolean isUnknownTypeSerializer(final JsonSerializer<?> ser)
    '''
def defaultSerializeValue():
    '''    public final void defaultSerializeValue(final Object value, final JsonGenerator gen)
    '''
def defaultSerializeField():
    '''    public final void defaultSerializeField(final String fieldName, final Object value, final JsonGenerator gen)
    '''
def defaultSerializeDateValue():
    '''    public final void defaultSerializeDateValue(final long timestamp, final JsonGenerator gen)
    public final void defaultSerializeDateValue(final Date date, final JsonGenerator gen)
    '''
def defaultSerializeDateKey():
    '''    public void defaultSerializeDateKey(final long timestamp, final JsonGenerator gen)
    public void defaultSerializeDateKey(final Date date, final JsonGenerator gen)
    '''
def defaultSerializeNull():
    '''    public final void defaultSerializeNull(final JsonGenerator gen)
    '''
def reportMappingProblem():
    '''    public void reportMappingProblem(final String message, final Object... args)
    public void reportMappingProblem(final Throwable t, String message, final Object... msgArgs)
    '''
def reportBadTypeDefinition():
    '''    public <T> T reportBadTypeDefinition(final BeanDescription bean, String msg, final Object... msgArgs)
    '''
def reportBadPropertyDefinition():
    '''    public <T> T reportBadPropertyDefinition(final BeanDescription bean, final BeanPropertyDefinition prop, String message, final Object... msgArgs)
    '''
def reportBadDefinition():
    '''    public <T> T reportBadDefinition(final JavaType type, final String msg)
    public <T> T reportBadDefinition(final JavaType type, final String msg, final Throwable cause)
    public <T> T reportBadDefinition(final Class<?> raw, final String msg, final Throwable cause)
    '''
def invalidTypeIdException():
    '''    public JsonMappingException invalidTypeIdException(final JavaType baseType, final String typeId, final String extraDesc)
    '''
def mappingException():
    '''    public JsonMappingException mappingException(final String message, final Object... msgArgs)
    '''
