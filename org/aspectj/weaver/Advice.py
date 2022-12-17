ExtraArgument = "int  1"
ThisJoinPoint = "int  2"
ThisJoinPointStaticPart = "int  4"
ThisEnclosingJoinPointStaticPart = "int  8"
ParameterMask = "int  15"
ConstantReference = "int  16"
ConstantValue = "int  32"
ThisAspectInstance = "int  64"
def ():
    '''returns Advice\n\n
    (final AjAttribute.AdviceAttribute attribute, final Pointcut pointcut, final Member signature)\n
    '''
def match():
    '''returns boolean\n\n
    match(final Shadow shadow, final World world)\n
    '''
def getKind():
    '''returns AdviceKind\n\n
    getKind()\n
    '''
def getSignature():
    '''returns Member\n\n
    getSignature()\n
    '''
def hasExtraParameter():
    '''returns boolean\n\n
    hasExtraParameter()\n
    '''
def getBindingParameterTypes():
    '''returns UnresolvedType[]\n\n
    getBindingParameterTypes()\n
    '''
def setBindingParameterTypes():
    '''returns None\n\n
    setBindingParameterTypes(final UnresolvedType[] types)\n
    '''
def getBaseParameterCount():
    '''returns int\n\n
    getBaseParameterCount()\n
    '''
def getBaseParameterNames():
    '''returns String[]\n\n
    getBaseParameterNames(final World world)\n
    '''
def getExtraParameterType():
    '''returns UnresolvedType\n\n
    getExtraParameterType()\n
    '''
def getDeclaringAspect():
    '''returns UnresolvedType\n\n
    getDeclaringAspect()\n
    '''
def getPointcut():
    '''returns Pointcut\n\n
    getPointcut()\n
    '''
def concretize():
    '''returns ShadowMunger\n\n
    concretize(final ResolvedType fromType, final World world, final PerClause clause)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object other)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def setLexicalPosition():
    '''returns None\n\n
    setLexicalPosition(final int lexicalPosition)\n
    '''
def isAnnotationStyle():
    '''returns boolean\n\n
    isAnnotationStyle()\n
    '''
def getConcreteAspect():
    '''returns ResolvedType\n\n
    getConcreteAspect()\n
    '''
def hasMatchedSomething():
    '''returns boolean\n\n
    hasMatchedSomething()\n
    '''
def setHasMatchedSomething():
    '''returns None\n\n
    setHasMatchedSomething(final boolean hasMatchedSomething)\n
    '''
