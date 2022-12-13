ACTIVE_DOCUMENT_NAME = "String  \"ActiveDocument\""
SHOW_FILE_CHOOSER_ICONS_PROPERTY = "String  \"ShowFileChooserIcons\""
def IlvDocumentManager():
    '''    public IlvDocumentManager()
    '''
def readSettings():
    '''    public void readSettings(final IlvSettingsElement ilvSettingsElement, final Object o)
    public void readSettings(final IlvSettingsManager settings)
    '''
def writeSettings():
    '''    public void writeSettings(final IlvSettingsElement ilvSettingsElement, final Object o)
    '''
def propertyChange():
    '''    public void propertyChange(final PropertyChangeEvent propertyChangeEvent)
    public void propertyChange(final PropertyChangeEvent propertyChangeEvent)
    public void propertyChange(final PropertyChangeEvent propertyChangeEvent)
    '''
def isValidDocument():
    '''    public boolean isValidDocument(final URL url)
    '''
def openDocument():
    '''    public IlvDocument openDocument(final URL url, final boolean b, final boolean b2)
    public IlvFileDocument openDocument(final IlvFileDocumentTemplate ilvFileDocumentTemplate, URL url, IlvFileFilter ilvFileFilter, final boolean b, final boolean b2)
    public IlvDocument openDocument(final boolean b, final IlvMainWindow ilvMainWindow)
    '''
def initializeDocument():
    '''    public boolean initializeDocument(final IlvDocument ilvDocument, final Object o, final DocTemplateInfo docTemplateInfo)
    public boolean initializeDocument(final IlvDocument ilvDocument, final Object o, final DocTemplateInfo docTemplateInfo)
    '''
def getOpenedDocument():
    '''    public IlvDocument getOpenedDocument(final URL url)
    public IlvDocument getOpenedDocument(final int n)
    '''
def getOpenDocuments():
    '''    public IlvDocument[] getOpenDocuments()
    public IlvDocument[] getOpenDocuments(final IlvDocumentTemplate ilvDocumentTemplate)
    '''
def openRecentFile():
    '''    public void openRecentFile(final int n)
    '''
def showFileChooser():
    '''    public IlvFileChooserSelection[] showFileChooser(final String s, final String s2, final int n, final IlvFileDocumentTemplate ilvFileDocumentTemplate, Component mainComponent)
    '''
def initializeFileChooser():
    '''    public void initializeFileChooser(final JFileChooser fileChooser, final String pathname, final int n, final IlvFileDocumentTemplate e)
    '''
def accept():
    '''    public boolean accept(final File file)
    '''
def getDescription():
    '''    public String getDescription()
    public String getDescription(final File file)
    '''
def getName():
    '''    public String getName(final File file)
    '''
def isTraversable():
    '''    public Boolean isTraversable(final File file)
    '''
def getTypeDescription():
    '''    public String getTypeDescription(final File file)
    '''
def getIcon():
    '''    public Icon getIcon(final File file)
    '''
def showAppletFileChooser():
    '''    public IlvFileChooserSelection[] showAppletFileChooser(final String s, final String s2, final int n, final IlvFileDocumentTemplate ilvFileDocumentTemplate, final Component comp)
    '''
def findBestTemplate():
    '''    public IlvFileDocumentTemplate findBestTemplate(final URL url)
    public IlvFileDocumentTemplate findBestTemplate(final String s)
    '''
def createHTMLBrowser():
    '''    public Window createHTMLBrowser(String string, final URL page, final HyperlinkListener listener, final boolean b, final Frame frame)
    '''
def hyperlinkUpdate():
    '''    public void hyperlinkUpdate(final HyperlinkEvent hyperlinkEvent)
    public void hyperlinkUpdate(final HyperlinkEvent hyperlinkEvent)
    '''
def run():
    '''    public void run()
    '''
def mouseEntered():
    '''    public void mouseEntered(final MouseEvent mouseEvent)
    '''
def mouseExited():
    '''    public void mouseExited(final MouseEvent mouseEvent)
    '''
def mousePressed():
    '''    public void mousePressed(final MouseEvent mouseEvent)
    '''
def mouseReleased():
    '''    public void mouseReleased(final MouseEvent mouseEvent)
    '''
def actionPerformed():
    '''    public void actionPerformed(final ActionEvent actionEvent)
    '''
def newDocument():
    '''    public IlvDocument newDocument(final boolean b, final IlvDocumentTemplate ilvDocumentTemplate, final DocumentInitializer documentInitializer, final Object o)
    public IlvDocument newDocument(final boolean b, final IlvMainWindow ilvMainWindow)
    public IlvDocument newDocument(final IlvDocumentTemplate ilvDocumentTemplate, final boolean b, final Object o)
    public IlvDocument newDocument(final Object o, final boolean b)
    public final IlvDocument newDocument(final boolean b)
    public final IlvDocument newDocument()
    '''
def getMainDocumentTemplates():
    '''    public IlvDocumentTemplate[] getMainDocumentTemplates(final boolean b)
    '''
def newDocumentOnLastTemplate():
    '''    public IlvDocument newDocumentOnLastTemplate(final boolean b, final IlvMainWindow ilvMainWindow)
    '''
def canCreateDocument():
    '''    public boolean canCreateDocument(final Object o)
    '''
def findDocumentTemplate():
    '''    public IlvDocumentTemplate findDocumentTemplate(final Object o)
    '''
def saveAllDocuments():
    '''    public boolean saveAllDocuments()
    public boolean saveAllDocuments()
    '''
def saveAllDocumentsUI():
    '''    public void saveAllDocumentsUI(final Action action)
    '''
def saveDocument():
    '''    public boolean saveDocument(final IlvDocument ilvDocument)
    '''
def saveFileDocument():
    '''    public boolean saveFileDocument(final IlvFileDocument ilvFileDocument, final String s, IlvFileFilter ilvFileFilter, final boolean b)
    '''
def saveAsDocument():
    '''    public boolean saveAsDocument(final IlvFileDocument ilvFileDocument)
    '''
def saveDocumentModifications():
    '''    public boolean saveDocumentModifications(final IlvDocument ilvDocument)
    '''
def isEditable():
    '''    public boolean isEditable(final IlvDocument ilvDocument)
    '''
def isSaveable():
    '''    public boolean isSaveable(final IlvDocument ilvDocument)
    '''
def closeAllDocuments():
    '''    public boolean closeAllDocuments(final boolean b)
    '''
def closeAllDocumentsUI():
    '''    public boolean closeAllDocumentsUI(final Action action)
    '''
def closeDocument():
    '''    public boolean closeDocument(final IlvDocument ilvDocument, final boolean b)
    '''
def saveModifications():
    '''    public boolean saveModifications()
    '''
def getOpenedDocumentCount():
    '''    public int getOpenedDocumentCount()
    public int getOpenedDocumentCount()
    '''
def addToRecentFileList():
    '''    public void addToRecentFileList(final URL url)
    '''
def addDocumentTemplate():
    '''    public void addDocumentTemplate(final IlvDocumentTemplate ilvDocumentTemplate)
    '''
def removeDocumentTemplate():
    '''    public boolean removeDocumentTemplate(final IlvDocumentTemplate ilvDocumentTemplate)
    '''
def removeDocTemplate():
    '''    public boolean removeDocTemplate(final IlvDocumentTemplate ilvDocumentTemplate)
    '''
def getDocumentTemplate():
    '''    public IlvDocumentTemplate getDocumentTemplate(final int n)
    public IlvDocumentTemplate getDocumentTemplate()
    '''
def getDocumentTemplatesCount():
    '''    public int getDocumentTemplatesCount()
    '''
def findDocTemplate():
    '''    public IlvDocumentTemplate findDocTemplate(final String anObject)
    '''
def getApplication():
    '''    public IlvApplication getApplication()
    '''
def readRegistries():
    '''    public void readRegistries()
    '''
def writeRegistries():
    '''    public void writeRegistries()
    '''
def getRecentFilesList():
    '''    public IlvRecentFileList getRecentFilesList()
    '''
def open():
    '''    public boolean open(final IlvRecentFileList.FileInfo fileInfo, final int n)
    '''
def getLocale():
    '''    public Locale getLocale()
    '''
def setApplication():
    '''    public void setApplication(final IlvApplication application)
    '''
def getMainWindow():
    '''    public IlvMainWindow getMainWindow()
    '''
def setMainWindow():
    '''    public void setMainWindow(final IlvMainWindow f)
    '''
def addOpenedDocument():
    '''    public void addOpenedDocument(final IlvDocument ilvDocument)
    public void addOpenedDocument(final IlvDocument ilvDocument)
    '''
def removeOpenDocument():
    '''    public boolean removeOpenDocument(final IlvDocument ilvDocument)
    public boolean removeOpenDocument(final IlvDocument ilvDocument)
    '''
def getOpenedDocuments():
    '''    public IlvDocument[] getOpenedDocuments(final IlvDocumentTemplate ilvDocumentTemplate)
    public IlvDocument[] getOpenedDocuments()
    '''
def getOpenedDocumentFromPath():
    '''    public IlvDocument getOpenedDocumentFromPath(final IlvFileDocumentTemplate ilvFileDocumentTemplate, final URL other)
    '''
def getApplicationListenerList():
    '''    public IlvApplicationListenerList getApplicationListenerList()
    '''
def setApplicationListenerList():
    '''    public void setApplicationListenerList(final IlvApplicationListenerList g)
    '''
def addApplicationListener():
    '''    public void addApplicationListener(final ApplicationListener applicationListener)
    '''
def removeApplicationListener():
    '''    public void removeApplicationListener(final ApplicationListener applicationListener)
    '''
def attachDocument():
    '''    public void attachDocument(final IlvDocument ilvDocument, final IlvDocument ilvDocument2)
    '''
def detachDocument():
    '''    public void detachDocument(final IlvDocument ilvDocument, final IlvDocument ilvDocument2)
    '''
def getActiveDocument():
    '''    public IlvDocument getActiveDocument(final boolean b)
    '''
def getActiveView():
    '''    public IlvDocumentView getActiveView(final boolean b)
    '''
def ShortName():
    '''    public static String ShortName(final Object o)
    '''
def setActiveDocument():
    '''    public void setActiveDocument(final IlvDocument ilvDocument, final IlvDocumentView ilvDocumentView, final boolean b)
    '''
def setActiveView():
    '''    public void setActiveView(final IlvDocumentView ilvDocumentView, final boolean b)
    '''
def getActiveDocTemplate():
    '''    public IlvDocumentTemplate getActiveDocTemplate()
    '''
def needSaving():
    '''    public boolean needSaving()
    '''
def getRecentFileList():
    '''    public IlvRecentFileList getRecentFileList()
    '''
def setRecentFileList():
    '''    public void setRecentFileList(final IlvRecentFileList c)
    '''
def getUntitledCount():
    '''    public int getUntitledCount()
    '''
def setUntitledCount():
    '''    public void setUntitledCount(final int d)
    '''
def FileChooserListener():
    '''    public FileChooserListener()
    '''
def getSelections():
    '''    public IlvFileChooserSelection[] getSelections()
    '''
