def createNewStructureModel():
'''public static AsmManager createNewStructureModel(final Map<File, String> inpathMap)
'''
pass
def getHierarchy():
'''public IHierarchy getHierarchy()
'''
pass
def getRelationshipMap():
'''public IRelationshipMap getRelationshipMap()
'''
pass
def fireModelUpdated():
'''public void fireModelUpdated()
'''
pass
def getInlineAnnotations():
'''public HashMap<Integer, List<IProgramElement>> getInlineAnnotations(final String sourceFile, final boolean showSubMember, final boolean showMemberAndType)
'''
pass
def addListener():
'''public void addListener(final IHierarchyListener listener)
'''
pass
def removeStructureListener():
'''public void removeStructureListener(final IHierarchyListener listener)
'''
pass
def removeAllListeners():
'''public void removeAllListeners()
'''
pass
def getHandleProvider():
'''public IElementHandleProvider getHandleProvider()
'''
pass
def setHandleProvider():
'''public void setHandleProvider(final IElementHandleProvider handleProvider)
'''
pass
def writeStructureModel():
'''public void writeStructureModel(final String configFilePath)
'''
pass
def readStructureModel():
'''public void readStructureModel(final String configFilePath)
'''
pass
def getCanonicalFilePath():
'''public String getCanonicalFilePath(final File f)
'''
pass
def getCanonicalFilePathMap():
'''public CanonicalFilePathMap getCanonicalFilePathMap()
'''
pass
def setReporting():
'''public static void setReporting(final String filename, final boolean dModel, final boolean dRels, final boolean dDeltaProcessing, final boolean deletefile)
public static void setReporting(final String filename, final boolean dModel, final boolean dRels, final boolean dDeltaProcessing, final boolean deletefile, final IModelFilter aFilter)
'''
pass
def isReporting():
'''public static boolean isReporting()
'''
pass
def setDontReport():
'''public static void setDontReport()
'''
pass
def reportModelInfo():
'''public void reportModelInfo(final String reasonForReport)
'''
pass
def dumptree():
'''public static void dumptree(final Writer w, final IProgramElement node, final int indent)
public static void dumptree(final IProgramElement node, final int indent)
'''
pass
def dumprels():
'''public void dumprels(final Writer w)
'''
pass
def removeStructureModelForFiles():
'''public boolean removeStructureModelForFiles(final Writer fw, final Collection<File> files)
'''
pass
def processDelta():
'''public void processDelta(final Collection<File> files_tobecompiled, final Set<File> files_added, final Set<File> files_deleted)
'''
pass
def removeRelationshipsTargettingThisType():
'''public void removeRelationshipsTargettingThisType(final String typename)
'''
pass
def verifyAssumption():
'''public static void verifyAssumption(final boolean b, final String info)
public static void verifyAssumption(final boolean b)
'''
pass
def summarizeModel():
'''public ModelInfo summarizeModel()
'''
pass
def setCompletingTypeBindings():
'''public static void setCompletingTypeBindings(final boolean b)
'''
pass
def isCompletingTypeBindings():
'''public static boolean isCompletingTypeBindings()
'''
pass
def resetDeltaProcessing():
'''public void resetDeltaProcessing()
'''
pass
def getModelChangesOnLastBuild():
'''public Set<File> getModelChangesOnLastBuild()
'''
pass
def getAspectsWeavingFilesOnLastBuild():
'''public Set<File> getAspectsWeavingFilesOnLastBuild()
'''
pass
def addAspectInEffectThisBuild():
'''public void addAspectInEffectThisBuild(final File f)
'''
pass
def setLastActiveStructureModel():
'''public static void setLastActiveStructureModel(final AsmManager structureModel)
'''
pass
def getHandleElementForInpath():
'''public String getHandleElementForInpath(final String binaryPath)
'''
pass
def get():
'''public String get(final File f)
'''
pass
def toString():
'''public String toString()
'''
pass
def getProperties():
'''public Properties getProperties()
'''
pass
def recordStat():
'''public void recordStat(final String string, final String string2)
'''
pass
