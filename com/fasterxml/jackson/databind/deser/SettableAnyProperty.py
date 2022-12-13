def SettableAnyProperty():
'''public SettableAnyProperty(final BeanProperty property, final AnnotatedMember setter, final JavaType type, final KeyDeserializer keyDeser, final JsonDeserializer<Object> valueDeser, final TypeDeserializer typeDeser)
public SettableAnyProperty(final BeanProperty property, final AnnotatedMember setter, final JavaType type, final JsonDeserializer<Object> valueDeser, final TypeDeserializer typeDeser)
'''
pass
def withValueDeserializer():
'''public SettableAnyProperty withValueDeserializer(final JsonDeserializer<Object> deser)
'''
pass
def fixAccess():
'''public void fixAccess(final DeserializationConfig config)
'''
pass
def getProperty():
'''public BeanProperty getProperty()
'''
pass
def hasValueDeserializer():
'''public boolean hasValueDeserializer()
'''
pass
def getType():
'''public JavaType getType()
'''
pass
def deserializeAndSet():
'''public final void deserializeAndSet(final JsonParser p, final DeserializationContext ctxt, final Object instance, final String propName)
'''
pass
def deserialize():
'''public Object deserialize(final JsonParser p, final DeserializationContext ctxt)
'''
pass
def set():
'''public void set(final Object instance, final Object propName, final Object value)
'''
pass
def toString():
'''public String toString()
'''
pass
def AnySetterReferring():
'''public AnySetterReferring(final SettableAnyProperty parent, final UnresolvedForwardReference reference, final Class<?> type, final Object instance, final String propName)
'''
pass
def handleResolvedForwardReference():
'''public void handleResolvedForwardReference(final Object id, final Object value)
'''
pass
