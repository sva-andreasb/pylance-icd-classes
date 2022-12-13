def NrsService():
    '''    public NrsService()
    '''
def init():
    '''    public INrsNamePlugin init(final Connection connection)
    '''
def registerNames():
    '''    public void registerNames(final Guid[] returnGuids, final ArrayList readyList, final HashMap[] identifyingAttributeMaps, final HashMap[] cleansedAttributeMaps)
    '''
def checkSuperior():
    '''    public NrsMasterAliasMap[] checkSuperior(final String classType, final HashMap superiorMap, final HashMap identifyingAttributeMap)
    '''
def addNameInstance():
    '''    public PreparedStatement[] addNameInstance(final PreparedStatement[] addPreparedStmts, final NrsMasterAliasMap nameInstance)
    '''
def getExistedNameInstances():
    '''    public ArrayList getExistedNameInstances(final NrsMasterAliasMap[] validNames)
    '''
def selectMaster():
    '''    public NrsMasterAliasMap selectMaster(final ArrayList masterAliasList)
    '''
def fixNames():
    '''    public PreparedStatement[] fixNames(PreparedStatement[] addPreparedStmts, final NrsMasterAliasMap nameInstance, final NrsMasterAliasMap theMasterNameInstance, final ArrayList duplicateList)
    '''
def buildNameListDB2():
    '''    public ArrayList buildNameListDB2(final byte[] guid)
    '''
def buildNameList():
    '''    public ArrayList buildNameList(final byte[] guid)
    '''
def getAffectedNameInstances():
    '''    public ArrayList getAffectedNameInstances(final ArrayList fixList)
    '''
def isNewName():
    '''    public boolean isNewName(final NrsMasterAliasMap nameInstance)
    '''
def convergeMasters():
    '''    public void convergeMasters(final Guid masterGuid1, final Guid masterGuid2)
    '''
def isMatch():
    '''    public boolean isMatch(final String nameUri)
    public boolean isMatch(final Guid guid1, final Guid guid2)
    '''
def getAliases():
    '''    public Guid[] getAliases(final Guid masterGuid)
    public Map<Guid, List<Guid>> getAliases(final Guid[] masterGuids)
    '''
def getMaster():
    '''    public Guid getMaster(final Guid aliasGuid)
    '''
def getMasterAndAliases():
    '''    public Guid[] getMasterAndAliases(final Guid guid)
    '''
def getNames():
    '''    public NrsMasterAliasInfo[] getNames(final Guid[] guids)
    '''
def delete():
    '''    public void delete(final Guid guid)
    '''
def addDeleteEvents():
    '''    public void addDeleteEvents(final ArrayList aList)
    '''
def getNameeGuids():
    '''    public ArrayList getNameeGuids(final ArrayList superiorList)
    '''
def getDuplicates():
    '''    public NrsDuplicateInfo[] getDuplicates(final String classType, final Date date)
    '''
def deleteDuplicates():
    '''    public void deleteDuplicates(final String classType, final Date date)
    '''
def deleteChangeEvents():
    '''    public void deleteChangeEvents(final int type, final Date date)
    '''
def deleteMeAssociations():
    '''    public void deleteMeAssociations(final ArrayList aList)
    '''
def getRelationshipGuid():
    '''    public byte[] getRelationshipGuid(final String nameSpace, final String relType, final byte[] sourceGuid, final byte[] targetGuid)
    '''
