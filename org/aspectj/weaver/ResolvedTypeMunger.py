SUPER_DISPATCH_NAME = "String  \"superDispatch\""
def ():
    '''returns ResolvedTypeMunger\n\n
    (final Kind kind, final ResolvedMember signature)\n
    '''
def setSourceLocation():
    '''returns None\n\n
    setSourceLocation(final ISourceLocation isl)\n
    '''
def getSourceLocation():
    '''returns ISourceLocation\n\n
    getSourceLocation()\n
    '''
def matches():
    '''returns boolean\n\n
    matches(final ResolvedType matchType, final ResolvedType aspectType)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
def getKind():
    '''returns Kind\n\n
    getKind()\n
    '''
def setSuperMethodsCalled():
    '''returns None\n\n
    setSuperMethodsCalled(final Set<ResolvedMember> c)\n
    '''
def getSuperMethodsCalled():
    '''returns Set<ResolvedMember>\n\n
    getSuperMethodsCalled()\n
    '''
def getSignature():
    '''returns ResolvedMember\n\n
    getSignature()\n
    '''
def getMatchingSyntheticMember():
    '''returns ResolvedMember\n\n
    getMatchingSyntheticMember(final Member member, final ResolvedType aspectType)\n
    '''
def changesPublicSignature():
    '''returns boolean\n\n
    changesPublicSignature()\n
    '''
def needsAccessToTopmostImplementor():
    '''returns boolean\n\n
    needsAccessToTopmostImplementor()\n
    '''
def getTypeVariableAliases():
    '''returns List<String>\n\n
    getTypeVariableAliases()\n
    '''
def hasTypeVariableAliases():
    '''returns boolean\n\n
    hasTypeVariableAliases()\n
    '''
def sharesTypeVariablesWithGenericType():
    '''returns boolean\n\n
    sharesTypeVariablesWithGenericType()\n
    '''
def parameterizedFor():
    '''returns ResolvedTypeMunger\n\n
    parameterizedFor(final ResolvedType target)\n
    '''
def setDeclaredSignature():
    '''returns None\n\n
    setDeclaredSignature(final ResolvedMember rm)\n
    '''
def getDeclaredSignature():
    '''returns ResolvedMember\n\n
    getDeclaredSignature()\n
    '''
def isLateMunger():
    '''returns boolean\n\n
    isLateMunger()\n
    '''
def existsToSupportShadowMunging():
    '''returns boolean\n\n
    existsToSupportShadowMunging()\n
    '''
def parameterizeWith():
    '''returns ResolvedTypeMunger\n\n
    parameterizeWith(final Map<String, UnresolvedType> m, final World w)\n
    '''
def getDeclaringType():
    '''returns UnresolvedType\n\n
    getDeclaringType()\n
    '''
