def ():
    '''returns SysDataElementALNDOMAIN\n\n
    ()\n
    (final String name, final Namespace namespace)\n
    (final String name)\n
    (final String name, final String uri)\n
    (final String name, final String prefix, final String uri)\n
    (final String tbname, final TreeMap newCol, final TreeMap oldCol, final TreeMap newData, final TreeMap oldData, final TreeMap newDataOldKeys, final TreeMap keyCols, final File codefile)\n
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
def deleteRow():
    '''returns ArrayList\n\n
    deleteRow(final Element row)\n
    '''
def updateRow():
    '''returns ArrayList\n\n
    updateRow(final Element row, final HashMap currentData, final String siteid, final String orgid)\n
    '''
def insertRow():
    '''returns ArrayList\n\n
    insertRow(final Element row, final String siteid, final String orgid)\n
    '''
