def disableControlTS():
    '''public void disableControlTS()
    '''
def ConfigDB():
    '''public ConfigDB()
    public ConfigDB(final MXServer server)
    '''
def setUpgradeCallout():
    '''public void setUpgradeCallout(final String val)
    '''
def process():
    '''public void process()
    '''
def setObjectNames():
    '''public void setObjectNames(final HashSet objects)
    '''
def setSRTableExists():
    '''public void setSRTableExists()
    '''
def checkForBackup():
    '''public boolean checkForBackup()
    '''
def adjustMetadata():
    '''public void adjustMetadata()
    '''
def spaceCheck():
    '''public boolean spaceCheck()
    '''
def getMetadata():
    '''public void getMetadata()
    '''
def configureTables():
    '''public void configureTables()
    '''
def rebuildExtensionView():
    '''public void rebuildExtensionView(final String objectName, final String tableName, final boolean isView)
    '''
def dropTable():
    '''public void dropTable(final String tablename)
    '''
def createTable():
    '''public void createTable(final HashMap objInfo)
    '''
def addRowstamp():
    '''public void addRowstamp(final String tablename)
    '''
def addTenantid():
    '''public void addTenantid(final String tablename, final String uniqueColumnName, final MTStorageType storageType)
    '''
def addUniqueColumnToImportedTable():
    '''public int addUniqueColumnToImportedTable(final String tablename, final String uniqueColumnName, final String sequenceName, final TreeMap attrs)
    '''
def createRowstampTrigger():
    '''public void createRowstampTrigger(final String tablename)
    '''
def rebuildTable():
    '''public void rebuildTable(final String tempTbName, final HashMap objInfo)
    '''
def changingVarcharMultiplier():
    '''public void changingVarcharMultiplier(final boolean val)
    '''
def alterTable():
    '''public void alterTable(final HashMap objInfo)
    '''
def addMTPermissions():
    '''public void addMTPermissions(final String tablename, final String uniqueColumnName, final MTStorageType storageType)
    '''
def getUpgradeDefaultSql():
    '''public ArrayList getUpgradeDefaultSql(String tablename, String columnname)
    '''
def refreshAttributes():
    '''public void refreshAttributes()
    '''
def updateTenantsDelta():
    '''public void updateTenantsDelta(final HashMap<String, HashMap<String, HashMap<String, String[]>>> changedObjects, final TreeMap<String, HashMap<String, String>> cfgAttrs, final Map<String, Integer> lastNumbers)
    '''
def updateDelta():
    '''public void updateDelta(final Connection tenantCon, final int tenanatId, final TreeMap<String, HashMap<String, String>> cfgAttrs, final Map<String, Integer> lastNumbers)
    '''
def renumberAttributeNumber():
    '''public int renumberAttributeNumber(final String objectname, final TreeMap attrs)
    '''
def configureViews():
    '''public void configureViews()
    '''
def refreshObjects():
    '''public void refreshObjects()
    '''
def configureIndexes():
    '''public void configureIndexes()
    '''
def rebuildIndexes():
    '''public void rebuildIndexes(TreeMap indexMeta)
    '''
def doLastUpdates():
    '''public void doLastUpdates()
    '''
def updateStoragePartition():
    '''public void updateStoragePartition()
    '''
def syncEauditParams():
    '''public void syncEauditParams()
    '''
def updateMaxvars():
    '''public void updateMaxvars()
    '''
def showLastMessages():
    '''public void showLastMessages()
    '''
def remindUserToCheckIndexes():
    '''public void remindUserToCheckIndexes()
    '''
def remindUserBadTriggers():
    '''public void remindUserBadTriggers()
    '''
def remindUserToRestoreData():
    '''public void remindUserToRestoreData()
    '''
def callRestoreFromBackup():
    '''public void callRestoreFromBackup()
    '''
def addQuotes():
    '''public String addQuotes(String value)
    '''
def doCommit():
    '''public void doCommit()
    '''
def doSql():
    '''public void doSql(final ArrayList list)
    public void doSql(final List list)
    public void doSql(final String sql)
    '''
def doSqlCatchReorg():
    '''public void doSqlCatchReorg(final AbstractList list)
    public void doSqlCatchReorg(final String sql)
    '''
def showMsg():
    '''public void showMsg(final String str)
    '''
def setBypassTextSearchForUpgrade():
    '''public void setBypassTextSearchForUpgrade(final boolean value)
    '''
def setDoReorgCheck():
    '''public void setDoReorgCheck(final boolean value)
    '''
def getTextSearchHelper():
    '''public TextSearch getTextSearchHelper()
    '''
def upgradeCallout():
    '''public void upgradeCallout(String methodName, final String methodPlace, String objectname)
    '''
def setThrowErrorFromPrechecks():
    '''public void setThrowErrorFromPrechecks(final boolean value)
    '''
def endSetupInstance():
    '''public void endSetupInstance(final String outdir, final String outfile, final HashMap params)
    '''
def endProcessInstance():
    '''public void endProcessInstance()
    '''
def setUserIfno():
    '''public void setUserIfno(final UserInfo ui)
    '''
def main():
    '''public static void main(final String[] argv)
    '''
