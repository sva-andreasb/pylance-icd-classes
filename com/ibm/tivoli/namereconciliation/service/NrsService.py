def NrsService():
'''public NrsService()
'''
pass
def init():
'''public INrsNamePlugin init(final Connection connection)
'''
pass
def registerNames():
'''public void registerNames(final Guid[] returnGuids, final ArrayList readyList, final HashMap[] identifyingAttributeMaps, final HashMap[] cleansedAttributeMaps)
'''
pass
def checkSuperior():
'''public NrsMasterAliasMap[] checkSuperior(final String classType, final HashMap superiorMap, final HashMap identifyingAttributeMap)
'''
pass
def addNameInstance():
'''public PreparedStatement[] addNameInstance(final PreparedStatement[] addPreparedStmts, final NrsMasterAliasMap nameInstance)
'''
pass
def getExistedNameInstances():
'''public ArrayList getExistedNameInstances(final NrsMasterAliasMap[] validNames)
'''
pass
def selectMaster():
'''public NrsMasterAliasMap selectMaster(final ArrayList masterAliasList)
'''
pass
def fixNames():
'''public PreparedStatement[] fixNames(PreparedStatement[] addPreparedStmts, final NrsMasterAliasMap nameInstance, final NrsMasterAliasMap theMasterNameInstance, final ArrayList duplicateList)
'''
pass
def buildNameListDB2():
'''public ArrayList buildNameListDB2(final byte[] guid)
'''
pass
def buildNameList():
'''public ArrayList buildNameList(final byte[] guid)
'''
pass
def getAffectedNameInstances():
'''public ArrayList getAffectedNameInstances(final ArrayList fixList)
'''
pass
def isNewName():
'''public boolean isNewName(final NrsMasterAliasMap nameInstance)
'''
pass
def convergeMasters():
'''public void convergeMasters(final Guid masterGuid1, final Guid masterGuid2)
'''
pass
def isMatch():
'''public boolean isMatch(final String nameUri)
public boolean isMatch(final Guid guid1, final Guid guid2)
'''
pass
def getAliases():
'''public Guid[] getAliases(final Guid masterGuid)
public Map<Guid, List<Guid>> getAliases(final Guid[] masterGuids)
'''
pass
def getMaster():
'''public Guid getMaster(final Guid aliasGuid)
'''
pass
def getMasterAndAliases():
'''public Guid[] getMasterAndAliases(final Guid guid)
'''
pass
def getNames():
'''public NrsMasterAliasInfo[] getNames(final Guid[] guids)
'''
pass
def delete():
'''public void delete(final Guid guid)
'''
pass
def addDeleteEvents():
'''public void addDeleteEvents(final ArrayList aList)
'''
pass
def getNameeGuids():
'''public ArrayList getNameeGuids(final ArrayList superiorList)
'''
pass
def getDuplicates():
'''public NrsDuplicateInfo[] getDuplicates(final String classType, final Date date)
'''
pass
def deleteDuplicates():
'''public void deleteDuplicates(final String classType, final Date date)
'''
pass
def deleteChangeEvents():
'''public void deleteChangeEvents(final int type, final Date date)
'''
pass
def deleteMeAssociations():
'''public void deleteMeAssociations(final ArrayList aList)
'''
pass
def getRelationshipGuid():
'''public byte[] getRelationshipGuid(final String nameSpace, final String relType, final byte[] sourceGuid, final byte[] targetGuid)
'''
pass
