def ():
    '''returns AspectJElementHierarchy\n\n
    (final AsmManager asm)\n
    '''
def getElement():
    '''returns IProgramElement\n\n
    getElement(final String handle)\n
    '''
def setAsmManager():
    '''returns None\n\n
    setAsmManager(final AsmManager asm)\n
    '''
def getRoot():
    '''returns IProgramElement\n\n
    getRoot()\n
    '''
def toSummaryString():
    '''returns String\n\n
    toSummaryString()\n
    '''
def setRoot():
    '''returns None\n\n
    setRoot(final IProgramElement root)\n
    '''
def addToFileMap():
    '''returns None\n\n
    addToFileMap(final String key, final IProgramElement value)\n
    '''
def removeFromFileMap():
    '''returns boolean\n\n
    removeFromFileMap(final String canonicalFilePath)\n
    '''
def setFileMap():
    '''returns None\n\n
    setFileMap(final HashMap<String, IProgramElement> fileMap)\n
    '''
def findInFileMap():
    '''returns Object\n\n
    findInFileMap(final Object key)\n
    '''
def isValid():
    '''returns boolean\n\n
    isValid()\n
    '''
def findElementForSignature():
    '''returns IProgramElement\n\n
    findElementForSignature(final IProgramElement parent, final IProgramElement.Kind kind, final String signature)\n
    '''
def findElementForLabel():
    '''returns IProgramElement\n\n
    findElementForLabel(final IProgramElement parent, final IProgramElement.Kind kind, final String label)\n
    '''
def findElementForType():
    '''returns IProgramElement\n\n
    findElementForType(final String packageName, final String typeName)\n
    '''
def findMatchingPackages():
    '''returns List<IProgramElement>\n\n
    findMatchingPackages(final String packagename)\n
    '''
def findElementForSourceFile():
    '''returns IProgramElement\n\n
    findElementForSourceFile(final String sourceFile)\n
    '''
def findElementForSourceLine():
    '''returns IProgramElement\n\n
    findElementForSourceLine(final ISourceLocation location)\n
    findElementForSourceLine(final String sourceFilePath, final int lineNumber)\n
    '''
def findNodeForSourceFile():
    '''returns IProgramElement\n\n
    findNodeForSourceFile(final IProgramElement node, final String sourcefilePath)\n
    '''
def findElementForOffSet():
    '''returns IProgramElement\n\n
    findElementForOffSet(final String sourceFilePath, final int lineNumber, final int offSet)\n
    '''
def findCloserMatchForLineNumber():
    '''returns IProgramElement\n\n
    findCloserMatchForLineNumber(final IProgramElement node, final int lineno)\n
    '''
def getConfigFile():
    '''returns String\n\n
    getConfigFile()\n
    '''
def setConfigFile():
    '''returns None\n\n
    setConfigFile(final String configFile)\n
    '''
def findElementForHandle():
    '''returns IProgramElement\n\n
    findElementForHandle(final String handle)\n
    '''
def findElementForHandleOrCreate():
    '''returns IProgramElement\n\n
    findElementForHandleOrCreate(final String handle, final boolean create)\n
    '''
def flushTypeMap():
    '''returns None\n\n
    flushTypeMap()\n
    '''
def flushHandleMap():
    '''returns None\n\n
    flushHandleMap()\n
    '''
def flushFileMap():
    '''returns None\n\n
    flushFileMap()\n
    '''
def forget():
    '''returns None\n\n
    forget(final IProgramElement compilationUnitNode, final IProgramElement typeNode)\n
    '''
def updateHandleMap():
    '''returns None\n\n
    updateHandleMap(final Set<String> deletedFiles)\n
    '''
