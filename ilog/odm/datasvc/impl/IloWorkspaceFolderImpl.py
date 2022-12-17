COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloWorkspaceFolderImpl\n\n
    (final IloAbstractWorkspace workspace, final IloPersistentRow fpo)\n
    (final IloAbstractWorkspace workspace, final IloRow fpo)\n
    '''
def createChildScenario():
    '''returns IloScenarioLink\n\n
    createChildScenario(final int index)\n
    createChildScenario(final int index, final IloScenario source)\n
    '''
def createChildScenarioLink():
    '''returns IloScenarioLink\n\n
    createChildScenarioLink(final int index, final IloScenario source)\n
    '''
def getChildren():
    '''returns List<IloWorkspaceItem>\n\n
    getChildren()\n
    '''
def importScenarioSet():
    '''returns IloWorkspaceItem\n\n
    importScenarioSet(final File source)\n
    '''
def moveChild():
    '''returns None\n\n
    moveChild(final int index, final IloWorkspaceItem item)\n
    '''
def setName():
    '''returns None\n\n
    setName(final String name)\n
    '''
