def login():
    '''    public String login(final String user, final String password, String host, final Integer port)
    '''
def logout():
    '''    public void logout()
    '''
def startDiscovery():
    '''    public void startDiscovery(final String[] scope, final String runName)
    '''
def abortDiscovery():
    '''    public void abortDiscovery()
    '''
def getStatus():
    '''    public String getStatus()
    '''
def clearTopology():
    '''    public void clearTopology()
    '''
def rebuildTopology():
    '''    public void rebuildTopology()
    '''
def find():
    '''    public String find(final String query, final int depth, final int indent, final String mssGuid)
    '''
def findUsingMssName():
    '''    public String findUsingMssName(final String query, final int depth, final int indent, final String mssName)
    '''
def findUsingGuid():
    '''    public String findUsingGuid(final String guid, final int depth, final int indent)
    '''
def findBasedOnChange():
    '''    public String findBasedOnChange(final String root, final int depth, final int indent, final long start, final long end, final int changeType)
    '''
def getClassNames():
    '''    public String getClassNames()
    '''
def insert():
    '''    public String insert(final String xml, final String mssGuid)
    '''
def insertUsingMssName():
    '''    public String insertUsingMssName(final String xml, final String mssName)
    '''
def getChangeHistory():
    '''    public String getChangeHistory(final String guid, final long start, final long end)
    public String getChangeHistory(final String[] guids, final long start, final long end)
    '''
def createVersion():
    '''    public String createVersion(final String name, final String description)
    '''
def createEmptyVersion():
    '''    public String createEmptyVersion(final String name, final String description)
    '''
def deleteVersion():
    '''    public void deleteVersion(final long versionId)
    '''
def deleteVersionUsingName():
    '''    public void deleteVersionUsingName(final String versionName)
    '''
def getAllVersions():
    '''    public String getAllVersions()
    '''
def exportData():
    '''    public void exportData(final String directoryToWriteTo, final long maxfilesize, final String mssGuid)
    '''
def exportDataUsingMssName():
    '''    public void exportDataUsingMssName(final String directoryToWriteTo, final long maxfilesize, final String mssName)
    '''
def importData():
    '''    public void importData(final String source, final boolean rebuildTopo, final long timeout, final String mssGuid)
    '''
def importDataUsingMssName():
    '''    public void importDataUsingMssName(final String source, final boolean rebuildTopo, final long timeout, final String mssName)
    '''
