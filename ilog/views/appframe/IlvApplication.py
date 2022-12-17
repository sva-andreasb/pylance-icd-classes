CLOSE_ALL_DOCUMENTS_CMD = "String  \"CloseAllDocuments\""
CLOSE_DOCUMENT_CMD = "String  \"CloseDocument\""
OPEN_DOCUMENT_CMD = "String  \"OpenDocument\""
NEW_DOCUMENT_CMD = "String  \"NewDocument\""
NEW_DOCUMENT_ON_LAST_TEMPLATE_CMD = "String  \"NewDocumentOnLastChoice\""
SAVE_ALL_DOCUMENTS_CMD = "String  \"SaveAllDocuments\""
SAVE_DOCUMENT_CMD = "String  \"SaveDocument\""
SAVE_AS_DOCUMENT_CMD = "String  \"SaveAsDocument\""
REVERT_DOCUMENT_CMD = "String  \"RevertDocument\""
EXIT_CMD = "String  \"Exit\""
OPEN_MULTIPLE_FILES = "int  1"
OPEN_FILE_MUST_EXIST = "int  2"
OPEN_MODE = "int  8"
SAVE_MODE = "int  16"
SAVE_AS_MODE = "int  32"
TITLE_PROPERTY = "String  \"Title\""
ICON_PROPERTY = "String  \"Icon\""
STATUS_MESSAGE = "String  \"MainStatusMessage\""
STATUS_BAR_PROPERTY = "String  \"StatusBar\""
MENU_BAR_PROPERTY = "String  \"MenuBar\""
MAIN_WINDOW_PROPERTY = "String  \"MainWindow\""
SETTINGS_TYPE = "String  \"application\""
def ():
    '''returns SessionSettingsManager\n\n
    ()\n
    (final String name)\n
    (final String[] array)\n
    (final String name, final String[] array)\n
    ()\n
    (final IlvApplication a)\n
    (final String s)\n
    '''
def settingsInitialized():
    '''returns None\n\n
    settingsInitialized(final IlvSettings ilvSettings)\n
    '''
def settingsModified():
    '''returns None\n\n
    settingsModified(final IlvSettings ilvSettings)\n
    '''
def settingsAdded():
    '''returns None\n\n
    settingsAdded(final IlvSettings ilvSettings)\n
    '''
def settingsRemoved():
    '''returns None\n\n
    settingsRemoved(final IlvSettings ilvSettings)\n
    '''
def saveChanges():
    '''returns None\n\n
    saveChanges(final IlvSettings ilvSettings)\n
    '''
def propertyChange():
    '''returns None\n\n
    propertyChange(final PropertyChangeEvent propertyChangeEvent)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    run()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    getName()\n
    '''
def setName():
    '''returns None\n\n
    setName(final String s)\n
    '''
def setTitle():
    '''returns None\n\n
    setTitle(final String s)\n
    '''
def getTitle():
    '''returns String\n\n
    getTitle()\n
    '''
def setImageIcon():
    '''returns None\n\n
    setImageIcon(final ImageIcon imageIcon)\n
    '''
def getImageIcon():
    '''returns ImageIcon\n\n
    getImageIcon()\n
    getImageIcon(final String s)\n
    '''
def sendActionEvent():
    '''returns None\n\n
    sendActionEvent(final ActionEvent actionEvent)\n
    sendActionEvent(final String command)\n
    '''
def sendMessage():
    '''returns None\n\n
    sendMessage(final String s, final Object o, final String s2, final Object[] array)\n
    sendMessage(final String s, final MessageEvent messageEvent)\n
    '''
def addMessageListener():
    '''returns None\n\n
    addMessageListener(final MessageListener messageListener, final String s)\n
    '''
def removeMessageListener():
    '''returns None\n\n
    removeMessageListener(final MessageListener messageListener)\n
    '''
def addActionHandler():
    '''returns None\n\n
    addActionHandler(final ActionHandler actionHandler)\n
    '''
def getActionHandlers():
    '''returns ActionHandler[]\n\n
    getActionHandlers(final String s)\n
    '''
def removeActionHandler():
    '''returns None\n\n
    removeActionHandler(final ActionHandler actionHandler)\n
    '''
def getAction():
    '''returns Action\n\n
    getAction(final String s)\n
    '''
def addAction():
    '''returns None\n\n
    addAction(final Action action)\n
    '''
def removeAction():
    '''returns None\n\n
    removeAction(final Action action)\n
    '''
def initialize():
    '''returns boolean\n\n
    initialize()\n
    '''
def isInitialized():
    '''returns boolean\n\n
    isInitialized()\n
    '''
def close():
    '''returns boolean\n\n
    close(final boolean b)\n
    '''
def addSettings():
    '''returns boolean\n\n
    addSettings(final IlvSettings ilvSettings)\n
    addSettings(final IlvSettings ilvSettings, final String s)\n
    '''
def addXMLSettings():
    '''returns IlvXMLSettings\n\n
    addXMLSettings(final String s)\n
    addXMLSettings(final URL url)\n
    '''
def removeSettings():
    '''returns boolean\n\n
    removeSettings(final IlvSettings ilvSettings)\n
    removeSettings(final IlvSettings ilvSettings)\n
    '''
def getSettings():
    '''returns IlvSettings[]\n\n
    getSettings(final String s)\n
    getSettings()\n
    '''
def addSettingsListener():
    '''returns None\n\n
    addSettingsListener(final SettingsListener settingsListener)\n
    '''
def removeSettingsListener():
    '''returns boolean\n\n
    removeSettingsListener(final SettingsListener settingsListener)\n
    '''
def getSettingsManager():
    '''returns IlvSettingsManager\n\n
    getSettingsManager()\n
    '''
def selectElement():
    '''returns IlvSettingsElement\n\n
    selectElement(final IlvSettingsQuery ilvSettingsQuery)\n
    selectElement(final String s, final String s2, final Object o)\n
    '''
def select():
    '''returns IlvSettingsElement[]\n\n
    select(final IlvSettingsQuery ilvSettingsQuery)\n
    select(final String s, final IlvSettingsElement[] relativeElementList)\n
    select(final IlvSettingsQuery ilvSettingsQuery, final IlvSettingsElement[] relativeElementList)\n
    '''
def commitSettingsChanges():
    '''returns None\n\n
    commitSettingsChanges()\n
    '''
def addLocaleSettingsListener():
    '''returns None\n\n
    addLocaleSettingsListener(final LocaleSettingsListener e)\n
    '''
def removeLocaleSettingsListener():
    '''returns boolean\n\n
    removeLocaleSettingsListener(final LocaleSettingsListener o)\n
    '''
def setMainWindow():
    '''returns None\n\n
    setMainWindow(final IlvMainWindow mainWindow)\n
    '''
def windowOpened():
    '''returns None\n\n
    windowOpened(final WindowEvent windowEvent)\n
    '''
def getMainComponent():
    '''returns Component\n\n
    getMainComponent()\n
    '''
def getMainWindow():
    '''returns IlvMainWindow\n\n
    getMainWindow()\n
    '''
def getMainContainer():
    '''returns Container\n\n
    getMainContainer()\n
    '''
def isApplet():
    '''returns boolean\n\n
    isApplet()\n
    '''
def getApplet():
    '''returns Applet\n\n
    getApplet()\n
    '''
def readApplicationSettings():
    '''returns None\n\n
    readApplicationSettings()\n
    '''
def getDocumentTemplateCount():
    '''returns int\n\n
    getDocumentTemplateCount()\n
    '''
def getDocumentTemplate():
    '''returns IlvDocumentTemplate\n\n
    getDocumentTemplate(final int n)\n
    getDocumentTemplate(final String anObject)\n
    '''
def addDocumentTemplate():
    '''returns None\n\n
    addDocumentTemplate(final IlvDocumentTemplate ilvDocumentTemplate)\n
    '''
def removeDocumentTemplate():
    '''returns boolean\n\n
    removeDocumentTemplate(final IlvDocumentTemplate ilvDocumentTemplate)\n
    '''
def openDocument():
    '''returns IlvDocument\n\n
    openDocument()\n
    openDocument(final IlvFileDocumentTemplate ilvFileDocumentTemplate)\n
    '''
def openDocumentFile():
    '''returns IlvDocument\n\n
    openDocumentFile(final String pathname, final boolean b, final boolean b2)\n
    '''
def isValidDocumentFile():
    '''returns boolean\n\n
    isValidDocumentFile(final String pathname)\n
    '''
def initializeFileChooser():
    '''returns None\n\n
    initializeFileChooser(final JFileChooser fileChooser, final String s, final int n, final IlvFileDocumentTemplate ilvFileDocumentTemplate)\n
    '''
def showFileChooser():
    '''returns IlvFileChooserSelection[]\n\n
    showFileChooser(final String s, final String s2, final int n, final IlvFileDocumentTemplate ilvFileDocumentTemplate, final Component component)\n
    '''
def newDocument():
    '''returns IlvDocument\n\n
    newDocument()\n
    newDocument(final IlvDocumentTemplate ilvDocumentTemplate, final boolean b, final Object o)\n
    newDocument(final Object o, final boolean b)\n
    '''
def newDocumentOnLastTemplate():
    '''returns IlvDocument\n\n
    newDocumentOnLastTemplate()\n
    '''
def canCreateDocument():
    '''returns boolean\n\n
    canCreateDocument(final Object o)\n
    '''
def saveAllDocuments():
    '''returns boolean\n\n
    saveAllDocuments()\n
    '''
def closeAllDocuments():
    '''returns boolean\n\n
    closeAllDocuments(final boolean b)\n
    '''
def closeActiveDocument():
    '''returns boolean\n\n
    closeActiveDocument(final boolean b)\n
    '''
def closeDocument():
    '''returns boolean\n\n
    closeDocument(final IlvDocument ilvDocument, final boolean b)\n
    '''
def saveActiveDocument():
    '''returns boolean\n\n
    saveActiveDocument(final boolean b)\n
    '''
def saveDocument():
    '''returns boolean\n\n
    saveDocument(final String spec)\n
    saveDocument(final IlvDocument ilvDocument)\n
    '''
def saveDocumentModifications():
    '''returns boolean\n\n
    saveDocumentModifications(final IlvDocument ilvDocument)\n
    '''
def saveAsActiveDocument():
    '''returns boolean\n\n
    saveAsActiveDocument(final boolean b)\n
    '''
def findDocument():
    '''returns IlvDocument\n\n
    findDocument(final String spec)\n
    '''
def getOpenedDocumentCount():
    '''returns int\n\n
    getOpenedDocumentCount()\n
    '''
def getOpenDocuments():
    '''returns IlvDocument[]\n\n
    getOpenDocuments()\n
    getOpenDocuments(final IlvDocumentTemplate ilvDocumentTemplate)\n
    '''
def openRecentOpenedFile():
    '''returns IlvDocument\n\n
    openRecentOpenedFile(final int n)\n
    '''
def getRecentOpenedFile():
    '''returns String\n\n
    getRecentOpenedFile(final int n)\n
    '''
def getRecentOpenedFileCount():
    '''returns int\n\n
    getRecentOpenedFileCount()\n
    '''
def getRecentFileList():
    '''returns IlvRecentFileList\n\n
    getRecentFileList()\n
    '''
def getActiveDocument():
    '''returns IlvDocument\n\n
    getActiveDocument(final boolean b)\n
    '''
def setActiveDocument():
    '''returns None\n\n
    setActiveDocument(final IlvDocument ilvDocument, final IlvDocumentView ilvDocumentView, final boolean b)\n
    '''
def setActiveView():
    '''returns None\n\n
    setActiveView(final IlvDocumentView ilvDocumentView, final boolean b)\n
    '''
def getActiveView():
    '''returns IlvDocumentView\n\n
    getActiveView(final boolean b)\n
    '''
def getActiveViewContainer():
    '''returns IlvViewContainer\n\n
    getActiveViewContainer()\n
    '''
def addApplicationListener():
    '''returns None\n\n
    addApplicationListener(final ApplicationListener applicationListener)\n
    addApplicationListener(final String s, final ApplicationListener applicationListener)\n
    '''
def removeApplicationListener():
    '''returns None\n\n
    removeApplicationListener(final ApplicationListener applicationListener)\n
    removeApplicationListener(final String s, final ApplicationListener applicationListener)\n
    '''
def attachDocument():
    '''returns None\n\n
    attachDocument(final IlvDocument ilvDocument, final IlvDocument ilvDocument2)\n
    '''
def detachDocument():
    '''returns None\n\n
    detachDocument(final IlvDocument ilvDocument, final IlvDocument ilvDocument2)\n
    '''
def updateAction():
    '''returns boolean\n\n
    updateAction(final String s)\n
    updateAction(final Action action)\n
    updateAction(final Action action)\n
    '''
def updateActions():
    '''returns None\n\n
    updateActions()\n
    '''
def updateActionsByCategory():
    '''returns None\n\n
    updateActionsByCategory(final String s)\n
    '''
def getClassLoader():
    '''returns ClassLoader\n\n
    getClassLoader()\n
    '''
def findResource():
    '''returns URL\n\n
    findResource(final String s)\n
    '''
def getResource():
    '''returns URL\n\n
    getResource(final String s)\n
    '''
def loadClass():
    '''returns Class\n\n
    loadClass(final String s)\n
    '''
def addClassLoader():
    '''returns None\n\n
    addClassLoader(final ClassLoader e)\n
    '''
def removeClassLoader():
    '''returns boolean\n\n
    removeClassLoader(final ClassLoader o)\n
    '''
def getClassForName():
    '''returns Class\n\n
    getClassForName(final String s)\n
    '''
def setLocale():
    '''returns None\n\n
    setLocale(final Locale locale)\n
    '''
def getLocale():
    '''returns Locale\n\n
    getLocale()\n
    '''
def getResourceBundleManager():
    '''returns IlvResourceBundleManager\n\n
    getResourceBundleManager()\n
    '''
def setResourceBundleManager():
    '''returns None\n\n
    setResourceBundleManager(final IlvResourceBundleManager ilvResourceBundleManager)\n
    '''
def addResourcePropertyFile():
    '''returns ResourceBundle\n\n
    addResourcePropertyFile(final String s)\n
    '''
def removeResourcePropertyFile():
    '''returns ResourceBundle\n\n
    removeResourcePropertyFile(final String s)\n
    '''
def addResourceBundle():
    '''returns None\n\n
    addResourceBundle(final ResourceBundle resourceBundle)\n
    '''
def getString():
    '''returns String\n\n
    getString(final String key)\n
    '''
def getFormattedString():
    '''returns String\n\n
    getFormattedString(final String s, final Object[] array)\n
    '''
def getComponentOrientation():
    '''returns ComponentOrientation\n\n
    getComponentOrientation()\n
    '''
def applyCursor():
    '''returns HashMap\n\n
    applyCursor(final Cursor cursor)\n
    '''
def restoreCursor():
    '''returns None\n\n
    restoreCursor(final HashMap hashMap)\n
    restoreCursor()\n
    '''
def setCursor():
    '''returns None\n\n
    setCursor(final Cursor cursor)\n
    '''
def getUserSettingsURL():
    '''returns URL\n\n
    getUserSettingsURL()\n
    '''
def setUserSettingsURL():
    '''returns None\n\n
    setUserSettingsURL(final URL userSettingsURL)\n
    '''
def getUserHomeDirectory():
    '''returns URL\n\n
    getUserHomeDirectory()\n
    '''
def setUserHomeDirectory():
    '''returns None\n\n
    setUserHomeDirectory(final URL userHomeDirectory)\n
    '''
def getSoftwareProvider():
    '''returns String\n\n
    getSoftwareProvider()\n
    '''
def setSoftwareProvider():
    '''returns None\n\n
    setSoftwareProvider(final String softwareProvider)\n
    '''
def getUserSettingsSubDirectory():
    '''returns String\n\n
    getUserSettingsSubDirectory()\n
    '''
def setUserSettingsSubDirectory():
    '''returns None\n\n
    setUserSettingsSubDirectory(final String userSettingsSubDirectory)\n
    '''
def resolveURL():
    '''returns URL\n\n
    resolveURL(final String s)\n
    '''
def getAbbreviateForm():
    '''returns String\n\n
    getAbbreviateForm(final URL url)\n
    '''
def addURLResolver():
    '''returns None\n\n
    addURLResolver(final IlvURLResolver ilvURLResolver)\n
    '''
def removeURLResolver():
    '''returns boolean\n\n
    removeURLResolver(final IlvURLResolver ilvURLResolver)\n
    '''
def getURLResolverManager():
    '''returns IlvURLResolverManager\n\n
    getURLResolverManager()\n
    '''
def getDocumentBase():
    '''returns URL\n\n
    getDocumentBase()\n
    '''
def setDocumentBase():
    '''returns None\n\n
    setDocumentBase(final URL documentBase)\n
    '''
def setProperty():
    '''returns Object\n\n
    setProperty(final String s, final Object o)\n
    '''
def getProperty():
    '''returns Object\n\n
    getProperty(final String s)\n
    '''
def addPropertyChangeListener():
    '''returns None\n\n
    addPropertyChangeListener(final PropertyChangeListener propertyChangeListener)\n
    '''
def removePropertyChangeListener():
    '''returns None\n\n
    removePropertyChangeListener(final PropertyChangeListener propertyChangeListener)\n
    '''
def setSplashWindow():
    '''returns None\n\n
    setSplashWindow(final IlvSplashWindow r)\n
    '''
def getSplashWindow():
    '''returns IlvSplashWindow\n\n
    getSplashWindow()\n
    '''
def installObject():
    '''returns boolean\n\n
    installObject(final Object o, final IlvSettingsElement ilvSettingsElement, final IlvApplication ilvApplication)\n
    '''
def uninstallObject():
    '''returns boolean\n\n
    uninstallObject(final Object o, final IlvSettingsElement ilvSettingsElement, final IlvApplication ilvApplication)\n
    '''
def actionPerformed():
    '''returns None\n\n
    actionPerformed(final ActionEvent actionEvent)\n
    '''
def isProcessingAction():
    '''returns boolean\n\n
    isProcessingAction(final String s)\n
    '''
def initializeSettings():
    '''returns boolean\n\n
    initializeSettings()\n
    initializeSettings()\n
    '''
def areSettingsInitialized():
    '''returns boolean\n\n
    areSettingsInitialized()\n
    '''
def setModel():
    '''returns None\n\n
    setModel(final IlvSettingsModel a)\n
    '''
def commit():
    '''returns None\n\n
    commit()\n
    '''
def getWritableSettings():
    '''returns IlvSettings\n\n
    getWritableSettings()\n
    '''
def mainWindowIntialized():
    '''returns None\n\n
    mainWindowIntialized(final IlvMainWindow ilvMainWindow)\n
    '''
