def ():
    '''returns InvUse\n\n
    (final MboSet ms)\n
    '''
def getProcess():
    '''returns String\n\n
    getProcess()\n
    '''
def getStatusListName():
    '''returns String\n\n
    getStatusListName()\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def initFieldFlagsOnMbo():
    '''returns None\n\n
    initFieldFlagsOnMbo(final String attrName)\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def getStatus():
    '''returns String\n\n
    getStatus()\n
    '''
def addInvUseLine():
    '''returns InvUseLineRemote\n\n
    addInvUseLine(final MboRemote owner)\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(final String status, final Date date, final String memo, final long accessModifier)\n
    changeStatus(final String status, final Date date, final String memo, final String binflag, final String stagingbin, final boolean listtab, final long accessModifier)\n
    '''
def validateStatus():
    '''returns None\n\n
    validateStatus(final String status, final Date date, final String memo, final String binflag, final String stagingbin, final boolean listtab)\n
    '''
def chkPickListMbo():
    '''returns boolean\n\n
    chkPickListMbo(final MboRemote owner)\n
    '''
def checkReservationandSetBin():
    '''returns None\n\n
    checkReservationandSetBin(final String binflag, final String stagebin, final String status)\n
    '''
def validateLineReservationandSetBin():
    '''returns boolean\n\n
    validateLineReservationandSetBin(final boolean listtab, final String binflag, final String stagebin, final String status)\n
    '''
def processInvUseLines():
    '''returns boolean\n\n
    processInvUseLines()\n
    '''
def deleteInvUseLines():
    '''returns None\n\n
    deleteInvUseLines()\n
    '''
def cancelInvUseLines():
    '''returns None\n\n
    cancelInvUseLines()\n
    '''
def getInvUseLineNum():
    '''returns String\n\n
    getInvUseLineNum()\n
    '''
def allReservationDeletedInSet():
    '''returns boolean\n\n
    allReservationDeletedInSet()\n
    '''
def isEntered():
    '''returns boolean\n\n
    isEntered()\n
    '''
def isStaged():
    '''returns boolean\n\n
    isStaged()\n
    '''
def isShipped():
    '''returns boolean\n\n
    isShipped()\n
    '''
def isCompleted():
    '''returns boolean\n\n
    isCompleted()\n
    '''
def isCancelled():
    '''returns boolean\n\n
    isCancelled()\n
    '''
def copyInvUseLineSetForReturn():
    '''returns None\n\n
    copyInvUseLineSetForReturn(final MboSetRemote matUseTransSet)\n
    '''
def copyInvReserveSetForInvUse():
    '''returns None\n\n
    copyInvReserveSetForInvUse(final MboSetRemote invReserveSet)\n
    '''
def copySparePartSetForInvUse():
    '''returns None\n\n
    copySparePartSetForInvUse(final MboSetRemote sparePartSet)\n
    '''
def copyInvBalancesSetForItems():
    '''returns None\n\n
    copyInvBalancesSetForItems(final MboSetRemote invBalancesSet)\n
    '''
def isTransfer():
    '''returns boolean\n\n
    isTransfer()\n
    '''
def isIssue():
    '''returns boolean\n\n
    isIssue()\n
    '''
def staged():
    '''returns None\n\n
    staged()\n
    '''
def complete():
    '''returns None\n\n
    complete(final String currentMaxStatus)\n
    '''
def shipped():
    '''returns None\n\n
    shipped(final String currentMaxStatus)\n
    '''
def cancelled():
    '''returns None\n\n
    cancelled()\n
    '''
def isSplitNeeded():
    '''returns None\n\n
    isSplitNeeded(final MboRemote invUseLine)\n
    '''
def isListSelected():
    '''returns boolean\n\n
    isListSelected()\n
    '''
def setListSelected():
    '''returns None\n\n
    setListSelected(final boolean isListSelected)\n
    '''
def validateLines():
    '''returns None\n\n
    validateLines(final String status)\n
    '''
def checkNegativeBalanace():
    '''returns None\n\n
    checkNegativeBalanace(final MboRemote invuseline)\n
    '''
def validateRotatingAssets():
    '''returns None\n\n
    validateRotatingAssets(final MboRemote invUseLine)\n
    '''
def validateGLAccounts():
    '''returns None\n\n
    validateGLAccounts(final MboRemote invuseline)\n
    '''
def modify():
    '''returns None\n\n
    modify()\n
    '''
def getUseType():
    '''returns String\n\n
    getUseType()\n
    '''
def validatedata():
    '''returns None\n\n
    validatedata()\n
    '''
def checkReturnLinesinSet():
    '''returns boolean\n\n
    checkReturnLinesinSet()\n
    '''
def setQtyMap():
    '''returns None\n\n
    setQtyMap(final Long invBalId, final Double qty)\n
    '''
def removeQtyMap():
    '''returns None\n\n
    removeQtyMap(final Long invBalId)\n
    '''
def setUsedRotAssetNSMap():
    '''returns None\n\n
    setUsedRotAssetNSMap(final String keyid, final String rotassetnum)\n
    '''
def removeUsedRotAssetNSMap():
    '''returns None\n\n
    removeUsedRotAssetNSMap(final String keyid)\n
    '''
def setUsedRotAssetSMap():
    '''returns None\n\n
    setUsedRotAssetSMap(final String keyid, final String rotassetnum)\n
    '''
def removeUsedRotAssetSMap():
    '''returns None\n\n
    removeUsedRotAssetSMap(final String keyid)\n
    '''
def setRotQtyMap():
    '''returns None\n\n
    setRotQtyMap(final Long keyid, final Double qty)\n
    '''
def removeRotQtyMap():
    '''returns None\n\n
    removeRotQtyMap(final Long keyid)\n
    '''
def getDeletedInvUseLineList():
    '''returns ArrayList<Long>\n\n
    getDeletedInvUseLineList()\n
    '''
def setInvBalQtyNSMap():
    '''returns None\n\n
    setInvBalQtyNSMap(final Long invBalId, final Double qty)\n
    '''
def removeInvBalQtyNSMap():
    '''returns None\n\n
    removeInvBalQtyNSMap(final Long invBalId)\n
    '''
def getUsedRotAssetList():
    '''returns ArrayList<String>\n\n
    getUsedRotAssetList()\n
    '''
def addToUsedRotAssetList():
    '''returns None\n\n
    addToUsedRotAssetList(final String rotassetnum)\n
    '''
def checkRotAssetNumList():
    '''returns None\n\n
    checkRotAssetNumList(final String key, final String rotassetnum, final boolean newasset)\n
    '''
def canDelete():
    '''returns None\n\n
    canDelete()\n
    '''
def setShipmentLines():
    '''returns MboRemote\n\n
    setShipmentLines()\n
    '''
def addShipmentLines():
    '''returns None\n\n
    addShipmentLines(final MboRemote shipment)\n
    '''
def validateForShipped():
    '''returns None\n\n
    validateForShipped(final MboRemote invUseLine)\n
    '''
def getClearingAcct():
    '''returns String\n\n
    getClearingAcct()\n
    '''
def save():
    '''returns None\n\n
    save()\n
    '''
def updateInvUseReceipts():
    '''returns None\n\n
    updateInvUseReceipts(final InvUseLineRemote invUseLine)\n
    '''
def getExchangeRate():
    '''returns double\n\n
    getExchangeRate(final Date date)\n
    '''
def getExchangeRate2():
    '''returns double\n\n
    getExchangeRate2(final Date date)\n
    '''
def validateHardReservation():
    '''returns None\n\n
    validateHardReservation(final MboRemote invUseLine)\n
    '''
def getEvaluateSplitFlag():
    '''returns int\n\n
    getEvaluateSplitFlag()\n
    '''
def setEvaluateSplitFlag():
    '''returns int\n\n
    setEvaluateSplitFlag(final int split)\n
    '''
def setValidateStatusHasBeenCalled():
    '''returns None\n\n
    setValidateStatusHasBeenCalled(final boolean hasBeenCalled)\n
    '''
def getValidateStatusHasBeenCalled():
    '''returns boolean\n\n
    getValidateStatusHasBeenCalled()\n
    '''
def createInvUsageForPartialIssues():
    '''returns MboRemote\n\n
    createInvUsageForPartialIssues(final MboSetRemote invReserveSet)\n
    '''
def duplicate():
    '''returns MboRemote\n\n
    duplicate()\n
    '''
def selectAllInSet():
    '''returns None\n\n
    selectAllInSet(final MboSetRemote invReserveSet)\n
    '''
def appValidate():
    '''returns None\n\n
    appValidate()\n
    '''
def validateFinancialPeriods():
    '''returns None\n\n
    validateFinancialPeriods(final String newStatus)\n
    '''
def canUseNextFinancialPeriod():
    '''returns Boolean\n\n
    canUseNextFinancialPeriod()\n
    '''
def getValidateFinancialPeriodsHasBeenCalled():
    '''returns boolean\n\n
    getValidateFinancialPeriodsHasBeenCalled()\n
    '''
def setValidateFinancialPeriodsCalled():
    '''returns None\n\n
    setValidateFinancialPeriodsCalled(final boolean hasBeenCalled)\n
    '''
