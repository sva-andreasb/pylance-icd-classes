def createNewStructureModel():
    '''public static AsmManager createNewStructureModel(final Map<File, String> inpathMap)
    '''
def getHierarchy():
    '''public IHierarchy getHierarchy()
    '''
def getRelationshipMap():
    '''public IRelationshipMap getRelationshipMap()
    '''
def fireModelUpdated():
    '''public void fireModelUpdated()
    '''
def getInlineAnnotations():
    '''public HashMap<Integer, List<IProgramElement>> getInlineAnnotations(final String sourceFile, final boolean showSubMember, final boolean showMemberAndType)
    '''
def addListener():
    '''public void addListener(final IHierarchyListener listener)
    '''
def removeStructureListener():
    '''public void removeStructureListener(final IHierarchyListener listener)
    '''
def removeAllListeners():
    '''public void removeAllListeners()
    '''
def getHandleProvider():
    '''public IElementHandleProvider getHandleProvider()
    '''
def setHandleProvider():
    '''public void setHandleProvider(final IElementHandleProvider handleProvider)
    '''
def writeStructureModel():
    '''public void writeStructureModel(final String configFilePath)
    '''
def readStructureModel():
    '''public void readStructureModel(final String configFilePath)
    '''
def getCanonicalFilePath():
    '''public String getCanonicalFilePath(final File f)
    '''
def getCanonicalFilePathMap():
    '''public CanonicalFilePathMap getCanonicalFilePathMap()
    '''
def setReporting():
    '''public static void setReporting(final String filename, final boolean dModel, final boolean dRels, final boolean dDeltaProcessing, final boolean deletefile)
    public static void setReporting(final String filename, final boolean dModel, final boolean dRels, final boolean dDeltaProcessing, final boolean deletefile, final IModelFilter aFilter)
    '''
def isReporting():
    '''public static boolean isReporting()
    '''
def setDontReport():
    '''public static void setDontReport()
    '''
def reportModelInfo():
    '''public void reportModelInfo(final String reasonForReport)
    '''
def dumptree():
    '''public static void dumptree(final Writer w, final IProgramElement node, final int indent)
    public static void dumptree(final IProgramElement node, final int indent)
    '''
def dumprels():
    '''public void dumprels(final Writer w)
    '''
def removeStructureModelForFiles():
    '''public boolean removeStructureModelForFiles(final Writer fw, final Collection<File> files)
    '''
def processDelta():
    '''public void processDelta(final Collection<File> files_tobecompiled, final Set<File> files_added, final Set<File> files_deleted)
    '''
def removeRelationshipsTargettingThisType():
    '''public void removeRelationshipsTargettingThisType(final String typename)
    '''
def verifyAssumption():
    '''public static void verifyAssumption(final boolean b, final String info)
    public static void verifyAssumption(final boolean b)
    '''
def summarizeModel():
    '''public ModelInfo summarizeModel()
    '''
def setCompletingTypeBindings():
    '''public static void setCompletingTypeBindings(final boolean b)
    '''
def isCompletingTypeBindings():
    '''public static boolean isCompletingTypeBindings()
    '''
def resetDeltaProcessing():
    '''public void resetDeltaProcessing()
    '''
def getModelChangesOnLastBuild():
    '''public Set<File> getModelChangesOnLastBuild()
    '''
def getAspectsWeavingFilesOnLastBuild():
    '''public Set<File> getAspectsWeavingFilesOnLastBuild()
    '''
def addAspectInEffectThisBuild():
    '''public void addAspectInEffectThisBuild(final File f)
    '''
def setLastActiveStructureModel():
    '''public static void setLastActiveStructureModel(final AsmManager structureModel)
    '''
def getHandleElementForInpath():
    '''public String getHandleElementForInpath(final String binaryPath)
    '''
def get():
    '''public String get(final File f)
    '''
def toString():
    '''public String toString()
    '''
def getProperties():
    '''public Properties getProperties()
    '''
def recordStat():
    '''public void recordStat(final String string, final String string2)
    '''
