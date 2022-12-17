def ():
    '''returns AtomicReferenceDeserializer\n\n
    (final JavaType fullType, final ValueInstantiator inst, final TypeDeserializer typeDeser, final JsonDeserializer<?> deser)\n
    '''
def withResolved():
    '''returns AtomicReferenceDeserializer\n\n
    withResolved(final TypeDeserializer typeDeser, final JsonDeserializer<?> valueDeser)\n
    '''
def getNullValue():
    '''returns AtomicReference<Object>\n\n
    getNullValue(final DeserializationContext ctxt)\n
    '''
def getEmptyValue():
    '''returns Object\n\n
    getEmptyValue(final DeserializationContext ctxt)\n
    '''
def referenceValue():
    '''returns AtomicReference<Object>\n\n
    referenceValue(final Object contents)\n
    '''
def getReferenced():
    '''returns Object\n\n
    getReferenced(final AtomicReference<Object> reference)\n
    '''
def updateReference():
    '''returns AtomicReference<Object>\n\n
    updateReference(final AtomicReference<Object> reference, final Object contents)\n
    '''
def supportsUpdate():
    '''returns Boolean\n\n
    supportsUpdate(final DeserializationConfig config)\n
    '''
