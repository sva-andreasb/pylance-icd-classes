IBM_COPYRIGHT = "String  \"\n\nLicensed Materials - Property of IBM\n5725-E24\n(C)Copyright IBM Corporation 2007, 2013.\nAll Rights Reserved.\nUS Government Users Restricted Rights - Use, duplication \nor disclosure restricted by GSA ADP Schedule Contract with IBM Corp.\n\n\""
DECOMMISSION_CIS_IN_BASELINE_PROPERTY = "String  \"cci.changestatus.decommissionCIsInBaseline\""
intLinkMethodUI = "String  \"User Interface\""
intLinkMethodReconciliation = "String  \"Reconciliation\""
intLinkMethodOther = "String  \"Other\""
linkRuleCreateGeneric = "String  \"CCIAssetCICreateGeneric\""
def ():
    '''returns CCICI\n\n
    (final MboSet ms)\n
    '''
def isTopLevel():
    '''returns boolean\n\n
    isTopLevel()\n
    '''
def save():
    '''returns None\n\n
    save()\n
    '''
def getDISInfo():
    '''returns DISInfo\n\n
    getDISInfo()\n
    '''
def updateCIAssetLinkInfo():
    '''returns None\n\n
    updateCIAssetLinkInfo(final Date linkDate, final String linkBy, final String linkMethod, final String linkRule, final boolean toUpdateLinkRule)\n
    '''
def syncAuthorizedCI():
    '''returns ArrayList<CCIPromotionResults>\n\n
    syncAuthorizedCI(final long synchronizationOptions)\n
    syncAuthorizedCI(final long synchronizationOptions, final CCITraversalCache cache)\n
    '''
def copyAttributeFromActualCI():
    '''returns None\n\n
    copyAttributeFromActualCI(final CISpecRemote ciSpec)\n
    '''
def getSpecificationAttribute():
    '''returns SpecificationMboRemote\n\n
    getSpecificationAttribute(final String assetAttrID)\n
    '''
def delete():
    '''returns None\n\n
    delete(final long accessModifier)\n
    delete(final boolean dontCheckoptherApps, final long accessModifier)\n
    '''
def undelete():
    '''returns None\n\n
    undelete()\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(final String status, final Date asOfDate, final String memo)\n
    changeStatus(final String status, final Date asOfDate, final String memo, final boolean childFlag)\n
    '''
def duplicate():
    '''returns MboRemote\n\n
    duplicate()\n
    '''
def getSourceRelations():
    '''returns MboSetRemote\n\n
    getSourceRelations(final Date asOf)\n
    getSourceRelations()\n
    '''
def getTargetRelations():
    '''returns MboSetRemote\n\n
    getTargetRelations(final Date asOf)\n
    getTargetRelations()\n
    '''
def handleRFC():
    '''returns None\n\n
    handleRFC(final MboRemote parentCI)\n
    '''
def generateSpecSet():
    '''returns MboSetRemote\n\n
    generateSpecSet(final CCITraversalCache tc)\n
    '''
def processOldAndNewSpecSets():
    '''returns None\n\n
    processOldAndNewSpecSets(final MboSetRemote oldSpecDeletedSet, final MboSetRemote newSpecSet)\n
    '''
def sortedClassSpecSet():
    '''returns Vector\n\n
    sortedClassSpecSet(final MboSetRemote classSpecSet, final MboRemote mbo)\n
    '''
def addDetailInfor():
    '''returns None\n\n
    addDetailInfor(final SpecificationMboRemote smr, final MboRemote wo, final CCITraversalCache.ClassSpecInfo csi, final CCITraversalCache.ClassSpecUseWithInfo csuwi)\n
    '''
def createGenericAsset():
    '''returns boolean\n\n
    createGenericAsset()\n
    createGenericAsset(final String reconTaskName)\n
    createGenericAsset(final boolean isValidateDupDisGuid, final boolean isValidateLinkRule, final LinkValidatorMetaLoader linkRuleMetaLoader)\n
    '''
def getDefaultStatus():
    '''returns String\n\n
    getDefaultStatus()\n
    '''
def changeStatusBypassingChecks():
    '''returns None\n\n
    changeStatusBypassingChecks(final String targetStatus, String memo)\n
    '''
def hasServiceAddress():
    '''returns boolean\n\n
    hasServiceAddress()\n
    '''
def saveGISData():
    '''returns None\n\n
    saveGISData(final String address, final String lat, final String lng)\n
    '''
def isGISDataReadonly():
    '''returns boolean\n\n
    isGISDataReadonly()\n
    '''
def getLatitudeY():
    '''returns Double\n\n
    getLatitudeY()\n
    '''
def getLongitudeX():
    '''returns Double\n\n
    getLongitudeX()\n
    '''
def getAddressString():
    '''returns String\n\n
    getAddressString()\n
    '''
def getSAMboFromAssetLoc():
    '''returns MboRemote\n\n
    getSAMboFromAssetLoc()\n
    '''
def getMboSet():
    '''returns MboSetRemote\n\n
    getMboSet(final String name)\n
    '''
def getServiceAddress():
    '''returns ServiceAddressRemote\n\n
    getServiceAddress()\n
    '''
def hasCoords():
    '''returns Boolean\n\n
    hasCoords()\n
    '''
def actionOnAssetNumFld():
    '''returns None\n\n
    actionOnAssetNumFld(final MboRemote asset)\n
    '''
