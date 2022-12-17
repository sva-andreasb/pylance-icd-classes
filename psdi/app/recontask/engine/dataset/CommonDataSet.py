def ():
    '''returns CommonDataSet\n\n
    ()\n
    '''
def setContext():
    '''returns None\n\n
    setContext(final DataSetContext context)\n
    '''
def getDataSetName():
    '''returns String\n\n
    getDataSetName()\n
    '''
def setDataSetName():
    '''returns None\n\n
    setDataSetName(final String datasetName)\n
    '''
def getMainObjectPrimaryKeys():
    '''returns String[]\n\n
    getMainObjectPrimaryKeys()\n
    '''
def getMainObjectUID():
    '''returns String\n\n
    getMainObjectUID()\n
    '''
def getObjectUID():
    '''returns String\n\n
    getObjectUID(final String objectName)\n
    '''
def getMasterForSpec():
    '''returns String\n\n
    getMasterForSpec(final String objectname)\n
    '''
def getSpecForMaster():
    '''returns String\n\n
    getSpecForMaster(final String objectname)\n
    '''
def getFixedTaskFilterWhereClause():
    '''returns String\n\n
    getFixedTaskFilterWhereClause()\n
    '''
def getRootClassstructureID():
    '''returns String\n\n
    getRootClassstructureID(final String objectName)\n
    '''
def readMaxVar():
    '''returns String\n\n
    readMaxVar(final String varName, final boolean hasDefaultValue)\n
    '''
def getTableJoinWhereClauseForComparison():
    '''returns String\n\n
    getTableJoinWhereClauseForComparison(final String tableName, final Map uidKeys)\n
    '''
def getTableNameForTaskFilter():
    '''returns String\n\n
    getTableNameForTaskFilter(final String attributeName)\n
    '''
def getTableColumnNameForTaskFilter():
    '''returns String\n\n
    getTableColumnNameForTaskFilter(final String attributeName)\n
    '''
def getExtraTableNamesForComparison():
    '''returns String[]\n\n
    getExtraTableNamesForComparison(final String tableName)\n
    '''
def getTableJoinWhereClauseForTaskFilter():
    '''returns String\n\n
    getTableJoinWhereClauseForTaskFilter(final String tableName)\n
    '''
def getRecordCount():
    '''returns int\n\n
    getRecordCount(final Map uidKeys, final String objectName, final String classStructureID)\n
    '''
def isUnitOfMeasureAllowed():
    '''returns boolean\n\n
    isUnitOfMeasureAllowed(final String objectName)\n
    '''
def getTaskFilterClause():
    '''returns String\n\n
    getTaskFilterClause()\n
    '''
def setTaskFilterClause():
    '''returns None\n\n
    setTaskFilterClause(final String filterClause)\n
    '''
def getReconLinker():
    '''returns ReconLinkerI\n\n
    getReconLinker()\n
    '''
