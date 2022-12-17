def getConfig():
    '''returns DeserializationConfig\n\n
    getConfig()\n
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
    '''returns DeserializationContext\n\n
    setAttribute(final Object key, final Object value)\n
    '''
def getContextualType():
    '''returns JavaType\n\n
    getContextualType()\n
    '''
def getFactory():
    '''returns DeserializerFactory\n\n
    getFactory()\n
    '''
def hasValueDeserializerFor():
    '''returns boolean\n\n
    hasValueDeserializerFor(final JavaType type, final AtomicReference<Throwable> cause)\n
    '''
def parseDate():
    '''returns Date\n\n
    parseDate(final String dateStr)\n
    '''
def constructCalendar():
    '''returns Calendar\n\n
    constructCalendar(final Date d)\n
    '''
def handleUnknownProperty():
    '''returns boolean\n\n
    handleUnknownProperty(final JsonParser p, final JsonDeserializer<?> deser, final Object instanceOrClass, final String propName)\n
    '''
def handleWeirdKey():
    '''returns Object\n\n
    handleWeirdKey(final Class<?> keyClass, final String keyValue, String msg, final Object... msgArgs)\n
    '''
def handleWeirdStringValue():
    '''returns Object\n\n
    handleWeirdStringValue(final Class<?> targetClass, final String value, String msg, final Object... msgArgs)\n
    '''
def handleWeirdNumberValue():
    '''returns Object\n\n
    handleWeirdNumberValue(final Class<?> targetClass, final Number value, String msg, final Object... msgArgs)\n
    '''
def handleWeirdNativeValue():
    '''returns Object\n\n
    handleWeirdNativeValue(final JavaType targetType, final Object badValue, final JsonParser p)\n
    '''
def handleMissingInstantiator():
    '''returns Object\n\n
    handleMissingInstantiator(final Class<?> instClass, final ValueInstantiator valueInst, JsonParser p, String msg, final Object... msgArgs)\n
    '''
def handleInstantiationProblem():
    '''returns Object\n\n
    handleInstantiationProblem(final Class<?> instClass, final Object argument, final Throwable t)\n
    '''
def handleUnexpectedToken():
    '''returns Object\n\n
    handleUnexpectedToken(final Class<?> instClass, final JsonParser p)\n
    handleUnexpectedToken(final Class<?> instClass, final JsonToken t, final JsonParser p, String msg, final Object... msgArgs)\n
    '''
def handleUnknownTypeId():
    '''returns JavaType\n\n
    handleUnknownTypeId(final JavaType baseType, final String id, final TypeIdResolver idResolver, final String extraDesc)\n
    '''
def handleMissingTypeId():
    '''returns JavaType\n\n
    handleMissingTypeId(final JavaType baseType, final TypeIdResolver idResolver, final String extraDesc)\n
    '''
def reportWrongTokenException():
    '''returns None\n\n
    reportWrongTokenException(final JsonDeserializer<?> deser, final JsonToken expToken, String msg, final Object... msgArgs)\n
    reportWrongTokenException(final JavaType targetType, final JsonToken expToken, String msg, final Object... msgArgs)\n
    reportWrongTokenException(final Class<?> targetType, final JsonToken expToken, String msg, final Object... msgArgs)\n
    reportWrongTokenException(final JsonParser p, final JsonToken expToken, String msg, final Object... msgArgs)\n
    '''
def reportUnknownProperty():
    '''returns None\n\n
    reportUnknownProperty(final Object instanceOrClass, final String fieldName, final JsonDeserializer<?> deser)\n
    '''
def reportMissingContent():
    '''returns None\n\n
    reportMissingContent(final String msg, final Object... msgArgs)\n
    '''
def wrongTokenException():
    '''returns JsonMappingException\n\n
    wrongTokenException(final JsonParser p, final JavaType targetType, final JsonToken expToken, final String extra)\n
    wrongTokenException(final JsonParser p, final Class<?> targetType, final JsonToken expToken, final String extra)\n
    wrongTokenException(final JsonParser p, final JsonToken expToken, final String msg)\n
    '''
def weirdKeyException():
    '''returns JsonMappingException\n\n
    weirdKeyException(final Class<?> keyClass, final String keyValue, final String msg)\n
    '''
def weirdStringException():
    '''returns JsonMappingException\n\n
    weirdStringException(final String value, final Class<?> instClass, final String msg)\n
    '''
def weirdNumberException():
    '''returns JsonMappingException\n\n
    weirdNumberException(final Number value, final Class<?> instClass, final String msg)\n
    '''
def weirdNativeValueException():
    '''returns JsonMappingException\n\n
    weirdNativeValueException(final Object value, final Class<?> instClass)\n
    '''
def instantiationException():
    '''returns JsonMappingException\n\n
    instantiationException(final Class<?> instClass, final Throwable cause)\n
    instantiationException(final Class<?> instClass, final String msg0)\n
    '''
def invalidTypeIdException():
    '''returns JsonMappingException\n\n
    invalidTypeIdException(final JavaType baseType, final String typeId, final String extraDesc)\n
    '''
def missingTypeIdException():
    '''returns JsonMappingException\n\n
    missingTypeIdException(final JavaType baseType, final String extraDesc)\n
    '''
def unknownTypeException():
    '''returns JsonMappingException\n\n
    unknownTypeException(final JavaType type, final String id, final String extraDesc)\n
    '''
def endOfInputException():
    '''returns JsonMappingException\n\n
    endOfInputException(final Class<?> instClass)\n
    '''
def reportMappingException():
    '''returns None\n\n
    reportMappingException(final String msg, final Object... msgArgs)\n
    '''
def mappingException():
    '''returns JsonMappingException\n\n
    mappingException(final String message)\n
    mappingException(final String msg, final Object... msgArgs)\n
    mappingException(final Class<?> targetClass)\n
    mappingException(final Class<?> targetClass, final JsonToken token)\n
    '''
