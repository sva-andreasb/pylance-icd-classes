def ():
    '''returns ClassSpec\n\n
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
def userSaidToDelete():
    '''returns boolean\n\n
    userSaidToDelete()\n
    '''
def delete():
    '''returns None\n\n
    delete(final long access)\n
    '''
def undelete():
    '''returns None\n\n
    undelete()\n
    '''
def getAssetAttributeMbo():
    '''returns MboRemote\n\n
    getAssetAttributeMbo()\n
    '''
def addOtherSpecs():
    '''returns None\n\n
    addOtherSpecs(final MboSetRemote mboSet)\n
    '''
def setColumnsReadOnly():
    '''returns None\n\n
    setColumnsReadOnly(final boolean setReadOnly)\n
    '''
def appValidate():
    '''returns None\n\n
    appValidate()\n
    '''
def populateClassSpecUseWith():
    '''returns None\n\n
    populateClassSpecUseWith(final MboRemote parentClassStructure)\n
    populateClassSpecUseWith(final MboSetRemote newClassSpecUseWithSet)\n
    '''
def populateSequence():
    '''returns int\n\n
    populateSequence(final MboRemote newClassSpecUseWith)\n
    '''
def getTableDomainObject():
    '''returns MboRemote\n\n
    getTableDomainObject()\n
    '''
def getClassStructure():
    '''returns ClassStructure\n\n
    getClassStructure()\n
    '''
def applyDownHierarchy():
    '''returns None\n\n
    applyDownHierarchy()\n
    '''
def UnApplyDownHierarchy():
    '''returns None\n\n
    UnApplyDownHierarchy()\n
    '''
def inClassificationApp():
    '''returns boolean\n\n
    inClassificationApp()\n
    '''
def checkRequiredFields():
    '''returns None\n\n
    checkRequiredFields()\n
    '''
def setClassSpecForApplyDownHier():
    '''returns None\n\n
    setClassSpecForApplyDownHier(final MboRemote classSpecApplyDownHier)\n
    '''
def getClassSpecForApplyDownHier():
    '''returns MboRemote\n\n
    getClassSpecForApplyDownHier()\n
    '''
def copy():
    '''returns MboRemote\n\n
    copy(final MboSetRemote newClassSpecSet, final long mboAddFlags)\n
    '''
def getValueToCrossOver():
    '''returns String\n\n
    getValueToCrossOver(final String srcAttrCSNN, final String tgtSpecObj, final String tgtSpecAttr)\n
    '''
def canChangeOrgSite():
    '''returns None\n\n
    canChangeOrgSite(final MboValue orgSiteMbv)\n
    '''
def storeExistingSpec():
    '''returns Hashtable\n\n
    storeExistingSpec(final MboSetRemote existingSpecSet, final String attrName, final String siteidORitemsetid)\n
    '''
def addOtherSpecsLargeForSqlServer():
    '''returns None\n\n
    addOtherSpecsLargeForSqlServer(final String tableName, final String where, int counter)\n
    '''
def copyValuesToChildClassSpec():
    '''returns None\n\n
    copyValuesToChildClassSpec(final MboRemote childClassSpec)\n
    '''
def setValue():
    '''returns None\n\n
    setValue(final String attributeName, final String val, final long accessModifier)\n
    '''
def getMinMaxSeq():
    '''returns long\n\n
    getMinMaxSeq(final String select)\n
    '''
def getUserDefinedRequired():
    '''returns String[]\n\n
    getUserDefinedRequired(final String specName, int startingIndex)\n
    '''
