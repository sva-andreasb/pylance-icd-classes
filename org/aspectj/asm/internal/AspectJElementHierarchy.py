def AspectJElementHierarchy():
    '''public AspectJElementHierarchy(final AsmManager asm)
    '''
def getElement():
    '''public IProgramElement getElement(final String handle)
    '''
def setAsmManager():
    '''public void setAsmManager(final AsmManager asm)
    '''
def getRoot():
    '''public IProgramElement getRoot()
    '''
def toSummaryString():
    '''public String toSummaryString()
    '''
def setRoot():
    '''public void setRoot(final IProgramElement root)
    '''
def addToFileMap():
    '''public void addToFileMap(final String key, final IProgramElement value)
    '''
def removeFromFileMap():
    '''public boolean removeFromFileMap(final String canonicalFilePath)
    '''
def setFileMap():
    '''public void setFileMap(final HashMap<String, IProgramElement> fileMap)
    '''
def findInFileMap():
    '''public Object findInFileMap(final Object key)
    '''
def isValid():
    '''public boolean isValid()
    '''
def findElementForSignature():
    '''public IProgramElement findElementForSignature(final IProgramElement parent, final IProgramElement.Kind kind, final String signature)
    '''
def findElementForLabel():
    '''public IProgramElement findElementForLabel(final IProgramElement parent, final IProgramElement.Kind kind, final String label)
    '''
def findElementForType():
    '''public IProgramElement findElementForType(final String packageName, final String typeName)
    '''
def findMatchingPackages():
    '''public List<IProgramElement> findMatchingPackages(final String packagename)
    '''
def findElementForSourceFile():
    '''public IProgramElement findElementForSourceFile(final String sourceFile)
    '''
def findElementForSourceLine():
    '''public IProgramElement findElementForSourceLine(final ISourceLocation location)
    public IProgramElement findElementForSourceLine(final String sourceFilePath, final int lineNumber)
    '''
def findNodeForSourceFile():
    '''public IProgramElement findNodeForSourceFile(final IProgramElement node, final String sourcefilePath)
    '''
def findElementForOffSet():
    '''public IProgramElement findElementForOffSet(final String sourceFilePath, final int lineNumber, final int offSet)
    '''
def findCloserMatchForLineNumber():
    '''public IProgramElement findCloserMatchForLineNumber(final IProgramElement node, final int lineno)
    '''
def getConfigFile():
    '''public String getConfigFile()
    '''
def setConfigFile():
    '''public void setConfigFile(final String configFile)
    '''
def findElementForHandle():
    '''public IProgramElement findElementForHandle(final String handle)
    '''
def findElementForHandleOrCreate():
    '''public IProgramElement findElementForHandleOrCreate(final String handle, final boolean create)
    '''
def flushTypeMap():
    '''public void flushTypeMap()
    '''
def flushHandleMap():
    '''public void flushHandleMap()
    '''
def flushFileMap():
    '''public void flushFileMap()
    '''
def forget():
    '''public void forget(final IProgramElement compilationUnitNode, final IProgramElement typeNode)
    '''
def updateHandleMap():
    '''public void updateHandleMap(final Set<String> deletedFiles)
    '''
