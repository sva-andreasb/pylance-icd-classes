def getNewGeneratedNameTag():
    '''returns String\n\n
    getNewGeneratedNameTag()\n
    '''
def ():
    '''returns LazyClassGen\n\n
    (final String class_name, final String super_class_name, final String file_name, final int access_flags, final String[] interfaces, final World world)\n
    (final BcelObjectType myType)\n
    '''
def getInternalClassName():
    '''returns String\n\n
    getInternalClassName()\n
    '''
def getInternalFileName():
    '''returns String\n\n
    getInternalFileName()\n
    '''
def getPackageName():
    '''returns String\n\n
    getPackageName()\n
    '''
def addMethodGen():
    '''returns None\n\n
    addMethodGen(final LazyMethodGen gen)\n
    addMethodGen(final LazyMethodGen gen, final ISourceLocation sourceLocation)\n
    '''
def removeMethodGen():
    '''returns boolean\n\n
    removeMethodGen(final LazyMethodGen gen)\n
    '''
def errorOnAddedField():
    '''returns None\n\n
    errorOnAddedField(final FieldGen field, final ISourceLocation sourceLocation)\n
    '''
def warnOnAddedInterface():
    '''returns None\n\n
    warnOnAddedInterface(final String name, final ISourceLocation sourceLocation)\n
    '''
def warnOnAddedMethod():
    '''returns None\n\n
    warnOnAddedMethod(final Method method, final ISourceLocation sourceLocation)\n
    '''
def warnOnAddedStaticInitializer():
    '''returns None\n\n
    warnOnAddedStaticInitializer(final Shadow shadow, final ISourceLocation sourceLocation)\n
    '''
def warnOnModifiedSerialVersionUID():
    '''returns None\n\n
    warnOnModifiedSerialVersionUID(final ISourceLocation sourceLocation, final String reason)\n
    '''
def getWorld():
    '''returns World\n\n
    getWorld()\n
    '''
def getMethodGens():
    '''returns List<LazyMethodGen>\n\n
    getMethodGens()\n
    '''
def getFieldGens():
    '''returns List<BcelField>\n\n
    getFieldGens()\n
    '''
def fieldExists():
    '''returns boolean\n\n
    fieldExists(final String name)\n
    '''
def getJavaClass():
    '''returns JavaClass\n\n
    getJavaClass(final BcelWorld world)\n
    '''
def getJavaClassBytesIncludingReweavable():
    '''returns byte[]\n\n
    getJavaClassBytesIncludingReweavable(final BcelWorld world)\n
    '''
def addGeneratedInner():
    '''returns None\n\n
    addGeneratedInner(final LazyClassGen newClass)\n
    '''
def addInterface():
    '''returns None\n\n
    addInterface(final ResolvedType newInterface, final ISourceLocation sourceLocation)\n
    '''
def setSuperClass():
    '''returns None\n\n
    setSuperClass(ResolvedType newSuperclass)\n
    '''
def getSuperClass():
    '''returns ResolvedType\n\n
    getSuperClass()\n
    '''
def getInterfaceNames():
    '''returns String[]\n\n
    getInterfaceNames()\n
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
    toLongString()\n
    '''
def print():
    '''returns None\n\n
    print()\n
    print(final PrintStream out)\n
    '''
def getConstantPool():
    '''returns ConstantPool\n\n
    getConstantPool()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def isWoven():
    '''returns boolean\n\n
    isWoven()\n
    '''
def isReweavable():
    '''returns boolean\n\n
    isReweavable()\n
    '''
def getAspectsAffectingType():
    '''returns Set<String>\n\n
    getAspectsAffectingType()\n
    '''
def getOrCreateWeaverStateInfo():
    '''returns WeaverStateInfo\n\n
    getOrCreateWeaverStateInfo(final boolean inReweavableMode)\n
    '''
def getFactory():
    '''returns InstructionFactory\n\n
    getFactory()\n
    '''
def getStaticInitializer():
    '''returns LazyMethodGen\n\n
    getStaticInitializer()\n
    '''
def getAjcPreClinit():
    '''returns LazyMethodGen\n\n
    getAjcPreClinit()\n
    '''
def createExtendedAjcPreClinit():
    '''returns LazyMethodGen\n\n
    createExtendedAjcPreClinit(final LazyMethodGen previousPreClinit, final int i)\n
    '''
def getTjpField():
    '''returns Field\n\n
    getTjpField(final BcelShadow shadow, final boolean isEnclosingJp)\n
    '''
def getAnnotationCachingField():
    '''returns Field\n\n
    getAnnotationCachingField(final BcelShadow shadow, final ResolvedType toType, final boolean isWithin)\n
    '''
def compare():
    '''returns int\n\n
    compare(final Map.Entry<BcelShadow, Field> a, final Map.Entry<BcelShadow, Field> b)\n
    '''
def getType():
    '''returns ResolvedType\n\n
    getType()\n
    '''
def getBcelObjectType():
    '''returns BcelObjectType\n\n
    getBcelObjectType()\n
    '''
def getFileName():
    '''returns String\n\n
    getFileName()\n
    '''
def addField():
    '''returns None\n\n
    addField(final FieldGen field, final ISourceLocation sourceLocation)\n
    '''
def getClassName():
    '''returns String\n\n
    getClassName()\n
    '''
def isInterface():
    '''returns boolean\n\n
    isInterface()\n
    '''
def isAbstract():
    '''returns boolean\n\n
    isAbstract()\n
    '''
def getLazyMethodGen():
    '''returns LazyMethodGen\n\n
    getLazyMethodGen(final Member m)\n
    getLazyMethodGen(final String name, final String signature)\n
    getLazyMethodGen(final String name, final String signature, final boolean allowMissing)\n
    '''
def forcePublic():
    '''returns None\n\n
    forcePublic()\n
    '''
def hasAnnotation():
    '''returns boolean\n\n
    hasAnnotation(final UnresolvedType t)\n
    '''
def addAnnotation():
    '''returns None\n\n
    addAnnotation(final AnnotationGen a)\n
    '''
def addAttribute():
    '''returns None\n\n
    addAttribute(final AjAttribute attribute)\n
    '''
def isAtLeastJava5():
    '''returns boolean\n\n
    isAtLeastJava5()\n
    '''
def allocateField():
    '''returns String\n\n
    allocateField(final String prefix)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object other)\n
    '''
