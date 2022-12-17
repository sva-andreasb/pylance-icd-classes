LOGGER = "String  \"maximo.application.rsconfig\""
def ():
    '''returns RSConfigSet\n\n
    (final MboServerInterface ms)\n
    '''
def getColumns():
    '''returns Vector\n\n
    getColumns()\n
    '''
def setQueryId():
    '''returns None\n\n
    setQueryId(final String newQueryId)\n
    '''
def getQueryAppName():
    '''returns String\n\n
    getQueryAppName()\n
    '''
def setQueryAppName():
    '''returns None\n\n
    setQueryAppName(final String newAppName)\n
    '''
def runQuery():
    '''returns MboSetRemote\n\n
    runQuery(final UserInfo ui, final String sTableName, final String sWhereClause)\n
    '''
def getColumnsAsArray():
    '''returns String[]\n\n
    getColumnsAsArray()\n
    '''
def getKeyColumn():
    '''returns String\n\n
    getKeyColumn()\n
    '''
def getNoOfRecords():
    '''returns int\n\n
    getNoOfRecords()\n
    '''
def setKeyColumn():
    '''returns None\n\n
    setKeyColumn(final String col)\n
    '''
def setNoOfRecords():
    '''returns None\n\n
    setNoOfRecords(final int num)\n
    '''
def getResultSetData():
    '''returns MboSetData\n\n
    getResultSetData(int start, final int rowcount, final String sortBy, final Hashtable qbes)\n
    '''
def getResultSetWhere():
    '''returns String\n\n
    getResultSetWhere()\n
    '''
def getResultSetWhereWithoutOrderBy():
    '''returns String\n\n
    getResultSetWhereWithoutOrderBy()\n
    '''
def getOriginalResultSetWhere():
    '''returns String\n\n
    getOriginalResultSetWhere()\n
    '''
def getDataForGraph():
    '''returns ArrayList\n\n
    getDataForGraph()\n
    '''
def getConditionAttribute():
    '''returns String\n\n
    getConditionAttribute()\n
    '''
def getGroupByAttribute():
    '''returns String[]\n\n
    getGroupByAttribute()\n
    '''
def getConditions():
    '''returns HashSet\n\n
    getConditions()\n
    '''
def setDetails():
    '''returns boolean\n\n
    setDetails(final long selectedQueryId)\n
    '''
def addFromResultSetColumn():
    '''returns None\n\n
    addFromResultSetColumn()\n
    addFromResultSetColumn(final String appName)\n
    '''
def getQueryInfo():
    '''returns MboRemote\n\n
    getQueryInfo(final long queryId)\n
    '''
def getQueryId():
    '''returns String\n\n
    getQueryId()\n
    '''
def setQueryDetails():
    '''returns None\n\n
    setQueryDetails()\n
    '''
def getGraphDetails():
    '''returns Properties\n\n
    getGraphDetails()\n
    '''
def setUpDefaults():
    '''returns None\n\n
    setUpDefaults()\n
    '''
def queryExists():
    '''returns boolean\n\n
    queryExists()\n
    '''
def clearData():
    '''returns None\n\n
    clearData()\n
    '''
def checkAttributeChange():
    '''returns None\n\n
    checkAttributeChange()\n
    '''
def isErrorRunningQuery():
    '''returns boolean\n\n
    isErrorRunningQuery()\n
    '''
def resetErrorRunningQuery():
    '''returns None\n\n
    resetErrorRunningQuery()\n
    '''
def getErrorMsg():
    '''returns String\n\n
    getErrorMsg()\n
    '''
def getGraphErrorMsg():
    '''returns String\n\n
    getGraphErrorMsg()\n
    '''
def setLookupValue():
    '''returns None\n\n
    setLookupValue(final String attrib, final String value)\n
    '''
def setLookupValueFromSetGraphOptionsDialog():
    '''returns None\n\n
    setLookupValueFromSetGraphOptionsDialog(final String value)\n
    '''
def deleteLabels():
    '''returns None\n\n
    deleteLabels()\n
    '''
def getNonPersistentAttributes():
    '''returns ArrayList\n\n
    getNonPersistentAttributes()\n
    '''
def clearErrorMsg():
    '''returns None\n\n
    clearErrorMsg()\n
    '''
def getResultSetMboSet():
    '''returns MboSetRemote\n\n
    getResultSetMboSet(final String orderBy)\n
    '''
