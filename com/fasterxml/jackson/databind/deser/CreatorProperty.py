def CreatorProperty():
'''public CreatorProperty(final PropertyName name, final JavaType type, final PropertyName wrapperName, final TypeDeserializer typeDeser, final Annotations contextAnnotations, final AnnotatedParameter param, final int index, final Object injectableValueId, final PropertyMetadata metadata)
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
def setFallbackSetter():
'''public void setFallbackSetter(final SettableBeanProperty fallbackSetter)
'''
pass
def markAsIgnorable():
'''public void markAsIgnorable()
'''
pass
def isIgnorable():
'''public boolean isIgnorable()
'''
pass
def findInjectableValue():
'''public Object findInjectableValue(final DeserializationContext context, final Object beanInstance)
'''
pass
def inject():
'''public void inject(final DeserializationContext context, final Object beanInstance)
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
def getCreatorIndex():
'''public int getCreatorIndex()
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
'''public void set(final Object instance, final Object value)
'''
pass
def setAndReturn():
'''public Object setAndReturn(final Object instance, final Object value)
'''
pass
def getInjectableValueId():
'''public Object getInjectableValueId()
'''
pass
def toString():
'''public String toString()
'''
pass
