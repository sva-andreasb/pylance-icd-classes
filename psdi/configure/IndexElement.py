def IndexElement():
'''public IndexElement(final String name, final Namespace namespace)
public IndexElement(final String name)
public IndexElement(final String name, final String uri)
public IndexElement(final String name, final String prefix, final String uri)
public IndexElement(final String tbname, final String ixname, final HashMap newIndex, final HashMap oldIndex)
'''
pass
def getIndexName():
'''public String getIndexName()
'''
pass
def getIndexAttributes():
'''public List getIndexAttributes()
'''
pass
def getKeys():
'''public List getKeys()
'''
pass
def getColNames():
'''public String[] getColNames()
'''
pass
def getAddSql():
'''public ArrayList getAddSql(final String tbname, final String ixname, final Connection con, final Util util, HashMap oldIndex)
'''
pass
def getDropSql():
'''public ArrayList getDropSql(final String tbname, final String ixname, final Connection con, final Util util, final HashMap oldIndex)
'''
pass
def getStatus():
'''public String getStatus()
'''
pass
def getNewChanged():
'''public String getNewChanged()
'''
pass
def setNewChanged():
'''public void setNewChanged(final String in)
'''
pass
def getSequenceName():
'''public String getSequenceName(final String table, final String column)
'''
pass
def toHashmap():
'''public HashMap toHashmap(final HashMap oldMap)
'''
pass
