def SysDataElement():
    '''    public SysDataElement()
    public SysDataElement(final String name, final Namespace namespace)
    public SysDataElement(final String name)
    public SysDataElement(final String name, final String uri)
    public SysDataElement(final String name, final String prefix, final String uri)
    public SysDataElement(final String tbname, final TreeMap newCol, final TreeMap oldCol, final TreeMap newData, final TreeMap oldData, final TreeMap newDataOldKeys, final TreeMap keyCols, final File codefile)
    '''
def loadDoNotUpdateCols():
    '''    public void loadDoNotUpdateCols()
    '''
def getTableName():
    '''    public String getTableName()
    '''
def setTableName():
    '''    public void setTableName(final String tableName)
    '''
def scanKeyCols():
    '''    public void scanKeyCols()
    '''
def buildFromHashMaps():
    '''    public void buildFromHashMaps()
    '''
def addOneRow():
    '''    public void addOneRow(final String key, final HashMap newVals)
    '''
def removeOneRow():
    '''    public void removeOneRow(final String key, final HashMap oldVals)
    '''
def compareRows():
    '''    public void compareRows(final String key, final HashMap newVals, final HashMap oldVals)
    public ArrayList compareRows(final Element row, final TreeMap colsColno)
    '''
def setKeyAttributes():
    '''    public void setKeyAttributes(final Element row, final HashMap rowValues)
    '''
def haveDup():
    '''    public boolean haveDup(final Element checkEl)
    '''
def getKeys():
    '''    public List getKeys()
    '''
def getAttribute():
    '''    public Element getAttribute(final Element row, final String attrName)
    '''
def getSql():
    '''    public ArrayList getSql(final String tbname, final Connection con, final Util util, final TreeMap oldCol, final TreeMap keyCols)
    '''
def getDeleteSql():
    '''    public ArrayList getDeleteSql(final String tbname, final Connection con, final Util util, final TreeMap oldCol, final TreeMap keyCols)
    '''
def getWhereClause():
    '''    public String getWhereClause(final Element row, final boolean useSiteOrg, final String siteid, final String orgid)
    '''
def getStatus():
    '''    public String getStatus()
    '''
def setStatus():
    '''    public void setStatus(final String status)
    '''
def deleteRow():
    '''    public ArrayList deleteRow(final Element row)
    '''
def deleteRowExtension():
    '''    public ArrayList deleteRowExtension(final Element row, final ArrayList list)
    '''
def updateRow():
    '''    public ArrayList updateRow(final Element row, final HashMap currentData, final String siteid, final String orgid)
    '''
def canUpdateColumn():
    '''    public boolean canUpdateColumn(final String name)
    '''
def updateRowExtension():
    '''    public ArrayList updateRowExtension(final Element row, final HashMap currentData, final String siteid, final String orgid, final ArrayList list)
    '''
def insertRow():
    '''    public ArrayList insertRow(final Element row, final String siteid, final String orgid)
    '''
def insertRowExtension():
    '''    public ArrayList insertRowExtension(final Element row, final String siteid, final String orgid, final ArrayList list)
    '''
def getChunkUpdates():
    '''    public ArrayList getChunkUpdates(final Element row, final String colName, final String colValue, final int chunkSize)
    '''
def setUpgCodes():
    '''    public void setUpgCodes(final File codefile)
    '''
def addCodes():
    '''    public void addCodes(Element row, final String key)
    '''
def addCodesExtension():
    '''    public Element addCodesExtension(final Element row, final Element codeEl)
    '''
def getUpgCodesElement():
    '''    public Element getUpgCodesElement(final String key)
    '''
def getSequenceName():
    '''    public String getSequenceName(final String tableName, final String columnName)
    '''
def isUniqueColumnID():
    '''    public boolean isUniqueColumnID(final String columnName)
    '''
def initSequence():
    '''    public void initSequence(final String tableName)
    '''
def getMaxReserved():
    '''    public long getMaxReserved(final Element row)
    '''
def domainInUse():
    '''    public boolean domainInUse(final String domainID)
    '''
def getNextVal():
    '''    public int getNextVal(final String tableName, final String columnName)
    '''
def executeQuery():
    '''    public void executeQuery(final String sql)
    '''
