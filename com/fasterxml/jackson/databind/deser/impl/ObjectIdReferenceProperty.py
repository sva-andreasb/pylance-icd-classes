def ObjectIdReferenceProperty():
'''public ObjectIdReferenceProperty(final SettableBeanProperty forward, final ObjectIdInfo objectIdInfo)
public ObjectIdReferenceProperty(final ObjectIdReferenceProperty src, final JsonDeserializer<?> deser, final NullValueProvider nva)
public ObjectIdReferenceProperty(final ObjectIdReferenceProperty src, final PropertyName newName)
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
def PropertyReferring():
'''public PropertyReferring(final ObjectIdReferenceProperty parent, final UnresolvedForwardReference ref, final Class<?> type, final Object ob)
'''
pass
def handleResolvedForwardReference():
'''public void handleResolvedForwardReference(final Object id, final Object value)
'''
pass
