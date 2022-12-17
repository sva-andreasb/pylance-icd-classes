def disableControlTS():
    '''returns None\n\n
    disableControlTS()\n
    '''
def ():
    '''returns ConfigDB\n\n
    ()\n
    (final MXServer server)\n
    '''
def setUpgradeCallout():
    '''returns None\n\n
    setUpgradeCallout(final String val)\n
    '''
def process():
    '''returns None\n\n
    process()\n
    '''
def setObjectNames():
    '''returns None\n\n
    setObjectNames(final HashSet objects)\n
    '''
def setSRTableExists():
    '''returns None\n\n
    setSRTableExists()\n
    '''
def checkForBackup():
    '''returns boolean\n\n
    checkForBackup()\n
    '''
def adjustMetadata():
    '''returns None\n\n
    adjustMetadata()\n
    '''
def spaceCheck():
    '''returns boolean\n\n
    spaceCheck()\n
    '''
def getMetadata():
    '''returns None\n\n
    getMetadata()\n
    '''
def configureTables():
    '''returns None\n\n
    configureTables()\n
    '''
def rebuildExtensionView():
    '''returns None\n\n
    rebuildExtensionView(final String objectName, final String tableName, final boolean isView)\n
    '''
def dropTable():
    '''returns None\n\n
    dropTable(final String tablename)\n
    '''
def createTable():
    '''returns None\n\n
    createTable(final HashMap objInfo)\n
    '''
def addRowstamp():
    '''returns None\n\n
    addRowstamp(final String tablename)\n
    '''
def addTenantid():
    '''returns None\n\n
    addTenantid(final String tablename, final String uniqueColumnName, final MTStorageType storageType)\n
    '''
def addUniqueColumnToImportedTable():
    '''returns int\n\n
    addUniqueColumnToImportedTable(final String tablename, final String uniqueColumnName, final String sequenceName, final TreeMap attrs)\n
    '''
def createRowstampTrigger():
    '''returns None\n\n
    createRowstampTrigger(final String tablename)\n
    '''
def rebuildTable():
    '''returns None\n\n
    rebuildTable(final String tempTbName, final HashMap objInfo)\n
    '''
def changingVarcharMultiplier():
    '''returns None\n\n
    changingVarcharMultiplier(final boolean val)\n
    '''
def alterTable():
    '''returns None\n\n
    alterTable(final HashMap objInfo)\n
    '''
def addMTPermissions():
    '''returns None\n\n
    addMTPermissions(final String tablename, final String uniqueColumnName, final MTStorageType storageType)\n
    '''
def getUpgradeDefaultSql():
    '''returns ArrayList\n\n
    getUpgradeDefaultSql(String tablename, String columnname)\n
    '''
def refreshAttributes():
    '''returns None\n\n
    refreshAttributes()\n
    '''
def updateTenantsDelta():
    '''returns None\n\n
    updateTenantsDelta(final HashMap<String, HashMap<String, HashMap<String, String[]>>> changedObjects, final TreeMap<String, HashMap<String, String>> cfgAttrs, final Map<String, Integer> lastNumbers)\n
    '''
def updateDelta():
    '''returns None\n\n
    updateDelta(final Connection tenantCon, final int tenanatId, final TreeMap<String, HashMap<String, String>> cfgAttrs, final Map<String, Integer> lastNumbers)\n
    '''
def renumberAttributeNumber():
    '''returns int\n\n
    renumberAttributeNumber(final String objectname, final TreeMap attrs)\n
    '''
def configureViews():
    '''returns None\n\n
    configureViews()\n
    '''
def refreshObjects():
    '''returns None\n\n
    refreshObjects()\n
    '''
def configureIndexes():
    '''returns None\n\n
    configureIndexes()\n
    '''
def rebuildIndexes():
    '''returns None\n\n
    rebuildIndexes(TreeMap indexMeta)\n
    '''
def doLastUpdates():
    '''returns None\n\n
    doLastUpdates()\n
    '''
def updateStoragePartition():
    '''returns None\n\n
    updateStoragePartition()\n
    '''
def syncEauditParams():
    '''returns None\n\n
    syncEauditParams()\n
    '''
def updateMaxvars():
    '''returns None\n\n
    updateMaxvars()\n
    '''
def showLastMessages():
    '''returns None\n\n
    showLastMessages()\n
    '''
def remindUserToCheckIndexes():
    '''returns None\n\n
    remindUserToCheckIndexes()\n
    '''
def remindUserBadTriggers():
    '''returns None\n\n
    remindUserBadTriggers()\n
    '''
def remindUserToRestoreData():
    '''returns None\n\n
    remindUserToRestoreData()\n
    '''
def callRestoreFromBackup():
    '''returns None\n\n
    callRestoreFromBackup()\n
    '''
def addQuotes():
    '''returns String\n\n
    addQuotes(String value)\n
    '''
def doCommit():
    '''returns None\n\n
    doCommit()\n
    '''
def doSql():
    '''returns None\n\n
    doSql(final ArrayList list)\n
    doSql(final List list)\n
    doSql(final String sql)\n
    '''
def doSqlCatchReorg():
    '''returns None\n\n
    doSqlCatchReorg(final AbstractList list)\n
    doSqlCatchReorg(final String sql)\n
    '''
def showMsg():
    '''returns None\n\n
    showMsg(final String str)\n
    '''
def setBypassTextSearchForUpgrade():
    '''returns None\n\n
    setBypassTextSearchForUpgrade(final boolean value)\n
    '''
def setDoReorgCheck():
    '''returns None\n\n
    setDoReorgCheck(final boolean value)\n
    '''
def getTextSearchHelper():
    '''returns TextSearch\n\n
    getTextSearchHelper()\n
    '''
def upgradeCallout():
    '''returns None\n\n
    upgradeCallout(String methodName, final String methodPlace, String objectname)\n
    '''
def setThrowErrorFromPrechecks():
    '''returns None\n\n
    setThrowErrorFromPrechecks(final boolean value)\n
    '''
def endSetupInstance():
    '''returns None\n\n
    endSetupInstance(final String outdir, final String outfile, final HashMap params)\n
    '''
def endProcessInstance():
    '''returns None\n\n
    endProcessInstance()\n
    '''
def setUserIfno():
    '''returns None\n\n
    setUserIfno(final UserInfo ui)\n
    '''
