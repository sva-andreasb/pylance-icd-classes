def ():
    '''returns ClassStructure\n\n
    (final MboSet ms)\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def canDelete():
    '''returns None\n\n
    canDelete()\n
    '''
def delete():
    '''returns None\n\n
    delete(final long access)\n
    '''
def undelete():
    '''returns None\n\n
    undelete()\n
    '''
def duplicate():
    '''returns MboRemote\n\n
    duplicate()\n
    '''
def getClassificationMbo():
    '''returns MboRemote\n\n
    getClassificationMbo()\n
    '''
def isGenAssetDesc():
    '''returns boolean\n\n
    isGenAssetDesc()\n
    '''
def genClassstructureDesc():
    '''returns String\n\n
    genClassstructureDesc()\n
    '''
def isTop():
    '''returns boolean\n\n
    isTop()\n
    '''
def hasChildren():
    '''returns boolean\n\n
    hasChildren()\n
    '''
def hasParents():
    '''returns boolean\n\n
    hasParents()\n
    '''
def getChildren():
    '''returns MboSetRemote\n\n
    getChildren()\n
    '''
def getParents():
    '''returns MboSetRemote\n\n
    getParents()\n
    '''
def getTop():
    '''returns MboSetRemote\n\n
    getTop()\n
    '''
def storeParentClassStructures():
    '''returns None\n\n
    storeParentClassStructures()\n
    '''
def getParentClassStructures():
    '''returns Vector\n\n
    getParentClassStructures()\n
    '''
def storeChildClassStructures():
    '''returns None\n\n
    storeChildClassStructures()\n
    '''
def getChildClassStructures():
    '''returns Vector\n\n
    getChildClassStructures()\n
    '''
def getHierarchyPath():
    '''returns String\n\n
    getHierarchyPath()\n
    '''
def getHierarchies():
    '''returns String[]\n\n
    getHierarchies()\n
    '''
def uncheckUseWith():
    '''returns None\n\n
    uncheckUseWith(final String attributename)\n
    '''
def clearParentClassification():
    '''returns None\n\n
    clearParentClassification()\n
    '''
def appValidate():
    '''returns None\n\n
    appValidate()\n
    '''
def smartFindByObjectName():
    '''returns MboSetRemote\n\n
    smartFindByObjectName(final String sourceObj, final String targetAttrName, final String value, final boolean exact)\n
    '''
def hasSiteOrgSecurity():
    '''returns boolean\n\n
    hasSiteOrgSecurity()\n
    '''
def populateUseWith():
    '''returns None\n\n
    populateUseWith(final MboRemote parent)\n
    populateUseWith(final MboRemote parent, final MboSetRemote thisUseWithSet)\n
    '''
def getUseWith():
    '''returns MboRemote\n\n
    getUseWith(String objectName)\n
    '''
def deleteUseWith():
    '''returns MboSetRemote\n\n
    deleteUseWith(final MboRemote parent)\n
    '''
def applyUpHierarchy():
    '''returns None\n\n
    applyUpHierarchy(MboRemote parent)\n
    '''
def applyDownHierarchy():
    '''returns None\n\n
    applyDownHierarchy(final MboRemote classSpec)\n
    '''
def isTopLevel():
    '''returns boolean\n\n
    isTopLevel(final String objectName)\n
    '''
def inClassificationApp():
    '''returns boolean\n\n
    inClassificationApp()\n
    '''
def getMboSet():
    '''returns MboSetRemote\n\n
    getMboSet(final String name)\n
    '''
def getUseWithInClassificationApp():
    '''returns MboRemote\n\n
    getUseWithInClassificationApp(final String objectName)\n
    '''
def getMboValueData():
    '''returns MboValueData\n\n
    getMboValueData(final String attribute)\n
    '''
def getRealChildrenForUseWith():
    '''returns MboSetRemote\n\n
    getRealChildrenForUseWith(final String objectForUseWith, final String objectOrgId, final String orjectSiteId)\n
    '''
def getObjectsNotInUseWithDomain():
    '''returns MboSetRemote\n\n
    getObjectsNotInUseWithDomain(final String objectName, final boolean persistentObjectsOnly)\n
    '''
def userSaidToCheckOrgSite():
    '''returns boolean\n\n
    userSaidToCheckOrgSite()\n
    '''
def initFieldFlagsOnMbo():
    '''returns None\n\n
    initFieldFlagsOnMbo(final String attrName)\n
    '''
def canChangeOrgSite():
    '''returns None\n\n
    canChangeOrgSite(final String relationship, final MboValue orgSiteMbv)\n
    canChangeOrgSite(final MboValue orgSiteMbv)\n
    '''
def setApplicationRequired():
    '''returns None\n\n
    setApplicationRequired(final String attribute, final boolean required)\n
    '''
def setByPassSortOrderValidation():
    '''returns None\n\n
    setByPassSortOrderValidation(final Boolean byPassSortOrderValidation)\n
    '''
