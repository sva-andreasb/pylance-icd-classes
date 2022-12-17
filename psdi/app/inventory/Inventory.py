def ():
    '''returns Inventory\n\n
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
def setIsKitComponentToAddToStore():
    '''returns None\n\n
    setIsKitComponentToAddToStore(final boolean isKitComponentToAddToStore)\n
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
def setCostType():
    '''returns None\n\n
    setCostType()\n
    '''
def appValidate():
    '''returns None\n\n
    appValidate()\n
    '''
def isKit():
    '''returns boolean\n\n
    isKit()\n
    '''
def isCapitalized():
    '''returns boolean\n\n
    isCapitalized()\n
    '''
def save():
    '''returns None\n\n
    save()\n
    '''
def addUpdateInvVendor():
    '''returns None\n\n
    addUpdateInvVendor()\n
    '''
def getPrimaryInvVendor():
    '''returns MboRemote\n\n
    getPrimaryInvVendor(final MboSetRemote invVendSet)\n
    '''
def doAdjustment():
    '''returns MboRemote\n\n
    doAdjustment(final NonPersistentMboRemote invAdj)\n
    '''
def adjustCurrentBalance():
    '''returns MboRemote\n\n
    adjustCurrentBalance(final String binnum, final String lotnum, final double newBalance, final String conditionCode)\n
    '''
def adjustPhysicalCount():
    '''returns MboRemote\n\n
    adjustPhysicalCount(final String binnum, final String lotnum, final double quantity, final Date pCountDate)\n
    adjustPhysicalCount(final String binnum, final String lotnum, final double quantity, final Date pCountDate, final String ownersysid)\n
    adjustPhysicalCount(final String binnum, final String lotnum, final double quantity, final Date pCountDate, final String ownersysid, final String conditionCode)\n
    '''
def getDefaultIssueCost():
    '''returns double\n\n
    getDefaultIssueCost(final AssetRemote assetRemote, final String conditionCode)\n
    getDefaultIssueCost(final AssetRemote assetRemote)\n
    getDefaultIssueCost()\n
    getDefaultIssueCost(final String conditionCode)\n
    getDefaultIssueCost(final ArrayList<InvLifoFifoCost> invLifoFifoCostList)\n
    '''
def updateInventoryAverageCost():
    '''returns None\n\n
    updateInventoryAverageCost(final double quantity, final double totalvalue)\n
    updateInventoryAverageCost(final double quantity, final double totalvalue, final double exr)\n
    updateInventoryAverageCost(final double quantity, final double totalvalue, final double exr, final InvCost invCost)\n
    updateInventoryAverageCost(final double quantity, final double totalvalue, final double exr, InvCost invCost, final boolean transferWithinStore)\n
    updateInventoryAverageCost(final double quantity, final double totalvalue, final double exr, final String conditionCode)\n
    '''
def getInvCostRecord():
    '''returns MboRemote\n\n
    getInvCostRecord(final String conditionCode)\n
    '''
def addInvLifoFifoCostRecord():
    '''returns MboRemote\n\n
    addInvLifoFifoCostRecord(final String conditioncode)\n
    addInvLifoFifoCostRecord(final double quantity, final double unitcost, final String conditioncode, final String getName, final long matrectransid)\n
    '''
def updateInventoryIssueDetails():
    '''returns None\n\n
    updateInventoryIssueDetails(final Date issDate, final double quantity)\n
    '''
def updateInventoryLastCost():
    '''returns None\n\n
    updateInventoryLastCost(final double unitcost)\n
    updateInventoryLastCost(final double unitcost, final double exr)\n
    updateInventoryLastCost(final double unitcost, final double exr, InvCost invcost)\n
    '''
def updateInventoryDeliveryTime():
    '''returns None\n\n
    updateInventoryDeliveryTime(final double deliveryTime)\n
    '''
def adjustAverageCost():
    '''returns MboRemote\n\n
    adjustAverageCost(final double newcost, final String conditionCode)\n
    '''
def changeStockCategory():
    '''returns None\n\n
    changeStockCategory(final String newcat)\n
    '''
def adjustStandardCost():
    '''returns MboRemote\n\n
    adjustStandardCost(final double newcost, final String conditionCode)\n
    '''
def getDefaultAverageCost():
    '''returns double\n\n
    getDefaultAverageCost()\n
    '''
def zeroYTDQuantities():
    '''returns None\n\n
    zeroYTDQuantities()\n
    '''
def reconcileBalances():
    '''returns MboRemote\n\n
    reconcileBalances()\n
    reconcileBalances(final String controlacc, final String shrinkageacc, final String remark)\n
    reconcileBalances(final String binnum, final String lotnum)\n
    '''
def getCurrentBalance():
    '''returns double\n\n
    getCurrentBalance(final String binnum, final String lotnum)\n
    getCurrentBalance(final String binnum, final String lotnum, final String conditionCode)\n
    '''
def getPhysicalCount():
    '''returns double\n\n
    getPhysicalCount(final String binnum, final String lotnum)\n
    getPhysicalCount(final String binnum, final String lotnum, final String conditionCode)\n
    '''
def addInvBalancesRecord():
    '''returns InvBalancesRemote\n\n
    addInvBalancesRecord(final String binnum, final String lotnum, final double curbal)\n
    addInvBalancesRecord(String binnum, String lotnum, final double curbal, String conditionCode)\n
    '''
def canDelete():
    '''returns None\n\n
    canDelete()\n
    '''
def delete():
    '''returns None\n\n
    delete(final long access)\n
    '''
def getInvBalanceRecord():
    '''returns InvBalances\n\n
    getInvBalanceRecord(final String binnum, final String lotnum, final String conditionCode)\n
    getInvBalanceRecord(String binnum, String lotnum, String conditionCode, String storeLoc, String storeSite)\n
    '''
def getInvBalancesSetForKitComponent():
    '''returns MboSetRemote\n\n
    getInvBalancesSetForKitComponent(String binnum)\n
    '''
def createIssue():
    '''returns MboRemote\n\n
    createIssue()\n
    '''
def isStocked():
    '''returns boolean\n\n
    isStocked()\n
    '''
def isNonStocked():
    '''returns boolean\n\n
    isNonStocked()\n
    '''
def isSpecialOrder():
    '''returns boolean\n\n
    isSpecialOrder()\n
    '''
def changeCapitalizedStatus():
    '''returns None\n\n
    changeCapitalizedStatus(final boolean capitalized)\n
    changeCapitalizedStatus(final boolean capitalized, final String capitalacc, final String memo)\n
    '''
def calculateCurrentBalance():
    '''returns double\n\n
    calculateCurrentBalance()\n
    '''
def calculateRQtyNotStaged():
    '''returns double\n\n
    calculateRQtyNotStaged()\n
    '''
def calculateStagedQty():
    '''returns double\n\n
    calculateStagedQty()\n
    '''
def calculatePickedQty():
    '''returns double\n\n
    calculatePickedQty()\n
    '''
def calculateShippedQty():
    '''returns double\n\n
    calculateShippedQty()\n
    '''
def calculateReceivedQty():
    '''returns double\n\n
    calculateReceivedQty()\n
    '''
def calculateHardShippedQty():
    '''returns double\n\n
    calculateHardShippedQty()\n
    '''
def calculateAvailableQty():
    '''returns double\n\n
    calculateAvailableQty()\n
    '''
def calculateOverShippedQty():
    '''returns double\n\n
    calculateOverShippedQty()\n
    '''
def setAutoCreateInvCost():
    '''returns None\n\n
    setAutoCreateInvCost(final boolean flag)\n
    '''
def setAutoCreateInvBalances():
    '''returns None\n\n
    setAutoCreateInvBalances(final boolean flag)\n
    '''
def canTransferCurrentItem():
    '''returns None\n\n
    canTransferCurrentItem()\n
    '''
def canIssueCurrentItem():
    '''returns None\n\n
    canIssueCurrentItem()\n
    '''
def getInventoryStatus():
    '''returns String\n\n
    getInventoryStatus()\n
    '''
def canAdjustStdCost():
    '''returns None\n\n
    canAdjustStdCost()\n
    '''
def canAdjustAvgCost():
    '''returns None\n\n
    canAdjustAvgCost()\n
    '''
def canAdjustBalance():
    '''returns None\n\n
    canAdjustBalance()\n
    '''
def canReconcileBalances():
    '''returns None\n\n
    canReconcileBalances()\n
    '''
def updateCurrentBalance():
    '''returns MboRemote\n\n
    updateCurrentBalance(final String binnum, final String lotnum, final String conditionCode, final double toIncrement)\n
    '''
def getErrorMsg():
    '''returns MXApplicationException\n\n
    getErrorMsg()\n
    '''
def canDoAction():
    '''returns None\n\n
    canDoAction()\n
    '''
def siteReceiptsAndTransfers():
    '''returns MboSetRemote\n\n
    siteReceiptsAndTransfers()\n
    '''
def setKitAction():
    '''returns None\n\n
    setKitAction(final String makeOrBreak)\n
    '''
def getKitAction():
    '''returns String\n\n
    getKitAction()\n
    '''
def kitMakeOrBreak():
    '''returns None\n\n
    kitMakeOrBreak(final KitRemote kit)\n
    kitMakeOrBreak(final KitRemote kit, final boolean useSourceBinForInvKitAction)\n
    '''
def canKit():
    '''returns None\n\n
    canKit()\n
    '''
def refreshCountDate():
    '''returns None\n\n
    refreshCountDate()\n
    '''
def copyAssetsForIssue():
    '''returns None\n\n
    copyAssetsForIssue(final MboSetRemote assetSet, final MboRemote issueItemToAssetMbo)\n
    '''
def checkRequestAgainstItemMaxIssue():
    '''returns None\n\n
    checkRequestAgainstItemMaxIssue(final String assetnum, final double qtyRequested)\n
    '''
def checkWOExists():
    '''returns boolean\n\n
    checkWOExists()\n
    '''
def checkInvBalancesExists():
    '''returns boolean\n\n
    checkInvBalancesExists()\n
    '''
def checkAssetExists():
    '''returns boolean\n\n
    checkAssetExists()\n
    '''
def checkJPExists():
    '''returns boolean\n\n
    checkJPExists()\n
    '''
def checkMRExists():
    '''returns boolean\n\n
    checkMRExists()\n
    '''
def checkPRExists():
    '''returns boolean\n\n
    checkPRExists()\n
    '''
def checkPOExists():
    '''returns boolean\n\n
    checkPOExists()\n
    '''
def checkContractExists():
    '''returns boolean\n\n
    checkContractExists()\n
    '''
def checkCIExists():
    '''returns boolean\n\n
    checkCIExists()\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(final String status, final Date date, final String memo, final long accessModifier)\n
    '''
def validateChangeStatus():
    '''returns None\n\n
    validateChangeStatus(final String status, final Date date, final String memo)\n
    '''
def isPendobs():
    '''returns boolean\n\n
    isPendobs()\n
    '''
def isObsolete():
    '''returns boolean\n\n
    isObsolete()\n
    '''
def isPlanning():
    '''returns boolean\n\n
    isPlanning()\n
    '''
def checkInvUseStatusForPlanning():
    '''returns boolean\n\n
    checkInvUseStatusForPlanning()\n
    '''
def checkInvUseStatusForPndObs():
    '''returns boolean\n\n
    checkInvUseStatusForPndObs()\n
    '''
def getStatus():
    '''returns String\n\n
    getStatus()\n
    '''
def getCostType():
    '''returns String\n\n
    getCostType()\n
    '''
def getInvLifoFifoCostRecordSetSorted():
    '''returns MboSetRemote\n\n
    getInvLifoFifoCostRecordSetSorted(final String conditionCode)\n
    '''
def getInvLifoFifoCostRecordSet():
    '''returns MboSetRemote\n\n
    getInvLifoFifoCostRecordSet(final String conditionCode)\n
    getInvLifoFifoCostRecordSet(final String conditionCode, final long transid)\n
    '''
def consumeInvLifoFifoCostRecord():
    '''returns None\n\n
    consumeInvLifoFifoCostRecord(final double quantity, final String conditionCode)\n
    consumeInvLifoFifoCostRecord(final double quantity, final String conditionCode, final long transid)\n
    '''
def consumeInvLifoFifoCostRecordRemaining():
    '''returns None\n\n
    consumeInvLifoFifoCostRecordRemaining(final double quantity, final String conditionCode, final long transid)\n
    '''
def getAverageCost():
    '''returns double\n\n
    getAverageCost(final MboSetRemote invLifoFifoCostSet)\n
    '''
def setAutoCreateInvLifoFifoCost():
    '''returns None\n\n
    setAutoCreateInvLifoFifoCost(final boolean flag)\n
    '''
def getAutoCreateInvLifoFifoCost():
    '''returns boolean\n\n
    getAutoCreateInvLifoFifoCost()\n
    '''
def getInvLifoFifoCostRecord():
    '''returns MboRemote\n\n
    getInvLifoFifoCostRecord(final String conditionCode)\n
    '''
def setNextInvoiceDate():
    '''returns None\n\n
    setNextInvoiceDate()\n
    '''
def getNextDate():
    '''returns Date\n\n
    getNextDate()\n
    '''
def addMonths():
    '''returns Date\n\n
    addMonths(final int addMonths, final Date fromDate)\n
    '''
def addYears():
    '''returns Date\n\n
    addYears(final int addYears, final Date fromDate)\n
    '''
def isConsignment():
    '''returns boolean\n\n
    isConsignment()\n
    '''
def updateConsignment():
    '''returns None\n\n
    updateConsignment()\n
    '''
def checkReconcileFlag():
    '''returns boolean\n\n
    checkReconcileFlag()\n
    '''
def POPRExists():
    '''returns boolean\n\n
    POPRExists()\n
    '''
def pendingTransactionExists():
    '''returns boolean\n\n
    pendingTransactionExists(final MboSetRemote transSet)\n
    '''
def getInvGenType():
    '''returns String\n\n
    getInvGenType()\n
    '''
def invUpdateCostType():
    '''returns None\n\n
    invUpdateCostType()\n
    '''
def checkBalandPOPR():
    '''returns None\n\n
    checkBalandPOPR()\n
    '''
def setEditabilityFlags():
    '''returns None\n\n
    setEditabilityFlags()\n
    '''
def increaseAccumulativeTotalCurBal():
    '''returns None\n\n
    increaseAccumulativeTotalCurBal(final double currentReceiptQty)\n
    '''
def getAccumulativeTotalCurBal():
    '''returns double\n\n
    getAccumulativeTotalCurBal()\n
    '''
def checkComponentCostType():
    '''returns None\n\n
    checkComponentCostType(final MboSetRemote itemStructKitSet)\n
    '''
def getStatusSetByMaxvarFlag():
    '''returns boolean\n\n
    getStatusSetByMaxvarFlag()\n
    '''
def calculateRQtyNotStagedForAvailBal():
    '''returns double\n\n
    calculateRQtyNotStagedForAvailBal()\n
    '''
def calculateBinCnt():
    '''returns String\n\n
    calculateBinCnt()\n
    '''
def calculateLotCnt():
    '''returns String\n\n
    calculateLotCnt()\n
    '''
def hasMultipleInvBalance():
    '''returns Boolean\n\n
    hasMultipleInvBalance()\n
    '''
def previewReconcileBalances():
    '''returns MboRemote\n\n
    previewReconcileBalances(final String controlacc, final String shrinkageacc, final String remark)\n
    '''
def updateGLAccount():
    '''returns None\n\n
    updateGLAccount(final String controlacc, final String shrinkageacc)\n
    '''
def calculateConditionCodeCnt():
    '''returns String\n\n
    calculateConditionCodeCnt()\n
    '''
