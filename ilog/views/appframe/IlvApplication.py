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
def IlvApplication():
    '''    public IlvApplication()
    public IlvApplication(final String name)
    public IlvApplication(final String[] array)
    public IlvApplication(final String name, final String[] array)
    '''
def settingsInitialized():
    '''    public void settingsInitialized(final IlvSettings ilvSettings)
    '''
def settingsModified():
    '''    public void settingsModified(final IlvSettings ilvSettings)
    '''
def settingsAdded():
    '''    public void settingsAdded(final IlvSettings ilvSettings)
    '''
def settingsRemoved():
    '''    public void settingsRemoved(final IlvSettings ilvSettings)
    '''
def saveChanges():
    '''    public void saveChanges(final IlvSettings ilvSettings)
    '''
def propertyChange():
    '''    public void propertyChange(final PropertyChangeEvent propertyChangeEvent)
    '''
def run():
    '''    public void run()
    public void run()
    '''
def getName():
    '''    public String getName()
    public String getName()
    '''
def setName():
    '''    public void setName(final String s)
    '''
def setTitle():
    '''    public void setTitle(final String s)
    '''
def getTitle():
    '''    public String getTitle()
    '''
def setImageIcon():
    '''    public void setImageIcon(final ImageIcon imageIcon)
    '''
def getImageIcon():
    '''    public ImageIcon getImageIcon()
    public ImageIcon getImageIcon(final String s)
    '''
def sendActionEvent():
    '''    public void sendActionEvent(final ActionEvent actionEvent)
    public void sendActionEvent(final String command)
    '''
def sendMessage():
    '''    public void sendMessage(final String s, final Object o, final String s2, final Object[] array)
    public void sendMessage(final String s, final MessageEvent messageEvent)
    '''
def addMessageListener():
    '''    public void addMessageListener(final MessageListener messageListener, final String s)
    '''
def removeMessageListener():
    '''    public void removeMessageListener(final MessageListener messageListener)
    '''
def addActionHandler():
    '''    public void addActionHandler(final ActionHandler actionHandler)
    '''
def getActionHandlers():
    '''    public ActionHandler[] getActionHandlers(final String s)
    '''
def removeActionHandler():
    '''    public void removeActionHandler(final ActionHandler actionHandler)
    '''
def getAction():
    '''    public Action getAction(final String s)
    '''
def addAction():
    '''    public void addAction(final Action action)
    '''
def removeAction():
    '''    public void removeAction(final Action action)
    '''
def initialize():
    '''    public boolean initialize()
    '''
def isInitialized():
    '''    public boolean isInitialized()
    '''
def close():
    '''    public boolean close(final boolean b)
    '''
def addSettings():
    '''    public boolean addSettings(final IlvSettings ilvSettings)
    public boolean addSettings(final IlvSettings ilvSettings, final String s)
    '''
def addXMLSettings():
    '''    public IlvXMLSettings addXMLSettings(final String s)
    public IlvXMLSettings addXMLSettings(final URL url)
    '''
def removeSettings():
    '''    public boolean removeSettings(final IlvSettings ilvSettings)
    public boolean removeSettings(final IlvSettings ilvSettings)
    '''
def getSettings():
    '''    public IlvSettings getSettings(final String s)
    public IlvSettings[] getSettings()
    '''
def addSettingsListener():
    '''    public void addSettingsListener(final SettingsListener settingsListener)
    '''
def removeSettingsListener():
    '''    public boolean removeSettingsListener(final SettingsListener settingsListener)
    '''
def getSettingsManager():
    '''    public IlvSettingsManager getSettingsManager()
    '''
def selectElement():
    '''    public IlvSettingsElement selectElement(final IlvSettingsQuery ilvSettingsQuery)
    public IlvSettingsElement selectElement(final String s, final String s2, final Object o)
    '''
def select():
    '''    public IlvSettingsElement[] select(final IlvSettingsQuery ilvSettingsQuery)
    public IlvSettingsElement[] select(final String s, final IlvSettingsElement[] relativeElementList)
    public IlvSettingsElement[] select(final IlvSettingsQuery ilvSettingsQuery, final IlvSettingsElement[] relativeElementList)
    '''
def commitSettingsChanges():
    '''    public void commitSettingsChanges()
    '''
def addLocaleSettingsListener():
    '''    public void addLocaleSettingsListener(final LocaleSettingsListener e)
    '''
def removeLocaleSettingsListener():
    '''    public boolean removeLocaleSettingsListener(final LocaleSettingsListener o)
    '''
def setMainWindow():
    '''    public void setMainWindow(final IlvMainWindow mainWindow)
    '''
def windowOpened():
    '''    public void windowOpened(final WindowEvent windowEvent)
    '''
def getMainComponent():
    '''    public Component getMainComponent()
    '''
def getMainWindow():
    '''    public IlvMainWindow getMainWindow()
    '''
def getMainContainer():
    '''    public Container getMainContainer()
    '''
def isApplet():
    '''    public boolean isApplet()
    '''
def getApplet():
    '''    public Applet getApplet()
    '''
def readApplicationSettings():
    '''    public void readApplicationSettings()
    '''
def getDocumentTemplateCount():
    '''    public int getDocumentTemplateCount()
    '''
def getDocumentTemplate():
    '''    public IlvDocumentTemplate getDocumentTemplate(final int n)
    public IlvDocumentTemplate getDocumentTemplate(final String anObject)
    '''
def addDocumentTemplate():
    '''    public void addDocumentTemplate(final IlvDocumentTemplate ilvDocumentTemplate)
    '''
def removeDocumentTemplate():
    '''    public boolean removeDocumentTemplate(final IlvDocumentTemplate ilvDocumentTemplate)
    '''
def openDocument():
    '''    public IlvDocument openDocument()
    public IlvDocument openDocument(final IlvFileDocumentTemplate ilvFileDocumentTemplate)
    '''
def openDocumentFile():
    '''    public IlvDocument openDocumentFile(final String pathname, final boolean b, final boolean b2)
    '''
def isValidDocumentFile():
    '''    public boolean isValidDocumentFile(final String pathname)
    '''
def initializeFileChooser():
    '''    public void initializeFileChooser(final JFileChooser fileChooser, final String s, final int n, final IlvFileDocumentTemplate ilvFileDocumentTemplate)
    '''
def showFileChooser():
    '''    public IlvFileChooserSelection[] showFileChooser(final String s, final String s2, final int n, final IlvFileDocumentTemplate ilvFileDocumentTemplate, final Component component)
    '''
def newDocument():
    '''    public IlvDocument newDocument()
    public IlvDocument newDocument(final IlvDocumentTemplate ilvDocumentTemplate, final boolean b, final Object o)
    public IlvDocument newDocument(final Object o, final boolean b)
    '''
def newDocumentOnLastTemplate():
    '''    public IlvDocument newDocumentOnLastTemplate()
    '''
def canCreateDocument():
    '''    public boolean canCreateDocument(final Object o)
    '''
def saveAllDocuments():
    '''    public boolean saveAllDocuments()
    '''
def closeAllDocuments():
    '''    public boolean closeAllDocuments(final boolean b)
    '''
def closeActiveDocument():
    '''    public boolean closeActiveDocument(final boolean b)
    '''
def closeDocument():
    '''    public boolean closeDocument(final IlvDocument ilvDocument, final boolean b)
    '''
def saveActiveDocument():
    '''    public boolean saveActiveDocument(final boolean b)
    '''
def saveDocument():
    '''    public boolean saveDocument(final String spec)
    public boolean saveDocument(final IlvDocument ilvDocument)
    '''
def saveDocumentModifications():
    '''    public boolean saveDocumentModifications(final IlvDocument ilvDocument)
    '''
def saveAsActiveDocument():
    '''    public boolean saveAsActiveDocument(final boolean b)
    '''
def findDocument():
    '''    public IlvDocument findDocument(final String spec)
    '''
def getOpenedDocumentCount():
    '''    public int getOpenedDocumentCount()
    '''
def getOpenDocuments():
    '''    public IlvDocument[] getOpenDocuments()
    public IlvDocument[] getOpenDocuments(final IlvDocumentTemplate ilvDocumentTemplate)
    '''
def openRecentOpenedFile():
    '''    public IlvDocument openRecentOpenedFile(final int n)
    '''
def getRecentOpenedFile():
    '''    public String getRecentOpenedFile(final int n)
    '''
def getRecentOpenedFileCount():
    '''    public int getRecentOpenedFileCount()
    '''
def getRecentFileList():
    '''    public IlvRecentFileList getRecentFileList()
    '''
def getActiveDocument():
    '''    public IlvDocument getActiveDocument(final boolean b)
    '''
def setActiveDocument():
    '''    public void setActiveDocument(final IlvDocument ilvDocument, final IlvDocumentView ilvDocumentView, final boolean b)
    '''
def setActiveView():
    '''    public void setActiveView(final IlvDocumentView ilvDocumentView, final boolean b)
    '''
def getActiveView():
    '''    public IlvDocumentView getActiveView(final boolean b)
    '''
def getActiveViewContainer():
    '''    public IlvViewContainer getActiveViewContainer()
    '''
def addApplicationListener():
    '''    public void addApplicationListener(final ApplicationListener applicationListener)
    public void addApplicationListener(final String s, final ApplicationListener applicationListener)
    '''
def removeApplicationListener():
    '''    public void removeApplicationListener(final ApplicationListener applicationListener)
    public void removeApplicationListener(final String s, final ApplicationListener applicationListener)
    '''
def attachDocument():
    '''    public void attachDocument(final IlvDocument ilvDocument, final IlvDocument ilvDocument2)
    '''
def detachDocument():
    '''    public void detachDocument(final IlvDocument ilvDocument, final IlvDocument ilvDocument2)
    '''
def updateAction():
    '''    public boolean updateAction(final String s)
    public boolean updateAction(final Action action)
    public boolean updateAction(final Action action)
    '''
def updateActions():
    '''    public void updateActions()
    '''
def updateActionsByCategory():
    '''    public void updateActionsByCategory(final String s)
    '''
def getClassLoader():
    '''    public ClassLoader getClassLoader()
    '''
def findResource():
    '''    public URL findResource(final String s)
    '''
def getResource():
    '''    public URL getResource(final String s)
    '''
def loadClass():
    '''    public Class loadClass(final String s)
    '''
def addClassLoader():
    '''    public void addClassLoader(final ClassLoader e)
    '''
def removeClassLoader():
    '''    public boolean removeClassLoader(final ClassLoader o)
    '''
def getClassForName():
    '''    public Class getClassForName(final String s)
    '''
def setLocale():
    '''    public void setLocale(final Locale locale)
    '''
def getLocale():
    '''    public Locale getLocale()
    '''
def getResourceBundleManager():
    '''    public IlvResourceBundleManager getResourceBundleManager()
    '''
def setResourceBundleManager():
    '''    public void setResourceBundleManager(final IlvResourceBundleManager ilvResourceBundleManager)
    '''
def addResourcePropertyFile():
    '''    public ResourceBundle addResourcePropertyFile(final String s)
    '''
def removeResourcePropertyFile():
    '''    public ResourceBundle removeResourcePropertyFile(final String s)
    '''
def addResourceBundle():
    '''    public void addResourceBundle(final ResourceBundle resourceBundle)
    '''
def getString():
    '''    public String getString(final String key)
    '''
def getFormattedString():
    '''    public String getFormattedString(final String s, final Object[] array)
    '''
def getComponentOrientation():
    '''    public ComponentOrientation getComponentOrientation()
    '''
def applyCursor():
    '''    public HashMap applyCursor(final Cursor cursor)
    '''
def restoreCursor():
    '''    public void restoreCursor(final HashMap hashMap)
    public void restoreCursor()
    '''
def setCursor():
    '''    public void setCursor(final Cursor cursor)
    '''
def getUserSettingsURL():
    '''    public URL getUserSettingsURL()
    '''
def setUserSettingsURL():
    '''    public void setUserSettingsURL(final URL userSettingsURL)
    '''
def getUserHomeDirectory():
    '''    public URL getUserHomeDirectory()
    '''
def setUserHomeDirectory():
    '''    public void setUserHomeDirectory(final URL userHomeDirectory)
    '''
def getSoftwareProvider():
    '''    public String getSoftwareProvider()
    '''
def setSoftwareProvider():
    '''    public void setSoftwareProvider(final String softwareProvider)
    '''
def getUserSettingsSubDirectory():
    '''    public String getUserSettingsSubDirectory()
    '''
def setUserSettingsSubDirectory():
    '''    public void setUserSettingsSubDirectory(final String userSettingsSubDirectory)
    '''
def resolveURL():
    '''    public URL resolveURL(final String s)
    '''
def getAbbreviateForm():
    '''    public String getAbbreviateForm(final URL url)
    '''
def addURLResolver():
    '''    public void addURLResolver(final IlvURLResolver ilvURLResolver)
    '''
def removeURLResolver():
    '''    public boolean removeURLResolver(final IlvURLResolver ilvURLResolver)
    '''
def getURLResolverManager():
    '''    public IlvURLResolverManager getURLResolverManager()
    '''
def getDocumentBase():
    '''    public URL getDocumentBase()
    '''
def setDocumentBase():
    '''    public void setDocumentBase(final URL documentBase)
    '''
def setProperty():
    '''    public Object setProperty(final String s, final Object o)
    '''
def getProperty():
    '''    public Object getProperty(final String s)
    '''
def addPropertyChangeListener():
    '''    public void addPropertyChangeListener(final PropertyChangeListener propertyChangeListener)
    '''
def removePropertyChangeListener():
    '''    public void removePropertyChangeListener(final PropertyChangeListener propertyChangeListener)
    '''
def setSplashWindow():
    '''    public void setSplashWindow(final IlvSplashWindow r)
    '''
def getSplashWindow():
    '''    public IlvSplashWindow getSplashWindow()
    '''
def DocumentTemplateInstaller():
    '''    public DocumentTemplateInstaller()
    '''
def installObject():
    '''    public boolean installObject(final Object o, final IlvSettingsElement ilvSettingsElement, final IlvApplication ilvApplication)
    '''
def uninstallObject():
    '''    public boolean uninstallObject(final Object o, final IlvSettingsElement ilvSettingsElement, final IlvApplication ilvApplication)
    '''
def ApplicationActionHandler():
    '''    public ApplicationActionHandler(final IlvApplication a)
    '''
def actionPerformed():
    '''    public void actionPerformed(final ActionEvent actionEvent)
    '''
def isProcessingAction():
    '''    public boolean isProcessingAction(final String s)
    '''
def SessionSettingsManager():
    '''    public SessionSettingsManager(final String s)
    '''
def initializeSettings():
    '''    public boolean initializeSettings()
    public boolean initializeSettings()
    '''
def areSettingsInitialized():
    '''    public boolean areSettingsInitialized()
    '''
def setModel():
    '''    public void setModel(final IlvSettingsModel a)
    '''
def commit():
    '''    public void commit()
    '''
def getWritableSettings():
    '''    public IlvSettings getWritableSettings()
    '''
def mainWindowIntialized():
    '''    public void mainWindowIntialized(final IlvMainWindow ilvMainWindow)
    '''
