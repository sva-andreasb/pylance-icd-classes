def ():
    '''returns Pair\n\n
    ()\n
    (final Class javaType, final QName xmlType)\n
    '''
def getSupportedEncodings():
    '''returns String[]\n\n
    getSupportedEncodings()\n
    '''
def setSupportedEncodings():
    '''returns None\n\n
    setSupportedEncodings(final String[] namespaceURIs)\n
    '''
def isRegistered():
    '''returns boolean\n\n
    isRegistered(final Class javaType, final QName xmlType)\n
    '''
def register():
    '''returns None\n\n
    register(final Class javaType, final QName xmlType, final SerializerFactory sf, final DeserializerFactory dsf)\n
    '''
def getSerializer():
    '''returns SerializerFactory\n\n
    getSerializer(final Class javaType, QName xmlType)\n
    '''
def getXMLType():
    '''returns QName\n\n
    getXMLType(final Class javaType, QName xmlType, final boolean encoded)\n
    '''
def getDeserializer():
    '''returns DeserializerFactory\n\n
    getDeserializer(Class javaType, final QName xmlType, final TypeMappingDelegate start)\n
    '''
def removeSerializer():
    '''returns None\n\n
    removeSerializer(final Class javaType, final QName xmlType)\n
    '''
def removeDeserializer():
    '''returns None\n\n
    removeDeserializer(final Class javaType, final QName xmlType)\n
    '''
def getTypeQNameRecursive():
    '''returns QName\n\n
    getTypeQNameRecursive(Class javaType)\n
    '''
def getTypeQNameExact():
    '''returns QName\n\n
    getTypeQNameExact(final Class javaType, final TypeMappingDelegate next)\n
    '''
def getTypeQName():
    '''returns QName\n\n
    getTypeQName(final Class javaType, final TypeMappingDelegate next)\n
    '''
def getClassForQName():
    '''returns Class\n\n
    getClassForQName(final QName xmlType, Class javaType, final TypeMappingDelegate next)\n
    '''
def setDoAutoTypes():
    '''returns None\n\n
    setDoAutoTypes(final boolean doAutoTypes)\n
    '''
def shouldDoAutoTypes():
    '''returns boolean\n\n
    shouldDoAutoTypes()\n
    '''
def getAllClasses():
    '''returns Class[]\n\n
    getAllClasses(final TypeMappingDelegate next)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
