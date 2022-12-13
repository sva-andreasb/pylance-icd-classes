def IndexDefinition():
'''public IndexDefinition(final String tbname)
public IndexDefinition(final Connection connection, final String tbname)
'''
pass
def addKey():
'''public void addKey(final String column)
public void addKey(final String column, final boolean ascending)
'''
pass
def giveSuggestedName():
'''public void giveSuggestedName(final String ixname)
'''
pass
def setUnique():
'''public void setUnique(final boolean uniqueIndex)
'''
pass
def setTextSearch():
'''public void setTextSearch(final boolean textSearchIndex)
'''
pass
def setClustered():
'''public void setClustered(final boolean clusteredIndex)
'''
pass
def getKeys():
'''public List<String> getKeys()
'''
pass
def addFirstKey():
'''public void addFirstKey(final String column, final boolean ascending)
'''
pass
def getTable():
'''public String getTable()
'''
pass
def isClustered():
'''public Boolean isClustered()
'''
pass
def getKeyDef():
'''public Object getKeyDef()
'''
pass
def isUnique():
'''public boolean isUnique()
'''
pass
def getIndexName():
'''public String getIndexName()
'''
pass
def setIndexName():
'''public void setIndexName(final String ixname)
'''
pass
def hasIndexName():
'''public boolean hasIndexName()
'''
pass
def setPartition():
'''public void setPartition(final String indexPartition)
'''
pass
def fetchIndexDefinition():
'''public static List<IndexDefinition> fetchIndexDefinition(final Connection connection, final String whereClause)
'''
pass
def setRequired():
'''public void setRequired(final boolean required)
'''
pass
def isTextSearch():
'''public boolean isTextSearch()
'''
pass
def getPartition():
'''public String getPartition()
'''
pass
def hasPartition():
'''public boolean hasPartition()
'''
pass
def isRequired():
'''public boolean isRequired()
'''
pass
def insertMetaData():
'''public void insertMetaData(final Connection connection)
'''
pass
def includeTenantID():
'''public boolean includeTenantID()
'''
pass
def setIncludeTenantID():
'''public void setIncludeTenantID(final boolean includeTenantID)
'''
pass
