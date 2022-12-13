def NrsServiceExtension():
    '''    public NrsServiceExtension()
    '''
def registerMSS():
    '''    public Guid registerMSS(final HashMap mss)
    '''
def updateMSS():
    '''    public void updateMSS(final HashMap mss, final boolean checkIdentifyingAttributes)
    '''
def deleteMSS():
    '''    public void deleteMSS(final Guid mssGuid)
    '''
def getMSS():
    '''    public HashMap[] getMSS(final Date date)
    '''
def registerAttributes():
    '''    public void registerAttributes(final Guid mssGuid, final Guid[] guids, final HashMap[] attributeMaps, final HashMap[] cleansedAttributeMaps)
    '''
def searchAttribute():
    '''    public static int searchAttribute(final ArrayList aList, final String aString)
    '''
def addAttribute():
    '''    public PreparedStatement addAttribute(PreparedStatement addPreparedStmt, final byte[] mssGuid, final byte[] meGuid, final byte[] attrGuid, final String attrName, final String standardValue, final String oldValue, final int isIdentifyingAttr)
    '''
def addSourceToken():
    '''    public PreparedStatement addSourceToken(PreparedStatement addPreparedStmt, final byte[] mssGuid, final byte[] meGuid, final String sourceToken)
    '''
def update():
    '''    public void update(final Guid mssGuid, final HashMap[] attributeMaps)
    '''
def delete():
    '''    public void delete(final Guid mssGuid, final Guid[] guids)
    '''
def getDeleted():
    '''    public Guid[] getDeleted(final String classType, final Date date)
    '''
def addRelationships():
    '''    public Guid[] addRelationships(final Guid mssGuid, final HashMap[] relationships)
    '''
def addRelationshipsOracle():
    '''    public Guid[] addRelationshipsOracle(final Guid mssGuid, final HashMap[] relationships)
    '''
def addRelationship():
    '''    public PreparedStatement addRelationship(PreparedStatement addPreparedStmt, final byte[] relGuid, final String relType, final byte[] sourceClass, final byte[] sourceGuid, final byte[] targetClass, final byte[] targetGuid, final String label)
    '''
def addMSSRelationship():
    '''    public PreparedStatement addMSSRelationship(PreparedStatement addPreparedStmt, final byte[] mssGuid, final byte[] relGuid)
    '''
def deleteRelationships():
    '''    public void deleteRelationships(final Guid mssGuid, final HashMap[] relationships)
    public void deleteRelationships(final byte[][] relGuids)
    public void deleteRelationships(final Guid mssGuid, final HashMap filter)
    '''
def get():
    '''    public HashMap[] get(final byte[] mssGuid, final HashMap resourceFilter, final int scope)
    '''
def getManagedElements():
    '''    public HashMap[] getManagedElements(final String classType, final Date date)
    '''
def getSourceToken():
    '''    public String getSourceToken(final Guid mssGuid, final Guid meGuid)
    '''
def getSourceTokens():
    '''    public HashMap[] getSourceTokens(final Guid mssGuid, final Date date)
    '''
def getRelationships():
    '''    public HashMap[] getRelationships(final String relationshipType, final String sourceClass, final String targetClass, final Date date)
    '''
def removeStale():
    '''    public void removeStale(final Guid mssGuid, final Date date)
    '''
