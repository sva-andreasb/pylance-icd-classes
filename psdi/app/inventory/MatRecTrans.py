def ():
    '''returns MatRecTrans\n\n
    (final MboSet ms)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def getBinNumFlag():
    '''returns boolean\n\n
    getBinNumFlag()\n
    '''
def setBinNumFlag():
    '''returns None\n\n
    setBinNumFlag(final boolean binNumFlag)\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def canDelete():
    '''returns None\n\n
    canDelete()\n
    '''
def isTransfer():
    '''returns boolean\n\n
    isTransfer()\n
    '''
def isPicksTransfer():
    '''returns boolean\n\n
    isPicksTransfer()\n
    '''
def isPickRestock():
    '''returns boolean\n\n
    isPickRestock()\n
    '''
def isShipReceipt():
    '''returns boolean\n\n
    isShipReceipt()\n
    '''
def isTransferNoPO():
    '''returns boolean\n\n
    isTransferNoPO()\n
    '''
def isReceipt():
    '''returns boolean\n\n
    isReceipt()\n
    '''
def isReturn():
    '''returns boolean\n\n
    isReturn()\n
    '''
def isInvoice():
    '''returns boolean\n\n
    isInvoice()\n
    '''
def isMisclReceipt():
    '''returns boolean\n\n
    isMisclReceipt()\n
    '''
def isVoidReceipt():
    '''returns boolean\n\n
    isVoidReceipt()\n
    '''
def hasVoidReceipt():
    '''returns boolean\n\n
    hasVoidReceipt()\n
    '''
def isHolding():
    '''returns boolean\n\n
    isHolding()\n
    '''
def getHoldingLocationForSite():
    '''returns MboRemote\n\n
    getHoldingLocationForSite(final String siteid)\n
    '''
def isReject():
    '''returns boolean\n\n
    isReject()\n
    '''
def isShipReject():
    '''returns boolean\n\n
    isShipReject()\n
    '''
def getReceiptStatus():
    '''returns String\n\n
    getReceiptStatus()\n
    '''
def getClearingAcct():
    '''returns MboRemote\n\n
    getClearingAcct()\n
    '''
def approve():
    '''returns None\n\n
    approve(Date statusDate)\n
    approve(final MboSetRemote assetInputSet)\n
    '''
def updateInventory():
    '''returns None\n\n
    updateInventory(final InventoryRemote invmbo, final PORemote poMbo, final InvCost invcost)\n
    '''
def addRotatingAsset():
    '''returns None\n\n
    addRotatingAsset(final String assetnum)\n
    '''
def appValidate():
    '''returns None\n\n
    appValidate()\n
    '''
def save():
    '''returns None\n\n
    save()\n
    '''
def createInvoiceOnConsumption():
    '''returns None\n\n
    createInvoiceOnConsumption()\n
    '''
def updateInvReserveActualQty():
    '''returns None\n\n
    updateInvReserveActualQty(final MboRemote invUseLine)\n
    '''
def getReceiptForThisReturn():
    '''returns MboRemote\n\n
    getReceiptForThisReturn()\n
    '''
def getshipTransferForThisShipReceipt():
    '''returns MboRemote\n\n
    getshipTransferForThisShipReceipt()\n
    '''
def setAproveAfterCreatingAssets():
    '''returns None\n\n
    setAproveAfterCreatingAssets(final boolean flag)\n
    '''
def getApproveAfterCreatingAssets():
    '''returns boolean\n\n
    getApproveAfterCreatingAssets()\n
    '''
def rejectsForRotatingShipments():
    '''returns None\n\n
    rejectsForRotatingShipments()\n
    '''
def transferForRotatingShipments():
    '''returns None\n\n
    transferForRotatingShipments()\n
    '''
def approveShipReceipt():
    '''returns None\n\n
    approveShipReceipt()\n
    '''
def approveCrossSiteShipment():
    '''returns None\n\n
    approveCrossSiteShipment(final MboSetRemote assetInputSet, final MboRemote oneAssetInput)\n
    '''
def setInspectionRequiredEditibilityFlags():
    '''returns None\n\n
    setInspectionRequiredEditibilityFlags(final boolean flag)\n
    '''
def canApprove():
    '''returns None\n\n
    canApprove()\n
    '''
def onlyPayOnReceipt():
    '''returns None\n\n
    onlyPayOnReceipt(final PORemote poMbo, final POLineRemote poLineMbo)\n
    '''
def setToInvBalUpdated():
    '''returns None\n\n
    setToInvBalUpdated()\n
    '''
def setFromInvBalUpdated():
    '''returns None\n\n
    setFromInvBalUpdated()\n
    '''
def getCourierLaborTransientMatRec():
    '''returns MboRemote\n\n
    getCourierLaborTransientMatRec()\n
    '''
def getSharedInventory():
    '''returns MboRemote\n\n
    getSharedInventory(final String storeLoc, final String siteid)\n
    '''
def calculateUnInvoicedQtyCost():
    '''returns double[]\n\n
    calculateUnInvoicedQtyCost()\n
    '''
def createReturn():
    '''returns None\n\n
    createReturn(final MatRecTransRemote matrec)\n
    '''
def getInvCostRecord():
    '''returns MboRemote\n\n
    getInvCostRecord(final MboRemote toInventory)\n
    '''
def updateInventoryCostAndBalances():
    '''returns None\n\n
    updateInventoryCostAndBalances()\n
    '''
def isSwitchoffWOUpdate():
    '''returns boolean\n\n
    isSwitchoffWOUpdate()\n
    '''
def setSwitchoffWOUpdate():
    '''returns None\n\n
    setSwitchoffWOUpdate(final boolean switchoffWOUpdate)\n
    '''
def setInvReserveUpdatedFlag():
    '''returns None\n\n
    setInvReserveUpdatedFlag(final boolean updated)\n
    '''
def setCheckNegBalance():
    '''returns None\n\n
    setCheckNegBalance(final boolean updated)\n
    '''
def getPOLineUpdated():
    '''returns boolean\n\n
    getPOLineUpdated()\n
    '''
def setPOLineUpdated():
    '''returns None\n\n
    setPOLineUpdated()\n
    '''
def isStageTransfer():
    '''returns boolean\n\n
    isStageTransfer()\n
    '''
def isShipTransfer():
    '''returns boolean\n\n
    isShipTransfer()\n
    '''
def isShipCancel():
    '''returns boolean\n\n
    isShipCancel()\n
    '''
def isShipReturn():
    '''returns boolean\n\n
    isShipReturn()\n
    '''
def isVoidShipReceipt():
    '''returns boolean\n\n
    isVoidShipReceipt()\n
    '''
def createMatRecTransRecordforLifoFifo():
    '''returns None\n\n
    createMatRecTransRecordforLifoFifo(final MboRemote inv)\n
    '''
def canBeReturned():
    '''returns boolean\n\n
    canBeReturned()\n
    '''
def setShipmentMap():
    '''returns None\n\n
    setShipmentMap()\n
    '''
def isDirectIssueConversion():
    '''returns boolean\n\n
    isDirectIssueConversion()\n
    isDirectIssueConversion(final boolean includeStoreroom)\n
    '''
def getDirectIssueConversion():
    '''returns double\n\n
    getDirectIssueConversion()\n
    '''
def createStdRecAdjOnRotAssetTransferIn():
    '''returns None\n\n
    createStdRecAdjOnRotAssetTransferIn()\n
    '''
def isSameStoreTransfer():
    '''returns boolean\n\n
    isSameStoreTransfer()\n
    '''
def setOriginalCostDate():
    '''returns None\n\n
    setOriginalCostDate(final Date costDate)\n
    '''
def getOriginalCostDate():
    '''returns Date\n\n
    getOriginalCostDate()\n
    '''
def setWorkOrderUpdatedFlag():
    '''returns None\n\n
    setWorkOrderUpdatedFlag(final boolean updated)\n
    '''
def getWorkOrderUpdatedFlag():
    '''returns boolean\n\n
    getWorkOrderUpdatedFlag()\n
    '''
def isRejectedReturn():
    '''returns boolean\n\n
    isRejectedReturn()\n
    '''
def createShipReceiptRecordsforLifoFifo():
    '''returns None\n\n
    createShipReceiptRecordsforLifoFifo()\n
    '''
