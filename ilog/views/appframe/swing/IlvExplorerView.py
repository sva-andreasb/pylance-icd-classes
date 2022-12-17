DEFAULT_SETTINGS_TYPE = "String  \"explorerView\""
DEFAULT_SETTINGS_NAME = "String  \"default\""
INSERT_FOLDER_CMD = "String  \"InsertFolder\""
INSERT_FILE_CMD = "String  \"InsertFile\""
INSERT_PROJECT_CMD = "String  \"InsertProject\""
REMOVE_NODE_CMD = "String  \"RemoveProjecItem\""
OPEN_PROJECT_NODE_CMD = "String  \"OpenProjectNode\""
def ():
    '''returns ExplorerRenderer\n\n
    ()\n
    (final IlvSettingsElement ilvSettingsElement, final IlvApplication ilvApplication)\n
    ()\n
    '''
def initializeView():
    '''returns None\n\n
    initializeView(final IlvDocument b)\n
    '''
def valueChanged():
    '''returns None\n\n
    valueChanged(final TreeSelectionEvent treeSelectionEvent)\n
    '''
def getDataContainer():
    '''returns IlvDataContainer\n\n
    getDataContainer()\n
    '''
def propertyChange():
    '''returns None\n\n
    propertyChange(final PropertyChangeEvent propertyChangeEvent)\n
    '''
def nodeAdded():
    '''returns None\n\n
    nodeAdded(final DataContainerEvent dataContainerEvent)\n
    '''
def nodeRemoved():
    '''returns None\n\n
    nodeRemoved(final DataContainerEvent dataContainerEvent)\n
    '''
def nodePropertyChanged():
    '''returns None\n\n
    nodePropertyChanged(final NodePropertyChangeEvent nodePropertyChangeEvent)\n
    '''
def isProcessingAction():
    '''returns boolean\n\n
    isProcessingAction(final String s)\n
    '''
def updateAction():
    '''returns boolean\n\n
    updateAction(final Action action)\n
    '''
def actionPerformed():
    '''returns None\n\n
    actionPerformed(final ActionEvent actionEvent)\n
    '''
def readSettings():
    '''returns None\n\n
    readSettings(final IlvSettingsElement ilvSettingsElement, final IlvApplication application)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getIcon():
    '''returns Icon\n\n
    getIcon(final boolean b)\n
    '''
def getExpandedIcon():
    '''returns Icon\n\n
    getExpandedIcon()\n
    '''
def getPopupMenu():
    '''returns IlvPopupMenu\n\n
    getPopupMenu()\n
    '''
def getTreeCellRendererComponent():
    '''returns Component\n\n
    getTreeCellRendererComponent(final JTree tree, final Object value, final boolean sel, final boolean expanded, final boolean leaf, final int row, final boolean hasFocus)\n
    '''
