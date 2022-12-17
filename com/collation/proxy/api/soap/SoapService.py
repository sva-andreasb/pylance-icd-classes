def login():
    '''returns String\n\n
    login(final String user, final String password, String host, final Integer port)\n
    '''
def logout():
    '''returns None\n\n
    logout()\n
    '''
def startDiscovery():
    '''returns None\n\n
    startDiscovery(final String[] scope, final String runName)\n
    '''
def abortDiscovery():
    '''returns None\n\n
    abortDiscovery()\n
    '''
def getStatus():
    '''returns String\n\n
    getStatus()\n
    '''
def clearTopology():
    '''returns None\n\n
    clearTopology()\n
    '''
def rebuildTopology():
    '''returns None\n\n
    rebuildTopology()\n
    '''
def find():
    '''returns String\n\n
    find(final String query, final int depth, final int indent, final String mssGuid)\n
    '''
def findUsingMssName():
    '''returns String\n\n
    findUsingMssName(final String query, final int depth, final int indent, final String mssName)\n
    '''
def findUsingGuid():
    '''returns String\n\n
    findUsingGuid(final String guid, final int depth, final int indent)\n
    '''
def findBasedOnChange():
    '''returns String\n\n
    findBasedOnChange(final String root, final int depth, final int indent, final long start, final long end, final int changeType)\n
    '''
def getClassNames():
    '''returns String\n\n
    getClassNames()\n
    '''
def insert():
    '''returns String\n\n
    insert(final String xml, final String mssGuid)\n
    '''
def insertUsingMssName():
    '''returns String\n\n
    insertUsingMssName(final String xml, final String mssName)\n
    '''
def getChangeHistory():
    '''returns String\n\n
    getChangeHistory(final String guid, final long start, final long end)\n
    getChangeHistory(final String[] guids, final long start, final long end)\n
    '''
def createVersion():
    '''returns String\n\n
    createVersion(final String name, final String description)\n
    '''
def createEmptyVersion():
    '''returns String\n\n
    createEmptyVersion(final String name, final String description)\n
    '''
def deleteVersion():
    '''returns None\n\n
    deleteVersion(final long versionId)\n
    '''
def deleteVersionUsingName():
    '''returns None\n\n
    deleteVersionUsingName(final String versionName)\n
    '''
def getAllVersions():
    '''returns String\n\n
    getAllVersions()\n
    '''
def exportData():
    '''returns None\n\n
    exportData(final String directoryToWriteTo, final long maxfilesize, final String mssGuid)\n
    '''
def exportDataUsingMssName():
    '''returns None\n\n
    exportDataUsingMssName(final String directoryToWriteTo, final long maxfilesize, final String mssName)\n
    '''
def importData():
    '''returns None\n\n
    importData(final String source, final boolean rebuildTopo, final long timeout, final String mssGuid)\n
    '''
def importDataUsingMssName():
    '''returns None\n\n
    importDataUsingMssName(final String source, final boolean rebuildTopo, final long timeout, final String mssName)\n
    '''
