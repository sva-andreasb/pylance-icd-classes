serialVersionUID = "long  1L"
def ():
    '''returns ExtensionRegistry\n\n
    ()\n
    '''
def setDefaultSerializer():
    '''returns None\n\n
    setDefaultSerializer(final ExtensionSerializer defaultSer)\n
    '''
def getDefaultSerializer():
    '''returns ExtensionSerializer\n\n
    getDefaultSerializer()\n
    '''
def setDefaultDeserializer():
    '''returns None\n\n
    setDefaultDeserializer(final ExtensionDeserializer defaultDeser)\n
    '''
def getDefaultDeserializer():
    '''returns ExtensionDeserializer\n\n
    getDefaultDeserializer()\n
    '''
def registerSerializer():
    '''returns None\n\n
    registerSerializer(final Class clazz, final QName qName, final ExtensionSerializer extensionSerializer)\n
    '''
def registerDeserializer():
    '''returns None\n\n
    registerDeserializer(final Class clazz, final QName qName, final ExtensionDeserializer extensionDeserializer)\n
    '''
def querySerializer():
    '''returns ExtensionSerializer\n\n
    querySerializer(final Class clazz, final QName obj)\n
    '''
def queryDeserializer():
    '''returns ExtensionDeserializer\n\n
    queryDeserializer(final Class clazz, final QName obj)\n
    '''
def getAllowableExtensions():
    '''returns Set\n\n
    getAllowableExtensions(final Class clazz)\n
    '''
def mapExtensionTypes():
    '''returns None\n\n
    mapExtensionTypes(final Class clazz, final QName qName, final Class clazz2)\n
    '''
def createExtension():
    '''returns ExtensibilityElement\n\n
    createExtension(final Class clazz, final QName obj)\n
    '''
