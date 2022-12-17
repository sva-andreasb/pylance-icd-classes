def ():
    '''returns SysDataElement\n\n
    ()\n
    (final String name, final Namespace namespace)\n
    (final String name)\n
    (final String name, final String uri)\n
    (final String name, final String prefix, final String uri)\n
    (final String tbname, final TreeMap newCol, final TreeMap oldCol, final TreeMap newData, final TreeMap oldData, final TreeMap newDataOldKeys, final TreeMap keyCols, final File codefile)\n
    '''
def loadDoNotUpdateCols():
    '''returns None\n\n
    loadDoNotUpdateCols()\n
    '''
def getTableName():
    '''returns String\n\n
    getTableName()\n
    '''
def setTableName():
    '''returns None\n\n
    setTableName(final String tableName)\n
    '''
def scanKeyCols():
    '''returns None\n\n
    scanKeyCols()\n
    '''
def buildFromHashMaps():
    '''returns None\n\n
    buildFromHashMaps()\n
    '''
def addOneRow():
    '''returns None\n\n
    addOneRow(final String key, final HashMap newVals)\n
    '''
def removeOneRow():
    '''returns None\n\n
    removeOneRow(final String key, final HashMap oldVals)\n
    '''
def compareRows():
    '''returns ArrayList\n\n
    compareRows(final String key, final HashMap newVals, final HashMap oldVals)\n
    compareRows(final Element row, final TreeMap colsColno)\n
    '''
def setKeyAttributes():
    '''returns None\n\n
    setKeyAttributes(final Element row, final HashMap rowValues)\n
    '''
def haveDup():
    '''returns boolean\n\n
    haveDup(final Element checkEl)\n
    '''
def getKeys():
    '''returns List\n\n
    getKeys()\n
    '''
def getAttribute():
    '''returns Element\n\n
    getAttribute(final Element row, final String attrName)\n
    '''
def getSql():
    '''returns ArrayList\n\n
    getSql(final String tbname, final Connection con, final Util util, final TreeMap oldCol, final TreeMap keyCols)\n
    '''
def getDeleteSql():
    '''returns ArrayList\n\n
    getDeleteSql(final String tbname, final Connection con, final Util util, final TreeMap oldCol, final TreeMap keyCols)\n
    '''
def getWhereClause():
    '''returns String\n\n
    getWhereClause(final Element row, final boolean useSiteOrg, final String siteid, final String orgid)\n
    '''
def getStatus():
    '''returns String\n\n
    getStatus()\n
    '''
def setStatus():
    '''returns None\n\n
    setStatus(final String status)\n
    '''
def deleteRow():
    '''returns ArrayList\n\n
    deleteRow(final Element row)\n
    '''
def deleteRowExtension():
    '''returns ArrayList\n\n
    deleteRowExtension(final Element row, final ArrayList list)\n
    '''
def updateRow():
    '''returns ArrayList\n\n
    updateRow(final Element row, final HashMap currentData, final String siteid, final String orgid)\n
    '''
def canUpdateColumn():
    '''returns boolean\n\n
    canUpdateColumn(final String name)\n
    '''
def updateRowExtension():
    '''returns ArrayList\n\n
    updateRowExtension(final Element row, final HashMap currentData, final String siteid, final String orgid, final ArrayList list)\n
    '''
def insertRow():
    '''returns ArrayList\n\n
    insertRow(final Element row, final String siteid, final String orgid)\n
    '''
def insertRowExtension():
    '''returns ArrayList\n\n
    insertRowExtension(final Element row, final String siteid, final String orgid, final ArrayList list)\n
    '''
def getChunkUpdates():
    '''returns ArrayList\n\n
    getChunkUpdates(final Element row, final String colName, final String colValue, final int chunkSize)\n
    '''
def setUpgCodes():
    '''returns None\n\n
    setUpgCodes(final File codefile)\n
    '''
def addCodes():
    '''returns None\n\n
    addCodes(Element row, final String key)\n
    '''
def addCodesExtension():
    '''returns Element\n\n
    addCodesExtension(final Element row, final Element codeEl)\n
    '''
def getUpgCodesElement():
    '''returns Element\n\n
    getUpgCodesElement(final String key)\n
    '''
def getSequenceName():
    '''returns String\n\n
    getSequenceName(final String tableName, final String columnName)\n
    '''
def isUniqueColumnID():
    '''returns boolean\n\n
    isUniqueColumnID(final String columnName)\n
    '''
def initSequence():
    '''returns None\n\n
    initSequence(final String tableName)\n
    '''
def getMaxReserved():
    '''returns long\n\n
    getMaxReserved(final Element row)\n
    '''
def domainInUse():
    '''returns boolean\n\n
    domainInUse(final String domainID)\n
    '''
def getNextVal():
    '''returns int\n\n
    getNextVal(final String tableName, final String columnName)\n
    '''
def executeQuery():
    '''returns None\n\n
    executeQuery(final String sql)\n
    '''
