def ReferenceTypeDeserializer():
'''public ReferenceTypeDeserializer(final JavaType fullType, final ValueInstantiator vi, final TypeDeserializer typeDeser, final JsonDeserializer<?> deser)
public ReferenceTypeDeserializer(final JavaType fullType, final TypeDeserializer typeDeser, final JsonDeserializer<?> deser)
'''
pass
def getNullAccessPattern():
'''public AccessPattern getNullAccessPattern()
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
def getValueType():
'''public JavaType getValueType()
'''
pass
def supportsUpdate():
'''public Boolean supportsUpdate(final DeserializationConfig config)
'''
pass
def deserialize():
'''public T deserialize(final JsonParser p, final DeserializationContext ctxt)
public T deserialize(final JsonParser p, final DeserializationContext ctxt, final T reference)
'''
pass
def deserializeWithType():
'''public Object deserializeWithType(final JsonParser p, final DeserializationContext ctxt, final TypeDeserializer typeDeserializer)
'''
pass
