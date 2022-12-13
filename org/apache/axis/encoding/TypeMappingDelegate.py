def getSupportedEncodings():
'''public String[] getSupportedEncodings()
'''
pass
def setSupportedEncodings():
'''public void setSupportedEncodings(final String[] namespaceURIs)
'''
pass
def register():
'''public void register(final Class javaType, final QName xmlType, final SerializerFactory sf, final DeserializerFactory dsf)
'''
pass
def getSerializer():
'''public SerializerFactory getSerializer(final Class javaType, final QName xmlType)
public SerializerFactory getSerializer(final Class javaType)
'''
pass
def getDeserializer():
'''public DeserializerFactory getDeserializer(final Class javaType, final QName xmlType)
public DeserializerFactory getDeserializer(final Class javaType, final QName xmlType, final TypeMappingDelegate start)
public DeserializerFactory getDeserializer(final QName xmlType)
'''
pass
def removeSerializer():
'''public void removeSerializer(final Class javaType, final QName xmlType)
'''
pass
def removeDeserializer():
'''public void removeDeserializer(final Class javaType, final QName xmlType)
'''
pass
def isRegistered():
'''public boolean isRegistered(final Class javaType, final QName xmlType)
'''
pass
def getTypeQName():
'''public QName getTypeQName(final Class javaType)
'''
pass
def getClassForQName():
'''public Class getClassForQName(final QName xmlType)
public Class getClassForQName(final QName xmlType, final Class javaType)
'''
pass
def getTypeQNameExact():
'''public QName getTypeQNameExact(final Class javaType)
'''
pass
def setNext():
'''public void setNext(final TypeMappingDelegate next)
'''
pass
def getNext():
'''public TypeMappingDelegate getNext()
'''
pass
def getAllClasses():
'''public Class[] getAllClasses()
'''
pass
def getXMLType():
'''public QName getXMLType(final Class javaType, final QName xmlType, final boolean encoded)
'''
pass
def setDoAutoTypes():
'''public void setDoAutoTypes(final boolean doAutoTypes)
'''
pass
