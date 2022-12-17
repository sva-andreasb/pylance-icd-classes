def ():
    '''returns AsPropertyTypeDeserializer\n\n
    (final JavaType bt, final TypeIdResolver idRes, final String typePropertyName, final boolean typeIdVisible, final JavaType defaultImpl)\n
    (final JavaType bt, final TypeIdResolver idRes, final String typePropertyName, final boolean typeIdVisible, final JavaType defaultImpl, final JsonTypeInfo.As inclusion)\n
    (final AsPropertyTypeDeserializer src, final BeanProperty property)\n
    '''
def forProperty():
    '''returns TypeDeserializer\n\n
    forProperty(final BeanProperty prop)\n
    '''
def deserializeTypedFromObject():
    '''returns Object\n\n
    deserializeTypedFromObject(final JsonParser p, final DeserializationContext ctxt)\n
    '''
def deserializeTypedFromAny():
    '''returns Object\n\n
    deserializeTypedFromAny(final JsonParser p, final DeserializationContext ctxt)\n
    '''
