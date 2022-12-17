UNKNOWN = "int  -1"
METHOD = "int  1"
TYPE = "int  2"
def ():
    '''returns TypeVariable\n\n
    (final String name)\n
    (final String name, final UnresolvedType anUpperBound)\n
    (final String name, final UnresolvedType anUpperBound, final UnresolvedType[] superInterfaces)\n
    '''
def getFirstBound():
    '''returns UnresolvedType\n\n
    getFirstBound()\n
    '''
def getUpperBound():
    '''returns UnresolvedType\n\n
    getUpperBound()\n
    '''
def getSuperInterfaces():
    '''returns UnresolvedType[]\n\n
    getSuperInterfaces()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def resolve():
    '''returns TypeVariable\n\n
    resolve(final World world)\n
    '''
def canBeBoundTo():
    '''returns boolean\n\n
    canBeBoundTo(final ResolvedType candidate)\n
    '''
def setUpperBound():
    '''returns None\n\n
    setUpperBound(final UnresolvedType superclass)\n
    '''
def setAdditionalInterfaceBounds():
    '''returns None\n\n
    setAdditionalInterfaceBounds(final UnresolvedType[] superInterfaces)\n
    '''
def toDebugString():
    '''returns String\n\n
    toDebugString()\n
    '''
def getDisplayName():
    '''returns String\n\n
    getDisplayName()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getSignature():
    '''returns String\n\n
    getSignature()\n
    '''
def getSignatureForAttribute():
    '''returns String\n\n
    getSignatureForAttribute()\n
    '''
def setRank():
    '''returns None\n\n
    setRank(final int rank)\n
    '''
def getRank():
    '''returns int\n\n
    getRank()\n
    '''
def setDeclaringElement():
    '''returns None\n\n
    setDeclaringElement(final TypeVariableDeclaringElement element)\n
    '''
def getDeclaringElement():
    '''returns TypeVariableDeclaringElement\n\n
    getDeclaringElement()\n
    '''
def setDeclaringElementKind():
    '''returns None\n\n
    setDeclaringElementKind(final int kind)\n
    '''
def getDeclaringElementKind():
    '''returns int\n\n
    getDeclaringElementKind()\n
    '''
def write():
    '''returns None\n\n
    write(final CompressingDataOutputStream s)\n
    '''
def getGenericSignature():
    '''returns String\n\n
    getGenericSignature()\n
    '''
def getErasureSignature():
    '''returns String\n\n
    getErasureSignature()\n
    '''
def getSuperclass():
    '''returns UnresolvedType\n\n
    getSuperclass()\n
    '''
def setSuperclass():
    '''returns None\n\n
    setSuperclass(final UnresolvedType superclass)\n
    '''
