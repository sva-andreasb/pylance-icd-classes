def getSupportedEncodings():
    '''    public String[] getSupportedEncodings()
    '''
def setSupportedEncodings():
    '''    public void setSupportedEncodings(final String[] namespaceURIs)
    '''
def register():
    '''    public void register(final Class javaType, final QName xmlType, final SerializerFactory sf, final DeserializerFactory dsf)
    '''
def getSerializer():
    '''    public SerializerFactory getSerializer(final Class javaType, final QName xmlType)
    public SerializerFactory getSerializer(final Class javaType)
    '''
def getDeserializer():
    '''    public DeserializerFactory getDeserializer(final Class javaType, final QName xmlType)
    public DeserializerFactory getDeserializer(final Class javaType, final QName xmlType, final TypeMappingDelegate start)
    public DeserializerFactory getDeserializer(final QName xmlType)
    '''
def removeSerializer():
    '''    public void removeSerializer(final Class javaType, final QName xmlType)
    '''
def removeDeserializer():
    '''    public void removeDeserializer(final Class javaType, final QName xmlType)
    '''
def isRegistered():
    '''    public boolean isRegistered(final Class javaType, final QName xmlType)
    '''
def getTypeQName():
    '''    public QName getTypeQName(final Class javaType)
    '''
def getClassForQName():
    '''    public Class getClassForQName(final QName xmlType)
    public Class getClassForQName(final QName xmlType, final Class javaType)
    '''
def getTypeQNameExact():
    '''    public QName getTypeQNameExact(final Class javaType)
    '''
def setNext():
    '''    public void setNext(final TypeMappingDelegate next)
    '''
def getNext():
    '''    public TypeMappingDelegate getNext()
    '''
def getAllClasses():
    '''    public Class[] getAllClasses()
    '''
def getXMLType():
    '''    public QName getXMLType(final Class javaType, final QName xmlType, final boolean encoded)
    '''
def setDoAutoTypes():
    '''    public void setDoAutoTypes(final boolean doAutoTypes)
    '''
