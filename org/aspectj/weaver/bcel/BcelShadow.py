def ():
    '''returns BcelShadow\n\n
    (final BcelWorld world, final Kind kind, final Member signature, final LazyMethodGen enclosingMethod, final BcelShadow enclosingShadow)\n
    '''
def copyInto():
    '''returns BcelShadow\n\n
    copyInto(final LazyMethodGen recipient, final BcelShadow enclosing)\n
    '''
def getIWorld():
    '''returns World\n\n
    getIWorld()\n
    '''
def addAdvicePreventingLazyTjp():
    '''returns None\n\n
    addAdvicePreventingLazyTjp(final BcelAdvice advice)\n
    '''
def getRange():
    '''returns ShadowRange\n\n
    getRange()\n
    '''
def setRange():
    '''returns None\n\n
    setRange(final ShadowRange range)\n
    '''
def getSourceLine():
    '''returns int\n\n
    getSourceLine()\n
    '''
def getEnclosingType():
    '''returns ResolvedType\n\n
    getEnclosingType()\n
    '''
def getEnclosingClass():
    '''returns LazyClassGen\n\n
    getEnclosingClass()\n
    '''
def getWorld():
    '''returns BcelWorld\n\n
    getWorld()\n
    '''
def initIfaceInitializer():
    '''returns None\n\n
    initIfaceInitializer(final InstructionHandle end)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def terminatesWithReturn():
    '''returns boolean\n\n
    terminatesWithReturn()\n
    '''
def arg0HoldsThis():
    '''returns boolean\n\n
    arg0HoldsThis()\n
    '''
def getThisVar():
    '''returns Var\n\n
    getThisVar()\n
    '''
def getThisAnnotationVar():
    '''returns Var\n\n
    getThisAnnotationVar(final UnresolvedType forAnnotationType)\n
    '''
def getTargetVar():
    '''returns Var\n\n
    getTargetVar()\n
    '''
def getTargetAnnotationVar():
    '''returns Var\n\n
    getTargetAnnotationVar(final UnresolvedType forAnnotationType)\n
    '''
def getArgVar():
    '''returns Var\n\n
    getArgVar(final int i)\n
    '''
def getArgAnnotationVar():
    '''returns Var\n\n
    getArgAnnotationVar(final int i, final UnresolvedType forAnnotationType)\n
    '''
def getKindedAnnotationVar():
    '''returns Var\n\n
    getKindedAnnotationVar(final UnresolvedType forAnnotationType)\n
    '''
def getWithinAnnotationVar():
    '''returns Var\n\n
    getWithinAnnotationVar(final UnresolvedType forAnnotationType)\n
    '''
def getWithinCodeAnnotationVar():
    '''returns Var\n\n
    getWithinCodeAnnotationVar(final UnresolvedType forAnnotationType)\n
    '''
def requireThisJoinPoint():
    '''returns None\n\n
    requireThisJoinPoint(final boolean hasGuardTest, final boolean isAround)\n
    '''
def getThisJoinPointVar():
    '''returns Var\n\n
    getThisJoinPointVar()\n
    '''
def getThisJoinPointStaticPartBcelVar():
    '''returns BcelVar\n\n
    getThisJoinPointStaticPartBcelVar()\n
    getThisJoinPointStaticPartBcelVar(final boolean isEnclosingJp)\n
    '''
def getThisAspectInstanceVar():
    '''returns BcelVar\n\n
    getThisAspectInstanceVar(final ResolvedType aspectType)\n
    '''
def getThisEnclosingJoinPointStaticPartBcelVar():
    '''returns BcelVar\n\n
    getThisEnclosingJoinPointStaticPartBcelVar()\n
    '''
def getEnclosingCodeSignature():
    '''returns Member\n\n
    getEnclosingCodeSignature()\n
    '''
def getRealEnclosingCodeSignature():
    '''returns Member\n\n
    getRealEnclosingCodeSignature()\n
    '''
def initializeTargetVar():
    '''returns None\n\n
    initializeTargetVar()\n
    '''
def ensureTargetTypeIsCorrect():
    '''returns UnresolvedType\n\n
    ensureTargetTypeIsCorrect(final UnresolvedType tx)\n
    '''
def ensureInitializedArgVar():
    '''returns None\n\n
    ensureInitializedArgVar(final int argNumber)\n
    '''
def initializeArgVars():
    '''returns None\n\n
    initializeArgVars()\n
    '''
def initializeForAroundClosure():
    '''returns None\n\n
    initializeForAroundClosure()\n
    '''
def initializeThisAnnotationVars():
    '''returns None\n\n
    initializeThisAnnotationVars()\n
    '''
def initializeTargetAnnotationVars():
    '''returns None\n\n
    initializeTargetAnnotationVars()\n
    '''
def initializeKindedAnnotationVars():
    '''returns None\n\n
    initializeKindedAnnotationVars()\n
    '''
def initializeWithinAnnotationVars():
    '''returns None\n\n
    initializeWithinAnnotationVars()\n
    '''
def initializeWithinCodeAnnotationVars():
    '''returns None\n\n
    initializeWithinCodeAnnotationVars()\n
    '''
def weaveAfter():
    '''returns None\n\n
    weaveAfter(final BcelAdvice munger)\n
    '''
def weaveAfterReturning():
    '''returns None\n\n
    weaveAfterReturning(final BcelAdvice munger)\n
    '''
def weaveAfterThrowing():
    '''returns None\n\n
    weaveAfterThrowing(final BcelAdvice munger, final UnresolvedType catchType)\n
    '''
def weaveSoftener():
    '''returns None\n\n
    weaveSoftener(final BcelAdvice munger, final UnresolvedType catchType)\n
    '''
def weavePerObjectEntry():
    '''returns None\n\n
    weavePerObjectEntry(final BcelAdvice munger, final BcelVar onVar)\n
    '''
def weavePerTypeWithinAspectInitialization():
    '''returns None\n\n
    weavePerTypeWithinAspectInitialization(final BcelAdvice munger, final UnresolvedType t)\n
    '''
def weaveCflowEntry():
    '''returns None\n\n
    weaveCflowEntry(final BcelAdvice munger, final Member cflowField)\n
    '''
def getAdviceInstructions():
    '''returns InstructionList\n\n
    getAdviceInstructions(final BcelShadow s, final BcelVar extraArgVar, final InstructionHandle ifNoAdvice)\n
    '''
def weaveAroundInline():
    '''returns None\n\n
    weaveAroundInline(final BcelAdvice munger, final boolean hasDynamicTest)\n
    '''
def weaveAroundClosure():
    '''returns None\n\n
    weaveAroundClosure(final BcelAdvice munger, final boolean hasDynamicTest)\n
    '''
def genTempVar():
    '''returns BcelVar\n\n
    genTempVar(final UnresolvedType utype)\n
    genTempVar(final UnresolvedType typeX, final String localName)\n
    '''
def getFactory():
    '''returns InstructionFactory\n\n
    getFactory()\n
    '''
def getSourceLocation():
    '''returns ISourceLocation\n\n
    getSourceLocation()\n
    '''
def getEnclosingShadow():
    '''returns Shadow\n\n
    getEnclosingShadow()\n
    '''
def getEnclosingMethod():
    '''returns LazyMethodGen\n\n
    getEnclosingMethod()\n
    '''
def isFallsThrough():
    '''returns boolean\n\n
    isFallsThrough()\n
    '''
def setActualTargetType():
    '''returns None\n\n
    setActualTargetType(final String className)\n
    '''
def getActualTargetType():
    '''returns String\n\n
    getActualTargetType()\n
    '''
def visit():
    '''returns Object\n\n
    visit(final ThisOrTargetPointcut node, final Object data)\n
    visit(final AndPointcut node, final Object data)\n
    visit(final NotPointcut node, final Object data)\n
    visit(final OrPointcut node, final Object data)\n
    visit(final ThisOrTargetPointcut node, final Object data)\n
    visit(final AndPointcut node, final Object data)\n
    visit(final NotPointcut node, final Object data)\n
    visit(final OrPointcut node, final Object data)\n
    '''
