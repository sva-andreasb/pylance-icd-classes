def AssetCatalogService():
    '''    public AssetCatalogService()
    public AssetCatalogService(final MXServer mxServer)
    '''
def getClassStructure():
    '''    public MboRemote getClassStructure(final UserInfo userInfo, final String[] classificationsArray)
    public MboRemote getClassStructure(final UserInfo userInfo, final String[] classificationsArray, final boolean returnANewMbo)
    public MboRemote getClassStructure(final UserInfo userInfo, final String classStructureUID)
    '''
def init():
    '''    public void init()
    '''
def getClassStructureFromPath():
    '''    public MboRemote getClassStructureFromPath(final UserInfo userInfo, final String hierarchyPath)
    public MboRemote getClassStructureFromPath(final UserInfo userInfo, final String hierarchyPath, final String objectName)
    public MboRemote getClassStructureFromPath(final UserInfo userInfo, final String hierarchyPath, String orgid, String siteid)
    '''
def parsePathIntoVector():
    '''    public Vector parsePathIntoVector(final String hierarchyPathPassed)
    '''
def getClassStructureMboList():
    '''    public MboSetRemote getClassStructureMboList(final UserInfo userInfo, final String[] classificationsArray)
    '''
def getClassStructureList():
    '''    public String getClassStructureList(final UserInfo userInfo, final String[] classificationsArray)
    '''
def getAllAttributes():
    '''    public MboSetRemote getAllAttributes(final UserInfo userInfo, final String[] classificationsArray)
    '''
def getAllItems():
    '''    public MboSetRemote getAllItems(final UserInfo userInfo, final String[] classificationsArray)
    '''
def classStructureSearch():
    '''    public MboSetRemote classStructureSearch(final UserInfo userInfo, final String objectName, final String[] classificationsArray)
    public MboSetRemote classStructureSearch(final UserInfo userInfo, final String objectName, final String classStructureid)
    '''
def anyLevelSearch():
    '''    public MboSetRemote anyLevelSearch(final UserInfo userInfo, final String objectName, final String[] classificationsArray)
    '''
def classAndAttributesSearch():
    '''    public MboSetRemote classAndAttributesSearch(final UserInfo userInfo, final String objectName, final String classStructureid, final String[][] attrAndValues)
    public MboSetRemote classAndAttributesSearch(final UserInfo userInfo, final String objectName, final String classStructureid, final String[][] attrAndValues, final boolean convertArray)
    public MboSetRemote classAndAttributesSearch(final UserInfo userInfo, final String objectName, final String[] classificationsArray, final String[][] attrAndValues, final boolean convertArray)
    public MboSetRemote classAndAttributesSearch(final UserInfo userInfo, final String objectName, final String[][] itemColumns, final String[][] invVendorColumns, final String[][] attrAndValues, final String[] classificationsArray)
    public String classAndAttributesSearch(final UserInfo userInfo, final String objectName, final MboRemote selectedClassStructureMbo, final MboSetRemote classSpecSet)
    '''
def getClassAndAttributesSearchWhere():
    '''    public String getClassAndAttributesSearchWhere(final UserInfo userInfo, final String objectName, final String classStructureid, final String[][] attrAndValues, final String[][] itemWhere, final String[][] invVendorWhere)
    '''
def attributesSearch():
    '''    public MboSetRemote attributesSearch(final UserInfo userInfo, final String objectName, final String[][] attrAndValues)
    public MboSetRemote attributesSearch(final UserInfo userInfo, final String objectName, final String[][] attrAndValues, final boolean convertArray)
    public String attributesSearch(final UserInfo userInfo, final String objectName, final MboSetRemote searchAttrSet)
    public String attributesSearch(final UserInfo userInfo, final String objectName, final MboSetRemote searchAttrSet, final MboSetRemote relatedAttrSet)
    '''
def getMeasureUnits():
    '''    public MboSetRemote getMeasureUnits(final UserInfo userInfo, final String classStructureId, final String assetAttrid, final String objectName)
    '''
def getClassStructureId():
    '''    public String getClassStructureId(final UserInfo userInfo, final String objectName, final String attrName, final String attrValue)
    '''
def getAttributeValues():
    '''    public MboSetRemote getAttributeValues(final UserInfo userInfo, final String classstructureid, final String assetattrid)
    public MboSetRemote getAttributeValues(final UserInfo userInfo, final String assetattrid)
    '''
def validateObjectName():
    '''    public void validateObjectName(final String objectName)
    '''
def getSpecifications():
    '''    public MboSetRemote getSpecifications(final MboRemote mbo)
    '''
def getChildren():
    '''    public MboSetRemote getChildren(final UserInfo userInfo, final String[] classificationsArray, final int currentLevel, String searchString, String searchType)
    '''
def convertList():
    '''    public String[][] convertList(final UserInfo userInfo, final String[][] attrAndValues)
    public String[][] convertList(final String classstructureid, final String[][] attrAndValues)
    '''
def stringBySearchType():
    '''    public String stringBySearchType(final String searchType, final String searchString)
    '''
def classAndAttributesSearchCU():
    '''    public MboSetRemote classAndAttributesSearchCU(final UserInfo userInfo, final String[] classificationsArray, final String[][] attrAndValues, final boolean convertArray)
    '''
def getClassAndRelatedAttributesSearchWhere():
    '''    public String getClassAndRelatedAttributesSearchWhere(final UserInfo userInfo, final String objectName, final String[][] attrAndValues)
    '''
def createRelatedAttributeWhereClause():
    '''    public String createRelatedAttributeWhereClause(final String[][] attrAndValues, final MboSetRemote specSet)
    '''
def generateDescription():
    '''    public String generateDescription(final ClassStructureRemote classMbo, final SpecificationMboSetRemote specSet)
    '''
def generateSpecSet():
    '''    public MboSetRemote generateSpecSet(final MboRemote mbo)
    public MboSetRemote generateSpecSet(final MboRemote mbo, final String itemNum)
    public MboSetRemote generateSpecSet(final MboRemote mbo, final String itemNum, final MboRemote baseMbo)
    '''
def getCorrectObjectName():
    '''    public String getCorrectObjectName(final MboRemote mbo)
    public String getCorrectObjectName(final UserInfo userInfo, final String objectName)
    '''
def getUseWithDomainBaseObjects():
    '''    public Vector getUseWithDomainBaseObjects(final UserInfo userInfo)
    '''
def getUseWithDomainObjects():
    '''    public MboSetRemote getUseWithDomainObjects(final UserInfo userInfo, final boolean persistentObjectsOnly)
    '''
def getClassSpecUseWith():
    '''    public MboRemote getClassSpecUseWith(final MboRemote classSpec, String objectName)
    '''
def getClassUseWithDomain():
    '''    public MboRemote getClassUseWithDomain(final UserInfo userInfo, final String objectName)
    '''
def processOldAndNewSpecSets():
    '''    public void processOldAndNewSpecSets(final MboSetRemote oldSpecDeletedSet, final MboSetRemote newSpecSet)
    '''
def setAttributesSearchMboSet():
    '''    public void setAttributesSearchMboSet(final MboSetRemote mboSet)
    '''
def getAttributesSearchMboSet():
    '''    public MboSetRemote getAttributesSearchMboSet()
    '''
def deleteMbosetNotViaMbo():
    '''    public void deleteMbosetNotViaMbo(final MboRemote mbo, final MboSetRemote mboSetReferencedNotViaMbo)
    '''
def doNotGenerateDescForThisObject():
    '''    public void doNotGenerateDescForThisObject(final String objectName)
    '''
def toGenerateDescForThisObject():
    '''    public boolean toGenerateDescForThisObject(final String objectName)
    '''
def getDescDelimiter():
    '''    public String getDescDelimiter()
    public String getDescDelimiter(final boolean isForClassDesc)
    '''
def sortedClassSpecSet():
    '''    public Vector sortedClassSpecSet(final MboSetRemote classSpecSet, final MboRemote mbo)
    '''
def getClassStructureTopDown():
    '''    public MboSetRemote getClassStructureTopDown(final MboSetRemote parentSet, final Vector classificationVector, final int whichElement)
    '''
def reprocessClassStructureSortOrder():
    '''    public void reprocessClassStructureSortOrder()
    '''
def createCategoryToSR():
    '''    public void createCategoryToSR(final String description, final Integer order)
    '''
def createSubCategoryToSR():
    '''    public void createSubCategoryToSR(final String parent, final String description, final Integer order)
    '''
def updateClassification():
    '''    public void updateClassification(@WSMboKey("CLASSSTRUCTURE") final MboRemote classstructure, final String description, final Integer sortOrder)
    '''
def getAttributeInternalType():
    '''    public String getAttributeInternalType(final String assetattrid, final String orgid, final String siteid)
    '''
def setAttributeInternalTye():
    '''    public void setAttributeInternalTye(final String assetattrid, final String orgid, final String siteid, final String internalType)
    '''
def clearAssetAttrHash():
    '''    public void clearAssetAttrHash()
    '''
