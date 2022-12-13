SETTINGS_TYPE = "String  \"documentTemplate\""
NAME_PROPERTY = "String  \"name\""
ICON_PROPERTY = "String  \"icon\""
DESCRIPTION_PROPERTY = "String  \"description\""
SHORT_NAME_PROPERTY = "String  \"shortName\""
DEFAULT_DOCUMENT_NAME_PROPERTY = "String  \"defaultDocumentName\""
SELECTED_CONFIGURATION_PROPERTY = "String  \"selectedConfiguration\""
DATA_CLASS_PROPERTY = "String  \"dataClass\""
UNDO_LIMIT_PROPERTY = "String  \"undoLimit\""
DOCUMENT_CLASS_PROPERTY = "String  \"documentClass\""
def IlvDocumentTemplate():
    '''public IlvDocumentTemplate()
    public IlvDocumentTemplate(String original)
    '''
def createDocumentViews():
    '''public boolean createDocumentViews(final IlvMainWindow ilvMainWindow, final IlvDocument ilvDocument)
    '''
def matchData():
    '''public int matchData(final Object o)
    '''
def closeDocumentViews():
    '''public void closeDocumentViews(final IlvDocument ilvDocument)
    '''
def getDocumentContainers():
    '''public IlvViewContainer[] getDocumentContainers(final IlvDocument ilvDocument)
    '''
def newViewContainer():
    '''public IlvViewContainer newViewContainer(final IlvDocument ilvDocument, final String s, final boolean b)
    public IlvViewContainer newViewContainer(final IlvDocument ilvDocument, final IlvContainerTemplate ilvContainerTemplate, final String s)
    '''
def newMDIViewContainer():
    '''public IlvMDIViewContainer newMDIViewContainer(final IlvDocument ilvDocument, final IlvMDIContainerTemplate ilvMDIContainerTemplate, final String s)
    '''
def activateDocumentView():
    '''public void activateDocumentView(final IlvDocumentView ilvDocumentView)
    public void activateDocumentView(final IlvDocument ilvDocument)
    '''
def documentActivated():
    '''public void documentActivated(final IlvDocument ilvDocument, final boolean b)
    '''
def documentViewExists():
    '''public IlvDocumentView documentViewExists(final IlvDocument ilvDocument, final String s)
    '''
def ensureDocumentViewExists():
    '''public IlvDocumentView ensureDocumentViewExists(final IlvDocument ilvDocument, final String s, final boolean b)
    '''
def closeDocumentView():
    '''public boolean closeDocumentView(final IlvDocument ilvDocument, final String s)
    '''
def initializeDocumentViews():
    '''public void initializeDocumentViews(final IlvDocument ilvDocument)
    '''
def updateViewContainerTitles():
    '''public void updateViewContainerTitles(final IlvDocument ilvDocument)
    '''
def createDocument():
    '''public IlvDocument createDocument()
    '''
def alwaysShowMenu():
    '''public boolean alwaysShowMenu()
    '''
def insertBars():
    '''public void insertBars(final IlvMainWindow ilvMainWindow)
    '''
def removeBars():
    '''public void removeBars(final IlvMainWindow ilvMainWindow)
    '''
def getName():
    '''public String getName()
    '''
def setName():
    '''public void setName(final String s)
    '''
def getApplication():
    '''public IlvApplication getApplication()
    '''
def setApplication():
    '''public void setApplication(final IlvApplication application)
    '''
def getSettings():
    '''public IlvSettings getSettings()
    '''
def setSettings():
    '''public void setSettings(final IlvSettings settings)
    '''
def getDocumentClass():
    '''public Class getDocumentClass()
    '''
def setDocumentClass():
    '''public void setDocumentClass(final Class clazz)
    '''
def getDataClass():
    '''public Class getDataClass()
    '''
def getShortName():
    '''public String getShortName()
    '''
def setShortName():
    '''public void setShortName(final String s)
    '''
def getDescription():
    '''public String getDescription()
    '''
def setDescription():
    '''public void setDescription(final String t)
    '''
def getDefaultDocumentName():
    '''public String getDefaultDocumentName()
    '''
def setDefaultDocumentName():
    '''public void setDefaultDocumentName(final String u)
    '''
def isMDI():
    '''public boolean isMDI()
    '''
def setMDI():
    '''public void setMDI(final boolean r)
    '''
def hasOwnRecentFileList():
    '''public boolean hasOwnRecentFileList()
    '''
def getRecentFileListCommand():
    '''public String getRecentFileListCommand()
    '''
def connectMainWindow():
    '''public void connectMainWindow(final IlvMainWindow ilvMainWindow)
    '''
def applicationEventReceived():
    '''public void applicationEventReceived(final ApplicationEvent applicationEvent)
    '''
def getMenuCompletion():
    '''public IlvMenuCompletion getMenuCompletion(final IlvMainWindow ilvMainWindow)
    '''
def readSettings():
    '''public boolean readSettings(final IlvSettings settings, final IlvApplication application)
    public void readSettings(final IlvSettingsElement ilvSettingsElement, final Object o)
    public boolean readSettings(final IlvSettingsElement settingsElement, final IlvApplication application)
    '''
def writeSettings():
    '''public void writeSettings(final IlvSettingsElement ilvSettingsElement, final Object o)
    '''
def getSettingsElement():
    '''public IlvSettingsElement getSettingsElement()
    '''
def actionPerformed():
    '''public void actionPerformed(final ActionEvent actionEvent)
    '''
def isProcessingAction():
    '''public boolean isProcessingAction(final String s)
    '''
def updateAction():
    '''public boolean updateAction(final Action action)
    '''
def getIcon():
    '''public Icon getIcon()
    public Icon getIcon(final String s)
    '''
def closeDocument():
    '''public boolean closeDocument(final IlvDocument ilvDocument, final boolean b)
    '''
def saveDocumentModifications():
    '''public boolean saveDocumentModifications(final IlvDocument ilvDocument)
    '''
def closeViewContainer():
    '''public boolean closeViewContainer(final IlvMDIViewContainer ilvMDIViewContainer)
    public boolean closeViewContainer(final IlvMDIViewContainer ilvMDIViewContainer, final boolean b)
    '''
def canCloseViewContainer():
    '''public boolean canCloseViewContainer(final IlvViewContainer ilvViewContainer)
    '''
def setProperty():
    '''public Object setProperty(final String s, final Object o)
    '''
def getProperty():
    '''public Object getProperty(final String s)
    '''
def addPropertyChangeListener():
    '''public void addPropertyChangeListener(final PropertyChangeListener propertyChangeListener)
    '''
def removePropertyChangeListener():
    '''public void removePropertyChangeListener(final PropertyChangeListener propertyChangeListener)
    '''
def getViewConfiguration():
    '''public IlvDocumentViewConfiguration getViewConfiguration(final String s)
    public IlvDocumentViewConfiguration getViewConfiguration(final int n)
    '''
def getViewConfigurationCount():
    '''public int getViewConfigurationCount()
    '''
def propertyChange():
    '''public void propertyChange(final PropertyChangeEvent propertyChangeEvent)
    '''
