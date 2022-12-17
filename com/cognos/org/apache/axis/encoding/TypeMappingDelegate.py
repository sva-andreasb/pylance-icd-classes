def getSupportedEncodings():
    '''returns String[]\n\n
    getSupportedEncodings()\n
    '''
def setSupportedEncodings():
    '''returns None\n\n
    setSupportedEncodings(final String[] namespaceURIs)\n
    '''
def register():
    '''returns None\n\n
    register(final Class javaType, final QName xmlType, final SerializerFactory sf, final DeserializerFactory dsf)\n
    '''
def getSerializer():
    '''returns SerializerFactory\n\n
    getSerializer(final Class javaType, final QName xmlType)\n
    getSerializer(final Class javaType)\n
    '''
def getDeserializer():
    '''returns DeserializerFactory\n\n
    getDeserializer(final Class javaType, final QName xmlType)\n
    getDeserializer(final Class javaType, final QName xmlType, final TypeMappingDelegate start)\n
    getDeserializer(final QName xmlType)\n
    '''
def removeSerializer():
    '''returns None\n\n
    removeSerializer(final Class javaType, final QName xmlType)\n
    '''
def removeDeserializer():
    '''returns None\n\n
    removeDeserializer(final Class javaType, final QName xmlType)\n
    '''
def isRegistered():
    '''returns boolean\n\n
    isRegistered(final Class javaType, final QName xmlType)\n
    '''
def getTypeQName():
    '''returns QName\n\n
    getTypeQName(final Class javaType)\n
    '''
def getClassForQName():
    '''returns Class\n\n
    getClassForQName(final QName xmlType)\n
    getClassForQName(final QName xmlType, final Class javaType)\n
    '''
def getTypeQNameExact():
    '''returns QName\n\n
    getTypeQNameExact(final Class javaType)\n
    '''
def setNext():
    '''returns None\n\n
    setNext(final TypeMappingDelegate next)\n
    '''
def getNext():
    '''returns TypeMappingDelegate\n\n
    getNext()\n
    '''
def getAllClasses():
    '''returns Class[]\n\n
    getAllClasses()\n
    '''
def getXMLType():
    '''returns QName\n\n
    getXMLType(final Class javaType, final QName xmlType, final boolean encoded)\n
    '''
def setDoAutoTypes():
    '''returns None\n\n
    setDoAutoTypes(final boolean doAutoTypes)\n
    '''
