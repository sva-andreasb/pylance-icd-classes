ALN = "int  1"
UPPER = "int  2"
LOWER = "int  3"
INTEGER = "int  4"
YORN = "int  5"
CRYPTO = "int  6"
def VMMDataMap():
'''public VMMDataMap()
'''
pass
def addDataMap():
'''public void addDataMap(final String tableId, String table, String column, final String attribute, final boolean keyColumn, final boolean required, final boolean allowRecDelete, final String type)
'''
pass
def getTableName():
'''public String getTableName(final String tableId)
'''
pass
def getTableId():
'''public String getTableId(final String objectName)
'''
pass
def getObjectName():
'''public String getObjectName(final String tableId, final Connection con)
'''
pass
def allowRecDelete():
'''public boolean allowRecDelete(final String tableId)
'''
pass
def getTableIds():
'''public Iterator getTableIds()
'''
pass
def isUniqueIdColumn():
'''public boolean isUniqueIdColumn(final String tableId, String column)
'''
pass
def isSysDateColumn():
'''public boolean isSysDateColumn(final String tableId, String column)
'''
pass
def getColumnNames():
'''public Iterator getColumnNames(final String tableId)
'''
pass
def getKeyColumnNames():
'''public Iterator getKeyColumnNames(final String tableId)
'''
pass
def getColumnNameForAttribute():
'''public String getColumnNameForAttribute(final String tableId, final String attributeName)
'''
pass
def isMappedToVMMAttribute():
'''public boolean isMappedToVMMAttribute(final String tableId, final String column)
'''
pass
def getAttribute():
'''public String getAttribute(final String tableId, String column)
'''
pass
def isRequired():
'''public boolean isRequired(final String tableId, String column)
public boolean isRequired()
'''
pass
def getType():
'''public String getType(final String tableId, String column)
public String getType()
'''
pass
def getTypeAsInt():
'''public int getTypeAsInt(final String tableId, String column)
public int getTypeAsInt()
'''
pass
def getVMMAttributes():
'''public String[] getVMMAttributes()
'''
pass
def toString():
'''public String toString()
'''
pass
def getAttributeName():
'''public String getAttributeName()
'''
pass
def setAttributeName():
'''public void setAttributeName(final String name)
'''
pass
def getColumnName():
'''public String getColumnName()
'''
pass
def setColumnName():
'''public void setColumnName(final String name)
'''
pass
def setRequired():
'''public void setRequired(final boolean req)
'''
pass
def setType():
'''public void setType(final String t)
'''
pass
