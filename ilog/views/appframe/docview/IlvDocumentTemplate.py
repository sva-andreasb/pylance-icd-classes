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
def ():
    '''returns IlvDocumentTemplate\n\n
    ()\n
    (String original)\n
    '''
def createDocumentViews():
    '''returns boolean\n\n
    createDocumentViews(final IlvMainWindow ilvMainWindow, final IlvDocument ilvDocument)\n
    '''
def matchData():
    '''returns int\n\n
    matchData(final Object o)\n
    '''
def closeDocumentViews():
    '''returns None\n\n
    closeDocumentViews(final IlvDocument ilvDocument)\n
    '''
def getDocumentContainers():
    '''returns IlvViewContainer[]\n\n
    getDocumentContainers(final IlvDocument ilvDocument)\n
    '''
def newViewContainer():
    '''returns IlvViewContainer\n\n
    newViewContainer(final IlvDocument ilvDocument, final String s, final boolean b)\n
    newViewContainer(final IlvDocument ilvDocument, final IlvContainerTemplate ilvContainerTemplate, final String s)\n
    '''
def newMDIViewContainer():
    '''returns IlvMDIViewContainer\n\n
    newMDIViewContainer(final IlvDocument ilvDocument, final IlvMDIContainerTemplate ilvMDIContainerTemplate, final String s)\n
    '''
def activateDocumentView():
    '''returns None\n\n
    activateDocumentView(final IlvDocumentView ilvDocumentView)\n
    activateDocumentView(final IlvDocument ilvDocument)\n
    '''
def documentActivated():
    '''returns None\n\n
    documentActivated(final IlvDocument ilvDocument, final boolean b)\n
    '''
def documentViewExists():
    '''returns IlvDocumentView\n\n
    documentViewExists(final IlvDocument ilvDocument, final String s)\n
    '''
def ensureDocumentViewExists():
    '''returns IlvDocumentView\n\n
    ensureDocumentViewExists(final IlvDocument ilvDocument, final String s, final boolean b)\n
    '''
def closeDocumentView():
    '''returns boolean\n\n
    closeDocumentView(final IlvDocument ilvDocument, final String s)\n
    '''
def initializeDocumentViews():
    '''returns None\n\n
    initializeDocumentViews(final IlvDocument ilvDocument)\n
    '''
def updateViewContainerTitles():
    '''returns None\n\n
    updateViewContainerTitles(final IlvDocument ilvDocument)\n
    '''
def createDocument():
    '''returns IlvDocument\n\n
    createDocument()\n
    '''
def alwaysShowMenu():
    '''returns boolean\n\n
    alwaysShowMenu()\n
    '''
def insertBars():
    '''returns None\n\n
    insertBars(final IlvMainWindow ilvMainWindow)\n
    '''
def removeBars():
    '''returns None\n\n
    removeBars(final IlvMainWindow ilvMainWindow)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def setName():
    '''returns None\n\n
    setName(final String s)\n
    '''
def getApplication():
    '''returns IlvApplication\n\n
    getApplication()\n
    '''
def setApplication():
    '''returns None\n\n
    setApplication(final IlvApplication application)\n
    '''
def getSettings():
    '''returns IlvSettings\n\n
    getSettings()\n
    '''
def setSettings():
    '''returns None\n\n
    setSettings(final IlvSettings settings)\n
    '''
def getDocumentClass():
    '''returns Class\n\n
    getDocumentClass()\n
    '''
def setDocumentClass():
    '''returns None\n\n
    setDocumentClass(final Class clazz)\n
    '''
def getDataClass():
    '''returns Class\n\n
    getDataClass()\n
    '''
def getShortName():
    '''returns String\n\n
    getShortName()\n
    '''
def setShortName():
    '''returns None\n\n
    setShortName(final String s)\n
    '''
def getDescription():
    '''returns String\n\n
    getDescription()\n
    '''
def setDescription():
    '''returns None\n\n
    setDescription(final String t)\n
    '''
def getDefaultDocumentName():
    '''returns String\n\n
    getDefaultDocumentName()\n
    '''
def setDefaultDocumentName():
    '''returns None\n\n
    setDefaultDocumentName(final String u)\n
    '''
def isMDI():
    '''returns boolean\n\n
    isMDI()\n
    '''
def setMDI():
    '''returns None\n\n
    setMDI(final boolean r)\n
    '''
def hasOwnRecentFileList():
    '''returns boolean\n\n
    hasOwnRecentFileList()\n
    '''
def getRecentFileListCommand():
    '''returns String\n\n
    getRecentFileListCommand()\n
    '''
def connectMainWindow():
    '''returns None\n\n
    connectMainWindow(final IlvMainWindow ilvMainWindow)\n
    '''
def applicationEventReceived():
    '''returns None\n\n
    applicationEventReceived(final ApplicationEvent applicationEvent)\n
    '''
def getMenuCompletion():
    '''returns IlvMenuCompletion\n\n
    getMenuCompletion(final IlvMainWindow ilvMainWindow)\n
    '''
def readSettings():
    '''returns boolean\n\n
    readSettings(final IlvSettings settings, final IlvApplication application)\n
    readSettings(final IlvSettingsElement ilvSettingsElement, final Object o)\n
    readSettings(final IlvSettingsElement settingsElement, final IlvApplication application)\n
    '''
def writeSettings():
    '''returns None\n\n
    writeSettings(final IlvSettingsElement ilvSettingsElement, final Object o)\n
    '''
def getSettingsElement():
    '''returns IlvSettingsElement\n\n
    getSettingsElement()\n
    '''
def actionPerformed():
    '''returns None\n\n
    actionPerformed(final ActionEvent actionEvent)\n
    '''
def isProcessingAction():
    '''returns boolean\n\n
    isProcessingAction(final String s)\n
    '''
def updateAction():
    '''returns boolean\n\n
    updateAction(final Action action)\n
    '''
def getIcon():
    '''returns Icon\n\n
    getIcon()\n
    getIcon(final String s)\n
    '''
def closeDocument():
    '''returns boolean\n\n
    closeDocument(final IlvDocument ilvDocument, final boolean b)\n
    '''
def saveDocumentModifications():
    '''returns boolean\n\n
    saveDocumentModifications(final IlvDocument ilvDocument)\n
    '''
def closeViewContainer():
    '''returns boolean\n\n
    closeViewContainer(final IlvMDIViewContainer ilvMDIViewContainer)\n
    closeViewContainer(final IlvMDIViewContainer ilvMDIViewContainer, final boolean b)\n
    '''
def canCloseViewContainer():
    '''returns boolean\n\n
    canCloseViewContainer(final IlvViewContainer ilvViewContainer)\n
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
def getViewConfiguration():
    '''returns IlvDocumentViewConfiguration\n\n
    getViewConfiguration(final String s)\n
    getViewConfiguration(final int n)\n
    '''
def getViewConfigurationCount():
    '''returns int\n\n
    getViewConfigurationCount()\n
    '''
def propertyChange():
    '''returns None\n\n
    propertyChange(final PropertyChangeEvent propertyChangeEvent)\n
    '''
