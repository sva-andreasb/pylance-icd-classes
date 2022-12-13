serialVersionUID = "long  1L"
def ExtensionRegistry():
'''public ExtensionRegistry()
'''
pass
def setDefaultSerializer():
'''public void setDefaultSerializer(final ExtensionSerializer defaultSer)
'''
pass
def getDefaultSerializer():
'''public ExtensionSerializer getDefaultSerializer()
'''
pass
def setDefaultDeserializer():
'''public void setDefaultDeserializer(final ExtensionDeserializer defaultDeser)
'''
pass
def getDefaultDeserializer():
'''public ExtensionDeserializer getDefaultDeserializer()
'''
pass
def registerSerializer():
'''public void registerSerializer(final Class clazz, final QName qName, final ExtensionSerializer extensionSerializer)
'''
pass
def registerDeserializer():
'''public void registerDeserializer(final Class clazz, final QName qName, final ExtensionDeserializer extensionDeserializer)
'''
pass
def querySerializer():
'''public ExtensionSerializer querySerializer(final Class clazz, final QName obj)
'''
pass
def queryDeserializer():
'''public ExtensionDeserializer queryDeserializer(final Class clazz, final QName obj)
'''
pass
def getAllowableExtensions():
'''public Set getAllowableExtensions(final Class clazz)
'''
pass
def mapExtensionTypes():
'''public void mapExtensionTypes(final Class clazz, final QName qName, final Class clazz2)
'''
pass
def createExtension():
'''public ExtensibilityElement createExtension(final Class clazz, final QName obj)
'''
pass
