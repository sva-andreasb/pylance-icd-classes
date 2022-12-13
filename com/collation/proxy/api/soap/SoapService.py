def login():
'''public String login(final String user, final String password, String host, final Integer port)
'''
pass
def logout():
'''public void logout()
'''
pass
def startDiscovery():
'''public void startDiscovery(final String[] scope, final String runName)
'''
pass
def abortDiscovery():
'''public void abortDiscovery()
'''
pass
def getStatus():
'''public String getStatus()
'''
pass
def clearTopology():
'''public void clearTopology()
'''
pass
def rebuildTopology():
'''public void rebuildTopology()
'''
pass
def find():
'''public String find(final String query, final int depth, final int indent, final String mssGuid)
'''
pass
def findUsingMssName():
'''public String findUsingMssName(final String query, final int depth, final int indent, final String mssName)
'''
pass
def findUsingGuid():
'''public String findUsingGuid(final String guid, final int depth, final int indent)
'''
pass
def findBasedOnChange():
'''public String findBasedOnChange(final String root, final int depth, final int indent, final long start, final long end, final int changeType)
'''
pass
def getClassNames():
'''public String getClassNames()
'''
pass
def insert():
'''public String insert(final String xml, final String mssGuid)
'''
pass
def insertUsingMssName():
'''public String insertUsingMssName(final String xml, final String mssName)
'''
pass
def getChangeHistory():
'''public String getChangeHistory(final String guid, final long start, final long end)
public String getChangeHistory(final String[] guids, final long start, final long end)
'''
pass
def createVersion():
'''public String createVersion(final String name, final String description)
'''
pass
def createEmptyVersion():
'''public String createEmptyVersion(final String name, final String description)
'''
pass
def deleteVersion():
'''public void deleteVersion(final long versionId)
'''
pass
def deleteVersionUsingName():
'''public void deleteVersionUsingName(final String versionName)
'''
pass
def getAllVersions():
'''public String getAllVersions()
'''
pass
def exportData():
'''public void exportData(final String directoryToWriteTo, final long maxfilesize, final String mssGuid)
'''
pass
def exportDataUsingMssName():
'''public void exportDataUsingMssName(final String directoryToWriteTo, final long maxfilesize, final String mssName)
'''
pass
def importData():
'''public void importData(final String source, final boolean rebuildTopo, final long timeout, final String mssGuid)
'''
pass
def importDataUsingMssName():
'''public void importDataUsingMssName(final String source, final boolean rebuildTopo, final long timeout, final String mssName)
'''
pass
