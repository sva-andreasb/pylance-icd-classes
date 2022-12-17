def getHierarchy():
    '''returns IHierarchy\n\n
    getHierarchy()\n
    '''
def getRelationshipMap():
    '''returns IRelationshipMap\n\n
    getRelationshipMap()\n
    '''
def fireModelUpdated():
    '''returns None\n\n
    fireModelUpdated()\n
    '''
def addListener():
    '''returns None\n\n
    addListener(final IHierarchyListener listener)\n
    '''
def removeStructureListener():
    '''returns None\n\n
    removeStructureListener(final IHierarchyListener listener)\n
    '''
def removeAllListeners():
    '''returns None\n\n
    removeAllListeners()\n
    '''
def getHandleProvider():
    '''returns IElementHandleProvider\n\n
    getHandleProvider()\n
    '''
def setHandleProvider():
    '''returns None\n\n
    setHandleProvider(final IElementHandleProvider handleProvider)\n
    '''
def writeStructureModel():
    '''returns None\n\n
    writeStructureModel(final String configFilePath)\n
    '''
def readStructureModel():
    '''returns None\n\n
    readStructureModel(final String configFilePath)\n
    '''
def getCanonicalFilePath():
    '''returns String\n\n
    getCanonicalFilePath(final File f)\n
    '''
def getCanonicalFilePathMap():
    '''returns CanonicalFilePathMap\n\n
    getCanonicalFilePathMap()\n
    '''
def reportModelInfo():
    '''returns None\n\n
    reportModelInfo(final String reasonForReport)\n
    '''
def dumprels():
    '''returns None\n\n
    dumprels(final Writer w)\n
    '''
def removeStructureModelForFiles():
    '''returns boolean\n\n
    removeStructureModelForFiles(final Writer fw, final Collection<File> files)\n
    '''
def processDelta():
    '''returns None\n\n
    processDelta(final Collection<File> files_tobecompiled, final Set<File> files_added, final Set<File> files_deleted)\n
    '''
def removeRelationshipsTargettingThisType():
    '''returns None\n\n
    removeRelationshipsTargettingThisType(final String typename)\n
    '''
def summarizeModel():
    '''returns ModelInfo\n\n
    summarizeModel()\n
    '''
def resetDeltaProcessing():
    '''returns None\n\n
    resetDeltaProcessing()\n
    '''
def getModelChangesOnLastBuild():
    '''returns Set<File>\n\n
    getModelChangesOnLastBuild()\n
    '''
def getAspectsWeavingFilesOnLastBuild():
    '''returns Set<File>\n\n
    getAspectsWeavingFilesOnLastBuild()\n
    '''
def addAspectInEffectThisBuild():
    '''returns None\n\n
    addAspectInEffectThisBuild(final File f)\n
    '''
def getHandleElementForInpath():
    '''returns String\n\n
    getHandleElementForInpath(final String binaryPath)\n
    '''
def get():
    '''returns String\n\n
    get(final File f)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getProperties():
    '''returns Properties\n\n
    getProperties()\n
    '''
def recordStat():
    '''returns None\n\n
    recordStat(final String string, final String string2)\n
    '''
