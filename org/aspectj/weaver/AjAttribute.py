AttributePrefix = "String  \"org.aspectj.weaver\""
AttributeName = "String  \"org.aspectj.weaver.EffectiveSignature\""
WEAVER_VERSION_MAJOR_UNKNOWN = "short  0"
WEAVER_VERSION_MINOR_UNKNOWN = "short  0"
WEAVER_VERSION_MAJOR_AJ121 = "short  1"
WEAVER_VERSION_MINOR_AJ121 = "short  0"
WEAVER_VERSION_MAJOR_AJ150M4 = "short  3"
WEAVER_VERSION_MAJOR_AJ150 = "short  2"
WEAVER_VERSION_MINOR_AJ150 = "short  0"
WEAVER_VERSION_MAJOR_AJ160M2 = "short  5"
WEAVER_VERSION_MAJOR_AJ160 = "short  4"
WEAVER_VERSION_MINOR_AJ160 = "short  0"
WEAVER_VERSION_MAJOR_AJ161 = "short  6"
WEAVER_VERSION_MINOR_AJ161 = "short  0"
WEAVER_VERSION_AJ169 = "short  7"
def getNameChars():
    '''returns char[]\n\n
    getNameChars()\n
    '''
def getBytes():
    '''returns byte[]\n\n
    getBytes(final ConstantPoolWriter compressor)\n
    '''
def getAllBytes():
    '''returns byte[]\n\n
    getAllBytes(final short nameIndex, final ConstantPoolWriter dataCompressor)\n
    '''
def getNameString():
    '''returns String\n\n
    getNameString()\n
    getNameString()\n
    getNameString()\n
    getNameString()\n
    getNameString()\n
    getNameString()\n
    getNameString()\n
    getNameString()\n
    getNameString()\n
    getNameString()\n
    getNameString()\n
    getNameString()\n
    '''
def write():
    '''returns None\n\n
    write(final CompressingDataOutputStream s)\n
    write(final CompressingDataOutputStream s)\n
    write(final CompressingDataOutputStream s)\n
    write(final CompressingDataOutputStream s)\n
    write(final CompressingDataOutputStream s)\n
    write(final CompressingDataOutputStream s)\n
    write(final CompressingDataOutputStream s)\n
    write(final CompressingDataOutputStream s)\n
    write(final CompressingDataOutputStream s)\n
    write(final CompressingDataOutputStream s)\n
    write(final CompressingDataOutputStream s)\n
    write(final CompressingDataOutputStream s)\n
    '''
def ():
    '''returns EffectiveSignatureAttribute\n\n
    (final ResolvedTypeMunger munger)\n
    (final WeaverStateInfo kind)\n
    ()\n
    (final short major, final short minor)\n
    (final String sourceFileName, final int[] lineBreaks)\n
    (final int line, final int offset)\n
    (final ResolvedPointcutDefinition pointcutDef)\n
    (final Declare declare)\n
    (final AdviceKind kind, final Pointcut pointcut, final int extraArgumentFlags, final int start, final int end, final ISourceContext sourceContext)\n
    (final AdviceKind kind, final Pointcut pointcut, final int extraArgumentFlags, final int start, final int end, final ISourceContext sourceContext, final boolean proceedInInners, final ResolvedMember[] proceedCallSignatures, final boolean[] formalsUnchangedToProceed, final UnresolvedType[] declaredExceptions)\n
    (final PerClause perClause)\n
    (final ResolvedMember[] accessedMembers)\n
    (final ResolvedMember effectiveSignature, final Shadow.Kind shadowKind, final boolean weaveBody)\n
    '''
def reify():
    '''returns PerClause\n\n
    reify(final World world, final ResolvedType aspectType)\n
    reify()\n
    reify()\n
    reify(final Member signature, final World world, final ResolvedType concreteAspect)\n
    reify(final ResolvedType inAspect)\n
    '''
def getMajorVersion():
    '''returns short\n\n
    getMajorVersion()\n
    '''
def getMinorVersion():
    '''returns short\n\n
    getMinorVersion()\n
    '''
def setBuildstamp():
    '''returns None\n\n
    setBuildstamp(final long stamp)\n
    '''
def getBuildstamp():
    '''returns long\n\n
    getBuildstamp()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    toString()\n
    toString()\n
    '''
def getLineBreaks():
    '''returns int[]\n\n
    getLineBreaks()\n
    '''
def getSourceFileName():
    '''returns String\n\n
    getSourceFileName()\n
    '''
def getLineNumber():
    '''returns int\n\n
    getLineNumber()\n
    '''
def getOffset():
    '''returns int\n\n
    getOffset()\n
    '''
def getDeclare():
    '''returns Declare\n\n
    getDeclare()\n
    '''
def getExtraParameterFlags():
    '''returns int\n\n
    getExtraParameterFlags()\n
    '''
def getKind():
    '''returns AdviceKind\n\n
    getKind()\n
    '''
def getPointcut():
    '''returns Pointcut\n\n
    getPointcut()\n
    '''
def getDeclaredExceptions():
    '''returns UnresolvedType[]\n\n
    getDeclaredExceptions()\n
    '''
def getFormalsUnchangedToProceed():
    '''returns boolean[]\n\n
    getFormalsUnchangedToProceed()\n
    '''
def getProceedCallSignatures():
    '''returns ResolvedMember[]\n\n
    getProceedCallSignatures()\n
    '''
def isProceedInInners():
    '''returns boolean\n\n
    isProceedInInners()\n
    '''
def getEnd():
    '''returns int\n\n
    getEnd()\n
    '''
def getSourceContext():
    '''returns ISourceContext\n\n
    getSourceContext()\n
    '''
def getStart():
    '''returns int\n\n
    getStart()\n
    '''
def reifyFromAtAspectJ():
    '''returns PerClause\n\n
    reifyFromAtAspectJ(final ResolvedType inAspect)\n
    '''
def setResolutionScope():
    '''returns None\n\n
    setResolutionScope(final IScope binding)\n
    '''
def getAccessedMembers():
    '''returns ResolvedMember[]\n\n
    getAccessedMembers()\n
    '''
def getEffectiveSignature():
    '''returns ResolvedMember\n\n
    getEffectiveSignature()\n
    '''
def isWeaveBody():
    '''returns boolean\n\n
    isWeaveBody()\n
    '''
