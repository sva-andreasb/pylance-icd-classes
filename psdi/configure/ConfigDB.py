def disableControlTS():
'''public void disableControlTS()
'''
pass
def ConfigDB():
'''public ConfigDB()
public ConfigDB(final MXServer server)
'''
pass
def setUpgradeCallout():
'''public void setUpgradeCallout(final String val)
'''
pass
def process():
'''public void process()
'''
pass
def setObjectNames():
'''public void setObjectNames(final HashSet objects)
'''
pass
def setSRTableExists():
'''public void setSRTableExists()
'''
pass
def checkForBackup():
'''public boolean checkForBackup()
'''
pass
def adjustMetadata():
'''public void adjustMetadata()
'''
pass
def spaceCheck():
'''public boolean spaceCheck()
'''
pass
def getMetadata():
'''public void getMetadata()
'''
pass
def configureTables():
'''public void configureTables()
'''
pass
def rebuildExtensionView():
'''public void rebuildExtensionView(final String objectName, final String tableName, final boolean isView)
'''
pass
def dropTable():
'''public void dropTable(final String tablename)
'''
pass
def createTable():
'''public void createTable(final HashMap objInfo)
'''
pass
def addRowstamp():
'''public void addRowstamp(final String tablename)
'''
pass
def addTenantid():
'''public void addTenantid(final String tablename, final String uniqueColumnName, final MTStorageType storageType)
'''
pass
def addUniqueColumnToImportedTable():
'''public int addUniqueColumnToImportedTable(final String tablename, final String uniqueColumnName, final String sequenceName, final TreeMap attrs)
'''
pass
def createRowstampTrigger():
'''public void createRowstampTrigger(final String tablename)
'''
pass
def rebuildTable():
'''public void rebuildTable(final String tempTbName, final HashMap objInfo)
'''
pass
def changingVarcharMultiplier():
'''public void changingVarcharMultiplier(final boolean val)
'''
pass
def alterTable():
'''public void alterTable(final HashMap objInfo)
'''
pass
def addMTPermissions():
'''public void addMTPermissions(final String tablename, final String uniqueColumnName, final MTStorageType storageType)
'''
pass
def getUpgradeDefaultSql():
'''public ArrayList getUpgradeDefaultSql(String tablename, String columnname)
'''
pass
def refreshAttributes():
'''public void refreshAttributes()
'''
pass
def updateTenantsDelta():
'''public void updateTenantsDelta(final HashMap<String, HashMap<String, HashMap<String, String[]>>> changedObjects, final TreeMap<String, HashMap<String, String>> cfgAttrs, final Map<String, Integer> lastNumbers)
'''
pass
def updateDelta():
'''public void updateDelta(final Connection tenantCon, final int tenanatId, final TreeMap<String, HashMap<String, String>> cfgAttrs, final Map<String, Integer> lastNumbers)
'''
pass
def renumberAttributeNumber():
'''public int renumberAttributeNumber(final String objectname, final TreeMap attrs)
'''
pass
def configureViews():
'''public void configureViews()
'''
pass
def refreshObjects():
'''public void refreshObjects()
'''
pass
def configureIndexes():
'''public void configureIndexes()
'''
pass
def rebuildIndexes():
'''public void rebuildIndexes(TreeMap indexMeta)
'''
pass
def doLastUpdates():
'''public void doLastUpdates()
'''
pass
def updateStoragePartition():
'''public void updateStoragePartition()
'''
pass
def syncEauditParams():
'''public void syncEauditParams()
'''
pass
def updateMaxvars():
'''public void updateMaxvars()
'''
pass
def showLastMessages():
'''public void showLastMessages()
'''
pass
def remindUserToCheckIndexes():
'''public void remindUserToCheckIndexes()
'''
pass
def remindUserBadTriggers():
'''public void remindUserBadTriggers()
'''
pass
def remindUserToRestoreData():
'''public void remindUserToRestoreData()
'''
pass
def callRestoreFromBackup():
'''public void callRestoreFromBackup()
'''
pass
def addQuotes():
'''public String addQuotes(String value)
'''
pass
def doCommit():
'''public void doCommit()
'''
pass
def doSql():
'''public void doSql(final ArrayList list)
public void doSql(final List list)
public void doSql(final String sql)
'''
pass
def doSqlCatchReorg():
'''public void doSqlCatchReorg(final AbstractList list)
public void doSqlCatchReorg(final String sql)
'''
pass
def showMsg():
'''public void showMsg(final String str)
'''
pass
def setBypassTextSearchForUpgrade():
'''public void setBypassTextSearchForUpgrade(final boolean value)
'''
pass
def setDoReorgCheck():
'''public void setDoReorgCheck(final boolean value)
'''
pass
def getTextSearchHelper():
'''public TextSearch getTextSearchHelper()
'''
pass
def upgradeCallout():
'''public void upgradeCallout(String methodName, final String methodPlace, String objectname)
'''
pass
def setThrowErrorFromPrechecks():
'''public void setThrowErrorFromPrechecks(final boolean value)
'''
pass
def endSetupInstance():
'''public void endSetupInstance(final String outdir, final String outfile, final HashMap params)
'''
pass
def endProcessInstance():
'''public void endProcessInstance()
'''
pass
def setUserIfno():
'''public void setUserIfno(final UserInfo ui)
'''
pass
def main():
'''public static void main(final String[] argv)
'''
pass
