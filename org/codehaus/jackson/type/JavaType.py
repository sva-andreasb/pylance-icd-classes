def withValueHandler():
    '''returns JavaType\n\n
    withValueHandler(final Object h)\n
    '''
def withContentValueHandler():
    '''returns JavaType\n\n
    withContentValueHandler(final Object h)\n
    '''
def setValueHandler():
    '''returns None\n\n
    setValueHandler(final Object h)\n
    '''
def narrowBy():
    '''returns JavaType\n\n
    narrowBy(final Class<?> subclass)\n
    '''
def forcedNarrowBy():
    '''returns JavaType\n\n
    forcedNarrowBy(final Class<?> subclass)\n
    '''
def widenBy():
    '''returns JavaType\n\n
    widenBy(final Class<?> superclass)\n
    '''
def isAbstract():
    '''returns boolean\n\n
    isAbstract()\n
    '''
def isConcrete():
    '''returns boolean\n\n
    isConcrete()\n
    '''
def isThrowable():
    '''returns boolean\n\n
    isThrowable()\n
    '''
def isArrayType():
    '''returns boolean\n\n
    isArrayType()\n
    '''
def isCollectionLikeType():
    '''returns boolean\n\n
    isCollectionLikeType()\n
    '''
def isMapLikeType():
    '''returns boolean\n\n
    isMapLikeType()\n
    '''
def hasGenericTypes():
    '''returns boolean\n\n
    hasGenericTypes()\n
    '''
def getKeyType():
    '''returns JavaType\n\n
    getKeyType()\n
    '''
def getContentType():
    '''returns JavaType\n\n
    getContentType()\n
    '''
def containedTypeCount():
    '''returns int\n\n
    containedTypeCount()\n
    '''
def containedType():
    '''returns JavaType\n\n
    containedType(final int index)\n
    '''
def containedTypeName():
    '''returns String\n\n
    containedTypeName(final int index)\n
    '''
def getGenericSignature():
    '''returns String\n\n
    getGenericSignature()\n
    '''
def getErasedSignature():
    '''returns String\n\n
    getErasedSignature()\n
    '''
