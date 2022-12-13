def TypeMappingImpl():
    '''public TypeMappingImpl()
    '''
def getSupportedEncodings():
    '''public String[] getSupportedEncodings()
    '''
def setSupportedEncodings():
    '''public void setSupportedEncodings(final String[] namespaceURIs)
    '''
def isRegistered():
    '''public boolean isRegistered(final Class javaType, final QName xmlType)
    '''
def register():
    '''public void register(final Class javaType, final QName xmlType, final SerializerFactory sf, final DeserializerFactory dsf)
    '''
def getSerializer():
    '''public SerializerFactory getSerializer(final Class javaType, QName xmlType)
    '''
def getXMLType():
    '''public QName getXMLType(final Class javaType, QName xmlType, final boolean encoded)
    '''
def getDeserializer():
    '''public DeserializerFactory getDeserializer(Class javaType, final QName xmlType, final TypeMappingDelegate start)
    '''
def removeSerializer():
    '''public void removeSerializer(final Class javaType, final QName xmlType)
    '''
def removeDeserializer():
    '''public void removeDeserializer(final Class javaType, final QName xmlType)
    '''
def getTypeQNameRecursive():
    '''public QName getTypeQNameRecursive(Class javaType)
    '''
def getTypeQNameExact():
    '''public QName getTypeQNameExact(final Class javaType, final TypeMappingDelegate next)
    '''
def getTypeQName():
    '''public QName getTypeQName(final Class javaType, final TypeMappingDelegate next)
    '''
def getClassForQName():
    '''public Class getClassForQName(final QName xmlType, Class javaType, final TypeMappingDelegate next)
    '''
def setDoAutoTypes():
    '''public void setDoAutoTypes(final boolean doAutoTypes)
    '''
def shouldDoAutoTypes():
    '''public boolean shouldDoAutoTypes()
    '''
def getAllClasses():
    '''public Class[] getAllClasses(final TypeMappingDelegate next)
    '''
def Pair():
    '''public Pair(final Class javaType, final QName xmlType)
    '''
def equals():
    '''public boolean equals(final Object o)
    '''
def hashCode():
    '''public int hashCode()
    '''
