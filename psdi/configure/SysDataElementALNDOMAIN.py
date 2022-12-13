def SysDataElementALNDOMAIN():
'''public SysDataElementALNDOMAIN()
public SysDataElementALNDOMAIN(final String name, final Namespace namespace)
public SysDataElementALNDOMAIN(final String name)
public SysDataElementALNDOMAIN(final String name, final String uri)
public SysDataElementALNDOMAIN(final String name, final String prefix, final String uri)
public SysDataElementALNDOMAIN(final String tbname, final TreeMap newCol, final TreeMap oldCol, final TreeMap newData, final TreeMap oldData, final TreeMap newDataOldKeys, final TreeMap keyCols, final File codefile)
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
def deleteRow():
'''public ArrayList deleteRow(final Element row)
'''
pass
def updateRow():
'''public ArrayList updateRow(final Element row, final HashMap currentData, final String siteid, final String orgid)
'''
pass
def insertRow():
'''public ArrayList insertRow(final Element row, final String siteid, final String orgid)
'''
pass
