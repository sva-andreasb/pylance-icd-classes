HOSTNAME = "String  \"HOSTNAME\""
PORT = "String  \"PORT\""
USERNAME = "String  \"USERNAME\""
PASSWORD = "String  \"PASSWORD\""
def ():
    '''returns TADDMHandler\n\n
    (final MaxEndPointInfo endPointInfo)\n
    ()\n
    '''
def invoke():
    '''returns byte[]\n\n
    invoke(final Map<String, ?> metaData, byte[] data)\n
    '''
def getProperties():
    '''returns List<RouterPropsInfo>\n\n
    getProperties()\n
    '''
def getCollectionGuidByName():
    '''returns Guid\n\n
    getCollectionGuidByName(final String colName)\n
    '''
def addMembersToCollection():
    '''returns None\n\n
    addMembersToCollection(final Guid collection, final Guid[] members)\n
    '''
def removeMembersToCollection():
    '''returns None\n\n
    removeMembersToCollection(final Guid collection, final Guid[] members)\n
    '''
def addAccessCollection():
    '''returns Guid\n\n
    addAccessCollection(final Guid mssGuid, final String collectionName)\n
    '''
def deleteAccessCollection():
    '''returns int\n\n
    deleteAccessCollection(final Guid mssGuid, final Guid collectionGuid)\n
    '''
