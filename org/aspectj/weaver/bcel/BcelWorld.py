def ():
    '''returns WeavingXmlConfig\n\n
    ()\n
    (final String cp)\n
    (final List classPath, final IMessageHandler handler, final ICrossReferenceHandler xrefHandler)\n
    (final ClassPathManager cpm, final IMessageHandler handler, final ICrossReferenceHandler xrefHandler)\n
    (final ClassLoader loader, final IMessageHandler handler, final ICrossReferenceHandler xrefHandler)\n
    (final BcelWorld bcelWorld, final int mode)\n
    '''
def reportMatch():
    '''returns None\n\n
    reportMatch(final ShadowMunger munger, final Shadow shadow)\n
    '''
def ensureRepositorySetup():
    '''returns None\n\n
    ensureRepositorySetup()\n
    '''
def getClassLoaderRepositoryFor():
    '''returns Repository\n\n
    getClassLoaderRepositoryFor(final ClassLoaderReference loader)\n
    '''
def addPath():
    '''returns None\n\n
    addPath(final String name)\n
    '''
def resolve():
    '''returns ResolvedType\n\n
    resolve(final Type t)\n
    '''
def buildBcelDelegate():
    '''returns BcelObjectType\n\n
    buildBcelDelegate(final ReferenceType type, final JavaClass jc, final boolean artificial, final boolean exposedToWeaver)\n
    '''
def addSourceObjectType():
    '''returns BcelObjectType\n\n
    addSourceObjectType(final JavaClass jc, final boolean artificial)\n
    addSourceObjectType(final String classname, final JavaClass jc, final boolean artificial)\n
    addSourceObjectType(final String classname, final byte[] bytes, final boolean artificial)\n
    '''
def makeJoinPointSignatureFromMethod():
    '''returns Member\n\n
    makeJoinPointSignatureFromMethod(final LazyMethodGen mg, final MemberKind kind)\n
    '''
def makeJoinPointSignatureForMonitorEnter():
    '''returns Member\n\n
    makeJoinPointSignatureForMonitorEnter(final LazyClassGen cg, final InstructionHandle h)\n
    '''
def makeJoinPointSignatureForMonitorExit():
    '''returns Member\n\n
    makeJoinPointSignatureForMonitorExit(final LazyClassGen cg, final InstructionHandle h)\n
    '''
def makeJoinPointSignatureForArrayConstruction():
    '''returns Member\n\n
    makeJoinPointSignatureForArrayConstruction(final LazyClassGen cg, final InstructionHandle handle)\n
    '''
def makeJoinPointSignatureForMethodInvocation():
    '''returns Member\n\n
    makeJoinPointSignatureForMethodInvocation(final LazyClassGen cg, final InvokeInstruction ii)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def tidyUp():
    '''returns None\n\n
    tidyUp()\n
    '''
def findClass():
    '''returns JavaClass\n\n
    findClass(final String className)\n
    '''
def loadClass():
    '''returns JavaClass\n\n
    loadClass(final String className)\n
    loadClass(final Class clazz)\n
    '''
def storeClass():
    '''returns None\n\n
    storeClass(final JavaClass clazz)\n
    '''
def removeClass():
    '''returns None\n\n
    removeClass(final JavaClass clazz)\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def validateType():
    '''returns None\n\n
    validateType(final UnresolvedType type)\n
    '''
def getWeavingSupport():
    '''returns IWeavingSupport\n\n
    getWeavingSupport()\n
    '''
def reportCheckerMatch():
    '''returns None\n\n
    reportCheckerMatch(final Checker checker, final Shadow shadow)\n
    '''
def getModelAsAsmManager():
    '''returns AsmManager\n\n
    getModelAsAsmManager()\n
    '''
def setXmlFiles():
    '''returns None\n\n
    setXmlFiles(final List<File> xmlFiles)\n
    '''
def addScopedAspect():
    '''returns None\n\n
    addScopedAspect(final String name, final String scope)\n
    addScopedAspect(final String aspectName, final String scope)\n
    '''
def setXmlConfigured():
    '''returns None\n\n
    setXmlConfigured(final boolean b)\n
    '''
def isXmlConfigured():
    '''returns boolean\n\n
    isXmlConfigured()\n
    '''
def getXmlConfiguration():
    '''returns WeavingXmlConfig\n\n
    getXmlConfiguration()\n
    '''
def isAspectIncluded():
    '''returns boolean\n\n
    isAspectIncluded(final ResolvedType aspectType)\n
    '''
def getAspectScope():
    '''returns TypePattern\n\n
    getAspectScope(final ResolvedType declaringType)\n
    '''
def hasUnsatisfiedDependency():
    '''returns boolean\n\n
    hasUnsatisfiedDependency(final ResolvedType aspectType)\n
    '''
def addAspectRequires():
    '''returns None\n\n
    addAspectRequires(final String aspectClassName, final String requiredType)\n
    '''
def getTypeMap():
    '''returns TypeMap\n\n
    getTypeMap()\n
    '''
def isLoadtimeWeaving():
    '''returns boolean\n\n
    isLoadtimeWeaving()\n
    '''
def addTypeDelegateResolver():
    '''returns None\n\n
    addTypeDelegateResolver(final TypeDelegateResolver typeDelegateResolver)\n
    '''
def classWriteEvent():
    '''returns None\n\n
    classWriteEvent(final char[][] compoundName)\n
    '''
def demote():
    '''returns None\n\n
    demote(final ResolvedType type)\n
    '''
def add():
    '''returns None\n\n
    add(final Definition d)\n
    '''
def ensureInitialized():
    '''returns None\n\n
    ensureInitialized()\n
    '''
def specifiesInclusionOfAspect():
    '''returns boolean\n\n
    specifiesInclusionOfAspect(final String name)\n
    '''
def getScopeFor():
    '''returns TypePattern\n\n
    getScopeFor(final String name)\n
    '''
def excludesType():
    '''returns boolean\n\n
    excludesType(final ResolvedType type)\n
    '''
