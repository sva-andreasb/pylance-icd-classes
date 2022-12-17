def ():
    '''returns TypePatternVisitor\n\n
    (final MemberKind kind, final ModifiersPattern modifiers, final TypePattern returnType, final TypePattern declaringType, final NamePattern name, final TypePatternList parameterTypes, final ThrowsPattern throwsPattern, final AnnotationTypePattern annotationPattern)\n
    (final IScope scope, final boolean targetsOtherThanTypeAllowed, final boolean parameterTargettingAnnotationsAllowed)\n
    '''
def resolveBindings():
    '''returns SignaturePattern\n\n
    resolveBindings(final IScope scope, final Bindings bindings)\n
    '''
def postRead():
    '''returns None\n\n
    postRead(final ResolvedType enclosingType)\n
    '''
def parameterizeWith():
    '''returns SignaturePattern\n\n
    parameterizeWith(final Map<String, UnresolvedType> typeVariableMap, final World w)\n
    '''
def matches():
    '''returns boolean\n\n
    matches(final Member joinPointSignature, final World world, final boolean allowBridgeMethods)\n
    '''
def declaringTypeMatchAllowingForCovariance():
    '''returns boolean\n\n
    declaringTypeMatchAllowingForCovariance(final Member member, final UnresolvedType shadowDeclaringType, final World world, final TypePattern returnTypePattern, final ResolvedType sigReturn)\n
    '''
def getName():
    '''returns NamePattern\n\n
    getName()\n
    '''
def getDeclaringType():
    '''returns TypePattern\n\n
    getDeclaringType()\n
    '''
def getKind():
    '''returns MemberKind\n\n
    getKind()\n
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
def write():
    '''returns None\n\n
    write(final CompressingDataOutputStream s)\n
    '''
def getModifiers():
    '''returns ModifiersPattern\n\n
    getModifiers()\n
    '''
def getParameterTypes():
    '''returns TypePatternList\n\n
    getParameterTypes()\n
    '''
def getReturnType():
    '''returns TypePattern\n\n
    getReturnType()\n
    '''
def getThrowsPattern():
    '''returns ThrowsPattern\n\n
    getThrowsPattern()\n
    '''
def getAnnotationPattern():
    '''returns AnnotationTypePattern\n\n
    getAnnotationPattern()\n
    '''
def isStarAnnotation():
    '''returns boolean\n\n
    isStarAnnotation()\n
    '''
def accept():
    '''returns Object\n\n
    accept(final PatternNodeVisitor visitor, final Object data)\n
    '''
def isExactDeclaringTypePattern():
    '''returns boolean\n\n
    isExactDeclaringTypePattern()\n
    '''
def isMatchOnAnyName():
    '''returns boolean\n\n
    isMatchOnAnyName()\n
    '''
def getExactDeclaringTypes():
    '''returns List<ExactTypePattern>\n\n
    getExactDeclaringTypes()\n
    '''
def couldEverMatch():
    '''returns boolean\n\n
    couldEverMatch(final ResolvedType type)\n
    '''
def visit():
    '''returns Object\n\n
    visit(final WildAnnotationTypePattern node, final Object data)\n
    visit(final ExactAnnotationTypePattern node, final Object data)\n
    visit(final ExactTypePattern node, final Object data)\n
    visit(final AndTypePattern node, final Object data)\n
    visit(final OrTypePattern node, final Object data)\n
    visit(final AnyWithAnnotationTypePattern node, final Object data)\n
    '''
def containedIncorrectTargetKind():
    '''returns boolean\n\n
    containedIncorrectTargetKind()\n
    '''
