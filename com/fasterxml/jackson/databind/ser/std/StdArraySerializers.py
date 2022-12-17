def ():
    '''returns DoubleArraySerializer\n\n
    ()\n
    ()\n
    (final ShortArraySerializer src, final BeanProperty prop, final Boolean unwrapSingle)\n
    ()\n
    ()\n
    ()\n
    (final LongArraySerializer src, final BeanProperty prop, final Boolean unwrapSingle)\n
    ()\n
    (final FloatArraySerializer src, final BeanProperty prop, final Boolean unwrapSingle)\n
    ()\n
    '''
def getContentType():
    '''returns JavaType\n\n
    getContentType()\n
    getContentType()\n
    getContentType()\n
    getContentType()\n
    getContentType()\n
    getContentType()\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty(final SerializerProvider prov, final boolean[] value)\n
    isEmpty(final SerializerProvider prov, final short[] value)\n
    isEmpty(final SerializerProvider prov, final char[] value)\n
    isEmpty(final SerializerProvider prov, final int[] value)\n
    isEmpty(final SerializerProvider prov, final long[] value)\n
    isEmpty(final SerializerProvider prov, final float[] value)\n
    isEmpty(final SerializerProvider prov, final double[] value)\n
    '''
def hasSingleElement():
    '''returns boolean\n\n
    hasSingleElement(final boolean[] value)\n
    hasSingleElement(final short[] value)\n
    hasSingleElement(final int[] value)\n
    hasSingleElement(final long[] value)\n
    hasSingleElement(final float[] value)\n
    hasSingleElement(final double[] value)\n
    '''
def serializeContents():
    '''returns None\n\n
    serializeContents(final boolean[] value, final JsonGenerator g, final SerializerProvider provider)\n
    serializeContents(final short[] value, final JsonGenerator g, final SerializerProvider provider)\n
    serializeContents(final int[] value, final JsonGenerator g, final SerializerProvider provider)\n
    serializeContents(final long[] value, final JsonGenerator g, final SerializerProvider provider)\n
    serializeContents(final float[] value, final JsonGenerator g, final SerializerProvider provider)\n
    serializeContents(final double[] value, final JsonGenerator g, final SerializerProvider provider)\n
    '''
def getSchema():
    '''returns JsonNode\n\n
    getSchema(final SerializerProvider provider, final Type typeHint)\n
    getSchema(final SerializerProvider provider, final Type typeHint)\n
    getSchema(final SerializerProvider provider, final Type typeHint)\n
    getSchema(final SerializerProvider provider, final Type typeHint)\n
    getSchema(final SerializerProvider provider, final Type typeHint)\n
    getSchema(final SerializerProvider provider, final Type typeHint)\n
    getSchema(final SerializerProvider provider, final Type typeHint)\n
    '''
def acceptJsonFormatVisitor():
    '''returns None\n\n
    acceptJsonFormatVisitor(final JsonFormatVisitorWrapper visitor, final JavaType typeHint)\n
    acceptJsonFormatVisitor(final JsonFormatVisitorWrapper visitor, final JavaType typeHint)\n
    acceptJsonFormatVisitor(final JsonFormatVisitorWrapper visitor, final JavaType typeHint)\n
    acceptJsonFormatVisitor(final JsonFormatVisitorWrapper visitor, final JavaType typeHint)\n
    acceptJsonFormatVisitor(final JsonFormatVisitorWrapper visitor, final JavaType typeHint)\n
    acceptJsonFormatVisitor(final JsonFormatVisitorWrapper visitor, final JavaType typeHint)\n
    acceptJsonFormatVisitor(final JsonFormatVisitorWrapper visitor, final JavaType typeHint)\n
    '''
def serialize():
    '''returns None\n\n
    serialize(final char[] value, final JsonGenerator g, final SerializerProvider provider)\n
    '''
def serializeWithType():
    '''returns None\n\n
    serializeWithType(final char[] value, final JsonGenerator g, final SerializerProvider provider, final TypeSerializer typeSer)\n
    '''
