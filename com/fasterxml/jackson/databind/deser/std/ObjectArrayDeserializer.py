def ObjectArrayDeserializer():
'''public ObjectArrayDeserializer(final JavaType arrayType, final JsonDeserializer<Object> elemDeser, final TypeDeserializer elemTypeDeser)
'''
pass
def withDeserializer():
'''public ObjectArrayDeserializer withDeserializer(final TypeDeserializer elemTypeDeser, final JsonDeserializer<?> elemDeser)
'''
pass
def withResolved():
'''public ObjectArrayDeserializer withResolved(final TypeDeserializer elemTypeDeser, final JsonDeserializer<?> elemDeser, final NullValueProvider nuller, final Boolean unwrapSingle)
'''
pass
def isCachable():
'''public boolean isCachable()
'''
pass
def getContentDeserializer():
'''public JsonDeserializer<Object> getContentDeserializer()
'''
pass
def getEmptyAccessPattern():
'''public AccessPattern getEmptyAccessPattern()
'''
pass
def getEmptyValue():
'''public Object getEmptyValue(final DeserializationContext ctxt)
'''
pass
def deserialize():
'''public Object[] deserialize(final JsonParser p, final DeserializationContext ctxt)
public Object[] deserialize(final JsonParser p, final DeserializationContext ctxt, final Object[] intoValue)
'''
pass
def deserializeWithType():
'''public Object[] deserializeWithType(final JsonParser p, final DeserializationContext ctxt, final TypeDeserializer typeDeserializer)
'''
pass
