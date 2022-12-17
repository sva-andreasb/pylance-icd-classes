def ():
    '''returns NrsService\n\n
    ()\n
    '''
def init():
    '''returns INrsNamePlugin\n\n
    init(final Connection connection)\n
    '''
def registerNames():
    '''returns None\n\n
    registerNames(final Guid[] returnGuids, final ArrayList readyList, final HashMap[] identifyingAttributeMaps, final HashMap[] cleansedAttributeMaps)\n
    '''
def checkSuperior():
    '''returns NrsMasterAliasMap[]\n\n
    checkSuperior(final String classType, final HashMap superiorMap, final HashMap identifyingAttributeMap)\n
    '''
def addNameInstance():
    '''returns PreparedStatement[]\n\n
    addNameInstance(final PreparedStatement[] addPreparedStmts, final NrsMasterAliasMap nameInstance)\n
    '''
def getExistedNameInstances():
    '''returns ArrayList\n\n
    getExistedNameInstances(final NrsMasterAliasMap[] validNames)\n
    '''
def selectMaster():
    '''returns NrsMasterAliasMap\n\n
    selectMaster(final ArrayList masterAliasList)\n
    '''
def fixNames():
    '''returns PreparedStatement[]\n\n
    fixNames(PreparedStatement[] addPreparedStmts, final NrsMasterAliasMap nameInstance, final NrsMasterAliasMap theMasterNameInstance, final ArrayList duplicateList)\n
    '''
def buildNameListDB2():
    '''returns ArrayList\n\n
    buildNameListDB2(final byte[] guid)\n
    '''
def buildNameList():
    '''returns ArrayList\n\n
    buildNameList(final byte[] guid)\n
    '''
def getAffectedNameInstances():
    '''returns ArrayList\n\n
    getAffectedNameInstances(final ArrayList fixList)\n
    '''
def isNewName():
    '''returns boolean\n\n
    isNewName(final NrsMasterAliasMap nameInstance)\n
    '''
def convergeMasters():
    '''returns None\n\n
    convergeMasters(final Guid masterGuid1, final Guid masterGuid2)\n
    '''
def isMatch():
    '''returns boolean\n\n
    isMatch(final String nameUri)\n
    isMatch(final Guid guid1, final Guid guid2)\n
    '''
def getAliases():
    '''returns Guid[]\n\n
    getAliases(final Guid masterGuid)\n
    '''
def getMaster():
    '''returns Guid\n\n
    getMaster(final Guid aliasGuid)\n
    '''
def getMasterAndAliases():
    '''returns Guid[]\n\n
    getMasterAndAliases(final Guid guid)\n
    '''
def getNames():
    '''returns NrsMasterAliasInfo[]\n\n
    getNames(final Guid[] guids)\n
    '''
def delete():
    '''returns None\n\n
    delete(final Guid guid)\n
    '''
def addDeleteEvents():
    '''returns None\n\n
    addDeleteEvents(final ArrayList aList)\n
    '''
def getNameeGuids():
    '''returns ArrayList\n\n
    getNameeGuids(final ArrayList superiorList)\n
    '''
def getDuplicates():
    '''returns NrsDuplicateInfo[]\n\n
    getDuplicates(final String classType, final Date date)\n
    '''
def deleteDuplicates():
    '''returns None\n\n
    deleteDuplicates(final String classType, final Date date)\n
    '''
def deleteChangeEvents():
    '''returns None\n\n
    deleteChangeEvents(final int type, final Date date)\n
    '''
def deleteMeAssociations():
    '''returns None\n\n
    deleteMeAssociations(final ArrayList aList)\n
    '''
def getRelationshipGuid():
    '''returns byte[]\n\n
    getRelationshipGuid(final String nameSpace, final String relType, final byte[] sourceGuid, final byte[] targetGuid)\n
    '''
