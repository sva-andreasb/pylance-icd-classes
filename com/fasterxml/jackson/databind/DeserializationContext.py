def getConfig():
    '''public DeserializationConfig getConfig()
    '''
def canOverrideAccessModifiers():
    '''public final boolean canOverrideAccessModifiers()
    '''
def isEnabled():
    '''public final boolean isEnabled(final MapperFeature feature)
    public final boolean isEnabled(final DeserializationFeature feat)
    '''
def getAnnotationIntrospector():
    '''public final AnnotationIntrospector getAnnotationIntrospector()
    '''
def getTypeFactory():
    '''public final TypeFactory getTypeFactory()
    '''
def getLocale():
    '''public Locale getLocale()
    '''
def getTimeZone():
    '''public TimeZone getTimeZone()
    '''
def getAttribute():
    '''public Object getAttribute(final Object key)
    '''
def setAttribute():
    '''public DeserializationContext setAttribute(final Object key, final Object value)
    '''
def getContextualType():
    '''public JavaType getContextualType()
    '''
def getFactory():
    '''public DeserializerFactory getFactory()
    '''
def getDeserializationFeatures():
    '''public final int getDeserializationFeatures()
    '''
def hasDeserializationFeatures():
    '''public final boolean hasDeserializationFeatures(final int featureMask)
    '''
def hasSomeOfFeatures():
    '''public final boolean hasSomeOfFeatures(final int featureMask)
    '''
def getParser():
    '''public final JsonParser getParser()
    '''
def findInjectableValue():
    '''public final Object findInjectableValue(final Object valueId, final BeanProperty forProperty, final Object beanInstance)
    '''
def getBase64Variant():
    '''public final Base64Variant getBase64Variant()
    '''
def getNodeFactory():
    '''public final JsonNodeFactory getNodeFactory()
    '''
def hasValueDeserializerFor():
    '''public boolean hasValueDeserializerFor(final JavaType type, final AtomicReference<Throwable> cause)
    '''
def findContextualValueDeserializer():
    '''public final JsonDeserializer<Object> findContextualValueDeserializer(final JavaType type, final BeanProperty prop)
    '''
def findNonContextualValueDeserializer():
    '''public final JsonDeserializer<Object> findNonContextualValueDeserializer(final JavaType type)
    '''
def findRootValueDeserializer():
    '''public final JsonDeserializer<Object> findRootValueDeserializer(final JavaType type)
    '''
def findKeyDeserializer():
    '''public final KeyDeserializer findKeyDeserializer(final JavaType keyType, final BeanProperty prop)
    '''
def constructType():
    '''public final JavaType constructType(final Class<?> cls)
    '''
def leaseObjectBuffer():
    '''public final ObjectBuffer leaseObjectBuffer()
    '''
def returnObjectBuffer():
    '''public final void returnObjectBuffer(final ObjectBuffer buf)
    '''
def getArrayBuilders():
    '''public final ArrayBuilders getArrayBuilders()
    '''
def parseDate():
    '''public Date parseDate(final String dateStr)
    '''
def constructCalendar():
    '''public Calendar constructCalendar(final Date d)
    '''
def readValue():
    '''public <T> T readValue(final JsonParser p, final Class<T> type)
    public <T> T readValue(final JsonParser p, final JavaType type)
    '''
def readPropertyValue():
    '''public <T> T readPropertyValue(final JsonParser p, final BeanProperty prop, final Class<T> type)
    public <T> T readPropertyValue(final JsonParser p, final BeanProperty prop, final JavaType type)
    '''
def handleUnknownProperty():
    '''public boolean handleUnknownProperty(final JsonParser p, final JsonDeserializer<?> deser, final Object instanceOrClass, final String propName)
    '''
def handleWeirdKey():
    '''public Object handleWeirdKey(final Class<?> keyClass, final String keyValue, String msg, final Object... msgArgs)
    '''
def handleWeirdStringValue():
    '''public Object handleWeirdStringValue(final Class<?> targetClass, final String value, String msg, final Object... msgArgs)
    '''
def handleWeirdNumberValue():
    '''public Object handleWeirdNumberValue(final Class<?> targetClass, final Number value, String msg, final Object... msgArgs)
    '''
def handleWeirdNativeValue():
    '''public Object handleWeirdNativeValue(final JavaType targetType, final Object badValue, final JsonParser p)
    '''
def handleMissingInstantiator():
    '''public Object handleMissingInstantiator(final Class<?> instClass, final ValueInstantiator valueInst, JsonParser p, String msg, final Object... msgArgs)
    '''
def handleInstantiationProblem():
    '''public Object handleInstantiationProblem(final Class<?> instClass, final Object argument, final Throwable t)
    '''
def handleUnexpectedToken():
    '''public Object handleUnexpectedToken(final Class<?> instClass, final JsonParser p)
    public Object handleUnexpectedToken(final Class<?> instClass, final JsonToken t, final JsonParser p, String msg, final Object... msgArgs)
    '''
def handleUnknownTypeId():
    '''public JavaType handleUnknownTypeId(final JavaType baseType, final String id, final TypeIdResolver idResolver, final String extraDesc)
    '''
def handleMissingTypeId():
    '''public JavaType handleMissingTypeId(final JavaType baseType, final TypeIdResolver idResolver, final String extraDesc)
    '''
def reportWrongTokenException():
    '''public void reportWrongTokenException(final JsonDeserializer<?> deser, final JsonToken expToken, String msg, final Object... msgArgs)
    public void reportWrongTokenException(final JavaType targetType, final JsonToken expToken, String msg, final Object... msgArgs)
    public void reportWrongTokenException(final Class<?> targetType, final JsonToken expToken, String msg, final Object... msgArgs)
    public void reportWrongTokenException(final JsonParser p, final JsonToken expToken, String msg, final Object... msgArgs)
    '''
def reportUnresolvedObjectId():
    '''public <T> T reportUnresolvedObjectId(final ObjectIdReader oidReader, final Object bean)
    '''
def reportInputMismatch():
    '''public <T> T reportInputMismatch(final BeanProperty prop, String msg, final Object... msgArgs)
    public <T> T reportInputMismatch(final JsonDeserializer<?> src, String msg, final Object... msgArgs)
    public <T> T reportInputMismatch(final Class<?> targetType, String msg, final Object... msgArgs)
    public <T> T reportInputMismatch(final JavaType targetType, String msg, final Object... msgArgs)
    '''
def reportTrailingTokens():
    '''public <T> T reportTrailingTokens(final Class<?> targetType, final JsonParser p, final JsonToken trailingToken)
    '''
def reportUnknownProperty():
    '''public void reportUnknownProperty(final Object instanceOrClass, final String fieldName, final JsonDeserializer<?> deser)
    '''
def reportMissingContent():
    '''public void reportMissingContent(final String msg, final Object... msgArgs)
    '''
def reportBadTypeDefinition():
    '''public <T> T reportBadTypeDefinition(final BeanDescription bean, String msg, final Object... msgArgs)
    '''
def reportBadPropertyDefinition():
    '''public <T> T reportBadPropertyDefinition(final BeanDescription bean, final BeanPropertyDefinition prop, String msg, final Object... msgArgs)
    '''
def reportBadDefinition():
    '''public <T> T reportBadDefinition(final JavaType type, final String msg)
    '''
def reportBadMerge():
    '''public <T> T reportBadMerge(final JsonDeserializer<?> deser)
    '''
def wrongTokenException():
    '''public JsonMappingException wrongTokenException(final JsonParser p, final JavaType targetType, final JsonToken expToken, final String extra)
    public JsonMappingException wrongTokenException(final JsonParser p, final Class<?> targetType, final JsonToken expToken, final String extra)
    public JsonMappingException wrongTokenException(final JsonParser p, final JsonToken expToken, final String msg)
    '''
def weirdKeyException():
    '''public JsonMappingException weirdKeyException(final Class<?> keyClass, final String keyValue, final String msg)
    '''
def weirdStringException():
    '''public JsonMappingException weirdStringException(final String value, final Class<?> instClass, final String msg)
    '''
def weirdNumberException():
    '''public JsonMappingException weirdNumberException(final Number value, final Class<?> instClass, final String msg)
    '''
def weirdNativeValueException():
    '''public JsonMappingException weirdNativeValueException(final Object value, final Class<?> instClass)
    '''
def instantiationException():
    '''public JsonMappingException instantiationException(final Class<?> instClass, final Throwable cause)
    public JsonMappingException instantiationException(final Class<?> instClass, final String msg0)
    '''
def invalidTypeIdException():
    '''public JsonMappingException invalidTypeIdException(final JavaType baseType, final String typeId, final String extraDesc)
    '''
def missingTypeIdException():
    '''public JsonMappingException missingTypeIdException(final JavaType baseType, final String extraDesc)
    '''
def unknownTypeException():
    '''public JsonMappingException unknownTypeException(final JavaType type, final String id, final String extraDesc)
    '''
def endOfInputException():
    '''public JsonMappingException endOfInputException(final Class<?> instClass)
    '''
def reportMappingException():
    '''public void reportMappingException(final String msg, final Object... msgArgs)
    '''
def mappingException():
    '''public JsonMappingException mappingException(final String message)
    public JsonMappingException mappingException(final String msg, final Object... msgArgs)
    public JsonMappingException mappingException(final Class<?> targetClass)
    public JsonMappingException mappingException(final Class<?> targetClass, final JsonToken token)
    '''
