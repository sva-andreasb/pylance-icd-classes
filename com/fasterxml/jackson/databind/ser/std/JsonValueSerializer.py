def ():
    '''returns TypeSerializerRerouter\n\n
    (final AnnotatedMember accessor, final JsonSerializer<?> ser)\n
    (final JsonValueSerializer src, final BeanProperty property, final JsonSerializer<?> ser, final boolean forceTypeInfo)\n
    (final TypeSerializer ts, final Object ob)\n
    '''
def withResolved():
    '''returns JsonValueSerializer\n\n
    withResolved(final BeanProperty property, final JsonSerializer<?> ser, final boolean forceTypeInfo)\n
    '''
def serialize():
    '''returns None\n\n
    serialize(final Object bean, final JsonGenerator gen, final SerializerProvider prov)\n
    '''
def serializeWithType():
    '''returns None\n\n
    serializeWithType(final Object bean, final JsonGenerator gen, final SerializerProvider provider, final TypeSerializer typeSer0)\n
    '''
def getSchema():
    '''returns JsonNode\n\n
    getSchema(final SerializerProvider provider, final Type typeHint)\n
    '''
def acceptJsonFormatVisitor():
    '''returns None\n\n
    acceptJsonFormatVisitor(final JsonFormatVisitorWrapper visitor, final JavaType typeHint)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def forProperty():
    '''returns TypeSerializer\n\n
    forProperty(final BeanProperty prop)\n
    '''
def getPropertyName():
    '''returns String\n\n
    getPropertyName()\n
    '''
def getTypeIdResolver():
    '''returns TypeIdResolver\n\n
    getTypeIdResolver()\n
    '''
def writeTypePrefix():
    '''returns WritableTypeId\n\n
    writeTypePrefix(final JsonGenerator g, final WritableTypeId typeId)\n
    '''
def writeTypeSuffix():
    '''returns WritableTypeId\n\n
    writeTypeSuffix(final JsonGenerator g, final WritableTypeId typeId)\n
    '''
def writeTypePrefixForScalar():
    '''returns None\n\n
    writeTypePrefixForScalar(final Object value, final JsonGenerator gen)\n
    writeTypePrefixForScalar(final Object value, final JsonGenerator gen, final Class<?> type)\n
    '''
def writeTypePrefixForObject():
    '''returns None\n\n
    writeTypePrefixForObject(final Object value, final JsonGenerator gen)\n
    writeTypePrefixForObject(final Object value, final JsonGenerator gen, final Class<?> type)\n
    '''
def writeTypePrefixForArray():
    '''returns None\n\n
    writeTypePrefixForArray(final Object value, final JsonGenerator gen)\n
    writeTypePrefixForArray(final Object value, final JsonGenerator gen, final Class<?> type)\n
    '''
def writeTypeSuffixForScalar():
    '''returns None\n\n
    writeTypeSuffixForScalar(final Object value, final JsonGenerator gen)\n
    '''
def writeTypeSuffixForObject():
    '''returns None\n\n
    writeTypeSuffixForObject(final Object value, final JsonGenerator gen)\n
    '''
def writeTypeSuffixForArray():
    '''returns None\n\n
    writeTypeSuffixForArray(final Object value, final JsonGenerator gen)\n
    '''
def writeCustomTypePrefixForScalar():
    '''returns None\n\n
    writeCustomTypePrefixForScalar(final Object value, final JsonGenerator gen, final String typeId)\n
    '''
def writeCustomTypePrefixForObject():
    '''returns None\n\n
    writeCustomTypePrefixForObject(final Object value, final JsonGenerator gen, final String typeId)\n
    '''
def writeCustomTypePrefixForArray():
    '''returns None\n\n
    writeCustomTypePrefixForArray(final Object value, final JsonGenerator gen, final String typeId)\n
    '''
def writeCustomTypeSuffixForScalar():
    '''returns None\n\n
    writeCustomTypeSuffixForScalar(final Object value, final JsonGenerator gen, final String typeId)\n
    '''
def writeCustomTypeSuffixForObject():
    '''returns None\n\n
    writeCustomTypeSuffixForObject(final Object value, final JsonGenerator gen, final String typeId)\n
    '''
def writeCustomTypeSuffixForArray():
    '''returns None\n\n
    writeCustomTypeSuffixForArray(final Object value, final JsonGenerator gen, final String typeId)\n
    '''
