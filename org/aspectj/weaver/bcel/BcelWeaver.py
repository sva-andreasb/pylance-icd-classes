CLOSURE_CLASS_PREFIX = "String  \"$Ajc\""
SYNTHETIC_CLASS_POSTFIX = "String  \"$ajc\""
def ():
    '''returns AdviceLocation\n\n
    (final BcelWorld world)\n
    ()\n
    '''
def addLibraryAspect():
    '''returns ResolvedType\n\n
    addLibraryAspect(final String aspectName)\n
    '''
def addLibraryJarFile():
    '''returns None\n\n
    addLibraryJarFile(final File inFile)\n
    '''
def accept():
    '''returns boolean\n\n
    accept(final File pathname)\n
    accept(final File f)\n
    '''
def addDirectoryContents():
    '''returns List<UnwovenClassFile>\n\n
    addDirectoryContents(final File inFile, final File outDir)\n
    '''
def addJarFile():
    '''returns List<UnwovenClassFile>\n\n
    addJarFile(final File inFile, final File outDir, final boolean canBeDirectory)\n
    '''
def needToReweaveWorld():
    '''returns boolean\n\n
    needToReweaveWorld()\n
    '''
def addClassFile():
    '''returns UnwovenClassFile\n\n
    addClassFile(final UnwovenClassFile classFile, final boolean fromInpath)\n
    addClassFile(final File classFile, final File inPathDir, final File outDir)\n
    '''
def deleteClassFile():
    '''returns None\n\n
    deleteClassFile(final String typename)\n
    '''
def setIsBatchWeave():
    '''returns None\n\n
    setIsBatchWeave(final boolean b)\n
    '''
def prepareForWeave():
    '''returns None\n\n
    prepareForWeave()\n
    '''
def compare():
    '''returns int\n\n
    compare(final ShadowMunger sm1, final ShadowMunger sm2)\n
    '''
def setCustomMungerFactory():
    '''returns None\n\n
    setCustomMungerFactory(final CustomMungerFactory factory)\n
    '''
def addManifest():
    '''returns None\n\n
    addManifest(final Manifest newManifest)\n
    '''
def getManifest():
    '''returns Manifest\n\n
    getManifest(final boolean shouldCreate)\n
    '''
def weave():
    '''returns Collection<String>\n\n
    weave(final File file)\n
    weave(final IClassFileProvider input)\n
    '''
def isApplyAtAspectJMungersOnly():
    '''returns boolean\n\n
    isApplyAtAspectJMungersOnly()\n
    '''
def getClassFileIterator():
    '''returns Iterator<UnwovenClassFile>\n\n
    getClassFileIterator()\n
    '''
def getRequestor():
    '''returns IWeaveRequestor\n\n
    getRequestor()\n
    '''
def acceptResult():
    '''returns None\n\n
    acceptResult(final IUnwovenClassFile result)\n
    '''
def processingReweavableState():
    '''returns None\n\n
    processingReweavableState()\n
    '''
def addingTypeMungers():
    '''returns None\n\n
    addingTypeMungers()\n
    '''
def weavingAspects():
    '''returns None\n\n
    weavingAspects()\n
    '''
def weavingClasses():
    '''returns None\n\n
    weavingClasses()\n
    '''
def weaveCompleted():
    '''returns None\n\n
    weaveCompleted()\n
    '''
def allWeavingComplete():
    '''returns None\n\n
    allWeavingComplete()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def prepareToProcessReweavableState():
    '''returns None\n\n
    prepareToProcessReweavableState()\n
    '''
def processReweavableStateIfPresent():
    '''returns None\n\n
    processReweavableStateIfPresent(final String className, final BcelObjectType classType)\n
    '''
def getClassType():
    '''returns BcelObjectType\n\n
    getClassType(final String forClass)\n
    '''
def addParentTypeMungers():
    '''returns None\n\n
    addParentTypeMungers(final String typeName)\n
    '''
def addNormalTypeMungers():
    '''returns None\n\n
    addNormalTypeMungers(final String typeName)\n
    '''
def getClassFilesFor():
    '''returns UnwovenClassFile[]\n\n
    getClassFilesFor(final LazyClassGen clazz)\n
    '''
def weaveParentTypeMungers():
    '''returns None\n\n
    weaveParentTypeMungers(ResolvedType onType)\n
    '''
def weaveNormalTypeMungers():
    '''returns None\n\n
    weaveNormalTypeMungers(ResolvedType onType)\n
    '''
def weaveWithoutDump():
    '''returns LazyClassGen\n\n
    weaveWithoutDump(final UnwovenClassFile classFile, final BcelObjectType classType)\n
    '''
def setReweavableMode():
    '''returns None\n\n
    setReweavableMode(final boolean xNotReweavable)\n
    '''
def isReweavable():
    '''returns boolean\n\n
    isReweavable()\n
    '''
def getWorld():
    '''returns World\n\n
    getWorld()\n
    '''
def tidyUp():
    '''returns None\n\n
    tidyUp()\n
    '''
def write():
    '''returns None\n\n
    write(final CompressingDataOutputStream dos)\n
    '''
def setShadowMungers():
    '''returns None\n\n
    setShadowMungers(final List<ShadowMunger> shadowMungers)\n
    '''
