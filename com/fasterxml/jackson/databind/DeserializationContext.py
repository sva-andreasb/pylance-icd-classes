def getConfig():
'''public DeserializationConfig getConfig()
'''
pass
def canOverrideAccessModifiers():
'''public final boolean canOverrideAccessModifiers()
'''
pass
def isEnabled():
'''public final boolean isEnabled(final MapperFeature feature)
public final boolean isEnabled(final DeserializationFeature feat)
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
'''public DeserializationContext setAttribute(final Object key, final Object value)
'''
pass
def getContextualType():
'''public JavaType getContextualType()
'''
pass
def getFactory():
'''public DeserializerFactory getFactory()
'''
pass
def getDeserializationFeatures():
'''public final int getDeserializationFeatures()
'''
pass
def hasDeserializationFeatures():
'''public final boolean hasDeserializationFeatures(final int featureMask)
'''
pass
def hasSomeOfFeatures():
'''public final boolean hasSomeOfFeatures(final int featureMask)
'''
pass
def getParser():
'''public final JsonParser getParser()
'''
pass
def findInjectableValue():
'''public final Object findInjectableValue(final Object valueId, final BeanProperty forProperty, final Object beanInstance)
'''
pass
def getBase64Variant():
'''public final Base64Variant getBase64Variant()
'''
pass
def getNodeFactory():
'''public final JsonNodeFactory getNodeFactory()
'''
pass
def hasValueDeserializerFor():
'''public boolean hasValueDeserializerFor(final JavaType type, final AtomicReference<Throwable> cause)
'''
pass
def findContextualValueDeserializer():
'''public final JsonDeserializer<Object> findContextualValueDeserializer(final JavaType type, final BeanProperty prop)
'''
pass
def findNonContextualValueDeserializer():
'''public final JsonDeserializer<Object> findNonContextualValueDeserializer(final JavaType type)
'''
pass
def findRootValueDeserializer():
'''public final JsonDeserializer<Object> findRootValueDeserializer(final JavaType type)
'''
pass
def findKeyDeserializer():
'''public final KeyDeserializer findKeyDeserializer(final JavaType keyType, final BeanProperty prop)
'''
pass
def constructType():
'''public final JavaType constructType(final Class<?> cls)
'''
pass
def leaseObjectBuffer():
'''public final ObjectBuffer leaseObjectBuffer()
'''
pass
def returnObjectBuffer():
'''public final void returnObjectBuffer(final ObjectBuffer buf)
'''
pass
def getArrayBuilders():
'''public final ArrayBuilders getArrayBuilders()
'''
pass
def parseDate():
'''public Date parseDate(final String dateStr)
'''
pass
def constructCalendar():
'''public Calendar constructCalendar(final Date d)
'''
pass
def readValue():
'''public <T> T readValue(final JsonParser p, final Class<T> type)
public <T> T readValue(final JsonParser p, final JavaType type)
'''
pass
def readPropertyValue():
'''public <T> T readPropertyValue(final JsonParser p, final BeanProperty prop, final Class<T> type)
public <T> T readPropertyValue(final JsonParser p, final BeanProperty prop, final JavaType type)
'''
pass
def handleUnknownProperty():
'''public boolean handleUnknownProperty(final JsonParser p, final JsonDeserializer<?> deser, final Object instanceOrClass, final String propName)
'''
pass
def handleWeirdKey():
'''public Object handleWeirdKey(final Class<?> keyClass, final String keyValue, String msg, final Object... msgArgs)
'''
pass
def handleWeirdStringValue():
'''public Object handleWeirdStringValue(final Class<?> targetClass, final String value, String msg, final Object... msgArgs)
'''
pass
def handleWeirdNumberValue():
'''public Object handleWeirdNumberValue(final Class<?> targetClass, final Number value, String msg, final Object... msgArgs)
'''
pass
def handleWeirdNativeValue():
'''public Object handleWeirdNativeValue(final JavaType targetType, final Object badValue, final JsonParser p)
'''
pass
def handleMissingInstantiator():
'''public Object handleMissingInstantiator(final Class<?> instClass, final ValueInstantiator valueInst, JsonParser p, String msg, final Object... msgArgs)
'''
pass
def handleInstantiationProblem():
'''public Object handleInstantiationProblem(final Class<?> instClass, final Object argument, final Throwable t)
'''
pass
def handleUnexpectedToken():
'''public Object handleUnexpectedToken(final Class<?> instClass, final JsonParser p)
public Object handleUnexpectedToken(final Class<?> instClass, final JsonToken t, final JsonParser p, String msg, final Object... msgArgs)
'''
pass
def handleUnknownTypeId():
'''public JavaType handleUnknownTypeId(final JavaType baseType, final String id, final TypeIdResolver idResolver, final String extraDesc)
'''
pass
def handleMissingTypeId():
'''public JavaType handleMissingTypeId(final JavaType baseType, final TypeIdResolver idResolver, final String extraDesc)
'''
pass
def reportWrongTokenException():
'''public void reportWrongTokenException(final JsonDeserializer<?> deser, final JsonToken expToken, String msg, final Object... msgArgs)
public void reportWrongTokenException(final JavaType targetType, final JsonToken expToken, String msg, final Object... msgArgs)
public void reportWrongTokenException(final Class<?> targetType, final JsonToken expToken, String msg, final Object... msgArgs)
public void reportWrongTokenException(final JsonParser p, final JsonToken expToken, String msg, final Object... msgArgs)
'''
pass
def reportUnresolvedObjectId():
'''public <T> T reportUnresolvedObjectId(final ObjectIdReader oidReader, final Object bean)
'''
pass
def reportInputMismatch():
'''public <T> T reportInputMismatch(final BeanProperty prop, String msg, final Object... msgArgs)
public <T> T reportInputMismatch(final JsonDeserializer<?> src, String msg, final Object... msgArgs)
public <T> T reportInputMismatch(final Class<?> targetType, String msg, final Object... msgArgs)
public <T> T reportInputMismatch(final JavaType targetType, String msg, final Object... msgArgs)
'''
pass
def reportTrailingTokens():
'''public <T> T reportTrailingTokens(final Class<?> targetType, final JsonParser p, final JsonToken trailingToken)
'''
pass
def reportUnknownProperty():
'''public void reportUnknownProperty(final Object instanceOrClass, final String fieldName, final JsonDeserializer<?> deser)
'''
pass
def reportMissingContent():
'''public void reportMissingContent(final String msg, final Object... msgArgs)
'''
pass
def reportBadTypeDefinition():
'''public <T> T reportBadTypeDefinition(final BeanDescription bean, String msg, final Object... msgArgs)
'''
pass
def reportBadPropertyDefinition():
'''public <T> T reportBadPropertyDefinition(final BeanDescription bean, final BeanPropertyDefinition prop, String msg, final Object... msgArgs)
'''
pass
def reportBadDefinition():
'''public <T> T reportBadDefinition(final JavaType type, final String msg)
'''
pass
def reportBadMerge():
'''public <T> T reportBadMerge(final JsonDeserializer<?> deser)
'''
pass
def wrongTokenException():
'''public JsonMappingException wrongTokenException(final JsonParser p, final JavaType targetType, final JsonToken expToken, final String extra)
public JsonMappingException wrongTokenException(final JsonParser p, final Class<?> targetType, final JsonToken expToken, final String extra)
public JsonMappingException wrongTokenException(final JsonParser p, final JsonToken expToken, final String msg)
'''
pass
def weirdKeyException():
'''public JsonMappingException weirdKeyException(final Class<?> keyClass, final String keyValue, final String msg)
'''
pass
def weirdStringException():
'''public JsonMappingException weirdStringException(final String value, final Class<?> instClass, final String msg)
'''
pass
def weirdNumberException():
'''public JsonMappingException weirdNumberException(final Number value, final Class<?> instClass, final String msg)
'''
pass
def weirdNativeValueException():
'''public JsonMappingException weirdNativeValueException(final Object value, final Class<?> instClass)
'''
pass
def instantiationException():
'''public JsonMappingException instantiationException(final Class<?> instClass, final Throwable cause)
public JsonMappingException instantiationException(final Class<?> instClass, final String msg0)
'''
pass
def invalidTypeIdException():
'''public JsonMappingException invalidTypeIdException(final JavaType baseType, final String typeId, final String extraDesc)
'''
pass
def missingTypeIdException():
'''public JsonMappingException missingTypeIdException(final JavaType baseType, final String extraDesc)
'''
pass
def unknownTypeException():
'''public JsonMappingException unknownTypeException(final JavaType type, final String id, final String extraDesc)
'''
pass
def endOfInputException():
'''public JsonMappingException endOfInputException(final Class<?> instClass)
'''
pass
def reportMappingException():
'''public void reportMappingException(final String msg, final Object... msgArgs)
'''
pass
def mappingException():
'''public JsonMappingException mappingException(final String message)
public JsonMappingException mappingException(final String msg, final Object... msgArgs)
public JsonMappingException mappingException(final Class<?> targetClass)
public JsonMappingException mappingException(final Class<?> targetClass, final JsonToken token)
'''
pass
