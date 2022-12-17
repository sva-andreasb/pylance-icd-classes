def ():
    '''returns AbstractDeserializer\n\n
    (final BeanDeserializerBuilder builder, final BeanDescription beanDesc, final Map<String, SettableBeanProperty> backRefProps, final Map<String, SettableBeanProperty> props)\n
    (final BeanDeserializerBuilder builder, final BeanDescription beanDesc, final Map<String, SettableBeanProperty> backRefProps)\n
    '''
def isCachable():
    '''returns boolean\n\n
    isCachable()\n
    '''
def supportsUpdate():
    '''returns Boolean\n\n
    supportsUpdate(final DeserializationConfig config)\n
    '''
def getObjectIdReader():
    '''returns ObjectIdReader\n\n
    getObjectIdReader()\n
    '''
def findBackReference():
    '''returns SettableBeanProperty\n\n
    findBackReference(final String logicalName)\n
    '''
def deserializeWithType():
    '''returns Object\n\n
    deserializeWithType(final JsonParser p, final DeserializationContext ctxt, final TypeDeserializer typeDeserializer)\n
    '''
def deserialize():
    '''returns Object\n\n
    deserialize(final JsonParser p, final DeserializationContext ctxt)\n
    '''
