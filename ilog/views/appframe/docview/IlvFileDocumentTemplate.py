DEFAULT_FILE_FILTER_PROPERTY = "String  \"DefaultFileFilter\""
def IlvFileDocumentTemplate():
    '''    public IlvFileDocumentTemplate()
    public IlvFileDocumentTemplate(final String s)
    '''
def matchPathName():
    '''    public boolean matchPathName(final URL url)
    public boolean matchPathName(final String s)
    '''
def getMatchingFilter():
    '''    public IlvFileFilter getMatchingFilter(final URL url)
    public IlvFileFilter getMatchingFilter(final String s)
    '''
def readDocument():
    '''    public boolean readDocument(final IlvFileDocument ilvFileDocument, final URL url, final IlvFileFilter ilvFileFilter)
    public boolean readDocument(final IlvStreamDocument ilvStreamDocument, final Reader reader, final IlvFileFilter ilvFileFilter)
    '''
def setDocumentPathName():
    '''    public void setDocumentPathName(final IlvFileDocument ilvFileDocument, final URL pathName)
    '''
def revertDocument():
    '''    public boolean revertDocument(final IlvFileDocument ilvFileDocument)
    '''
def initializeFileChooser():
    '''    public void initializeFileChooser(final JFileChooser fileChooser, final boolean b)
    '''
def getFilterCount():
    '''    public int getFilterCount()
    '''
def getFilter():
    '''    public IlvFileFilter getFilter(final int n)
    '''
def addFilter():
    '''    public void addFilter(final IlvFileFilter ilvFileFilter)
    '''
def setDefaultFilter():
    '''    public IlvFileFilter setDefaultFilter(final IlvFileFilter ilvFileFilter)
    '''
def getDefaultFilter():
    '''    public IlvFileFilter getDefaultFilter()
    '''
def removeFilter():
    '''    public boolean removeFilter(final IlvFileFilter o)
    '''
def getFilterIndex():
    '''    public int getFilterIndex(final IlvFileFilter ilvFileFilter)
    '''
def appearsInLoadFileFilters():
    '''    public boolean appearsInLoadFileFilters()
    '''
def setAppearsInLoadFileFilters():
    '''    public void setAppearsInLoadFileFilters(final boolean b)
    '''
def appearsInNewDocuments():
    '''    public boolean appearsInNewDocuments()
    '''
def setAppearsInNewDocuments():
    '''    public void setAppearsInNewDocuments(final boolean c)
    '''
def actionPerformed():
    '''    public void actionPerformed(final ActionEvent actionEvent)
    '''
def isProcessingAction():
    '''    public boolean isProcessingAction(final String anObject)
    '''
def readSettings():
    '''    public boolean readSettings(final IlvSettingsElement ilvSettingsElement, final IlvApplication ilvApplication)
    '''
