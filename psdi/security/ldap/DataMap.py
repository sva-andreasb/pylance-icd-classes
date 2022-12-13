ALN = "int  1"
UPPER = "int  2"
LOWER = "int  3"
INTEGER = "int  4"
YORN = "int  5"
CRYPTO = "int  6"
def DataMap():
    '''public DataMap()
    '''
def addDataMap():
    '''public void addDataMap(final String tableId, String table, String column, final String attribute, final boolean keyColumn, final boolean required, final boolean allowRecDelete, final String type)
    '''
def getTableName():
    '''public String getTableName(final String tableId)
    '''
def getTableId():
    '''public String getTableId(final String objectName)
    '''
def getObjectName():
    '''public String getObjectName(final String tableId, final Connection con)
    '''
def allowRecDelete():
    '''public boolean allowRecDelete(final String tableId)
    '''
def getTableIds():
    '''public Iterator getTableIds()
    '''
def isUniqueIdColumn():
    '''public boolean isUniqueIdColumn(final String tableId, String column)
    '''
def isSysDateColumn():
    '''public boolean isSysDateColumn(final String tableId, String column)
    '''
def getColumnNames():
    '''public Iterator getColumnNames(final String tableId)
    '''
def getKeyColumnNames():
    '''public Iterator getKeyColumnNames(final String tableId)
    '''
def getColumnNameForAttribute():
    '''public String getColumnNameForAttribute(final String tableId, final String attributeName)
    '''
def isMappedToLdapAttribute():
    '''public boolean isMappedToLdapAttribute(final String tableId, final String column)
    '''
def getAttribute():
    '''public String getAttribute(final String tableId, String column)
    '''
def isRequired():
    '''public boolean isRequired(final String tableId, String column)
    public boolean isRequired()
    '''
def getType():
    '''public String getType(final String tableId, String column)
    public String getType()
    '''
def getTypeAsInt():
    '''public int getTypeAsInt(final String tableId, String column)
    public int getTypeAsInt()
    '''
def getLdapAttributes():
    '''public String[] getLdapAttributes()
    '''
def toString():
    '''public String toString()
    '''
def getAttributeName():
    '''public String getAttributeName()
    '''
def setAttributeName():
    '''public void setAttributeName(final String name)
    '''
def getColumnName():
    '''public String getColumnName()
    '''
def setColumnName():
    '''public void setColumnName(final String name)
    '''
def setRequired():
    '''public void setRequired(final boolean req)
    '''
def setType():
    '''public void setType(final String t)
    '''
