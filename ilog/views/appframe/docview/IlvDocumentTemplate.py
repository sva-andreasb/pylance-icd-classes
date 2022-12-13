SETTINGS_TYPE = "String  documentTemplate""
NAME_PROPERTY = "String  name""
ICON_PROPERTY = "String  icon""
DESCRIPTION_PROPERTY = "String  description""
SHORT_NAME_PROPERTY = "String  shortName""
DEFAULT_DOCUMENT_NAME_PROPERTY = "String  defaultDocumentName""
SELECTED_CONFIGURATION_PROPERTY = "String  selectedConfiguration""
DATA_CLASS_PROPERTY = "String  dataClass""
UNDO_LIMIT_PROPERTY = "String  undoLimit""
DOCUMENT_CLASS_PROPERTY = "String  documentClass""
def IlvDocumentTemplate():
'''public IlvDocumentTemplate()
public IlvDocumentTemplate(String original)
'''
pass
def createDocumentViews():
'''public boolean createDocumentViews(final IlvMainWindow ilvMainWindow, final IlvDocument ilvDocument)
'''
pass
def matchData():
'''public int matchData(final Object o)
'''
pass
def closeDocumentViews():
'''public void closeDocumentViews(final IlvDocument ilvDocument)
'''
pass
def getDocumentContainers():
'''public IlvViewContainer[] getDocumentContainers(final IlvDocument ilvDocument)
'''
pass
def newViewContainer():
'''public IlvViewContainer newViewContainer(final IlvDocument ilvDocument, final String s, final boolean b)
public IlvViewContainer newViewContainer(final IlvDocument ilvDocument, final IlvContainerTemplate ilvContainerTemplate, final String s)
'''
pass
def newMDIViewContainer():
'''public IlvMDIViewContainer newMDIViewContainer(final IlvDocument ilvDocument, final IlvMDIContainerTemplate ilvMDIContainerTemplate, final String s)
'''
pass
def activateDocumentView():
'''public void activateDocumentView(final IlvDocumentView ilvDocumentView)
public void activateDocumentView(final IlvDocument ilvDocument)
'''
pass
def documentActivated():
'''public void documentActivated(final IlvDocument ilvDocument, final boolean b)
'''
pass
def documentViewExists():
'''public IlvDocumentView documentViewExists(final IlvDocument ilvDocument, final String s)
'''
pass
def ensureDocumentViewExists():
'''public IlvDocumentView ensureDocumentViewExists(final IlvDocument ilvDocument, final String s, final boolean b)
'''
pass
def closeDocumentView():
'''public boolean closeDocumentView(final IlvDocument ilvDocument, final String s)
'''
pass
def initializeDocumentViews():
'''public void initializeDocumentViews(final IlvDocument ilvDocument)
'''
pass
def updateViewContainerTitles():
'''public void updateViewContainerTitles(final IlvDocument ilvDocument)
'''
pass
def createDocument():
'''public IlvDocument createDocument()
'''
pass
def alwaysShowMenu():
'''public boolean alwaysShowMenu()
'''
pass
def insertBars():
'''public void insertBars(final IlvMainWindow ilvMainWindow)
'''
pass
def removeBars():
'''public void removeBars(final IlvMainWindow ilvMainWindow)
'''
pass
def getName():
'''public String getName()
'''
pass
def setName():
'''public void setName(final String s)
'''
pass
def getApplication():
'''public IlvApplication getApplication()
'''
pass
def setApplication():
'''public void setApplication(final IlvApplication application)
'''
pass
def getSettings():
'''public IlvSettings getSettings()
'''
pass
def setSettings():
'''public void setSettings(final IlvSettings settings)
'''
pass
def getDocumentClass():
'''public Class getDocumentClass()
'''
pass
def setDocumentClass():
'''public void setDocumentClass(final Class clazz)
'''
pass
def getDataClass():
'''public Class getDataClass()
'''
pass
def getShortName():
'''public String getShortName()
'''
pass
def setShortName():
'''public void setShortName(final String s)
'''
pass
def getDescription():
'''public String getDescription()
'''
pass
def setDescription():
'''public void setDescription(final String t)
'''
pass
def getDefaultDocumentName():
'''public String getDefaultDocumentName()
'''
pass
def setDefaultDocumentName():
'''public void setDefaultDocumentName(final String u)
'''
pass
def isMDI():
'''public boolean isMDI()
'''
pass
def setMDI():
'''public void setMDI(final boolean r)
'''
pass
def hasOwnRecentFileList():
'''public boolean hasOwnRecentFileList()
'''
pass
def getRecentFileListCommand():
'''public String getRecentFileListCommand()
'''
pass
def connectMainWindow():
'''public void connectMainWindow(final IlvMainWindow ilvMainWindow)
'''
pass
def applicationEventReceived():
'''public void applicationEventReceived(final ApplicationEvent applicationEvent)
'''
pass
def getMenuCompletion():
'''public IlvMenuCompletion getMenuCompletion(final IlvMainWindow ilvMainWindow)
'''
pass
def readSettings():
'''public boolean readSettings(final IlvSettings settings, final IlvApplication application)
public void readSettings(final IlvSettingsElement ilvSettingsElement, final Object o)
public boolean readSettings(final IlvSettingsElement settingsElement, final IlvApplication application)
'''
pass
def writeSettings():
'''public void writeSettings(final IlvSettingsElement ilvSettingsElement, final Object o)
'''
pass
def getSettingsElement():
'''public IlvSettingsElement getSettingsElement()
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
def updateAction():
'''public boolean updateAction(final Action action)
'''
pass
def getIcon():
'''public Icon getIcon()
public Icon getIcon(final String s)
'''
pass
def closeDocument():
'''public boolean closeDocument(final IlvDocument ilvDocument, final boolean b)
'''
pass
def saveDocumentModifications():
'''public boolean saveDocumentModifications(final IlvDocument ilvDocument)
'''
pass
def closeViewContainer():
'''public boolean closeViewContainer(final IlvMDIViewContainer ilvMDIViewContainer)
public boolean closeViewContainer(final IlvMDIViewContainer ilvMDIViewContainer, final boolean b)
'''
pass
def canCloseViewContainer():
'''public boolean canCloseViewContainer(final IlvViewContainer ilvViewContainer)
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
def getViewConfiguration():
'''public IlvDocumentViewConfiguration getViewConfiguration(final String s)
public IlvDocumentViewConfiguration getViewConfiguration(final int n)
'''
pass
def getViewConfigurationCount():
'''public int getViewConfigurationCount()
'''
pass
def propertyChange():
'''public void propertyChange(final PropertyChangeEvent propertyChangeEvent)
'''
pass
