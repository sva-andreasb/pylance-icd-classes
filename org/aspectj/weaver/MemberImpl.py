def ():
    '''returns MemberImpl\n\n
    (final MemberKind kind, final UnresolvedType declaringType, final int modifiers, final String name, final String erasedSignature)\n
    (final MemberKind kind, final UnresolvedType declaringType, final int modifiers, final UnresolvedType returnType, final String name, final UnresolvedType[] parameterTypes)\n
    '''
def resolve():
    '''returns ResolvedMember\n\n
    resolve(final World world)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final Member other)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getKind():
    '''returns MemberKind\n\n
    getKind()\n
    '''
def getDeclaringType():
    '''returns UnresolvedType\n\n
    getDeclaringType()\n
    '''
def getReturnType():
    '''returns UnresolvedType\n\n
    getReturnType()\n
    '''
def getGenericReturnType():
    '''returns UnresolvedType\n\n
    getGenericReturnType()\n
    '''
def getGenericParameterTypes():
    '''returns UnresolvedType[]\n\n
    getGenericParameterTypes()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getParameterTypes():
    '''returns UnresolvedType[]\n\n
    getParameterTypes()\n
    '''
def getSignature():
    '''returns String\n\n
    getSignature()\n
    '''
def getArity():
    '''returns int\n\n
    getArity()\n
    '''
def getParameterSignature():
    '''returns String\n\n
    getParameterSignature()\n
    '''
def getModifiers():
    '''returns int\n\n
    getModifiers(final World world)\n
    getModifiers()\n
    '''
def getExceptions():
    '''returns UnresolvedType[]\n\n
    getExceptions(final World world)\n
    '''
def canBeParameterized():
    '''returns boolean\n\n
    canBeParameterized()\n
    '''
def getAnnotations():
    '''returns AnnotationAJ[]\n\n
    getAnnotations()\n
    '''
def getDeclaringTypes():
    '''returns Collection<ResolvedType>\n\n
    getDeclaringTypes(final World world)\n
    '''
def getParameterNames():
    '''returns String[]\n\n
    getParameterNames(final World world)\n
    '''
def getJoinPointSignatures():
    '''returns JoinPointSignatureIterator\n\n
    getJoinPointSignatures(final World inAWorld)\n
    '''
def wipeJoinpointSignatures():
    '''returns None\n\n
    wipeJoinpointSignatures()\n
    '''
