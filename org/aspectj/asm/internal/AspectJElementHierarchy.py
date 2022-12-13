def AspectJElementHierarchy():
'''public AspectJElementHierarchy(final AsmManager asm)
'''
pass
def getElement():
'''public IProgramElement getElement(final String handle)
'''
pass
def setAsmManager():
'''public void setAsmManager(final AsmManager asm)
'''
pass
def getRoot():
'''public IProgramElement getRoot()
'''
pass
def toSummaryString():
'''public String toSummaryString()
'''
pass
def setRoot():
'''public void setRoot(final IProgramElement root)
'''
pass
def addToFileMap():
'''public void addToFileMap(final String key, final IProgramElement value)
'''
pass
def removeFromFileMap():
'''public boolean removeFromFileMap(final String canonicalFilePath)
'''
pass
def setFileMap():
'''public void setFileMap(final HashMap<String, IProgramElement> fileMap)
'''
pass
def findInFileMap():
'''public Object findInFileMap(final Object key)
'''
pass
def isValid():
'''public boolean isValid()
'''
pass
def findElementForSignature():
'''public IProgramElement findElementForSignature(final IProgramElement parent, final IProgramElement.Kind kind, final String signature)
'''
pass
def findElementForLabel():
'''public IProgramElement findElementForLabel(final IProgramElement parent, final IProgramElement.Kind kind, final String label)
'''
pass
def findElementForType():
'''public IProgramElement findElementForType(final String packageName, final String typeName)
'''
pass
def findMatchingPackages():
'''public List<IProgramElement> findMatchingPackages(final String packagename)
'''
pass
def findElementForSourceFile():
'''public IProgramElement findElementForSourceFile(final String sourceFile)
'''
pass
def findElementForSourceLine():
'''public IProgramElement findElementForSourceLine(final ISourceLocation location)
public IProgramElement findElementForSourceLine(final String sourceFilePath, final int lineNumber)
'''
pass
def findNodeForSourceFile():
'''public IProgramElement findNodeForSourceFile(final IProgramElement node, final String sourcefilePath)
'''
pass
def findElementForOffSet():
'''public IProgramElement findElementForOffSet(final String sourceFilePath, final int lineNumber, final int offSet)
'''
pass
def findCloserMatchForLineNumber():
'''public IProgramElement findCloserMatchForLineNumber(final IProgramElement node, final int lineno)
'''
pass
def getConfigFile():
'''public String getConfigFile()
'''
pass
def setConfigFile():
'''public void setConfigFile(final String configFile)
'''
pass
def findElementForHandle():
'''public IProgramElement findElementForHandle(final String handle)
'''
pass
def findElementForHandleOrCreate():
'''public IProgramElement findElementForHandleOrCreate(final String handle, final boolean create)
'''
pass
def flushTypeMap():
'''public void flushTypeMap()
'''
pass
def flushHandleMap():
'''public void flushHandleMap()
'''
pass
def flushFileMap():
'''public void flushFileMap()
'''
pass
def forget():
'''public void forget(final IProgramElement compilationUnitNode, final IProgramElement typeNode)
'''
pass
def updateHandleMap():
'''public void updateHandleMap(final Set<String> deletedFiles)
'''
pass
