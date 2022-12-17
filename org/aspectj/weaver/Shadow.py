MethodCallBit = "int  2"
ConstructorCallBit = "int  4"
MethodExecutionBit = "int  8"
ConstructorExecutionBit = "int  16"
FieldGetBit = "int  32"
FieldSetBit = "int  64"
StaticInitializationBit = "int  128"
PreInitializationBit = "int  256"
AdviceExecutionBit = "int  512"
InitializationBit = "int  1024"
ExceptionHandlerBit = "int  2048"
SynchronizationLockBit = "int  4096"
SynchronizationUnlockBit = "int  8192"
MAX_SHADOW_KIND = "int  13"
def getMungers():
    '''returns List<ShadowMunger>\n\n
    getMungers()\n
    '''
def getArgTypes():
    '''returns UnresolvedType[]\n\n
    getArgTypes()\n
    '''
def isShadowForArrayConstructionJoinpoint():
    '''returns boolean\n\n
    isShadowForArrayConstructionJoinpoint()\n
    '''
def isShadowForMonitor():
    '''returns boolean\n\n
    isShadowForMonitor()\n
    '''
def getArgumentTypesForArrayConstructionShadow():
    '''returns ResolvedType[]\n\n
    getArgumentTypesForArrayConstructionShadow()\n
    '''
def getGenericArgTypes():
    '''returns UnresolvedType[]\n\n
    getGenericArgTypes()\n
    '''
def getArgType():
    '''returns UnresolvedType\n\n
    getArgType(final int arg)\n
    '''
def getArgCount():
    '''returns int\n\n
    getArgCount()\n
    '''
def getKind():
    '''returns Kind\n\n
    getKind()\n
    '''
def getSignature():
    '''returns Member\n\n
    getSignature()\n
    '''
def getMatchingSignature():
    '''returns Member\n\n
    getMatchingSignature()\n
    '''
def setMatchingSignature():
    '''returns None\n\n
    setMatchingSignature(final Member member)\n
    '''
def getResolvedSignature():
    '''returns ResolvedMember\n\n
    getResolvedSignature()\n
    '''
def getReturnType():
    '''returns UnresolvedType\n\n
    getReturnType()\n
    '''
def addMunger():
    '''returns None\n\n
    addMunger(final ShadowMunger munger)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def toResolvedString():
    '''returns String\n\n
    toResolvedString(final World world)\n
    '''
def ():
    '''returns Kind\n\n
    (final String name, final int key, final boolean argsOnStack)\n
    '''
def toLegalJavaIdentifier():
    '''returns String\n\n
    toLegalJavaIdentifier()\n
    '''
def argsOnStack():
    '''returns boolean\n\n
    argsOnStack()\n
    '''
def allowsExtraction():
    '''returns boolean\n\n
    allowsExtraction()\n
    '''
def isSet():
    '''returns boolean\n\n
    isSet(final int i)\n
    '''
def hasHighPriorityExceptions():
    '''returns boolean\n\n
    hasHighPriorityExceptions()\n
    '''
def hasReturnValue():
    '''returns boolean\n\n
    hasReturnValue()\n
    '''
def isEnclosingKind():
    '''returns boolean\n\n
    isEnclosingKind()\n
    '''
def isTargetSameAsThis():
    '''returns boolean\n\n
    isTargetSameAsThis()\n
    '''
def neverHasTarget():
    '''returns boolean\n\n
    neverHasTarget()\n
    '''
def neverHasThis():
    '''returns boolean\n\n
    neverHasThis()\n
    '''
def getSimpleName():
    '''returns String\n\n
    getSimpleName()\n
    '''
