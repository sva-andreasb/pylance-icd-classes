def ():
    '''returns CreatorProperty\n\n
    (final PropertyName name, final JavaType type, final PropertyName wrapperName, final TypeDeserializer typeDeser, final Annotations contextAnnotations, final AnnotatedParameter param, final int index, final Object injectableValueId, final PropertyMetadata metadata)\n
    '''
def withName():
    '''returns SettableBeanProperty\n\n
    withName(final PropertyName newName)\n
    '''
def withValueDeserializer():
    '''returns SettableBeanProperty\n\n
    withValueDeserializer(final JsonDeserializer<?> deser)\n
    '''
def withNullProvider():
    '''returns SettableBeanProperty\n\n
    withNullProvider(final NullValueProvider nva)\n
    '''
def fixAccess():
    '''returns None\n\n
    fixAccess(final DeserializationConfig config)\n
    '''
def setFallbackSetter():
    '''returns None\n\n
    setFallbackSetter(final SettableBeanProperty fallbackSetter)\n
    '''
def markAsIgnorable():
    '''returns None\n\n
    markAsIgnorable()\n
    '''
def isIgnorable():
    '''returns boolean\n\n
    isIgnorable()\n
    '''
def findInjectableValue():
    '''returns Object\n\n
    findInjectableValue(final DeserializationContext context, final Object beanInstance)\n
    '''
def inject():
    '''returns None\n\n
    inject(final DeserializationContext context, final Object beanInstance)\n
    '''
def getMember():
    '''returns AnnotatedMember\n\n
    getMember()\n
    '''
def getCreatorIndex():
    '''returns int\n\n
    getCreatorIndex()\n
    '''
def deserializeAndSet():
    '''returns None\n\n
    deserializeAndSet(final JsonParser p, final DeserializationContext ctxt, final Object instance)\n
    '''
def deserializeSetAndReturn():
    '''returns Object\n\n
    deserializeSetAndReturn(final JsonParser p, final DeserializationContext ctxt, final Object instance)\n
    '''
def set():
    '''returns None\n\n
    set(final Object instance, final Object value)\n
    '''
def setAndReturn():
    '''returns Object\n\n
    setAndReturn(final Object instance, final Object value)\n
    '''
def getInjectableValueId():
    '''returns Object\n\n
    getInjectableValueId()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
