def ():
    '''returns LazyMethodGen\n\n
    (final int modifiers, final Type returnType, final String name, final Type[] paramTypes, final String[] declaredExceptions, final LazyClassGen enclosingClass)\n
    (final Method m, final LazyClassGen enclosingClass)\n
    (final BcelMethod m, final LazyClassGen enclosingClass)\n
    '''
def hasDeclaredLineNumberInfo():
    '''returns boolean\n\n
    hasDeclaredLineNumberInfo()\n
    '''
def getDeclarationLineNumber():
    '''returns int\n\n
    getDeclarationLineNumber()\n
    '''
def getDeclarationOffset():
    '''returns int\n\n
    getDeclarationOffset()\n
    '''
def addAnnotation():
    '''returns None\n\n
    addAnnotation(final AnnotationAJ ax)\n
    '''
def removeAnnotation():
    '''returns None\n\n
    removeAnnotation(final ResolvedType annotationType)\n
    '''
def addParameterAnnotation():
    '''returns None\n\n
    addParameterAnnotation(final int parameterNumber, final AnnotationAJ anno)\n
    '''
def getAnnotationTypes():
    '''returns ResolvedType[]\n\n
    getAnnotationTypes()\n
    '''
def getAnnotations():
    '''returns AnnotationAJ[]\n\n
    getAnnotations()\n
    '''
def hasAnnotation():
    '''returns boolean\n\n
    hasAnnotation(final UnresolvedType annotationType)\n
    '''
def ensureAllLineNumberSetup():
    '''returns None\n\n
    ensureAllLineNumberSetup()\n
    '''
def allocateLocal():
    '''returns int\n\n
    allocateLocal(final Type type)\n
    allocateLocal(final int slots)\n
    '''
def getMethod():
    '''returns Method\n\n
    getMethod()\n
    '''
def markAsChanged():
    '''returns None\n\n
    markAsChanged()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def toShortString():
    '''returns String\n\n
    toShortString()\n
    '''
def toLongString():
    '''returns String\n\n
    toLongString(final AjAttribute.WeaverVersionInfo weaverVersion)\n
    '''
def print():
    '''returns None\n\n
    print(final AjAttribute.WeaverVersionInfo weaverVersion)\n
    print(final PrintStream out, final AjAttribute.WeaverVersionInfo weaverVersion)\n
    '''
def isStatic():
    '''returns boolean\n\n
    isStatic()\n
    '''
def isAbstract():
    '''returns boolean\n\n
    isAbstract()\n
    '''
def isBridgeMethod():
    '''returns boolean\n\n
    isBridgeMethod()\n
    '''
def addExceptionHandler():
    '''returns None\n\n
    addExceptionHandler(final InstructionHandle start, final InstructionHandle end, final InstructionHandle handlerStart, final ObjectType catchType, final boolean highPriority)\n
    '''
def getAccessFlags():
    '''returns int\n\n
    getAccessFlags()\n
    '''
def getAccessFlagsWithoutSynchronized():
    '''returns int\n\n
    getAccessFlagsWithoutSynchronized()\n
    '''
def isSynchronized():
    '''returns boolean\n\n
    isSynchronized()\n
    '''
def setAccessFlags():
    '''returns None\n\n
    setAccessFlags(final int newFlags)\n
    '''
def getArgumentTypes():
    '''returns Type[]\n\n
    getArgumentTypes()\n
    '''
def getEnclosingClass():
    '''returns LazyClassGen\n\n
    getEnclosingClass()\n
    '''
def getMaxLocals():
    '''returns int\n\n
    getMaxLocals()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getGenericReturnTypeSignature():
    '''returns String\n\n
    getGenericReturnTypeSignature()\n
    '''
def getReturnType():
    '''returns Type\n\n
    getReturnType()\n
    '''
def setMaxLocals():
    '''returns None\n\n
    setMaxLocals(final int maxLocals)\n
    '''
def getBody():
    '''returns InstructionList\n\n
    getBody()\n
    '''
def getBodyForPrint():
    '''returns InstructionList\n\n
    getBodyForPrint()\n
    '''
def hasBody():
    '''returns boolean\n\n
    hasBody()\n
    '''
def getAttributes():
    '''returns List<Attribute>\n\n
    getAttributes()\n
    '''
def getDeclaredExceptions():
    '''returns String[]\n\n
    getDeclaredExceptions()\n
    '''
def getClassName():
    '''returns String\n\n
    getClassName()\n
    '''
def pack():
    '''returns MethodGen\n\n
    pack()\n
    '''
def makeSynthetic():
    '''returns None\n\n
    makeSynthetic()\n
    '''
def packBody():
    '''returns None\n\n
    packBody(final MethodGen gen)\n
    '''
def optimizedPackBody():
    '''returns None\n\n
    optimizedPackBody(final MethodGen gen)\n
    '''
def isPrivate():
    '''returns boolean\n\n
    isPrivate()\n
    '''
def isProtected():
    '''returns boolean\n\n
    isProtected()\n
    '''
def isDefault():
    '''returns boolean\n\n
    isDefault()\n
    '''
def isPublic():
    '''returns boolean\n\n
    isPublic()\n
    '''
def assertGoodBody():
    '''returns None\n\n
    assertGoodBody()\n
    '''
def getSourceLocation():
    '''returns ISourceLocation\n\n
    getSourceLocation()\n
    '''
def setEffectiveSignature():
    '''returns None\n\n
    setEffectiveSignature(final ResolvedMember member, final Shadow.Kind kind, final boolean shouldWeave)\n
    '''
def getSignature():
    '''returns String\n\n
    getSignature()\n
    '''
def getParameterSignature():
    '''returns String\n\n
    getParameterSignature()\n
    '''
def getMemberView():
    '''returns BcelMethod\n\n
    getMemberView()\n
    '''
def forcePublic():
    '''returns None\n\n
    forcePublic()\n
    '''
def getCanInline():
    '''returns boolean\n\n
    getCanInline()\n
    '''
def setCanInline():
    '''returns None\n\n
    setCanInline(final boolean canInline)\n
    '''
def addAttribute():
    '''returns None\n\n
    addAttribute(final Attribute attribute)\n
    '''
def toTraceString():
    '''returns String\n\n
    toTraceString()\n
    '''
def getConstantPool():
    '''returns ConstantPool\n\n
    getConstantPool()\n
    '''
