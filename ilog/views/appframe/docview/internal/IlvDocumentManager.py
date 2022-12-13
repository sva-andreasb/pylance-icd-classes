ACTIVE_DOCUMENT_NAME = "String  ActiveDocument""
SHOW_FILE_CHOOSER_ICONS_PROPERTY = "String  ShowFileChooserIcons""
def IlvDocumentManager():
'''public IlvDocumentManager()
'''
pass
def readSettings():
'''public void readSettings(final IlvSettingsElement ilvSettingsElement, final Object o)
public void readSettings(final IlvSettingsManager settings)
'''
pass
def writeSettings():
'''public void writeSettings(final IlvSettingsElement ilvSettingsElement, final Object o)
'''
pass
def propertyChange():
'''public void propertyChange(final PropertyChangeEvent propertyChangeEvent)
public void propertyChange(final PropertyChangeEvent propertyChangeEvent)
public void propertyChange(final PropertyChangeEvent propertyChangeEvent)
'''
pass
def isValidDocument():
'''public boolean isValidDocument(final URL url)
'''
pass
def openDocument():
'''public IlvDocument openDocument(final URL url, final boolean b, final boolean b2)
public IlvFileDocument openDocument(final IlvFileDocumentTemplate ilvFileDocumentTemplate, URL url, IlvFileFilter ilvFileFilter, final boolean b, final boolean b2)
public IlvDocument openDocument(final boolean b, final IlvMainWindow ilvMainWindow)
'''
pass
def initializeDocument():
'''public boolean initializeDocument(final IlvDocument ilvDocument, final Object o, final DocTemplateInfo docTemplateInfo)
public boolean initializeDocument(final IlvDocument ilvDocument, final Object o, final DocTemplateInfo docTemplateInfo)
'''
pass
def getOpenedDocument():
'''public IlvDocument getOpenedDocument(final URL url)
public IlvDocument getOpenedDocument(final int n)
'''
pass
def getOpenDocuments():
'''public IlvDocument[] getOpenDocuments()
public IlvDocument[] getOpenDocuments(final IlvDocumentTemplate ilvDocumentTemplate)
'''
pass
def openRecentFile():
'''public void openRecentFile(final int n)
'''
pass
def showFileChooser():
'''public IlvFileChooserSelection[] showFileChooser(final String s, final String s2, final int n, final IlvFileDocumentTemplate ilvFileDocumentTemplate, Component mainComponent)
'''
pass
def initializeFileChooser():
'''public void initializeFileChooser(final JFileChooser fileChooser, final String pathname, final int n, final IlvFileDocumentTemplate e)
'''
pass
def accept():
'''public boolean accept(final File file)
'''
pass
def getDescription():
'''public String getDescription()
public String getDescription(final File file)
'''
pass
def getName():
'''public String getName(final File file)
'''
pass
def isTraversable():
'''public Boolean isTraversable(final File file)
'''
pass
def getTypeDescription():
'''public String getTypeDescription(final File file)
'''
pass
def getIcon():
'''public Icon getIcon(final File file)
'''
pass
def showAppletFileChooser():
'''public IlvFileChooserSelection[] showAppletFileChooser(final String s, final String s2, final int n, final IlvFileDocumentTemplate ilvFileDocumentTemplate, final Component comp)
'''
pass
def findBestTemplate():
'''public IlvFileDocumentTemplate findBestTemplate(final URL url)
public IlvFileDocumentTemplate findBestTemplate(final String s)
'''
pass
def createHTMLBrowser():
'''public Window createHTMLBrowser(String string, final URL page, final HyperlinkListener listener, final boolean b, final Frame frame)
'''
pass
def hyperlinkUpdate():
'''public void hyperlinkUpdate(final HyperlinkEvent hyperlinkEvent)
public void hyperlinkUpdate(final HyperlinkEvent hyperlinkEvent)
'''
pass
def run():
'''public void run()
'''
pass
def mouseEntered():
'''public void mouseEntered(final MouseEvent mouseEvent)
'''
pass
def mouseExited():
'''public void mouseExited(final MouseEvent mouseEvent)
'''
pass
def mousePressed():
'''public void mousePressed(final MouseEvent mouseEvent)
'''
pass
def mouseReleased():
'''public void mouseReleased(final MouseEvent mouseEvent)
'''
pass
def actionPerformed():
'''public void actionPerformed(final ActionEvent actionEvent)
'''
pass
def newDocument():
'''public IlvDocument newDocument(final boolean b, final IlvDocumentTemplate ilvDocumentTemplate, final DocumentInitializer documentInitializer, final Object o)
public IlvDocument newDocument(final boolean b, final IlvMainWindow ilvMainWindow)
public IlvDocument newDocument(final IlvDocumentTemplate ilvDocumentTemplate, final boolean b, final Object o)
public IlvDocument newDocument(final Object o, final boolean b)
public final IlvDocument newDocument(final boolean b)
public final IlvDocument newDocument()
'''
pass
def getMainDocumentTemplates():
'''public IlvDocumentTemplate[] getMainDocumentTemplates(final boolean b)
'''
pass
def newDocumentOnLastTemplate():
'''public IlvDocument newDocumentOnLastTemplate(final boolean b, final IlvMainWindow ilvMainWindow)
'''
pass
def canCreateDocument():
'''public boolean canCreateDocument(final Object o)
'''
pass
def findDocumentTemplate():
'''public IlvDocumentTemplate findDocumentTemplate(final Object o)
'''
pass
def saveAllDocuments():
'''public boolean saveAllDocuments()
public boolean saveAllDocuments()
'''
pass
def saveAllDocumentsUI():
'''public void saveAllDocumentsUI(final Action action)
'''
pass
def saveDocument():
'''public boolean saveDocument(final IlvDocument ilvDocument)
'''
pass
def saveFileDocument():
'''public boolean saveFileDocument(final IlvFileDocument ilvFileDocument, final String s, IlvFileFilter ilvFileFilter, final boolean b)
'''
pass
def saveAsDocument():
'''public boolean saveAsDocument(final IlvFileDocument ilvFileDocument)
'''
pass
def saveDocumentModifications():
'''public boolean saveDocumentModifications(final IlvDocument ilvDocument)
'''
pass
def isEditable():
'''public boolean isEditable(final IlvDocument ilvDocument)
'''
pass
def isSaveable():
'''public boolean isSaveable(final IlvDocument ilvDocument)
'''
pass
def closeAllDocuments():
'''public boolean closeAllDocuments(final boolean b)
'''
pass
def closeAllDocumentsUI():
'''public boolean closeAllDocumentsUI(final Action action)
'''
pass
def closeDocument():
'''public boolean closeDocument(final IlvDocument ilvDocument, final boolean b)
'''
pass
def saveModifications():
'''public boolean saveModifications()
'''
pass
def getOpenedDocumentCount():
'''public int getOpenedDocumentCount()
public int getOpenedDocumentCount()
'''
pass
def addToRecentFileList():
'''public void addToRecentFileList(final URL url)
'''
pass
def addDocumentTemplate():
'''public void addDocumentTemplate(final IlvDocumentTemplate ilvDocumentTemplate)
'''
pass
def removeDocumentTemplate():
'''public boolean removeDocumentTemplate(final IlvDocumentTemplate ilvDocumentTemplate)
'''
pass
def removeDocTemplate():
'''public boolean removeDocTemplate(final IlvDocumentTemplate ilvDocumentTemplate)
'''
pass
def getDocumentTemplate():
'''public IlvDocumentTemplate getDocumentTemplate(final int n)
public IlvDocumentTemplate getDocumentTemplate()
'''
pass
def getDocumentTemplatesCount():
'''public int getDocumentTemplatesCount()
'''
pass
def findDocTemplate():
'''public IlvDocumentTemplate findDocTemplate(final String anObject)
'''
pass
def getApplication():
'''public IlvApplication getApplication()
'''
pass
def readRegistries():
'''public void readRegistries()
'''
pass
def writeRegistries():
'''public void writeRegistries()
'''
pass
def getRecentFilesList():
'''public IlvRecentFileList getRecentFilesList()
'''
pass
def open():
'''public boolean open(final IlvRecentFileList.FileInfo fileInfo, final int n)
'''
pass
def getLocale():
'''public Locale getLocale()
'''
pass
def setApplication():
'''public void setApplication(final IlvApplication application)
'''
pass
def getMainWindow():
'''public IlvMainWindow getMainWindow()
'''
pass
def setMainWindow():
'''public void setMainWindow(final IlvMainWindow f)
'''
pass
def addOpenedDocument():
'''public void addOpenedDocument(final IlvDocument ilvDocument)
public void addOpenedDocument(final IlvDocument ilvDocument)
'''
pass
def removeOpenDocument():
'''public boolean removeOpenDocument(final IlvDocument ilvDocument)
public boolean removeOpenDocument(final IlvDocument ilvDocument)
'''
pass
def getOpenedDocuments():
'''public IlvDocument[] getOpenedDocuments(final IlvDocumentTemplate ilvDocumentTemplate)
public IlvDocument[] getOpenedDocuments()
'''
pass
def getOpenedDocumentFromPath():
'''public IlvDocument getOpenedDocumentFromPath(final IlvFileDocumentTemplate ilvFileDocumentTemplate, final URL other)
'''
pass
def getApplicationListenerList():
'''public IlvApplicationListenerList getApplicationListenerList()
'''
pass
def setApplicationListenerList():
'''public void setApplicationListenerList(final IlvApplicationListenerList g)
'''
pass
def addApplicationListener():
'''public void addApplicationListener(final ApplicationListener applicationListener)
'''
pass
def removeApplicationListener():
'''public void removeApplicationListener(final ApplicationListener applicationListener)
'''
pass
def attachDocument():
'''public void attachDocument(final IlvDocument ilvDocument, final IlvDocument ilvDocument2)
'''
pass
def detachDocument():
'''public void detachDocument(final IlvDocument ilvDocument, final IlvDocument ilvDocument2)
'''
pass
def getActiveDocument():
'''public IlvDocument getActiveDocument(final boolean b)
'''
pass
def getActiveView():
'''public IlvDocumentView getActiveView(final boolean b)
'''
pass
def ShortName():
'''public static String ShortName(final Object o)
'''
pass
def setActiveDocument():
'''public void setActiveDocument(final IlvDocument ilvDocument, final IlvDocumentView ilvDocumentView, final boolean b)
'''
pass
def setActiveView():
'''public void setActiveView(final IlvDocumentView ilvDocumentView, final boolean b)
'''
pass
def getActiveDocTemplate():
'''public IlvDocumentTemplate getActiveDocTemplate()
'''
pass
def needSaving():
'''public boolean needSaving()
'''
pass
def getRecentFileList():
'''public IlvRecentFileList getRecentFileList()
'''
pass
def setRecentFileList():
'''public void setRecentFileList(final IlvRecentFileList c)
'''
pass
def getUntitledCount():
'''public int getUntitledCount()
'''
pass
def setUntitledCount():
'''public void setUntitledCount(final int d)
'''
pass
def FileChooserListener():
'''public FileChooserListener()
'''
pass
def getSelections():
'''public IlvFileChooserSelection[] getSelections()
'''
pass
