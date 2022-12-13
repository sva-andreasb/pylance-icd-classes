def MethodProperty():
'''public MethodProperty(final BeanPropertyDefinition propDef, final JavaType type, final TypeDeserializer typeDeser, final Annotations contextAnnotations, final AnnotatedMethod method)
'''
pass
def withName():
'''public SettableBeanProperty withName(final PropertyName newName)
'''
pass
def withValueDeserializer():
'''public SettableBeanProperty withValueDeserializer(final JsonDeserializer<?> deser)
'''
pass
def withNullProvider():
'''public SettableBeanProperty withNullProvider(final NullValueProvider nva)
'''
pass
def fixAccess():
'''public void fixAccess(final DeserializationConfig config)
'''
pass
def getAnnotation():
'''public <A extends Annotation> A getAnnotation(final Class<A> acls)
'''
pass
def getMember():
'''public AnnotatedMember getMember()
'''
pass
def deserializeAndSet():
'''public void deserializeAndSet(final JsonParser p, final DeserializationContext ctxt, final Object instance)
'''
pass
def deserializeSetAndReturn():
'''public Object deserializeSetAndReturn(final JsonParser p, final DeserializationContext ctxt, final Object instance)
'''
pass
def set():
'''public final void set(final Object instance, final Object value)
'''
pass
def setAndReturn():
'''public Object setAndReturn(final Object instance, final Object value)
'''
pass
