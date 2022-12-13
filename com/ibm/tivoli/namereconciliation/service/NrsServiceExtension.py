def NrsServiceExtension():
'''public NrsServiceExtension()
'''
pass
def registerMSS():
'''public Guid registerMSS(final HashMap mss)
'''
pass
def updateMSS():
'''public void updateMSS(final HashMap mss, final boolean checkIdentifyingAttributes)
'''
pass
def deleteMSS():
'''public void deleteMSS(final Guid mssGuid)
'''
pass
def getMSS():
'''public HashMap[] getMSS(final Date date)
'''
pass
def registerAttributes():
'''public void registerAttributes(final Guid mssGuid, final Guid[] guids, final HashMap[] attributeMaps, final HashMap[] cleansedAttributeMaps)
'''
pass
def searchAttribute():
'''public static int searchAttribute(final ArrayList aList, final String aString)
'''
pass
def addAttribute():
'''public PreparedStatement addAttribute(PreparedStatement addPreparedStmt, final byte[] mssGuid, final byte[] meGuid, final byte[] attrGuid, final String attrName, final String standardValue, final String oldValue, final int isIdentifyingAttr)
'''
pass
def addSourceToken():
'''public PreparedStatement addSourceToken(PreparedStatement addPreparedStmt, final byte[] mssGuid, final byte[] meGuid, final String sourceToken)
'''
pass
def update():
'''public void update(final Guid mssGuid, final HashMap[] attributeMaps)
'''
pass
def delete():
'''public void delete(final Guid mssGuid, final Guid[] guids)
'''
pass
def getDeleted():
'''public Guid[] getDeleted(final String classType, final Date date)
'''
pass
def addRelationships():
'''public Guid[] addRelationships(final Guid mssGuid, final HashMap[] relationships)
'''
pass
def addRelationshipsOracle():
'''public Guid[] addRelationshipsOracle(final Guid mssGuid, final HashMap[] relationships)
'''
pass
def addRelationship():
'''public PreparedStatement addRelationship(PreparedStatement addPreparedStmt, final byte[] relGuid, final String relType, final byte[] sourceClass, final byte[] sourceGuid, final byte[] targetClass, final byte[] targetGuid, final String label)
'''
pass
def addMSSRelationship():
'''public PreparedStatement addMSSRelationship(PreparedStatement addPreparedStmt, final byte[] mssGuid, final byte[] relGuid)
'''
pass
def deleteRelationships():
'''public void deleteRelationships(final Guid mssGuid, final HashMap[] relationships)
public void deleteRelationships(final byte[][] relGuids)
public void deleteRelationships(final Guid mssGuid, final HashMap filter)
'''
pass
def get():
'''public HashMap[] get(final byte[] mssGuid, final HashMap resourceFilter, final int scope)
'''
pass
def getManagedElements():
'''public HashMap[] getManagedElements(final String classType, final Date date)
'''
pass
def getSourceToken():
'''public String getSourceToken(final Guid mssGuid, final Guid meGuid)
'''
pass
def getSourceTokens():
'''public HashMap[] getSourceTokens(final Guid mssGuid, final Date date)
'''
pass
def getRelationships():
'''public HashMap[] getRelationships(final String relationshipType, final String sourceClass, final String targetClass, final Date date)
'''
pass
def removeStale():
'''public void removeStale(final Guid mssGuid, final Date date)
'''
pass
