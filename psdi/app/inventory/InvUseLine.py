def ():
    '''returns InvUseLine\n\n
    (final MboSet ms)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def isIssue():
    '''returns boolean\n\n
    isIssue()\n
    '''
def isReturn():
    '''returns boolean\n\n
    isReturn()\n
    '''
def isMixed():
    '''returns boolean\n\n
    isMixed()\n
    '''
def isTransfer():
    '''returns boolean\n\n
    isTransfer()\n
    '''
def isRotating():
    '''returns boolean\n\n
    isRotating()\n
    '''
def isLotted():
    '''returns boolean\n\n
    isLotted()\n
    '''
def isTool():
    '''returns boolean\n\n
    isTool()\n
    '''
def getSharedInventory():
    '''returns MboRemote\n\n
    getSharedInventory()\n
    getSharedInventory(final String storeLoc, final String siteid)\n
    '''
def getSharedInvBalance():
    '''returns MboRemote\n\n
    getSharedInvBalance()\n
    getSharedInvBalance(final String binnum, final String lotnum)\n
    getSharedInvBalance(final String binnum, final String lotnum, final boolean sameBin)\n
    getSharedInvBalance(final String binnum, final String lotnum, final String storeloc, final String siteid)\n
    '''
def setIssueForThisReturn():
    '''returns None\n\n
    setIssueForThisReturn(final MboRemote issue)\n
    '''
def getWO():
    '''returns MboRemote\n\n
    getWO()\n
    '''
def validateInvUseLine():
    '''returns None\n\n
    validateInvUseLine(final ArrayList<InvUseLineSplitRemote> splitList)\n
    '''
def preValidateLine():
    '''returns None\n\n
    preValidateLine()\n
    '''
def validateLine():
    '''returns None\n\n
    validateLine()\n
    '''
def checkInvBal():
    '''returns None\n\n
    checkInvBal(final MboRemote invBal, final String parentInvUseStatus)\n
    '''
def checkLotExpiry():
    '''returns None\n\n
    checkLotExpiry(final MboRemote invBal, final ItemRemote item)\n
    '''
def checkAssetWOLocValidate():
    '''returns None\n\n
    checkAssetWOLocValidate()\n
    '''
def appValidate():
    '''returns None\n\n
    appValidate()\n
    '''
def getBinNumFlag():
    '''returns boolean\n\n
    getBinNumFlag()\n
    '''
def setBinNumFlag():
    '''returns None\n\n
    setBinNumFlag(final boolean binNumFlag)\n
    '''
def addUpdateInvUseLineSplit():
    '''returns MboRemote\n\n
    addUpdateInvUseLineSplit()\n
    '''
def save():
    '''returns None\n\n
    save()\n
    '''
def setPickListStatus():
    '''returns None\n\n
    setPickListStatus(final MboRemote owner)\n
    '''
def setInvUseStatus():
    '''returns None\n\n
    setInvUseStatus(final MboRemote owner)\n
    '''
def isPLActionApplied():
    '''returns boolean\n\n
    isPLActionApplied(final String action)\n
    '''
def chkPickListMbo():
    '''returns boolean\n\n
    chkPickListMbo(final MboRemote owner)\n
    '''
def updateAutoCreatedInvUseLineSplit():
    '''returns MboRemote\n\n
    updateAutoCreatedInvUseLineSplit()\n
    '''
def restockPickedQty():
    '''returns None\n\n
    restockPickedQty()\n
    '''
def restockStagedQty():
    '''returns None\n\n
    restockStagedQty()\n
    '''
def setStagingBin():
    '''returns None\n\n
    setStagingBin(final String binflag, final String stagingBin)\n
    '''
def checkForNegativeBalance():
    '''returns None\n\n
    checkForNegativeBalance(final MboRemote invBal, final MboRemote invuselinesplit)\n
    '''
def checkForNegativeAvlBalanceBeforeSplitting():
    '''returns None\n\n
    checkForNegativeAvlBalanceBeforeSplitting()\n
    '''
def getSharedInvReserveSet():
    '''returns MboSetRemote\n\n
    getSharedInvReserveSet()\n
    '''
def updateInvBalances():
    '''returns None\n\n
    updateInvBalances(final MboRemote mbo, final double quantity, final String status)\n
    '''
def updateStagedInvBalances():
    '''returns None\n\n
    updateStagedInvBalances(final String status)\n
    updateStagedInvBalances(final String status, final MboRemote mbo)\n
    '''
def updateInvReservePendingQty():
    '''returns None\n\n
    updateInvReservePendingQty()\n
    '''
def updateInvReserveStagedQty():
    '''returns None\n\n
    updateInvReserveStagedQty()\n
    updateInvReserveStagedQty(final MboRemote mbo)\n
    '''
def updateInvReservePickedQty():
    '''returns None\n\n
    updateInvReservePickedQty(final MboRemote mbo)\n
    '''
def updateInvReserveActualQty():
    '''returns None\n\n
    updateInvReserveActualQty()\n
    updateInvReserveActualQty(final boolean toUpdateWithNoRequestnum)\n
    updateInvReserveActualQty(final boolean toUpdateWithNoRequestnum, final MboRemote mbo)\n
    '''
def updateInvReserveShippedQty():
    '''returns None\n\n
    updateInvReserveShippedQty()\n
    '''
def updateInvReserveForCancel():
    '''returns None\n\n
    updateInvReserveForCancel()\n
    '''
def canDelete():
    '''returns None\n\n
    canDelete()\n
    '''
def delete():
    '''returns None\n\n
    delete(final long accessModifier)\n
    '''
def undelete():
    '''returns None\n\n
    undelete()\n
    '''
def checkReservationExist():
    '''returns boolean\n\n
    checkReservationExist()\n
    '''
def checkReservationExistForInfo():
    '''returns None\n\n
    checkReservationExistForInfo()\n
    '''
def checkIssueExist():
    '''returns boolean\n\n
    checkIssueExist()\n
    '''
def checkIssueExistForInfo():
    '''returns None\n\n
    checkIssueExistForInfo()\n
    '''
def updateInvUseLineForReservation():
    '''returns None\n\n
    updateInvUseLineForReservation(final MboRemote reservation)\n
    '''
def updateInvUseLineForReturn():
    '''returns None\n\n
    updateInvUseLineForReturn(final MboRemote issuedItemForReturn)\n
    '''
def addRecordForStageTransfer():
    '''returns None\n\n
    addRecordForStageTransfer(final MboSetRemote matrecMboSet, final ArrayList<InvUseLineSplitRemote> splitLineSplit)\n
    '''
def addMatRecTransRecordForPickTransfer():
    '''returns MboRemote\n\n
    addMatRecTransRecordForPickTransfer(final MboSetRemote matrecMboSet, final MboRemote mbo)\n
    '''
def addMatRecTransRecordForRestockTransfer():
    '''returns MboRemote\n\n
    addMatRecTransRecordForRestockTransfer(final MboSetRemote matrecMboSet, final MboRemote mbo)\n
    '''
def addMatRecTransRecordForStageTransfer():
    '''returns MboRemote\n\n
    addMatRecTransRecordForStageTransfer(final MboSetRemote matrecMboSet, final MboRemote mbo)\n
    '''
def addRecordForShipTransfer():
    '''returns None\n\n
    addRecordForShipTransfer(final MboSetRemote matrecMboSet, final ArrayList<InvUseLineSplitRemote> splitLineSplit)\n
    '''
def addMatRecTransRecordForShipTransfer():
    '''returns MboRemote\n\n
    addMatRecTransRecordForShipTransfer(final MboSetRemote matrecMboSet, final MboRemote mbo)\n
    '''
def addTransferRecordForComplete():
    '''returns None\n\n
    addTransferRecordForComplete(final MboSetRemote matrecMboSet, final ArrayList<InvUseLineSplitRemote> splitLineSplit)\n
    '''
def addMatRecTransRecordForComplete():
    '''returns MboRemote\n\n
    addMatRecTransRecordForComplete(final MboSetRemote matrecMboSet, final MboRemote mbo)\n
    '''
def addIssueReturnRecordForComplete():
    '''returns None\n\n
    addIssueReturnRecordForComplete(final MboSetRemote matrecMboSet, final ArrayList<InvUseLineSplitRemote> splitLineSplit)\n
    '''
def addMatUseTransRecordForComplete():
    '''returns MboRemote\n\n
    addMatUseTransRecordForComplete(final MboSetRemote matuseMboSet, final MboRemote mbo)\n
    '''
def addMatRecTransRecordForCancelStageTransfer():
    '''returns MboRemote\n\n
    addMatRecTransRecordForCancelStageTransfer()\n
    '''
def addMatRecTransRecordForCancelShipTransfer():
    '''returns MboRemote\n\n
    addMatRecTransRecordForCancelShipTransfer()\n
    '''
def getPO():
    '''returns MboRemote\n\n
    getPO()\n
    '''
def setOwnerPO():
    '''returns None\n\n
    setOwnerPO(final MboRemote po)\n
    '''
def getPOLine():
    '''returns MboRemote\n\n
    getPOLine()\n
    '''
def getTotalCurBalance():
    '''returns double\n\n
    getTotalCurBalance()\n
    '''
def getInvUseLineQtyForReturn():
    '''returns double\n\n
    getInvUseLineQtyForReturn(final long matusetransid)\n
    '''
def getQtyForReturn():
    '''returns double\n\n
    getQtyForReturn()\n
    '''
def updateUnitCost():
    '''returns None\n\n
    updateUnitCost()\n
    '''
def validateQty():
    '''returns boolean\n\n
    validateQty()\n
    '''
def needsSplitting():
    '''returns boolean\n\n
    needsSplitting()\n
    '''
def getDefaultLotNum():
    '''returns String\n\n
    getDefaultLotNum()\n
    '''
def canGoNegative():
    '''returns None\n\n
    canGoNegative(final UserInfo userInfo, final double toBeIssued, final double curbal, final double totalAvailable, final MboRemote sourceMbo)\n
    canGoNegative(final UserInfo userInfo, final double toBeIssued, final double totalAvailable, final MboRemote sourceMbo)\n
    '''
def modify():
    '''returns None\n\n
    modify()\n
    '''
def checkItemStatus():
    '''returns None\n\n
    checkItemStatus()\n
    '''
def setReservationUserPref():
    '''returns None\n\n
    setReservationUserPref()\n
    '''
def setReturnUserPref():
    '''returns None\n\n
    setReturnUserPref()\n
    '''
def setUserPref():
    '''returns None\n\n
    setUserPref(final MboRemote mbo)\n
    '''
def getPendingQty():
    '''returns double\n\n
    getPendingQty(final String requestnum, final String siteid)\n
    '''
def smartFindByObjectName():
    '''returns MboSetRemote\n\n
    smartFindByObjectName(final String sourceObj, final String targetAttrName, final String value, final boolean exact)\n
    '''
def checkRotatingAssetExistInToSite():
    '''returns boolean\n\n
    checkRotatingAssetExistInToSite(final String rotassetnum, final MboRemote mbo)\n
    '''
def updateAssetStatus():
    '''returns None\n\n
    updateAssetStatus(final String rotassetnum, final String status)\n
    '''
def updateReceiptsComplete():
    '''returns None\n\n
    updateReceiptsComplete()\n
    '''
def updateReceivedQty():
    '''returns None\n\n
    updateReceivedQty(final double receivedQty)\n
    '''
def updateReturnedQty():
    '''returns None\n\n
    updateReturnedQty(final double returnedQty)\n
    '''
def isInspectionRequired():
    '''returns boolean\n\n
    isInspectionRequired()\n
    '''
def initFieldFlagsOnMbo():
    '''returns None\n\n
    initFieldFlagsOnMbo(final String attrName)\n
    '''
def setDisplayUnitCost():
    '''returns None\n\n
    setDisplayUnitCost()\n
    '''
def updateLifoFifoTable():
    '''returns None\n\n
    updateLifoFifoTable(final MboRemote invUseLineSplit)\n
    '''
def updateLifoFifoForCancelled():
    '''returns None\n\n
    updateLifoFifoForCancelled(final MboRemote useLine)\n
    '''
def addTransactionRecordsLIFOFIFO():
    '''returns None\n\n
    addTransactionRecordsLIFOFIFO(final MboSetRemote transMboSet, final ArrayList<InvUseLineSplitRemote> splitLineSplit, final String status)\n
    '''
def updateInvLifoFifoCostSet():
    '''returns double\n\n
    updateInvLifoFifoCostSet(final MboSetRemote transMboSet, MboRemote invUseLineSplit, final MboSetRemote invlifofifocostset, final String status)\n
    '''
def setAttributesEditibiltyForReturn():
    '''returns None\n\n
    setAttributesEditibiltyForReturn()\n
    '''
def allKitComponentsAreInTransferToStore():
    '''returns None\n\n
    allKitComponentsAreInTransferToStore()\n
    '''
def updateMR():
    '''returns None\n\n
    updateMR(final MboRemote invReserve)\n
    '''
def getPhyscntDate():
    '''returns Date\n\n
    getPhyscntDate(Date phyCntDate, final Date actualDate)\n
    '''
def getInvReserveInVector():
    '''returns InvReserveRemote\n\n
    getInvReserveInVector(final Vector v, final MboRemote thisInvReserve)\n
    '''
def isSameStoreTransfer():
    '''returns boolean\n\n
    isSameStoreTransfer()\n
    '''
def getInvUse():
    '''returns MboRemote\n\n
    getInvUse()\n
    '''
def setCancelInvUseLines():
    '''returns None\n\n
    setCancelInvUseLines(final boolean hasBeenCalled)\n
    '''
def setValue():
    '''returns None\n\n
    setValue(final String attributeName, final String val, final long accessModifier)\n
    '''
