def SysDataElement():
'''public SysDataElement()
public SysDataElement(final String name, final Namespace namespace)
public SysDataElement(final String name)
public SysDataElement(final String name, final String uri)
public SysDataElement(final String name, final String prefix, final String uri)
public SysDataElement(final String tbname, final TreeMap newCol, final TreeMap oldCol, final TreeMap newData, final TreeMap oldData, final TreeMap newDataOldKeys, final TreeMap keyCols, final File codefile)
'''
pass
def loadDoNotUpdateCols():
'''public void loadDoNotUpdateCols()
'''
pass
def getTableName():
'''public String getTableName()
'''
pass
def setTableName():
'''public void setTableName(final String tableName)
'''
pass
def scanKeyCols():
'''public void scanKeyCols()
'''
pass
def buildFromHashMaps():
'''public void buildFromHashMaps()
'''
pass
def addOneRow():
'''public void addOneRow(final String key, final HashMap newVals)
'''
pass
def removeOneRow():
'''public void removeOneRow(final String key, final HashMap oldVals)
'''
pass
def compareRows():
'''public void compareRows(final String key, final HashMap newVals, final HashMap oldVals)
public ArrayList compareRows(final Element row, final TreeMap colsColno)
'''
pass
def setKeyAttributes():
'''public void setKeyAttributes(final Element row, final HashMap rowValues)
'''
pass
def haveDup():
'''public boolean haveDup(final Element checkEl)
'''
pass
def getKeys():
'''public List getKeys()
'''
pass
def getAttribute():
'''public Element getAttribute(final Element row, final String attrName)
'''
pass
def getSql():
'''public ArrayList getSql(final String tbname, final Connection con, final Util util, final TreeMap oldCol, final TreeMap keyCols)
'''
pass
def getDeleteSql():
'''public ArrayList getDeleteSql(final String tbname, final Connection con, final Util util, final TreeMap oldCol, final TreeMap keyCols)
'''
pass
def getWhereClause():
'''public String getWhereClause(final Element row, final boolean useSiteOrg, final String siteid, final String orgid)
'''
pass
def getStatus():
'''public String getStatus()
'''
pass
def setStatus():
'''public void setStatus(final String status)
'''
pass
def deleteRow():
'''public ArrayList deleteRow(final Element row)
'''
pass
def deleteRowExtension():
'''public ArrayList deleteRowExtension(final Element row, final ArrayList list)
'''
pass
def updateRow():
'''public ArrayList updateRow(final Element row, final HashMap currentData, final String siteid, final String orgid)
'''
pass
def canUpdateColumn():
'''public boolean canUpdateColumn(final String name)
'''
pass
def updateRowExtension():
'''public ArrayList updateRowExtension(final Element row, final HashMap currentData, final String siteid, final String orgid, final ArrayList list)
'''
pass
def insertRow():
'''public ArrayList insertRow(final Element row, final String siteid, final String orgid)
'''
pass
def insertRowExtension():
'''public ArrayList insertRowExtension(final Element row, final String siteid, final String orgid, final ArrayList list)
'''
pass
def getChunkUpdates():
'''public ArrayList getChunkUpdates(final Element row, final String colName, final String colValue, final int chunkSize)
'''
pass
def setUpgCodes():
'''public void setUpgCodes(final File codefile)
'''
pass
def addCodes():
'''public void addCodes(Element row, final String key)
'''
pass
def addCodesExtension():
'''public Element addCodesExtension(final Element row, final Element codeEl)
'''
pass
def getUpgCodesElement():
'''public Element getUpgCodesElement(final String key)
'''
pass
def getSequenceName():
'''public String getSequenceName(final String tableName, final String columnName)
'''
pass
def isUniqueColumnID():
'''public boolean isUniqueColumnID(final String columnName)
'''
pass
def initSequence():
'''public void initSequence(final String tableName)
'''
pass
def getMaxReserved():
'''public long getMaxReserved(final Element row)
'''
pass
def domainInUse():
'''public boolean domainInUse(final String domainID)
'''
pass
def getNextVal():
'''public int getNextVal(final String tableName, final String columnName)
'''
pass
def executeQuery():
'''public void executeQuery(final String sql)
'''
pass
