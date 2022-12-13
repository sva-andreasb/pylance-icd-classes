def TypeMappingImpl():
'''public TypeMappingImpl()
'''
pass
def getSupportedEncodings():
'''public String[] getSupportedEncodings()
'''
pass
def setSupportedEncodings():
'''public void setSupportedEncodings(final String[] namespaceURIs)
'''
pass
def isRegistered():
'''public boolean isRegistered(final Class javaType, final QName xmlType)
'''
pass
def register():
'''public void register(final Class javaType, final QName xmlType, final SerializerFactory sf, final DeserializerFactory dsf)
'''
pass
def getSerializer():
'''public SerializerFactory getSerializer(final Class javaType, QName xmlType)
'''
pass
def getXMLType():
'''public QName getXMLType(final Class javaType, QName xmlType, final boolean encoded)
'''
pass
def getDeserializer():
'''public DeserializerFactory getDeserializer(Class javaType, final QName xmlType, final TypeMappingDelegate start)
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
def getTypeQNameRecursive():
'''public QName getTypeQNameRecursive(Class javaType)
'''
pass
def getTypeQNameExact():
'''public QName getTypeQNameExact(final Class javaType, final TypeMappingDelegate next)
'''
pass
def getTypeQName():
'''public QName getTypeQName(final Class javaType, final TypeMappingDelegate next)
'''
pass
def getClassForQName():
'''public Class getClassForQName(final QName xmlType, Class javaType, final TypeMappingDelegate next)
'''
pass
def setDoAutoTypes():
'''public void setDoAutoTypes(final boolean doAutoTypes)
'''
pass
def shouldDoAutoTypes():
'''public boolean shouldDoAutoTypes()
'''
pass
def getAllClasses():
'''public Class[] getAllClasses(final TypeMappingDelegate next)
'''
pass
def Pair():
'''public Pair(final Class<?> javaType, final QName xmlType)
'''
pass
def equals():
'''public boolean equals(final Object o)
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
