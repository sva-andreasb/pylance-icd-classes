def ():
    '''returns BcelTypeMunger\n\n
    (final ResolvedTypeMunger munger, final ResolvedType aspectType)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def shouldOverwrite():
    '''returns boolean\n\n
    shouldOverwrite()\n
    '''
def munge():
    '''returns boolean\n\n
    munge(final BcelClassWeaver weaver)\n
    '''
def error():
    '''returns None\n\n
    error(final BcelClassWeaver weaver, final String text, final ISourceLocation primaryLoc, final ISourceLocation[] extraLocs)\n
    '''
def attemptToModifySuperCalls():
    '''returns boolean\n\n
    attemptToModifySuperCalls(final BcelClassWeaver weaver, final LazyClassGen newParentTarget, ResolvedType newParent)\n
    '''
def parameterizedFor():
    '''returns ConcreteTypeMunger\n\n
    parameterizedFor(final ResolvedType target)\n
    '''
def parameterizeWith():
    '''returns ConcreteTypeMunger\n\n
    parameterizeWith(final Map<String, UnresolvedType> m, final World w)\n
    '''
def getTypeVariableAliases():
    '''returns List<String>\n\n
    getTypeVariableAliases()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object other)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
