def ():
    '''returns UnwrappingBeanSerializer\n\n
    (final BeanSerializerBase src, final NameTransformer transformer)\n
    (final UnwrappingBeanSerializer src, final ObjectIdWriter objectIdWriter)\n
    (final UnwrappingBeanSerializer src, final ObjectIdWriter objectIdWriter, final Object filterId)\n
    '''
def unwrappingSerializer():
    '''returns JsonSerializer<Object>\n\n
    unwrappingSerializer(final NameTransformer transformer)\n
    '''
def isUnwrappingSerializer():
    '''returns boolean\n\n
    isUnwrappingSerializer()\n
    '''
def withObjectIdWriter():
    '''returns BeanSerializerBase\n\n
    withObjectIdWriter(final ObjectIdWriter objectIdWriter)\n
    '''
def withFilterId():
    '''returns BeanSerializerBase\n\n
    withFilterId(final Object filterId)\n
    '''
def serializeWithType():
    '''returns None\n\n
    serializeWithType(final Object bean, final JsonGenerator gen, final SerializerProvider provider, final TypeSerializer typeSer)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
