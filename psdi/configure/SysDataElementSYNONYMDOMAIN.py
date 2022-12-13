def SysDataElementSYNONYMDOMAIN():
    '''    public SysDataElementSYNONYMDOMAIN()
    public SysDataElementSYNONYMDOMAIN(final String name, final Namespace namespace)
    public SysDataElementSYNONYMDOMAIN(final String name)
    public SysDataElementSYNONYMDOMAIN(final String name, final String uri)
    public SysDataElementSYNONYMDOMAIN(final String name, final String prefix, final String uri)
    public SysDataElementSYNONYMDOMAIN(final String tbname, final TreeMap newCol, final TreeMap oldCol, final TreeMap newData, final TreeMap oldData, final TreeMap newDataOldKeys, final TreeMap keyCols, final File codefile)
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
def getSql():
    '''    public ArrayList getSql(final String tbname, final Connection con, final Util util, final TreeMap oldCol, final TreeMap keyCols)
    '''
def getDeleteSql():
    '''    public ArrayList getDeleteSql(final String tbname, final Connection con, final Util util, final TreeMap oldCol, final TreeMap keyCols)
    '''
def getWhereClause():
    '''    public String getWhereClause(final Element row, final boolean useSiteOrg, final String siteid, final String orgid)
    '''
def deleteRow():
    '''    public ArrayList deleteRow(final Element row)
    '''
def updateRow():
    '''    public ArrayList updateRow(final Element row, final HashMap currentData, final String siteid, final String orgid)
    '''
def insertRow():
    '''    public ArrayList insertRow(final Element row, final String siteid, final String orgid)
    '''
