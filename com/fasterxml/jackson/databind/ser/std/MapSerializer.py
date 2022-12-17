def _withValueTypeSerializer():
    '''returns MapSerializer\n\n
    _withValueTypeSerializer(final TypeSerializer vts)\n
    '''
def withResolved():
    '''returns MapSerializer\n\n
    withResolved(final BeanProperty property, final JsonSerializer<?> keySerializer, final JsonSerializer<?> valueSerializer, final Set<String> ignored, final boolean sortKeys)\n
    '''
def withFilterId():
    '''returns MapSerializer\n\n
    withFilterId(final Object filterId)\n
    '''
def withContentInclusion():
    '''returns MapSerializer\n\n
    withContentInclusion(final Object suppressableValue, final boolean suppressNulls)\n
    withContentInclusion(final Object suppressableValue)\n
    '''
def getContentType():
    '''returns JavaType\n\n
    getContentType()\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty(final SerializerProvider prov, final Map<?, ?> value)\n
    '''
def hasSingleElement():
    '''returns boolean\n\n
    hasSingleElement(final Map<?, ?> value)\n
    '''
def serialize():
    '''returns None\n\n
    serialize(Map<?, ?> value, final JsonGenerator gen, final SerializerProvider provider)\n
    '''
def serializeWithType():
    '''returns None\n\n
    serializeWithType(Map<?, ?> value, final JsonGenerator gen, final SerializerProvider provider, final TypeSerializer typeSer)\n
    '''
def serializeFields():
    '''returns None\n\n
    serializeFields(final Map<?, ?> value, final JsonGenerator gen, final SerializerProvider provider)\n
    '''
def serializeOptionalFields():
    '''returns None\n\n
    serializeOptionalFields(final Map<?, ?> value, final JsonGenerator gen, final SerializerProvider provider, final Object suppressableValue)\n
    '''
def serializeFieldsUsing():
    '''returns None\n\n
    serializeFieldsUsing(final Map<?, ?> value, final JsonGenerator gen, final SerializerProvider provider, final JsonSerializer<Object> ser)\n
    '''
def serializeFilteredFields():
    '''returns None\n\n
    serializeFilteredFields(final Map<?, ?> value, final JsonGenerator gen, final SerializerProvider provider, final PropertyFilter filter, final Object suppressableValue)\n
    '''
def serializeTypedFields():
    '''returns None\n\n
    serializeTypedFields(final Map<?, ?> value, final JsonGenerator gen, final SerializerProvider provider, final Object suppressableValue)\n
    '''
def serializeFilteredAnyProperties():
    '''returns None\n\n
    serializeFilteredAnyProperties(final SerializerProvider provider, final JsonGenerator gen, final Object bean, final Map<?, ?> value, final PropertyFilter filter, final Object suppressableValue)\n
    '''
def getSchema():
    '''returns JsonNode\n\n
    getSchema(final SerializerProvider provider, final Type typeHint)\n
    '''
def acceptJsonFormatVisitor():
    '''returns None\n\n
    acceptJsonFormatVisitor(final JsonFormatVisitorWrapper visitor, final JavaType typeHint)\n
    '''
