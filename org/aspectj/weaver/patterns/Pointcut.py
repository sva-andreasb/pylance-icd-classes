KINDED = "byte  1"
WITHIN = "byte  2"
THIS_OR_TARGET = "byte  3"
ARGS = "byte  4"
AND = "byte  5"
OR = "byte  6"
NOT = "byte  7"
REFERENCE = "byte  8"
IF = "byte  9"
CFLOW = "byte  10"
WITHINCODE = "byte  12"
HANDLER = "byte  13"
IF_TRUE = "byte  14"
IF_FALSE = "byte  15"
ANNOTATION = "byte  16"
ATWITHIN = "byte  17"
ATWITHINCODE = "byte  18"
ATTHIS_OR_TARGET = "byte  19"
NONE = "byte  20"
ATARGS = "byte  21"
USER_EXTENSION = "byte  22"
def ():
    '''returns State\n\n
    ()\n
    (final String name, final int key)\n
    '''
def getTypeVariablesInScope():
    '''returns String[]\n\n
    getTypeVariablesInScope()\n
    '''
def setTypeVariablesInScope():
    '''returns None\n\n
    setTypeVariablesInScope(final String[] typeVars)\n
    '''
def getPointcutKind():
    '''returns byte\n\n
    getPointcutKind()\n
    '''
def isDeclare():
    '''returns boolean\n\n
    isDeclare(final ShadowMunger munger)\n
    '''
def postRead():
    '''returns None\n\n
    postRead(final ResolvedType enclosingType)\n
    postRead(final ResolvedType enclosingType)\n
    '''
def check():
    '''returns None\n\n
    check(final ISourceContext ctx, final World world)\n
    '''
def assertState():
    '''returns None\n\n
    assertState(final State state)\n
    '''
def couldMatchKinds():
    '''returns int\n\n
    couldMatchKinds()\n
    '''
def fastMatch():
    '''returns FuzzyBoolean\n\n
    fastMatch(final FastMatchInfo type)\n
    '''
def resolveBindings():
    '''returns None\n\n
    resolveBindings(final IScope scope, final Bindings bindings)\n
    '''
def concretize1():
    '''returns Pointcut\n\n
    concretize1(final ResolvedType inAspect, final ResolvedType declaringType, final IntMap bindings)\n
    '''
def write():
    '''returns None\n\n
    write(final CompressingDataOutputStream s)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def accept():
    '''returns Object\n\n
    accept(final PatternNodeVisitor visitor, final Object data)\n
    '''
def parameterizeWith():
    '''returns Pointcut\n\n
    parameterizeWith(final Map<String, UnresolvedType> typeVariableMap, final World w)\n
    '''
