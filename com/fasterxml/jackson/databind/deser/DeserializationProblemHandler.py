def handleUnknownProperty():
'''public boolean handleUnknownProperty(final DeserializationContext ctxt, final JsonParser p, final JsonDeserializer<?> deserializer, final Object beanOrClass, final String propertyName)
'''
pass
def handleWeirdKey():
'''public Object handleWeirdKey(final DeserializationContext ctxt, final Class<?> rawKeyType, final String keyValue, final String failureMsg)
'''
pass
def handleWeirdStringValue():
'''public Object handleWeirdStringValue(final DeserializationContext ctxt, final Class<?> targetType, final String valueToConvert, final String failureMsg)
'''
pass
def handleWeirdNumberValue():
'''public Object handleWeirdNumberValue(final DeserializationContext ctxt, final Class<?> targetType, final Number valueToConvert, final String failureMsg)
'''
pass
def handleWeirdNativeValue():
'''public Object handleWeirdNativeValue(final DeserializationContext ctxt, final JavaType targetType, final Object valueToConvert, final JsonParser p)
'''
pass
def handleUnexpectedToken():
'''public Object handleUnexpectedToken(final DeserializationContext ctxt, final Class<?> targetType, final JsonToken t, final JsonParser p, final String failureMsg)
'''
pass
def handleInstantiationProblem():
'''public Object handleInstantiationProblem(final DeserializationContext ctxt, final Class<?> instClass, final Object argument, final Throwable t)
'''
pass
def handleMissingInstantiator():
'''public Object handleMissingInstantiator(final DeserializationContext ctxt, final Class<?> instClass, final ValueInstantiator valueInsta, final JsonParser p, final String msg)
public Object handleMissingInstantiator(final DeserializationContext ctxt, final Class<?> instClass, final JsonParser p, final String msg)
'''
pass
def handleUnknownTypeId():
'''public JavaType handleUnknownTypeId(final DeserializationContext ctxt, final JavaType baseType, final String subTypeId, final TypeIdResolver idResolver, final String failureMsg)
'''
pass
def handleMissingTypeId():
'''public JavaType handleMissingTypeId(final DeserializationContext ctxt, final JavaType baseType, final TypeIdResolver idResolver, final String failureMsg)
'''
pass