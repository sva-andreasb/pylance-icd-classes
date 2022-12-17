def ():
    '''returns AssetCatalogService\n\n
    ()\n
    (final MXServer mxServer)\n
    '''
def getClassStructure():
    '''returns MboRemote\n\n
    getClassStructure(final UserInfo userInfo, final String[] classificationsArray)\n
    getClassStructure(final UserInfo userInfo, final String[] classificationsArray, final boolean returnANewMbo)\n
    getClassStructure(final UserInfo userInfo, final String classStructureUID)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def getClassStructureFromPath():
    '''returns MboRemote\n\n
    getClassStructureFromPath(final UserInfo userInfo, final String hierarchyPath)\n
    getClassStructureFromPath(final UserInfo userInfo, final String hierarchyPath, final String objectName)\n
    getClassStructureFromPath(final UserInfo userInfo, final String hierarchyPath, String orgid, String siteid)\n
    '''
def parsePathIntoVector():
    '''returns Vector\n\n
    parsePathIntoVector(final String hierarchyPathPassed)\n
    '''
def getClassStructureMboList():
    '''returns MboSetRemote\n\n
    getClassStructureMboList(final UserInfo userInfo, final String[] classificationsArray)\n
    '''
def getClassStructureList():
    '''returns String\n\n
    getClassStructureList(final UserInfo userInfo, final String[] classificationsArray)\n
    '''
def getAllAttributes():
    '''returns MboSetRemote\n\n
    getAllAttributes(final UserInfo userInfo, final String[] classificationsArray)\n
    '''
def getAllItems():
    '''returns MboSetRemote\n\n
    getAllItems(final UserInfo userInfo, final String[] classificationsArray)\n
    '''
def classStructureSearch():
    '''returns MboSetRemote\n\n
    classStructureSearch(final UserInfo userInfo, final String objectName, final String[] classificationsArray)\n
    classStructureSearch(final UserInfo userInfo, final String objectName, final String classStructureid)\n
    '''
def anyLevelSearch():
    '''returns MboSetRemote\n\n
    anyLevelSearch(final UserInfo userInfo, final String objectName, final String[] classificationsArray)\n
    '''
def classAndAttributesSearch():
    '''returns String\n\n
    classAndAttributesSearch(final UserInfo userInfo, final String objectName, final String classStructureid, final String[][] attrAndValues)\n
    classAndAttributesSearch(final UserInfo userInfo, final String objectName, final String classStructureid, final String[][] attrAndValues, final boolean convertArray)\n
    classAndAttributesSearch(final UserInfo userInfo, final String objectName, final String[] classificationsArray, final String[][] attrAndValues, final boolean convertArray)\n
    classAndAttributesSearch(final UserInfo userInfo, final String objectName, final String[][] itemColumns, final String[][] invVendorColumns, final String[][] attrAndValues, final String[] classificationsArray)\n
    classAndAttributesSearch(final UserInfo userInfo, final String objectName, final MboRemote selectedClassStructureMbo, final MboSetRemote classSpecSet)\n
    '''
def getClassAndAttributesSearchWhere():
    '''returns String\n\n
    getClassAndAttributesSearchWhere(final UserInfo userInfo, final String objectName, final String classStructureid, final String[][] attrAndValues, final String[][] itemWhere, final String[][] invVendorWhere)\n
    '''
def attributesSearch():
    '''returns String\n\n
    attributesSearch(final UserInfo userInfo, final String objectName, final String[][] attrAndValues)\n
    attributesSearch(final UserInfo userInfo, final String objectName, final String[][] attrAndValues, final boolean convertArray)\n
    attributesSearch(final UserInfo userInfo, final String objectName, final MboSetRemote searchAttrSet)\n
    attributesSearch(final UserInfo userInfo, final String objectName, final MboSetRemote searchAttrSet, final MboSetRemote relatedAttrSet)\n
    '''
def getMeasureUnits():
    '''returns MboSetRemote\n\n
    getMeasureUnits(final UserInfo userInfo, final String classStructureId, final String assetAttrid, final String objectName)\n
    '''
def getClassStructureId():
    '''returns String\n\n
    getClassStructureId(final UserInfo userInfo, final String objectName, final String attrName, final String attrValue)\n
    '''
def getAttributeValues():
    '''returns MboSetRemote\n\n
    getAttributeValues(final UserInfo userInfo, final String classstructureid, final String assetattrid)\n
    getAttributeValues(final UserInfo userInfo, final String assetattrid)\n
    '''
def validateObjectName():
    '''returns None\n\n
    validateObjectName(final String objectName)\n
    '''
def getSpecifications():
    '''returns MboSetRemote\n\n
    getSpecifications(final MboRemote mbo)\n
    '''
def getChildren():
    '''returns MboSetRemote\n\n
    getChildren(final UserInfo userInfo, final String[] classificationsArray, final int currentLevel, String searchString, String searchType)\n
    '''
def convertList():
    '''returns String[][]\n\n
    convertList(final UserInfo userInfo, final String[][] attrAndValues)\n
    convertList(final String classstructureid, final String[][] attrAndValues)\n
    '''
def stringBySearchType():
    '''returns String\n\n
    stringBySearchType(final String searchType, final String searchString)\n
    '''
def classAndAttributesSearchCU():
    '''returns MboSetRemote\n\n
    classAndAttributesSearchCU(final UserInfo userInfo, final String[] classificationsArray, final String[][] attrAndValues, final boolean convertArray)\n
    '''
def getClassAndRelatedAttributesSearchWhere():
    '''returns String\n\n
    getClassAndRelatedAttributesSearchWhere(final UserInfo userInfo, final String objectName, final String[][] attrAndValues)\n
    '''
def createRelatedAttributeWhereClause():
    '''returns String\n\n
    createRelatedAttributeWhereClause(final String[][] attrAndValues, final MboSetRemote specSet)\n
    '''
def generateDescription():
    '''returns String\n\n
    generateDescription(final ClassStructureRemote classMbo, final SpecificationMboSetRemote specSet)\n
    '''
def generateSpecSet():
    '''returns MboSetRemote\n\n
    generateSpecSet(final MboRemote mbo)\n
    generateSpecSet(final MboRemote mbo, final String itemNum)\n
    generateSpecSet(final MboRemote mbo, final String itemNum, final MboRemote baseMbo)\n
    '''
def getCorrectObjectName():
    '''returns String\n\n
    getCorrectObjectName(final MboRemote mbo)\n
    getCorrectObjectName(final UserInfo userInfo, final String objectName)\n
    '''
def getUseWithDomainBaseObjects():
    '''returns Vector\n\n
    getUseWithDomainBaseObjects(final UserInfo userInfo)\n
    '''
def getUseWithDomainObjects():
    '''returns MboSetRemote\n\n
    getUseWithDomainObjects(final UserInfo userInfo, final boolean persistentObjectsOnly)\n
    '''
def getClassSpecUseWith():
    '''returns MboRemote\n\n
    getClassSpecUseWith(final MboRemote classSpec, String objectName)\n
    '''
def getClassUseWithDomain():
    '''returns MboRemote\n\n
    getClassUseWithDomain(final UserInfo userInfo, final String objectName)\n
    '''
def processOldAndNewSpecSets():
    '''returns None\n\n
    processOldAndNewSpecSets(final MboSetRemote oldSpecDeletedSet, final MboSetRemote newSpecSet)\n
    '''
def setAttributesSearchMboSet():
    '''returns None\n\n
    setAttributesSearchMboSet(final MboSetRemote mboSet)\n
    '''
def getAttributesSearchMboSet():
    '''returns MboSetRemote\n\n
    getAttributesSearchMboSet()\n
    '''
def deleteMbosetNotViaMbo():
    '''returns None\n\n
    deleteMbosetNotViaMbo(final MboRemote mbo, final MboSetRemote mboSetReferencedNotViaMbo)\n
    '''
def doNotGenerateDescForThisObject():
    '''returns None\n\n
    doNotGenerateDescForThisObject(final String objectName)\n
    '''
def toGenerateDescForThisObject():
    '''returns boolean\n\n
    toGenerateDescForThisObject(final String objectName)\n
    '''
def getDescDelimiter():
    '''returns String\n\n
    getDescDelimiter()\n
    getDescDelimiter(final boolean isForClassDesc)\n
    '''
def sortedClassSpecSet():
    '''returns Vector\n\n
    sortedClassSpecSet(final MboSetRemote classSpecSet, final MboRemote mbo)\n
    '''
def getClassStructureTopDown():
    '''returns MboSetRemote\n\n
    getClassStructureTopDown(final MboSetRemote parentSet, final Vector classificationVector, final int whichElement)\n
    '''
def reprocessClassStructureSortOrder():
    '''returns None\n\n
    reprocessClassStructureSortOrder()\n
    '''
def createCategoryToSR():
    '''returns None\n\n
    createCategoryToSR(final String description, final Integer order)\n
    '''
def createSubCategoryToSR():
    '''returns None\n\n
    createSubCategoryToSR(final String parent, final String description, final Integer order)\n
    '''
def updateClassification():
    '''returns None\n\n
    updateClassification(@WSMboKey("CLASSSTRUCTURE") final MboRemote classstructure, final String description, final Integer sortOrder)\n
    '''
def getAttributeInternalType():
    '''returns String\n\n
    getAttributeInternalType(final String assetattrid, final String orgid, final String siteid)\n
    '''
def setAttributeInternalTye():
    '''returns None\n\n
    setAttributeInternalTye(final String assetattrid, final String orgid, final String siteid, final String internalType)\n
    '''
def clearAssetAttrHash():
    '''returns None\n\n
    clearAssetAttrHash()\n
    '''
