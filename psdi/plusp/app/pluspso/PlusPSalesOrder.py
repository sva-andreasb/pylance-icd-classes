SALESORDER_STATUS_LIST = "String  \"PLUSPSOSTATUS\""
def ():
    '''returns PlusPSalesOrder\n\n
    (final MboSet ms)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def setFieldFlagsAccordingToGBTransRules():
    '''returns None\n\n
    setFieldFlagsAccordingToGBTransRules()\n
    '''
def editHistory():
    '''returns None\n\n
    editHistory()\n
    '''
def modify():
    '''returns None\n\n
    modify()\n
    '''
def canDelete():
    '''returns None\n\n
    canDelete()\n
    '''
def hasBeenExtractedForBilling():
    '''returns boolean\n\n
    hasBeenExtractedForBilling()\n
    '''
def duplicate():
    '''returns MboRemote\n\n
    duplicate()\n
    '''
def ownership():
    '''returns None\n\n
    ownership()\n
    '''
def insertOwnerHistory():
    '''returns None\n\n
    insertOwnerHistory(String personId, Date date, final String s, final String s2)\n
    '''
def generateAutoKey():
    '''returns None\n\n
    generateAutoKey()\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def toInternalSalesOrderStatus():
    '''returns String\n\n
    toInternalSalesOrderStatus(final String value)\n
    '''
def toExternalSalesOrderStatus():
    '''returns String\n\n
    toExternalSalesOrderStatus(final String value)\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(final String status, final Date asOfDate, final String memo, final long accessModifier)\n
    '''
def getStatusListName():
    '''returns String\n\n
    getStatusListName()\n
    '''
def applyAssetLoc():
    '''returns None\n\n
    applyAssetLoc()\n
    '''
def determineLocationAction():
    '''returns String[]\n\n
    determineLocationAction(final MboValue mboValue, String s, String string)\n
    '''
def coordinateAssetLocChange():
    '''returns None\n\n
    coordinateAssetLocChange(final MboValue mboValue, final String s, final String s2)\n
    '''
def determineAssetNumAction():
    '''returns String[]\n\n
    determineAssetNumAction(final MboValue mboValue, String s, String assetForLocation)\n
    '''
def copyFieldsToPlusPGBTrans():
    '''returns None\n\n
    copyFieldsToPlusPGBTrans(final PlusPGBTransRemote plusPGBTransRemote)\n
    '''
def isWAppr():
    '''returns boolean\n\n
    isWAppr()\n
    '''
def isAppr():
    '''returns boolean\n\n
    isAppr()\n
    '''
def isComp():
    '''returns boolean\n\n
    isComp()\n
    '''
def modifyLocation():
    '''returns None\n\n
    modifyLocation()\n
    '''
def modifyAsset():
    '''returns None\n\n
    modifyAsset()\n
    '''
def resetAddressUserInput():
    '''returns None\n\n
    resetAddressUserInput()\n
    '''
def setStreetAddress():
    '''returns None\n\n
    setStreetAddress()\n
    '''
def setModifySOFlags():
    '''returns None\n\n
    setModifySOFlags(final boolean b)\n
    '''
def removePS():
    '''returns boolean\n\n
    removePS()\n
    '''
def incrActFeePrice():
    '''returns None\n\n
    incrActFeePrice(final double n)\n
    '''
def delete():
    '''returns None\n\n
    delete(final long accessModifier)\n
    '''
def undelete():
    '''returns None\n\n
    undelete()\n
    '''
def setValue():
    '''returns None\n\n
    setValue(final String attributeName, final String val, final long accessModifier)\n
    '''
def warnAddRemoveFeesForSOwithCompStatus():
    '''returns boolean\n\n
    warnAddRemoveFeesForSOwithCompStatus()\n
    '''
def canChangeStatus():
    '''returns None\n\n
    canChangeStatus(final String changeToStatus, final long accessModifier)\n
    '''
def validateActions():
    '''returns None\n\n
    validateActions()\n
    '''
def hasBeenBilled():
    '''returns boolean\n\n
    hasBeenBilled()\n
    '''
def getServiceAddress():
    '''returns MboRemote\n\n
    getServiceAddress()\n
    '''
def hasServiceAddress():
    '''returns boolean\n\n
    hasServiceAddress()\n
    '''
def copyDataFromServiceAddress():
    '''returns None\n\n
    copyDataFromServiceAddress(final MboRemote sourceMbo)\n
    '''
def clearServiceAddress():
    '''returns None\n\n
    clearServiceAddress()\n
    '''
def recalculatePrices():
    '''returns None\n\n
    recalculatePrices(final MboRemote mboRemote)\n
    '''
def applyPriceScheduleToGBTrans():
    '''returns None\n\n
    applyPriceScheduleToGBTrans(final MboRemote mboRemote, final MboRemote mboRemote2, final boolean b)\n
    '''
def initRelationship():
    '''returns None\n\n
    initRelationship(final String s, final MboSetRemote mboSet)\n
    '''
def loadMatUseTransItemSaleSet():
    '''returns None\n\n
    loadMatUseTransItemSaleSet(final MboSetRemote mboSetRemote)\n
    '''
