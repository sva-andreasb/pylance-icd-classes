def StdDelegatingDeserializer():
'''public StdDelegatingDeserializer(final Converter<?, T> converter)
public StdDelegatingDeserializer(final Converter<Object, T> converter, final JavaType delegateType, final JsonDeserializer<?> delegateDeserializer)
'''
pass
def resolve():
'''public void resolve(final DeserializationContext ctxt)
'''
pass
def supportsUpdate():
'''public Boolean supportsUpdate(final DeserializationConfig config)
'''
pass
def deserialize():
'''public T deserialize(final JsonParser p, final DeserializationContext ctxt)
public T deserialize(final JsonParser p, final DeserializationContext ctxt, final Object intoValue)
'''
pass
def deserializeWithType():
'''public Object deserializeWithType(final JsonParser p, final DeserializationContext ctxt, final TypeDeserializer typeDeserializer)
'''
pass
