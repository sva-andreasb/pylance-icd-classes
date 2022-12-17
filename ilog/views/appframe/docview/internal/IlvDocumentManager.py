ACTIVE_DOCUMENT_NAME = "String  \"ActiveDocument\""
SHOW_FILE_CHOOSER_ICONS_PROPERTY = "String  \"ShowFileChooserIcons\""
def ():
    '''returns FileChooserListener\n\n
    ()\n
    ()\n
    '''
def readSettings():
    '''returns None\n\n
    readSettings(final IlvSettingsElement ilvSettingsElement, final Object o)\n
    readSettings(final IlvSettingsManager settings)\n
    '''
def writeSettings():
    '''returns None\n\n
    writeSettings(final IlvSettingsElement ilvSettingsElement, final Object o)\n
    '''
def propertyChange():
    '''returns None\n\n
    propertyChange(final PropertyChangeEvent propertyChangeEvent)\n
    propertyChange(final PropertyChangeEvent propertyChangeEvent)\n
    propertyChange(final PropertyChangeEvent propertyChangeEvent)\n
    '''
def isValidDocument():
    '''returns boolean\n\n
    isValidDocument(final URL url)\n
    '''
def openDocument():
    '''returns IlvDocument\n\n
    openDocument(final URL url, final boolean b, final boolean b2)\n
    openDocument(final IlvFileDocumentTemplate ilvFileDocumentTemplate, URL url, IlvFileFilter ilvFileFilter, final boolean b, final boolean b2)\n
    openDocument(final boolean b, final IlvMainWindow ilvMainWindow)\n
    '''
def initializeDocument():
    '''returns boolean\n\n
    initializeDocument(final IlvDocument ilvDocument, final Object o, final DocTemplateInfo docTemplateInfo)\n
    initializeDocument(final IlvDocument ilvDocument, final Object o, final DocTemplateInfo docTemplateInfo)\n
    '''
def getOpenedDocument():
    '''returns IlvDocument\n\n
    getOpenedDocument(final URL url)\n
    getOpenedDocument(final int n)\n
    '''
def getOpenDocuments():
    '''returns IlvDocument[]\n\n
    getOpenDocuments()\n
    getOpenDocuments(final IlvDocumentTemplate ilvDocumentTemplate)\n
    '''
def openRecentFile():
    '''returns None\n\n
    openRecentFile(final int n)\n
    '''
def showFileChooser():
    '''returns IlvFileChooserSelection[]\n\n
    showFileChooser(final String s, final String s2, final int n, final IlvFileDocumentTemplate ilvFileDocumentTemplate, Component mainComponent)\n
    '''
def initializeFileChooser():
    '''returns None\n\n
    initializeFileChooser(final JFileChooser fileChooser, final String pathname, final int n, final IlvFileDocumentTemplate e)\n
    '''
def accept():
    '''returns boolean\n\n
    accept(final File file)\n
    '''
def getDescription():
    '''returns String\n\n
    getDescription()\n
    getDescription(final File file)\n
    '''
def getName():
    '''returns String\n\n
    getName(final File file)\n
    '''
def isTraversable():
    '''returns Boolean\n\n
    isTraversable(final File file)\n
    '''
def getTypeDescription():
    '''returns String\n\n
    getTypeDescription(final File file)\n
    '''
def getIcon():
    '''returns Icon\n\n
    getIcon(final File file)\n
    '''
def showAppletFileChooser():
    '''returns IlvFileChooserSelection[]\n\n
    showAppletFileChooser(final String s, final String s2, final int n, final IlvFileDocumentTemplate ilvFileDocumentTemplate, final Component comp)\n
    '''
def findBestTemplate():
    '''returns IlvFileDocumentTemplate\n\n
    findBestTemplate(final URL url)\n
    findBestTemplate(final String s)\n
    '''
def createHTMLBrowser():
    '''returns Window\n\n
    createHTMLBrowser(String string, final URL page, final HyperlinkListener listener, final boolean b, final Frame frame)\n
    '''
def hyperlinkUpdate():
    '''returns None\n\n
    hyperlinkUpdate(final HyperlinkEvent hyperlinkEvent)\n
    hyperlinkUpdate(final HyperlinkEvent hyperlinkEvent)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
def mouseEntered():
    '''returns None\n\n
    mouseEntered(final MouseEvent mouseEvent)\n
    '''
def mouseExited():
    '''returns None\n\n
    mouseExited(final MouseEvent mouseEvent)\n
    '''
def mousePressed():
    '''returns None\n\n
    mousePressed(final MouseEvent mouseEvent)\n
    '''
def mouseReleased():
    '''returns None\n\n
    mouseReleased(final MouseEvent mouseEvent)\n
    '''
def actionPerformed():
    '''returns None\n\n
    actionPerformed(final ActionEvent actionEvent)\n
    '''
def newDocument():
    '''returns IlvDocument\n\n
    newDocument(final boolean b, final IlvDocumentTemplate ilvDocumentTemplate, final DocumentInitializer documentInitializer, final Object o)\n
    newDocument(final boolean b, final IlvMainWindow ilvMainWindow)\n
    newDocument(final IlvDocumentTemplate ilvDocumentTemplate, final boolean b, final Object o)\n
    newDocument(final Object o, final boolean b)\n
    '''
def getMainDocumentTemplates():
    '''returns IlvDocumentTemplate[]\n\n
    getMainDocumentTemplates(final boolean b)\n
    '''
def newDocumentOnLastTemplate():
    '''returns IlvDocument\n\n
    newDocumentOnLastTemplate(final boolean b, final IlvMainWindow ilvMainWindow)\n
    '''
def canCreateDocument():
    '''returns boolean\n\n
    canCreateDocument(final Object o)\n
    '''
def findDocumentTemplate():
    '''returns IlvDocumentTemplate\n\n
    findDocumentTemplate(final Object o)\n
    '''
def saveAllDocuments():
    '''returns boolean\n\n
    saveAllDocuments()\n
    saveAllDocuments()\n
    '''
def saveAllDocumentsUI():
    '''returns None\n\n
    saveAllDocumentsUI(final Action action)\n
    '''
def saveDocument():
    '''returns boolean\n\n
    saveDocument(final IlvDocument ilvDocument)\n
    '''
def saveFileDocument():
    '''returns boolean\n\n
    saveFileDocument(final IlvFileDocument ilvFileDocument, final String s, IlvFileFilter ilvFileFilter, final boolean b)\n
    '''
def saveAsDocument():
    '''returns boolean\n\n
    saveAsDocument(final IlvFileDocument ilvFileDocument)\n
    '''
def saveDocumentModifications():
    '''returns boolean\n\n
    saveDocumentModifications(final IlvDocument ilvDocument)\n
    '''
def isEditable():
    '''returns boolean\n\n
    isEditable(final IlvDocument ilvDocument)\n
    '''
def isSaveable():
    '''returns boolean\n\n
    isSaveable(final IlvDocument ilvDocument)\n
    '''
def closeAllDocuments():
    '''returns boolean\n\n
    closeAllDocuments(final boolean b)\n
    '''
def closeAllDocumentsUI():
    '''returns boolean\n\n
    closeAllDocumentsUI(final Action action)\n
    '''
def closeDocument():
    '''returns boolean\n\n
    closeDocument(final IlvDocument ilvDocument, final boolean b)\n
    '''
def saveModifications():
    '''returns boolean\n\n
    saveModifications()\n
    '''
def getOpenedDocumentCount():
    '''returns int\n\n
    getOpenedDocumentCount()\n
    getOpenedDocumentCount()\n
    '''
def addToRecentFileList():
    '''returns None\n\n
    addToRecentFileList(final URL url)\n
    '''
def addDocumentTemplate():
    '''returns None\n\n
    addDocumentTemplate(final IlvDocumentTemplate ilvDocumentTemplate)\n
    '''
def removeDocumentTemplate():
    '''returns boolean\n\n
    removeDocumentTemplate(final IlvDocumentTemplate ilvDocumentTemplate)\n
    '''
def removeDocTemplate():
    '''returns boolean\n\n
    removeDocTemplate(final IlvDocumentTemplate ilvDocumentTemplate)\n
    '''
def getDocumentTemplate():
    '''returns IlvDocumentTemplate\n\n
    getDocumentTemplate(final int n)\n
    getDocumentTemplate()\n
    '''
def getDocumentTemplatesCount():
    '''returns int\n\n
    getDocumentTemplatesCount()\n
    '''
def findDocTemplate():
    '''returns IlvDocumentTemplate\n\n
    findDocTemplate(final String anObject)\n
    '''
def getApplication():
    '''returns IlvApplication\n\n
    getApplication()\n
    '''
def readRegistries():
    '''returns None\n\n
    readRegistries()\n
    '''
def writeRegistries():
    '''returns None\n\n
    writeRegistries()\n
    '''
def getRecentFilesList():
    '''returns IlvRecentFileList\n\n
    getRecentFilesList()\n
    '''
def open():
    '''returns boolean\n\n
    open(final IlvRecentFileList.FileInfo fileInfo, final int n)\n
    '''
def getLocale():
    '''returns Locale\n\n
    getLocale()\n
    '''
def setApplication():
    '''returns None\n\n
    setApplication(final IlvApplication application)\n
    '''
def getMainWindow():
    '''returns IlvMainWindow\n\n
    getMainWindow()\n
    '''
def setMainWindow():
    '''returns None\n\n
    setMainWindow(final IlvMainWindow f)\n
    '''
def addOpenedDocument():
    '''returns None\n\n
    addOpenedDocument(final IlvDocument ilvDocument)\n
    addOpenedDocument(final IlvDocument ilvDocument)\n
    '''
def removeOpenDocument():
    '''returns boolean\n\n
    removeOpenDocument(final IlvDocument ilvDocument)\n
    removeOpenDocument(final IlvDocument ilvDocument)\n
    '''
def getOpenedDocuments():
    '''returns IlvDocument[]\n\n
    getOpenedDocuments(final IlvDocumentTemplate ilvDocumentTemplate)\n
    getOpenedDocuments()\n
    '''
def getOpenedDocumentFromPath():
    '''returns IlvDocument\n\n
    getOpenedDocumentFromPath(final IlvFileDocumentTemplate ilvFileDocumentTemplate, final URL other)\n
    '''
def getApplicationListenerList():
    '''returns IlvApplicationListenerList\n\n
    getApplicationListenerList()\n
    '''
def setApplicationListenerList():
    '''returns None\n\n
    setApplicationListenerList(final IlvApplicationListenerList g)\n
    '''
def addApplicationListener():
    '''returns None\n\n
    addApplicationListener(final ApplicationListener applicationListener)\n
    '''
def removeApplicationListener():
    '''returns None\n\n
    removeApplicationListener(final ApplicationListener applicationListener)\n
    '''
def attachDocument():
    '''returns None\n\n
    attachDocument(final IlvDocument ilvDocument, final IlvDocument ilvDocument2)\n
    '''
def detachDocument():
    '''returns None\n\n
    detachDocument(final IlvDocument ilvDocument, final IlvDocument ilvDocument2)\n
    '''
def getActiveDocument():
    '''returns IlvDocument\n\n
    getActiveDocument(final boolean b)\n
    '''
def getActiveView():
    '''returns IlvDocumentView\n\n
    getActiveView(final boolean b)\n
    '''
def setActiveDocument():
    '''returns None\n\n
    setActiveDocument(final IlvDocument ilvDocument, final IlvDocumentView ilvDocumentView, final boolean b)\n
    '''
def setActiveView():
    '''returns None\n\n
    setActiveView(final IlvDocumentView ilvDocumentView, final boolean b)\n
    '''
def getActiveDocTemplate():
    '''returns IlvDocumentTemplate\n\n
    getActiveDocTemplate()\n
    '''
def needSaving():
    '''returns boolean\n\n
    needSaving()\n
    '''
def getRecentFileList():
    '''returns IlvRecentFileList\n\n
    getRecentFileList()\n
    '''
def setRecentFileList():
    '''returns None\n\n
    setRecentFileList(final IlvRecentFileList c)\n
    '''
def getUntitledCount():
    '''returns int\n\n
    getUntitledCount()\n
    '''
def setUntitledCount():
    '''returns None\n\n
    setUntitledCount(final int d)\n
    '''
def getSelections():
    '''returns IlvFileChooserSelection[]\n\n
    getSelections()\n
    '''
