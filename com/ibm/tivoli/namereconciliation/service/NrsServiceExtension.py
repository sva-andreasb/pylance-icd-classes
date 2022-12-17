def ():
    '''returns NrsServiceExtension\n\n
    ()\n
    '''
def registerMSS():
    '''returns Guid\n\n
    registerMSS(final HashMap mss)\n
    '''
def updateMSS():
    '''returns None\n\n
    updateMSS(final HashMap mss, final boolean checkIdentifyingAttributes)\n
    '''
def deleteMSS():
    '''returns None\n\n
    deleteMSS(final Guid mssGuid)\n
    '''
def getMSS():
    '''returns HashMap[]\n\n
    getMSS(final Date date)\n
    '''
def registerAttributes():
    '''returns None\n\n
    registerAttributes(final Guid mssGuid, final Guid[] guids, final HashMap[] attributeMaps, final HashMap[] cleansedAttributeMaps)\n
    '''
def addAttribute():
    '''returns PreparedStatement\n\n
    addAttribute(PreparedStatement addPreparedStmt, final byte[] mssGuid, final byte[] meGuid, final byte[] attrGuid, final String attrName, final String standardValue, final String oldValue, final int isIdentifyingAttr)\n
    '''
def addSourceToken():
    '''returns PreparedStatement\n\n
    addSourceToken(PreparedStatement addPreparedStmt, final byte[] mssGuid, final byte[] meGuid, final String sourceToken)\n
    '''
def update():
    '''returns None\n\n
    update(final Guid mssGuid, final HashMap[] attributeMaps)\n
    '''
def delete():
    '''returns None\n\n
    delete(final Guid mssGuid, final Guid[] guids)\n
    '''
def getDeleted():
    '''returns Guid[]\n\n
    getDeleted(final String classType, final Date date)\n
    '''
def addRelationships():
    '''returns Guid[]\n\n
    addRelationships(final Guid mssGuid, final HashMap[] relationships)\n
    '''
def addRelationshipsOracle():
    '''returns Guid[]\n\n
    addRelationshipsOracle(final Guid mssGuid, final HashMap[] relationships)\n
    '''
def addRelationship():
    '''returns PreparedStatement\n\n
    addRelationship(PreparedStatement addPreparedStmt, final byte[] relGuid, final String relType, final byte[] sourceClass, final byte[] sourceGuid, final byte[] targetClass, final byte[] targetGuid, final String label)\n
    '''
def addMSSRelationship():
    '''returns PreparedStatement\n\n
    addMSSRelationship(PreparedStatement addPreparedStmt, final byte[] mssGuid, final byte[] relGuid)\n
    '''
def deleteRelationships():
    '''returns None\n\n
    deleteRelationships(final Guid mssGuid, final HashMap[] relationships)\n
    deleteRelationships(final byte[][] relGuids)\n
    deleteRelationships(final Guid mssGuid, final HashMap filter)\n
    '''
def get():
    '''returns HashMap[]\n\n
    get(final byte[] mssGuid, final HashMap resourceFilter, final int scope)\n
    '''
def getManagedElements():
    '''returns HashMap[]\n\n
    getManagedElements(final String classType, final Date date)\n
    '''
def getSourceToken():
    '''returns String\n\n
    getSourceToken(final Guid mssGuid, final Guid meGuid)\n
    '''
def getSourceTokens():
    '''returns HashMap[]\n\n
    getSourceTokens(final Guid mssGuid, final Date date)\n
    '''
def getRelationships():
    '''returns HashMap[]\n\n
    getRelationships(final String relationshipType, final String sourceClass, final String targetClass, final Date date)\n
    '''
def removeStale():
    '''returns None\n\n
    removeStale(final Guid mssGuid, final Date date)\n
    '''
