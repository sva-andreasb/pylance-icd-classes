def ():
    '''returns UnwrappingBeanPropertyWriter\n\n
    (final BeanPropertyWriter base, final NameTransformer unwrapper)\n
    '''
def rename():
    '''returns UnwrappingBeanPropertyWriter\n\n
    rename(NameTransformer transformer)\n
    '''
def isUnwrapping():
    '''returns boolean\n\n
    isUnwrapping()\n
    '''
def serializeAsField():
    '''returns None\n\n
    serializeAsField(final Object bean, final JsonGenerator gen, final SerializerProvider prov)\n
    '''
def assignSerializer():
    '''returns None\n\n
    assignSerializer(JsonSerializer<Object> ser)\n
    '''
def depositSchemaProperty():
    '''returns None\n\n
    depositSchemaProperty(final JsonObjectFormatVisitor visitor, final SerializerProvider provider)\n
    '''
def expectObjectFormat():
    '''returns JsonObjectFormatVisitor\n\n
    expectObjectFormat(final JavaType type)\n
    '''
