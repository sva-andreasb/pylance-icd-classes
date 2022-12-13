CLOSE_ALL_DOCUMENTS_CMD = "String  CloseAllDocuments""
CLOSE_DOCUMENT_CMD = "String  CloseDocument""
OPEN_DOCUMENT_CMD = "String  OpenDocument""
NEW_DOCUMENT_CMD = "String  NewDocument""
NEW_DOCUMENT_ON_LAST_TEMPLATE_CMD = "String  NewDocumentOnLastChoice""
SAVE_ALL_DOCUMENTS_CMD = "String  SaveAllDocuments""
SAVE_DOCUMENT_CMD = "String  SaveDocument""
SAVE_AS_DOCUMENT_CMD = "String  SaveAsDocument""
REVERT_DOCUMENT_CMD = "String  RevertDocument""
EXIT_CMD = "String  Exit""
OPEN_MULTIPLE_FILES = "int  1"
OPEN_FILE_MUST_EXIST = "int  2"
OPEN_MODE = "int  8"
SAVE_MODE = "int  16"
SAVE_AS_MODE = "int  32"
TITLE_PROPERTY = "String  Title""
ICON_PROPERTY = "String  Icon""
STATUS_MESSAGE = "String  MainStatusMessage""
STATUS_BAR_PROPERTY = "String  StatusBar""
MENU_BAR_PROPERTY = "String  MenuBar""
MAIN_WINDOW_PROPERTY = "String  MainWindow""
SETTINGS_TYPE = "String  application""
def IlvApplication():
'''public IlvApplication()
public IlvApplication(final String name)
public IlvApplication(final String[] array)
public IlvApplication(final String name, final String[] array)
'''
pass
def settingsInitialized():
'''public void settingsInitialized(final IlvSettings ilvSettings)
'''
pass
def settingsModified():
'''public void settingsModified(final IlvSettings ilvSettings)
'''
pass
def settingsAdded():
'''public void settingsAdded(final IlvSettings ilvSettings)
'''
pass
def settingsRemoved():
'''public void settingsRemoved(final IlvSettings ilvSettings)
'''
pass
def saveChanges():
'''public void saveChanges(final IlvSettings ilvSettings)
'''
pass
def propertyChange():
'''public void propertyChange(final PropertyChangeEvent propertyChangeEvent)
'''
pass
def run():
'''public void run()
public void run()
'''
pass
def getName():
'''public String getName()
public String getName()
'''
pass
def setName():
'''public void setName(final String s)
'''
pass
def setTitle():
'''public void setTitle(final String s)
'''
pass
def getTitle():
'''public String getTitle()
'''
pass
def setImageIcon():
'''public void setImageIcon(final ImageIcon imageIcon)
'''
pass
def getImageIcon():
'''public ImageIcon getImageIcon()
public ImageIcon getImageIcon(final String s)
'''
pass
def sendActionEvent():
'''public void sendActionEvent(final ActionEvent actionEvent)
public void sendActionEvent(final String command)
'''
pass
def sendMessage():
'''public void sendMessage(final String s, final Object o, final String s2, final Object[] array)
public void sendMessage(final String s, final MessageEvent messageEvent)
'''
pass
def addMessageListener():
'''public void addMessageListener(final MessageListener messageListener, final String s)
'''
pass
def removeMessageListener():
'''public void removeMessageListener(final MessageListener messageListener)
'''
pass
def addActionHandler():
'''public void addActionHandler(final ActionHandler actionHandler)
'''
pass
def getActionHandlers():
'''public ActionHandler[] getActionHandlers(final String s)
'''
pass
def removeActionHandler():
'''public void removeActionHandler(final ActionHandler actionHandler)
'''
pass
def getAction():
'''public Action getAction(final String s)
'''
pass
def addAction():
'''public void addAction(final Action action)
'''
pass
def removeAction():
'''public void removeAction(final Action action)
'''
pass
def initialize():
'''public boolean initialize()
'''
pass
def isInitialized():
'''public boolean isInitialized()
'''
pass
def close():
'''public boolean close(final boolean b)
'''
pass
def addSettings():
'''public boolean addSettings(final IlvSettings ilvSettings)
public boolean addSettings(final IlvSettings ilvSettings, final String s)
'''
pass
def addXMLSettings():
'''public IlvXMLSettings addXMLSettings(final String s)
public IlvXMLSettings addXMLSettings(final URL url)
'''
pass
def removeSettings():
'''public boolean removeSettings(final IlvSettings ilvSettings)
public boolean removeSettings(final IlvSettings ilvSettings)
'''
pass
def getSettings():
'''public IlvSettings getSettings(final String s)
public IlvSettings[] getSettings()
'''
pass
def addSettingsListener():
'''public void addSettingsListener(final SettingsListener settingsListener)
'''
pass
def removeSettingsListener():
'''public boolean removeSettingsListener(final SettingsListener settingsListener)
'''
pass
def getSettingsManager():
'''public IlvSettingsManager getSettingsManager()
'''
pass
def selectElement():
'''public IlvSettingsElement selectElement(final IlvSettingsQuery ilvSettingsQuery)
public IlvSettingsElement selectElement(final String s, final String s2, final Object o)
'''
pass
def select():
'''public IlvSettingsElement[] select(final IlvSettingsQuery ilvSettingsQuery)
public IlvSettingsElement[] select(final String s, final IlvSettingsElement[] relativeElementList)
public IlvSettingsElement[] select(final IlvSettingsQuery ilvSettingsQuery, final IlvSettingsElement[] relativeElementList)
'''
pass
def commitSettingsChanges():
'''public void commitSettingsChanges()
'''
pass
def addLocaleSettingsListener():
'''public void addLocaleSettingsListener(final LocaleSettingsListener e)
'''
pass
def removeLocaleSettingsListener():
'''public boolean removeLocaleSettingsListener(final LocaleSettingsListener o)
'''
pass
def setMainWindow():
'''public void setMainWindow(final IlvMainWindow mainWindow)
'''
pass
def windowOpened():
'''public void windowOpened(final WindowEvent windowEvent)
'''
pass
def getMainComponent():
'''public Component getMainComponent()
'''
pass
def getMainWindow():
'''public IlvMainWindow getMainWindow()
'''
pass
def getMainContainer():
'''public Container getMainContainer()
'''
pass
def isApplet():
'''public boolean isApplet()
'''
pass
def getApplet():
'''public Applet getApplet()
'''
pass
def readApplicationSettings():
'''public void readApplicationSettings()
'''
pass
def getDocumentTemplateCount():
'''public int getDocumentTemplateCount()
'''
pass
def getDocumentTemplate():
'''public IlvDocumentTemplate getDocumentTemplate(final int n)
public IlvDocumentTemplate getDocumentTemplate(final String anObject)
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
def openDocument():
'''public IlvDocument openDocument()
public IlvDocument openDocument(final IlvFileDocumentTemplate ilvFileDocumentTemplate)
'''
pass
def openDocumentFile():
'''public IlvDocument openDocumentFile(final String pathname, final boolean b, final boolean b2)
'''
pass
def isValidDocumentFile():
'''public boolean isValidDocumentFile(final String pathname)
'''
pass
def initializeFileChooser():
'''public void initializeFileChooser(final JFileChooser fileChooser, final String s, final int n, final IlvFileDocumentTemplate ilvFileDocumentTemplate)
'''
pass
def showFileChooser():
'''public IlvFileChooserSelection[] showFileChooser(final String s, final String s2, final int n, final IlvFileDocumentTemplate ilvFileDocumentTemplate, final Component component)
'''
pass
def newDocument():
'''public IlvDocument newDocument()
public IlvDocument newDocument(final IlvDocumentTemplate ilvDocumentTemplate, final boolean b, final Object o)
public IlvDocument newDocument(final Object o, final boolean b)
'''
pass
def newDocumentOnLastTemplate():
'''public IlvDocument newDocumentOnLastTemplate()
'''
pass
def canCreateDocument():
'''public boolean canCreateDocument(final Object o)
'''
pass
def saveAllDocuments():
'''public boolean saveAllDocuments()
'''
pass
def closeAllDocuments():
'''public boolean closeAllDocuments(final boolean b)
'''
pass
def closeActiveDocument():
'''public boolean closeActiveDocument(final boolean b)
'''
pass
def closeDocument():
'''public boolean closeDocument(final IlvDocument ilvDocument, final boolean b)
'''
pass
def saveActiveDocument():
'''public boolean saveActiveDocument(final boolean b)
'''
pass
def saveDocument():
'''public boolean saveDocument(final String spec)
public boolean saveDocument(final IlvDocument ilvDocument)
'''
pass
def saveDocumentModifications():
'''public boolean saveDocumentModifications(final IlvDocument ilvDocument)
'''
pass
def saveAsActiveDocument():
'''public boolean saveAsActiveDocument(final boolean b)
'''
pass
def findDocument():
'''public IlvDocument findDocument(final String spec)
'''
pass
def getOpenedDocumentCount():
'''public int getOpenedDocumentCount()
'''
pass
def getOpenDocuments():
'''public IlvDocument[] getOpenDocuments()
public IlvDocument[] getOpenDocuments(final IlvDocumentTemplate ilvDocumentTemplate)
'''
pass
def openRecentOpenedFile():
'''public IlvDocument openRecentOpenedFile(final int n)
'''
pass
def getRecentOpenedFile():
'''public String getRecentOpenedFile(final int n)
'''
pass
def getRecentOpenedFileCount():
'''public int getRecentOpenedFileCount()
'''
pass
def getRecentFileList():
'''public IlvRecentFileList getRecentFileList()
'''
pass
def getActiveDocument():
'''public IlvDocument getActiveDocument(final boolean b)
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
def getActiveView():
'''public IlvDocumentView getActiveView(final boolean b)
'''
pass
def getActiveViewContainer():
'''public IlvViewContainer getActiveViewContainer()
'''
pass
def addApplicationListener():
'''public void addApplicationListener(final ApplicationListener applicationListener)
public void addApplicationListener(final String s, final ApplicationListener applicationListener)
'''
pass
def removeApplicationListener():
'''public void removeApplicationListener(final ApplicationListener applicationListener)
public void removeApplicationListener(final String s, final ApplicationListener applicationListener)
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
def updateAction():
'''public boolean updateAction(final String s)
public boolean updateAction(final Action action)
public boolean updateAction(final Action action)
'''
pass
def updateActions():
'''public void updateActions()
'''
pass
def updateActionsByCategory():
'''public void updateActionsByCategory(final String s)
'''
pass
def getClassLoader():
'''public ClassLoader getClassLoader()
'''
pass
def findResource():
'''public URL findResource(final String s)
'''
pass
def getResource():
'''public URL getResource(final String s)
'''
pass
def loadClass():
'''public Class loadClass(final String s)
'''
pass
def addClassLoader():
'''public void addClassLoader(final ClassLoader e)
'''
pass
def removeClassLoader():
'''public boolean removeClassLoader(final ClassLoader o)
'''
pass
def getClassForName():
'''public Class getClassForName(final String s)
'''
pass
def setLocale():
'''public void setLocale(final Locale locale)
'''
pass
def getLocale():
'''public Locale getLocale()
'''
pass
def getResourceBundleManager():
'''public IlvResourceBundleManager getResourceBundleManager()
'''
pass
def setResourceBundleManager():
'''public void setResourceBundleManager(final IlvResourceBundleManager ilvResourceBundleManager)
'''
pass
def addResourcePropertyFile():
'''public ResourceBundle addResourcePropertyFile(final String s)
'''
pass
def removeResourcePropertyFile():
'''public ResourceBundle removeResourcePropertyFile(final String s)
'''
pass
def addResourceBundle():
'''public void addResourceBundle(final ResourceBundle resourceBundle)
'''
pass
def getString():
'''public String getString(final String key)
'''
pass
def getFormattedString():
'''public String getFormattedString(final String s, final Object[] array)
'''
pass
def getComponentOrientation():
'''public ComponentOrientation getComponentOrientation()
'''
pass
def applyCursor():
'''public HashMap applyCursor(final Cursor cursor)
'''
pass
def restoreCursor():
'''public void restoreCursor(final HashMap hashMap)
public void restoreCursor()
'''
pass
def setCursor():
'''public void setCursor(final Cursor cursor)
'''
pass
def getUserSettingsURL():
'''public URL getUserSettingsURL()
'''
pass
def setUserSettingsURL():
'''public void setUserSettingsURL(final URL userSettingsURL)
'''
pass
def getUserHomeDirectory():
'''public URL getUserHomeDirectory()
'''
pass
def setUserHomeDirectory():
'''public void setUserHomeDirectory(final URL userHomeDirectory)
'''
pass
def getSoftwareProvider():
'''public String getSoftwareProvider()
'''
pass
def setSoftwareProvider():
'''public void setSoftwareProvider(final String softwareProvider)
'''
pass
def getUserSettingsSubDirectory():
'''public String getUserSettingsSubDirectory()
'''
pass
def setUserSettingsSubDirectory():
'''public void setUserSettingsSubDirectory(final String userSettingsSubDirectory)
'''
pass
def resolveURL():
'''public URL resolveURL(final String s)
'''
pass
def getAbbreviateForm():
'''public String getAbbreviateForm(final URL url)
'''
pass
def addURLResolver():
'''public void addURLResolver(final IlvURLResolver ilvURLResolver)
'''
pass
def removeURLResolver():
'''public boolean removeURLResolver(final IlvURLResolver ilvURLResolver)
'''
pass
def getURLResolverManager():
'''public IlvURLResolverManager getURLResolverManager()
'''
pass
def getDocumentBase():
'''public URL getDocumentBase()
'''
pass
def setDocumentBase():
'''public void setDocumentBase(final URL documentBase)
'''
pass
def setProperty():
'''public Object setProperty(final String s, final Object o)
'''
pass
def getProperty():
'''public Object getProperty(final String s)
'''
pass
def addPropertyChangeListener():
'''public void addPropertyChangeListener(final PropertyChangeListener propertyChangeListener)
'''
pass
def removePropertyChangeListener():
'''public void removePropertyChangeListener(final PropertyChangeListener propertyChangeListener)
'''
pass
def setSplashWindow():
'''public void setSplashWindow(final IlvSplashWindow r)
'''
pass
def getSplashWindow():
'''public IlvSplashWindow getSplashWindow()
'''
pass
def DocumentTemplateInstaller():
'''public DocumentTemplateInstaller()
'''
pass
def installObject():
'''public boolean installObject(final Object o, final IlvSettingsElement ilvSettingsElement, final IlvApplication ilvApplication)
'''
pass
def uninstallObject():
'''public boolean uninstallObject(final Object o, final IlvSettingsElement ilvSettingsElement, final IlvApplication ilvApplication)
'''
pass
def ApplicationActionHandler():
'''public ApplicationActionHandler(final IlvApplication a)
'''
pass
def actionPerformed():
'''public void actionPerformed(final ActionEvent actionEvent)
'''
pass
def isProcessingAction():
'''public boolean isProcessingAction(final String s)
'''
pass
def SessionSettingsManager():
'''public SessionSettingsManager(final String s)
'''
pass
def initializeSettings():
'''public boolean initializeSettings()
public boolean initializeSettings()
'''
pass
def areSettingsInitialized():
'''public boolean areSettingsInitialized()
'''
pass
def setModel():
'''public void setModel(final IlvSettingsModel a)
'''
pass
def commit():
'''public void commit()
'''
pass
def getWritableSettings():
'''public IlvSettings getWritableSettings()
'''
pass
def mainWindowIntialized():
'''public void mainWindowIntialized(final IlvMainWindow ilvMainWindow)
'''
pass
