def ():
    '''returns IndexDefinition\n\n
    (final String tbname)\n
    (final Connection connection, final String tbname)\n
    '''
def addKey():
    '''returns None\n\n
    addKey(final String column)\n
    addKey(final String column, final boolean ascending)\n
    '''
def giveSuggestedName():
    '''returns None\n\n
    giveSuggestedName(final String ixname)\n
    '''
def setUnique():
    '''returns None\n\n
    setUnique(final boolean uniqueIndex)\n
    '''
def setTextSearch():
    '''returns None\n\n
    setTextSearch(final boolean textSearchIndex)\n
    '''
def setClustered():
    '''returns None\n\n
    setClustered(final boolean clusteredIndex)\n
    '''
def getKeys():
    '''returns List<String>\n\n
    getKeys()\n
    '''
def addFirstKey():
    '''returns None\n\n
    addFirstKey(final String column, final boolean ascending)\n
    '''
def getTable():
    '''returns String\n\n
    getTable()\n
    '''
def isClustered():
    '''returns Boolean\n\n
    isClustered()\n
    '''
def getKeyDef():
    '''returns Object\n\n
    getKeyDef()\n
    '''
def isUnique():
    '''returns boolean\n\n
    isUnique()\n
    '''
def getIndexName():
    '''returns String\n\n
    getIndexName()\n
    '''
def setIndexName():
    '''returns None\n\n
    setIndexName(final String ixname)\n
    '''
def hasIndexName():
    '''returns boolean\n\n
    hasIndexName()\n
    '''
def setPartition():
    '''returns None\n\n
    setPartition(final String indexPartition)\n
    '''
def setRequired():
    '''returns None\n\n
    setRequired(final boolean required)\n
    '''
def isTextSearch():
    '''returns boolean\n\n
    isTextSearch()\n
    '''
def getPartition():
    '''returns String\n\n
    getPartition()\n
    '''
def hasPartition():
    '''returns boolean\n\n
    hasPartition()\n
    '''
def isRequired():
    '''returns boolean\n\n
    isRequired()\n
    '''
def insertMetaData():
    '''returns None\n\n
    insertMetaData(final Connection connection)\n
    '''
def includeTenantID():
    '''returns boolean\n\n
    includeTenantID()\n
    '''
def setIncludeTenantID():
    '''returns None\n\n
    setIncludeTenantID(final boolean includeTenantID)\n
    '''
