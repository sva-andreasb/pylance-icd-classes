xsetAVOID_FINAL = "String  \"avoidFinal\""
xsetWEAVE_JAVA_PACKAGES = "String  \"weaveJavaPackages\""
xsetWEAVE_JAVAX_PACKAGES = "String  \"weaveJavaxPackages\""
xsetCAPTURE_ALL_CONTEXT = "String  \"captureAllContext\""
xsetRUN_MINIMAL_MEMORY = "String  \"runMinimalMemory\""
xsetDEBUG_STRUCTURAL_CHANGES_CODE = "String  \"debugStructuralChangesCode\""
xsetDEBUG_BRIDGING = "String  \"debugBridging\""
xsetTRANSIENT_TJP_FIELDS = "String  \"makeTjpFieldsTransient\""
xsetBCEL_REPOSITORY_CACHING = "String  \"bcelRepositoryCaching\""
xsetPIPELINE_COMPILATION = "String  \"pipelineCompilation\""
xsetGENERATE_STACKMAPS = "String  \"generateStackMaps\""
xsetPIPELINE_COMPILATION_DEFAULT = "String  \"true\""
xsetCOMPLETE_BINARY_TYPES = "String  \"completeBinaryTypes\""
xsetCOMPLETE_BINARY_TYPES_DEFAULT = "String  \"false\""
xsetTYPE_DEMOTION = "String  \"typeDemotion\""
xsetTYPE_DEMOTION_DEBUG = "String  \"typeDemotionDebug\""
xsetTYPE_REFS = "String  \"useWeakTypeRefs\""
xsetBCEL_REPOSITORY_CACHING_DEFAULT = "String  \"true\""
xsetFAST_PACK_METHODS = "String  \"fastPackMethods\""
xsetOVERWEAVING = "String  \"overWeaving\""
xsetOPTIMIZED_MATCHING = "String  \"optimizedMatching\""
xsetTIMERS_PER_JOINPOINT = "String  \"timersPerJoinpoint\""
xsetTIMERS_PER_FASTMATCH_CALL = "String  \"timersPerFastMatchCall\""
xsetITD_VERSION = "String  \"itdVersion\""
xsetITD_VERSION_ORIGINAL = "String  \"1\""
xsetITD_VERSION_2NDGEN = "String  \"2\""
xsetITD_VERSION_DEFAULT = "String  \"2\""
xsetMINIMAL_MODEL = "String  \"minimalModel\""
xsetTARGETING_RUNTIME_1610 = "String  \"targetRuntime1_6_10\""
DONT_USE_REFS = "int  0"
USE_WEAK_REFS = "int  1"
USE_SOFT_REFS = "int  2"
def accept():
    '''returns None\n\n
    accept(final Dump.IVisitor visitor)\n
    '''
def resolve():
    '''returns ResolvedMember\n\n
    resolve(final UnresolvedType ty)\n
    resolve(final UnresolvedType ty, final ISourceLocation isl)\n
    resolve(final UnresolvedType[] types)\n
    resolve(final UnresolvedType ty, final boolean allowMissing)\n
    resolve(final ResolvedType ty)\n
    resolve(final String name)\n
    resolve(final String name, final boolean allowMissing)\n
    resolve(final Member member)\n
    '''
def isLocallyDefined():
    '''returns boolean\n\n
    isLocallyDefined(final String classname)\n
    '''
def resolveToReferenceType():
    '''returns ReferenceType\n\n
    resolveToReferenceType(final String name)\n
    '''
def resolveGenericTypeFor():
    '''returns ResolvedType\n\n
    resolveGenericTypeFor(final UnresolvedType anUnresolvedType, final boolean allowMissing)\n
    '''
def getCoreType():
    '''returns ResolvedType\n\n
    getCoreType(final UnresolvedType tx)\n
    '''
def lookupOrCreateName():
    '''returns ReferenceType\n\n
    lookupOrCreateName(final UnresolvedType ty)\n
    '''
def lookupBySignature():
    '''returns ReferenceType\n\n
    lookupBySignature(final String signature)\n
    '''
def setAllLintIgnored():
    '''returns None\n\n
    setAllLintIgnored()\n
    '''
def areAllLintIgnored():
    '''returns boolean\n\n
    areAllLintIgnored()\n
    '''
def compareByPrecedence():
    '''returns int\n\n
    compareByPrecedence(final ResolvedType aspect1, final ResolvedType aspect2)\n
    compareByPrecedence(final ResolvedType firstAspect, final ResolvedType secondAspect)\n
    '''
def getPrecedenceIfAny():
    '''returns Integer\n\n
    getPrecedenceIfAny(final ResolvedType aspect1, final ResolvedType aspect2)\n
    getPrecedenceIfAny(final ResolvedType aspect1, final ResolvedType aspect2)\n
    '''
def compareByPrecedenceAndHierarchy():
    '''returns int\n\n
    compareByPrecedenceAndHierarchy(final ResolvedType aspect1, final ResolvedType aspect2)\n
    compareByPrecedenceAndHierarchy(final ResolvedType firstAspect, final ResolvedType secondAspect)\n
    '''
def getMessageHandler():
    '''returns IMessageHandler\n\n
    getMessageHandler()\n
    '''
def setMessageHandler():
    '''returns None\n\n
    setMessageHandler(final IMessageHandler messageHandler)\n
    '''
def showMessage():
    '''returns None\n\n
    showMessage(final IMessage.Kind kind, final String message, final ISourceLocation loc1, final ISourceLocation loc2)\n
    '''
def setCrossReferenceHandler():
    '''returns None\n\n
    setCrossReferenceHandler(final ICrossReferenceHandler xrefHandler)\n
    '''
def getCrossReferenceHandler():
    '''returns ICrossReferenceHandler\n\n
    getCrossReferenceHandler()\n
    '''
def setTypeVariableLookupScope():
    '''returns None\n\n
    setTypeVariableLookupScope(final TypeVariableDeclaringElement scope)\n
    '''
def getTypeVariableLookupScope():
    '''returns TypeVariableDeclaringElement\n\n
    getTypeVariableLookupScope()\n
    '''
def getDeclareParents():
    '''returns List<DeclareParents>\n\n
    getDeclareParents()\n
    '''
def getDeclareAnnotationOnTypes():
    '''returns List<DeclareAnnotation>\n\n
    getDeclareAnnotationOnTypes()\n
    '''
def getDeclareAnnotationOnFields():
    '''returns List<DeclareAnnotation>\n\n
    getDeclareAnnotationOnFields()\n
    '''
def getDeclareAnnotationOnMethods():
    '''returns List<DeclareAnnotation>\n\n
    getDeclareAnnotationOnMethods()\n
    '''
def getDeclareTypeEows():
    '''returns List<DeclareTypeErrorOrWarning>\n\n
    getDeclareTypeEows()\n
    '''
def getDeclareSoft():
    '''returns List<DeclareSoft>\n\n
    getDeclareSoft()\n
    '''
def getCrosscuttingMembersSet():
    '''returns CrosscuttingMembersSet\n\n
    getCrosscuttingMembersSet()\n
    '''
def getModel():
    '''returns IStructureModel\n\n
    getModel()\n
    '''
def setModel():
    '''returns None\n\n
    setModel(final IStructureModel model)\n
    '''
def getLint():
    '''returns Lint\n\n
    getLint()\n
    '''
def setLint():
    '''returns None\n\n
    setLint(final Lint lint)\n
    '''
def isXnoInline():
    '''returns boolean\n\n
    isXnoInline()\n
    '''
def setXnoInline():
    '''returns None\n\n
    setXnoInline(final boolean xnoInline)\n
    '''
def isXlazyTjp():
    '''returns boolean\n\n
    isXlazyTjp()\n
    '''
def setXlazyTjp():
    '''returns None\n\n
    setXlazyTjp(final boolean b)\n
    '''
def isHasMemberSupportEnabled():
    '''returns boolean\n\n
    isHasMemberSupportEnabled()\n
    '''
def setXHasMemberSupportEnabled():
    '''returns None\n\n
    setXHasMemberSupportEnabled(final boolean b)\n
    '''
def isInPinpointMode():
    '''returns boolean\n\n
    isInPinpointMode()\n
    '''
def setPinpointMode():
    '''returns None\n\n
    setPinpointMode(final boolean b)\n
    '''
def useFinal():
    '''returns boolean\n\n
    useFinal()\n
    '''
def isMinimalModel():
    '''returns boolean\n\n
    isMinimalModel()\n
    '''
def isTargettingRuntime1_6_10():
    '''returns boolean\n\n
    isTargettingRuntime1_6_10()\n
    '''
def setBehaveInJava5Way():
    '''returns None\n\n
    setBehaveInJava5Way(final boolean b)\n
    '''
def setTiming():
    '''returns None\n\n
    setTiming(final boolean timersOn, final boolean reportPeriodically)\n
    '''
def setErrorAndWarningThreshold():
    '''returns None\n\n
    setErrorAndWarningThreshold(final boolean errorThreshold, final boolean warningThreshold)\n
    '''
def isIgnoringUnusedDeclaredThrownException():
    '''returns boolean\n\n
    isIgnoringUnusedDeclaredThrownException()\n
    '''
def performExtraConfiguration():
    '''returns None\n\n
    performExtraConfiguration(String config)\n
    '''
def areInfoMessagesEnabled():
    '''returns boolean\n\n
    areInfoMessagesEnabled()\n
    '''
def getExtraConfiguration():
    '''returns Properties\n\n
    getExtraConfiguration()\n
    '''
def isInJava5Mode():
    '''returns boolean\n\n
    isInJava5Mode()\n
    '''
def isTimingEnabled():
    '''returns boolean\n\n
    isTimingEnabled()\n
    '''
def setTargetAspectjRuntimeLevel():
    '''returns None\n\n
    setTargetAspectjRuntimeLevel(final String s)\n
    '''
def setOptionalJoinpoints():
    '''returns None\n\n
    setOptionalJoinpoints(final String jps)\n
    '''
def isJoinpointArrayConstructionEnabled():
    '''returns boolean\n\n
    isJoinpointArrayConstructionEnabled()\n
    '''
def isJoinpointSynchronizationEnabled():
    '''returns boolean\n\n
    isJoinpointSynchronizationEnabled()\n
    '''
def getTargetAspectjRuntimeLevel():
    '''returns String\n\n
    getTargetAspectjRuntimeLevel()\n
    '''
def isTargettingAspectJRuntime12():
    '''returns boolean\n\n
    isTargettingAspectJRuntime12()\n
    '''
def validateType():
    '''returns None\n\n
    validateType(final UnresolvedType type)\n
    '''
def isDemotionActive():
    '''returns boolean\n\n
    isDemotionActive()\n
    '''
def getTypeVariablesCurrentlyBeingProcessed():
    '''returns TypeVariable[]\n\n
    getTypeVariablesCurrentlyBeingProcessed(final Class<?> baseClass)\n
    '''
def recordTypeVariablesCurrentlyBeingProcessed():
    '''returns None\n\n
    recordTypeVariablesCurrentlyBeingProcessed(final Class<?> baseClass, final TypeVariable[] typeVariables)\n
    '''
def forgetTypeVariablesCurrentlyBeingProcessed():
    '''returns None\n\n
    forgetTypeVariablesCurrentlyBeingProcessed(final Class<?> baseClass)\n
    '''
def setAddSerialVerUID():
    '''returns None\n\n
    setAddSerialVerUID(final boolean b)\n
    '''
def isAddSerialVerUID():
    '''returns boolean\n\n
    isAddSerialVerUID()\n
    '''
def flush():
    '''returns None\n\n
    flush()\n
    '''
def ensureAdvancedConfigurationProcessed():
    '''returns None\n\n
    ensureAdvancedConfigurationProcessed()\n
    '''
def isRunMinimalMemory():
    '''returns boolean\n\n
    isRunMinimalMemory()\n
    '''
def isTransientTjpFields():
    '''returns boolean\n\n
    isTransientTjpFields()\n
    '''
def isRunMinimalMemorySet():
    '''returns boolean\n\n
    isRunMinimalMemorySet()\n
    '''
def shouldFastPackMethods():
    '''returns boolean\n\n
    shouldFastPackMethods()\n
    '''
def shouldPipelineCompilation():
    '''returns boolean\n\n
    shouldPipelineCompilation()\n
    '''
def shouldGenerateStackMaps():
    '''returns boolean\n\n
    shouldGenerateStackMaps()\n
    '''
def setIncrementalCompileCouldFollow():
    '''returns None\n\n
    setIncrementalCompileCouldFollow(final boolean b)\n
    '''
def couldIncrementalCompileFollow():
    '''returns boolean\n\n
    couldIncrementalCompileFollow()\n
    '''
def setSynchronizationPointcutsInUse():
    '''returns None\n\n
    setSynchronizationPointcutsInUse()\n
    '''
def areSynchronizationPointcutsInUse():
    '''returns boolean\n\n
    areSynchronizationPointcutsInUse()\n
    '''
def registerPointcutHandler():
    '''returns None\n\n
    registerPointcutHandler(final PointcutDesignatorHandler designatorHandler)\n
    '''
def getRegisteredPointcutHandlers():
    '''returns Set<PointcutDesignatorHandler>\n\n
    getRegisteredPointcutHandlers()\n
    '''
def reportMatch():
    '''returns None\n\n
    reportMatch(final ShadowMunger munger, final Shadow shadow)\n
    '''
def isOverWeaving():
    '''returns boolean\n\n
    isOverWeaving()\n
    '''
def reportCheckerMatch():
    '''returns None\n\n
    reportCheckerMatch(final Checker checker, final Shadow shadow)\n
    '''
def isXmlConfigured():
    '''returns boolean\n\n
    isXmlConfigured()\n
    '''
def isAspectIncluded():
    '''returns boolean\n\n
    isAspectIncluded(final ResolvedType aspectType)\n
    '''
def hasUnsatisfiedDependency():
    '''returns boolean\n\n
    hasUnsatisfiedDependency(final ResolvedType aspectType)\n
    '''
def getAspectScope():
    '''returns TypePattern\n\n
    getAspectScope(final ResolvedType declaringType)\n
    '''
def demote():
    '''returns None\n\n
    demote()\n
    demote()\n
    demote(final boolean atEndOfCompile)\n
    demote(final ResolvedType type)\n
    '''
def record():
    '''returns None\n\n
    record(final Pointcut pointcut, final long timetaken)\n
    '''
def recordFastMatch():
    '''returns None\n\n
    recordFastMatch(final Pointcut pointcut, final long timetaken)\n
    '''
def reportTimers():
    '''returns None\n\n
    reportTimers()\n
    '''
def getTypeMap():
    '''returns TypeMap\n\n
    getTypeMap()\n
    '''
def getItdVersion():
    '''returns int\n\n
    getItdVersion()\n
    '''
def classWriteEvent():
    '''returns None\n\n
    classWriteEvent(final char[][] compoundName)\n
    classWriteEvent(final String classname)\n
    '''
def put():
    '''returns ResolvedType\n\n
    put(final String key, final ResolvedType type)\n
    '''
def report():
    '''returns None\n\n
    report()\n
    report()\n
    '''
def checkq():
    '''returns None\n\n
    checkq()\n
    '''
def get():
    '''returns ResolvedType\n\n
    get(final String key)\n
    '''
def remove():
    '''returns ResolvedType\n\n
    remove(final String key)\n
    '''
def ():
    '''returns PrecedenceCacheKey\n\n
    (final World forSomeWorld)\n
    (final ResolvedType a1, final ResolvedType a2)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
