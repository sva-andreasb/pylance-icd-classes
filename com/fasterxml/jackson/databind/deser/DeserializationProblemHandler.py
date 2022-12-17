def handleUnknownProperty():
    '''returns boolean\n\n
    handleUnknownProperty(final DeserializationContext ctxt, final JsonParser p, final JsonDeserializer<?> deserializer, final Object beanOrClass, final String propertyName)\n
    '''
def handleWeirdKey():
    '''returns Object\n\n
    handleWeirdKey(final DeserializationContext ctxt, final Class<?> rawKeyType, final String keyValue, final String failureMsg)\n
    '''
def handleWeirdStringValue():
    '''returns Object\n\n
    handleWeirdStringValue(final DeserializationContext ctxt, final Class<?> targetType, final String valueToConvert, final String failureMsg)\n
    '''
def handleWeirdNumberValue():
    '''returns Object\n\n
    handleWeirdNumberValue(final DeserializationContext ctxt, final Class<?> targetType, final Number valueToConvert, final String failureMsg)\n
    '''
def handleWeirdNativeValue():
    '''returns Object\n\n
    handleWeirdNativeValue(final DeserializationContext ctxt, final JavaType targetType, final Object valueToConvert, final JsonParser p)\n
    '''
def handleUnexpectedToken():
    '''returns Object\n\n
    handleUnexpectedToken(final DeserializationContext ctxt, final Class<?> targetType, final JsonToken t, final JsonParser p, final String failureMsg)\n
    '''
def handleInstantiationProblem():
    '''returns Object\n\n
    handleInstantiationProblem(final DeserializationContext ctxt, final Class<?> instClass, final Object argument, final Throwable t)\n
    '''
def handleMissingInstantiator():
    '''returns Object\n\n
    handleMissingInstantiator(final DeserializationContext ctxt, final Class<?> instClass, final ValueInstantiator valueInsta, final JsonParser p, final String msg)\n
    handleMissingInstantiator(final DeserializationContext ctxt, final Class<?> instClass, final JsonParser p, final String msg)\n
    '''
def handleUnknownTypeId():
    '''returns JavaType\n\n
    handleUnknownTypeId(final DeserializationContext ctxt, final JavaType baseType, final String subTypeId, final TypeIdResolver idResolver, final String failureMsg)\n
    '''
def handleMissingTypeId():
    '''returns JavaType\n\n
    handleMissingTypeId(final DeserializationContext ctxt, final JavaType baseType, final TypeIdResolver idResolver, final String failureMsg)\n
    '''
