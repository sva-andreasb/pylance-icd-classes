def IndexDefinition():
    '''public IndexDefinition(final String tbname)
    public IndexDefinition(final Connection connection, final String tbname)
    '''
def addKey():
    '''public void addKey(final String column)
    public void addKey(final String column, final boolean ascending)
    '''
def giveSuggestedName():
    '''public void giveSuggestedName(final String ixname)
    '''
def setUnique():
    '''public void setUnique(final boolean uniqueIndex)
    '''
def setTextSearch():
    '''public void setTextSearch(final boolean textSearchIndex)
    '''
def setClustered():
    '''public void setClustered(final boolean clusteredIndex)
    '''
def getKeys():
    '''public List<String> getKeys()
    '''
def addFirstKey():
    '''public void addFirstKey(final String column, final boolean ascending)
    '''
def getTable():
    '''public String getTable()
    '''
def isClustered():
    '''public Boolean isClustered()
    '''
def getKeyDef():
    '''public Object getKeyDef()
    '''
def isUnique():
    '''public boolean isUnique()
    '''
def getIndexName():
    '''public String getIndexName()
    '''
def setIndexName():
    '''public void setIndexName(final String ixname)
    '''
def hasIndexName():
    '''public boolean hasIndexName()
    '''
def setPartition():
    '''public void setPartition(final String indexPartition)
    '''
def fetchIndexDefinition():
    '''public static List<IndexDefinition> fetchIndexDefinition(final Connection connection, final String whereClause)
    '''
def setRequired():
    '''public void setRequired(final boolean required)
    '''
def isTextSearch():
    '''public boolean isTextSearch()
    '''
def getPartition():
    '''public String getPartition()
    '''
def hasPartition():
    '''public boolean hasPartition()
    '''
def isRequired():
    '''public boolean isRequired()
    '''
def insertMetaData():
    '''public void insertMetaData(final Connection connection)
    '''
def includeTenantID():
    '''public boolean includeTenantID()
    '''
def setIncludeTenantID():
    '''public void setIncludeTenantID(final boolean includeTenantID)
    '''
