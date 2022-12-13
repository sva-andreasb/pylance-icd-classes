def AssetCatalogService():
'''public AssetCatalogService()
public AssetCatalogService(final MXServer mxServer)
'''
pass
def getClassStructure():
'''public MboRemote getClassStructure(final UserInfo userInfo, final String[] classificationsArray)
public MboRemote getClassStructure(final UserInfo userInfo, final String[] classificationsArray, final boolean returnANewMbo)
public MboRemote getClassStructure(final UserInfo userInfo, final String classStructureUID)
'''
pass
def init():
'''public void init()
'''
pass
def getClassStructureFromPath():
'''public MboRemote getClassStructureFromPath(final UserInfo userInfo, final String hierarchyPath)
public MboRemote getClassStructureFromPath(final UserInfo userInfo, final String hierarchyPath, final String objectName)
public MboRemote getClassStructureFromPath(final UserInfo userInfo, final String hierarchyPath, String orgid, String siteid)
'''
pass
def parsePathIntoVector():
'''public Vector parsePathIntoVector(final String hierarchyPathPassed)
'''
pass
def getClassStructureMboList():
'''public MboSetRemote getClassStructureMboList(final UserInfo userInfo, final String[] classificationsArray)
'''
pass
def getClassStructureList():
'''public String getClassStructureList(final UserInfo userInfo, final String[] classificationsArray)
'''
pass
def getAllAttributes():
'''public MboSetRemote getAllAttributes(final UserInfo userInfo, final String[] classificationsArray)
'''
pass
def getAllItems():
'''public MboSetRemote getAllItems(final UserInfo userInfo, final String[] classificationsArray)
'''
pass
def classStructureSearch():
'''public MboSetRemote classStructureSearch(final UserInfo userInfo, final String objectName, final String[] classificationsArray)
public MboSetRemote classStructureSearch(final UserInfo userInfo, final String objectName, final String classStructureid)
'''
pass
def anyLevelSearch():
'''public MboSetRemote anyLevelSearch(final UserInfo userInfo, final String objectName, final String[] classificationsArray)
'''
pass
def classAndAttributesSearch():
'''public MboSetRemote classAndAttributesSearch(final UserInfo userInfo, final String objectName, final String classStructureid, final String[][] attrAndValues)
public MboSetRemote classAndAttributesSearch(final UserInfo userInfo, final String objectName, final String classStructureid, final String[][] attrAndValues, final boolean convertArray)
public MboSetRemote classAndAttributesSearch(final UserInfo userInfo, final String objectName, final String[] classificationsArray, final String[][] attrAndValues, final boolean convertArray)
public MboSetRemote classAndAttributesSearch(final UserInfo userInfo, final String objectName, final String[][] itemColumns, final String[][] invVendorColumns, final String[][] attrAndValues, final String[] classificationsArray)
public String classAndAttributesSearch(final UserInfo userInfo, final String objectName, final MboRemote selectedClassStructureMbo, final MboSetRemote classSpecSet)
'''
pass
def getClassAndAttributesSearchWhere():
'''public String getClassAndAttributesSearchWhere(final UserInfo userInfo, final String objectName, final String classStructureid, final String[][] attrAndValues, final String[][] itemWhere, final String[][] invVendorWhere)
'''
pass
def attributesSearch():
'''public MboSetRemote attributesSearch(final UserInfo userInfo, final String objectName, final String[][] attrAndValues)
public MboSetRemote attributesSearch(final UserInfo userInfo, final String objectName, final String[][] attrAndValues, final boolean convertArray)
public String attributesSearch(final UserInfo userInfo, final String objectName, final MboSetRemote searchAttrSet)
public String attributesSearch(final UserInfo userInfo, final String objectName, final MboSetRemote searchAttrSet, final MboSetRemote relatedAttrSet)
'''
pass
def getMeasureUnits():
'''public MboSetRemote getMeasureUnits(final UserInfo userInfo, final String classStructureId, final String assetAttrid, final String objectName)
'''
pass
def getClassStructureId():
'''public String getClassStructureId(final UserInfo userInfo, final String objectName, final String attrName, final String attrValue)
'''
pass
def getAttributeValues():
'''public MboSetRemote getAttributeValues(final UserInfo userInfo, final String classstructureid, final String assetattrid)
public MboSetRemote getAttributeValues(final UserInfo userInfo, final String assetattrid)
'''
pass
def validateObjectName():
'''public void validateObjectName(final String objectName)
'''
pass
def getSpecifications():
'''public MboSetRemote getSpecifications(final MboRemote mbo)
'''
pass
def getChildren():
'''public MboSetRemote getChildren(final UserInfo userInfo, final String[] classificationsArray, final int currentLevel, String searchString, String searchType)
'''
pass
def convertList():
'''public String[][] convertList(final UserInfo userInfo, final String[][] attrAndValues)
public String[][] convertList(final String classstructureid, final String[][] attrAndValues)
'''
pass
def stringBySearchType():
'''public String stringBySearchType(final String searchType, final String searchString)
'''
pass
def classAndAttributesSearchCU():
'''public MboSetRemote classAndAttributesSearchCU(final UserInfo userInfo, final String[] classificationsArray, final String[][] attrAndValues, final boolean convertArray)
'''
pass
def getClassAndRelatedAttributesSearchWhere():
'''public String getClassAndRelatedAttributesSearchWhere(final UserInfo userInfo, final String objectName, final String[][] attrAndValues)
'''
pass
def createRelatedAttributeWhereClause():
'''public String createRelatedAttributeWhereClause(final String[][] attrAndValues, final MboSetRemote specSet)
'''
pass
def generateDescription():
'''public String generateDescription(final ClassStructureRemote classMbo, final SpecificationMboSetRemote specSet)
'''
pass
def generateSpecSet():
'''public MboSetRemote generateSpecSet(final MboRemote mbo)
public MboSetRemote generateSpecSet(final MboRemote mbo, final String itemNum)
public MboSetRemote generateSpecSet(final MboRemote mbo, final String itemNum, final MboRemote baseMbo)
'''
pass
def getCorrectObjectName():
'''public String getCorrectObjectName(final MboRemote mbo)
public String getCorrectObjectName(final UserInfo userInfo, final String objectName)
'''
pass
def getUseWithDomainBaseObjects():
'''public Vector getUseWithDomainBaseObjects(final UserInfo userInfo)
'''
pass
def getUseWithDomainObjects():
'''public MboSetRemote getUseWithDomainObjects(final UserInfo userInfo, final boolean persistentObjectsOnly)
'''
pass
def getClassSpecUseWith():
'''public MboRemote getClassSpecUseWith(final MboRemote classSpec, String objectName)
'''
pass
def getClassUseWithDomain():
'''public MboRemote getClassUseWithDomain(final UserInfo userInfo, final String objectName)
'''
pass
def processOldAndNewSpecSets():
'''public void processOldAndNewSpecSets(final MboSetRemote oldSpecDeletedSet, final MboSetRemote newSpecSet)
'''
pass
def setAttributesSearchMboSet():
'''public void setAttributesSearchMboSet(final MboSetRemote mboSet)
'''
pass
def getAttributesSearchMboSet():
'''public MboSetRemote getAttributesSearchMboSet()
'''
pass
def deleteMbosetNotViaMbo():
'''public void deleteMbosetNotViaMbo(final MboRemote mbo, final MboSetRemote mboSetReferencedNotViaMbo)
'''
pass
def doNotGenerateDescForThisObject():
'''public void doNotGenerateDescForThisObject(final String objectName)
'''
pass
def toGenerateDescForThisObject():
'''public boolean toGenerateDescForThisObject(final String objectName)
'''
pass
def getDescDelimiter():
'''public String getDescDelimiter()
public String getDescDelimiter(final boolean isForClassDesc)
'''
pass
def sortedClassSpecSet():
'''public Vector sortedClassSpecSet(final MboSetRemote classSpecSet, final MboRemote mbo)
'''
pass
def getClassStructureTopDown():
'''public MboSetRemote getClassStructureTopDown(final MboSetRemote parentSet, final Vector classificationVector, final int whichElement)
'''
pass
def reprocessClassStructureSortOrder():
'''public void reprocessClassStructureSortOrder()
'''
pass
def createCategoryToSR():
'''public void createCategoryToSR(final String description, final Integer order)
'''
pass
def createSubCategoryToSR():
'''public void createSubCategoryToSR(final String parent, final String description, final Integer order)
'''
pass
def updateClassification():
'''public void updateClassification(@WSMboKey("CLASSSTRUCTURE") final MboRemote classstructure, final String description, final Integer sortOrder)
'''
pass
def getAttributeInternalType():
'''public String getAttributeInternalType(final String assetattrid, final String orgid, final String siteid)
'''
pass
def setAttributeInternalTye():
'''public void setAttributeInternalTye(final String assetattrid, final String orgid, final String siteid, final String internalType)
'''
pass
def clearAssetAttrHash():
'''public void clearAssetAttrHash()
'''
pass
