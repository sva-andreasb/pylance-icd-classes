serialVersionUID = "long  1L"
def ExtensionRegistry():
    '''public ExtensionRegistry()
    '''
def setDefaultSerializer():
    '''public void setDefaultSerializer(final ExtensionSerializer defaultSer)
    '''
def getDefaultSerializer():
    '''public ExtensionSerializer getDefaultSerializer()
    '''
def setDefaultDeserializer():
    '''public void setDefaultDeserializer(final ExtensionDeserializer defaultDeser)
    '''
def getDefaultDeserializer():
    '''public ExtensionDeserializer getDefaultDeserializer()
    '''
def registerSerializer():
    '''public void registerSerializer(final Class clazz, final QName qName, final ExtensionSerializer extensionSerializer)
    '''
def registerDeserializer():
    '''public void registerDeserializer(final Class clazz, final QName qName, final ExtensionDeserializer extensionDeserializer)
    '''
def querySerializer():
    '''public ExtensionSerializer querySerializer(final Class clazz, final QName obj)
    '''
def queryDeserializer():
    '''public ExtensionDeserializer queryDeserializer(final Class clazz, final QName obj)
    '''
def getAllowableExtensions():
    '''public Set getAllowableExtensions(final Class clazz)
    '''
def mapExtensionTypes():
    '''public void mapExtensionTypes(final Class clazz, final QName qName, final Class clazz2)
    '''
def createExtension():
    '''public ExtensibilityElement createExtension(final Class clazz, final QName obj)
    '''
