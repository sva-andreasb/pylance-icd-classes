UNBOUND = "int  0"
EXTENDS = "int  1"
SUPER = "int  2"
def ():
    '''returns BoundedReferenceType\n\n
    (final ReferenceType aBound, final boolean isExtends, final World world)\n
    (final ReferenceType aBound, final boolean isExtends, final World world, final ReferenceType[] additionalInterfaces)\n
    (final World world)\n
    '''
def getUpperBound():
    '''returns UnresolvedType\n\n
    getUpperBound()\n
    '''
def getLowerBound():
    '''returns UnresolvedType\n\n
    getLowerBound()\n
    '''
def getAdditionalBounds():
    '''returns ReferenceType[]\n\n
    getAdditionalBounds()\n
    '''
def parameterize():
    '''returns UnresolvedType\n\n
    parameterize(final Map<String, UnresolvedType> typeBindings)\n
    '''
def getSignatureForAttribute():
    '''returns String\n\n
    getSignatureForAttribute()\n
    '''
def hasLowerBound():
    '''returns boolean\n\n
    hasLowerBound()\n
    '''
def isExtends():
    '''returns boolean\n\n
    isExtends()\n
    '''
def isSuper():
    '''returns boolean\n\n
    isSuper()\n
    '''
def isUnbound():
    '''returns boolean\n\n
    isUnbound()\n
    '''
def alwaysMatches():
    '''returns boolean\n\n
    alwaysMatches(final ResolvedType aCandidateType)\n
    '''
def canBeCoercedTo():
    '''returns boolean\n\n
    canBeCoercedTo(final ResolvedType aCandidateType)\n
    '''
def getSimpleName():
    '''returns String\n\n
    getSimpleName()\n
    '''
def getDeclaredInterfaces():
    '''returns ResolvedType[]\n\n
    getDeclaredInterfaces()\n
    '''
def isGenericWildcard():
    '''returns boolean\n\n
    isGenericWildcard()\n
    '''
