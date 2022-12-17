COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloCatalogWorkspaceItemFactory\n\n
    (final IloApplicationContext context, final IloDataManagerImpl data_manager)\n
    (final File source, final ilog.odm.datasvc.IloSchemaCatalog catalog, final Map<String, String> fileMapping, final Map<String, String> schemaMapping)\n
    '''
def initialize():
    '''returns None\n\n
    initialize()\n
    '''
def dispose():
    '''returns None\n\n
    dispose()\n
    '''
def addLock():
    '''returns IloRow\n\n
    addLock(final Long workspace_id, final int type, final int description, final boolean persistent)\n
    '''
def createFolderItem():
    '''returns IloRowUpdate\n\n
    createFolderItem(final Long workspace_id, final Long parent_id, final Long parent_version, int index)\n
    '''
def createScenarioLinkItem():
    '''returns IloRowUpdate\n\n
    createScenarioLinkItem(final Long workspace_id, final Long parent_id, final Long parent_version, final Long scenario_id, int index)\n
    '''
def createWorkspace():
    '''returns IloRow\n\n
    createWorkspace()\n
    '''
def getRecycleBin():
    '''returns IloRow\n\n
    getRecycleBin()\n
    '''
def deleteItem():
    '''returns IloRowUpdate\n\n
    deleteItem(final Long workspace_id, final Long parent_id, final Long parent_version, final Long item_id, final Long item_version, final boolean move_recycle_bin)\n
    '''
def getLockVersion():
    '''returns Long\n\n
    getLockVersion(final Long workspace_id)\n
    '''
def getLocks():
    '''returns IloSchemaRowMap\n\n
    getLocks(final Long workspace_id, final Long current_version)\n
    '''
def getBulkLocks():
    '''returns IloSchemaRowMap\n\n
    getBulkLocks(final Long[] workspace_ids, final Long[] current_versions)\n
    '''
def getWorkspace():
    '''returns IloRow\n\n
    getWorkspace(final Long workspace_id)\n
    '''
def getWorkspaceItems():
    '''returns IloSchemaRowMap\n\n
    getWorkspaceItems(final Long workspace_id, final boolean include_workspace_items, final boolean include_scenario_items, final Long last_scenario_version)\n
    '''
def getWorkspaceUpdateStatus():
    '''returns IloUpdateStatus\n\n
    getWorkspaceUpdateStatus(final Long workspace_id)\n
    '''
def getWorkspaces():
    '''returns IloSchemaRowMap\n\n
    getWorkspaces()\n
    '''
def moveItem():
    '''returns IloRowUpdate\n\n
    moveItem(final Long workspace_id, final Long parent_id, final Long parent_version, final Long item_id, final Long item_version, int index)\n
    '''
def removeLock():
    '''returns None\n\n
    removeLock(final Long workspace_id, final Long lock_id)\n
    '''
def setName():
    '''returns IloRowUpdate\n\n
    setName(final Long workspace_id, final Long workspace_version, final String name)\n
    '''
def setItemName():
    '''returns IloRowUpdate\n\n
    setItemName(final Long workspace_id, final Long item_id, final Long item_version, final String name)\n
    '''
def tranfertLock():
    '''returns IloRow\n\n
    tranfertLock(final Long workspace_id, final Long lock_id, final Long user_id)\n
    '''
def delete():
    '''returns IloRowUpdate\n\n
    delete(final Long workspace_id, final boolean move_recycle_bin)\n
    '''
def importScenarioSet():
    '''returns IloRowUpdate\n\n
    importScenarioSet(final Long workspace_id, final Long parent_id, final Long parent_version, final File source)\n
    '''
def getRowUpdate():
    '''returns IloRowUpdate\n\n
    getRowUpdate()\n
    '''
def createChildFolder():
    '''returns IloWorkspaceFolder\n\n
    createChildFolder(final IloWorkspaceFolder parent, final String name)\n
    '''
def createChildScenario():
    '''returns IloScenarioLink\n\n
    createChildScenario(final IloWorkspaceFolder parent, final String name, final String uuid)\n
    '''
