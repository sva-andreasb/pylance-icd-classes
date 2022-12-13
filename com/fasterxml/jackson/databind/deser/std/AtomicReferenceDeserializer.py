def AtomicReferenceDeserializer():
    '''    public AtomicReferenceDeserializer(final JavaType fullType, final ValueInstantiator inst, final TypeDeserializer typeDeser, final JsonDeserializer<?> deser)
    '''
def withResolved():
    '''    public AtomicReferenceDeserializer withResolved(final TypeDeserializer typeDeser, final JsonDeserializer<?> valueDeser)
    '''
def getNullValue():
    '''    public AtomicReference<Object> getNullValue(final DeserializationContext ctxt)
    '''
def getEmptyValue():
    '''    public Object getEmptyValue(final DeserializationContext ctxt)
    '''
def referenceValue():
    '''    public AtomicReference<Object> referenceValue(final Object contents)
    '''
def getReferenced():
    '''    public Object getReferenced(final AtomicReference<Object> reference)
    '''
def updateReference():
    '''    public AtomicReference<Object> updateReference(final AtomicReference<Object> reference, final Object contents)
    '''
def supportsUpdate():
    '''    public Boolean supportsUpdate(final DeserializationConfig config)
    '''
