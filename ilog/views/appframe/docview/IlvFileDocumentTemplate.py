DEFAULT_FILE_FILTER_PROPERTY = "String  \"DefaultFileFilter\""
def ():
    '''returns IlvFileDocumentTemplate\n\n
    ()\n
    (final String s)\n
    '''
def matchPathName():
    '''returns boolean\n\n
    matchPathName(final URL url)\n
    matchPathName(final String s)\n
    '''
def getMatchingFilter():
    '''returns IlvFileFilter\n\n
    getMatchingFilter(final URL url)\n
    getMatchingFilter(final String s)\n
    '''
def readDocument():
    '''returns boolean\n\n
    readDocument(final IlvFileDocument ilvFileDocument, final URL url, final IlvFileFilter ilvFileFilter)\n
    readDocument(final IlvStreamDocument ilvStreamDocument, final Reader reader, final IlvFileFilter ilvFileFilter)\n
    '''
def setDocumentPathName():
    '''returns None\n\n
    setDocumentPathName(final IlvFileDocument ilvFileDocument, final URL pathName)\n
    '''
def revertDocument():
    '''returns boolean\n\n
    revertDocument(final IlvFileDocument ilvFileDocument)\n
    '''
def initializeFileChooser():
    '''returns None\n\n
    initializeFileChooser(final JFileChooser fileChooser, final boolean b)\n
    '''
def getFilterCount():
    '''returns int\n\n
    getFilterCount()\n
    '''
def getFilter():
    '''returns IlvFileFilter\n\n
    getFilter(final int n)\n
    '''
def addFilter():
    '''returns None\n\n
    addFilter(final IlvFileFilter ilvFileFilter)\n
    '''
def setDefaultFilter():
    '''returns IlvFileFilter\n\n
    setDefaultFilter(final IlvFileFilter ilvFileFilter)\n
    '''
def getDefaultFilter():
    '''returns IlvFileFilter\n\n
    getDefaultFilter()\n
    '''
def removeFilter():
    '''returns boolean\n\n
    removeFilter(final IlvFileFilter o)\n
    '''
def getFilterIndex():
    '''returns int\n\n
    getFilterIndex(final IlvFileFilter ilvFileFilter)\n
    '''
def appearsInLoadFileFilters():
    '''returns boolean\n\n
    appearsInLoadFileFilters()\n
    '''
def setAppearsInLoadFileFilters():
    '''returns None\n\n
    setAppearsInLoadFileFilters(final boolean b)\n
    '''
def appearsInNewDocuments():
    '''returns boolean\n\n
    appearsInNewDocuments()\n
    '''
def setAppearsInNewDocuments():
    '''returns None\n\n
    setAppearsInNewDocuments(final boolean c)\n
    '''
def actionPerformed():
    '''returns None\n\n
    actionPerformed(final ActionEvent actionEvent)\n
    '''
def isProcessingAction():
    '''returns boolean\n\n
    isProcessingAction(final String anObject)\n
    '''
def readSettings():
    '''returns boolean\n\n
    readSettings(final IlvSettingsElement ilvSettingsElement, final IlvApplication ilvApplication)\n
    '''
