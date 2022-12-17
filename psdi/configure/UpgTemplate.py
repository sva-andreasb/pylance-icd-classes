def ():
    '''returns UpgTemplate\n\n
    (final CommonShell shell)\n
    '''
def doSql():
    '''returns None\n\n
    doSql(final AbstractList list)\n
    doSql(final String sql)\n
    '''
def buildRenameColumnStatement():
    '''returns ArrayList\n\n
    buildRenameColumnStatement(final String tableName, final String oldColumnName, final String newColumnName)\n
    '''
def showMXException():
    '''returns None\n\n
    showMXException(final MXApplicationException e, final boolean infoOnly, final boolean hideErrorKey)\n
    showMXException(final MXApplicationException e)\n
    '''
def getDisplayMessage():
    '''returns String\n\n
    getDisplayMessage(final String errorkey, final Object[] params)\n
    getDisplayMessage(final String errorgroup, final String errorkey, final Object[] params)\n
    getDisplayMessage(final String errorkey)\n
    '''
def updateStatistics():
    '''returns None\n\n
    updateStatistics(final ArrayList tables, final TreeMap indexes)\n
    '''
def doSqlProcedure():
    '''returns None\n\n
    doSqlProcedure(final String storedProcedure, final LinkedHashMap<Object, Integer> parameters)\n
    '''
