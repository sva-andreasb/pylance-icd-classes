def Inventory():
    '''    public Inventory(final MboSet ms)
    '''
def getProcess():
    '''    public String getProcess()
    '''
def getStatusListName():
    '''    public String getStatusListName()
    '''
def setIsKitComponentToAddToStore():
    '''    public void setIsKitComponentToAddToStore(final boolean isKitComponentToAddToStore)
    '''
def init():
    '''    public void init()
    '''
def initFieldFlagsOnMbo():
    '''    public void initFieldFlagsOnMbo(final String attrName)
    '''
def add():
    '''    public void add()
    '''
def setCostType():
    '''    public void setCostType()
    '''
def appValidate():
    '''    public void appValidate()
    '''
def isKit():
    '''    public boolean isKit()
    '''
def isCapitalized():
    '''    public boolean isCapitalized()
    '''
def save():
    '''    public void save()
    '''
def addUpdateInvVendor():
    '''    public void addUpdateInvVendor()
    '''
def getPrimaryInvVendor():
    '''    public MboRemote getPrimaryInvVendor(final MboSetRemote invVendSet)
    '''
def doAdjustment():
    '''    public MboRemote doAdjustment(final NonPersistentMboRemote invAdj)
    '''
def adjustCurrentBalance():
    '''    public MboRemote adjustCurrentBalance(final String binnum, final String lotnum, final double newBalance, final String conditionCode)
    '''
def adjustPhysicalCount():
    '''    public MboRemote adjustPhysicalCount(final String binnum, final String lotnum, final double quantity, final Date pCountDate)
    public MboRemote adjustPhysicalCount(final String binnum, final String lotnum, final double quantity, final Date pCountDate, final String ownersysid)
    public MboRemote adjustPhysicalCount(final String binnum, final String lotnum, final double quantity, final Date pCountDate, final String ownersysid, final String conditionCode)
    '''
def getDefaultIssueCost():
    '''    public double getDefaultIssueCost(final AssetRemote assetRemote, final String conditionCode)
    public double getDefaultIssueCost(final AssetRemote assetRemote)
    public double getDefaultIssueCost()
    public double getDefaultIssueCost(final String conditionCode)
    public double getDefaultIssueCost(final ArrayList<InvLifoFifoCost> invLifoFifoCostList)
    '''
def updateInventoryAverageCost():
    '''    public void updateInventoryAverageCost(final double quantity, final double totalvalue)
    public void updateInventoryAverageCost(final double quantity, final double totalvalue, final double exr)
    public void updateInventoryAverageCost(final double quantity, final double totalvalue, final double exr, final InvCost invCost)
    public void updateInventoryAverageCost(final double quantity, final double totalvalue, final double exr, InvCost invCost, final boolean transferWithinStore)
    public void updateInventoryAverageCost(final double quantity, final double totalvalue, final double exr, final String conditionCode)
    '''
def getInvCostRecord():
    '''    public MboRemote getInvCostRecord(final String conditionCode)
    '''
def addInvLifoFifoCostRecord():
    '''    public MboRemote addInvLifoFifoCostRecord(final String conditioncode)
    public MboRemote addInvLifoFifoCostRecord(final double quantity, final double unitcost, final String conditioncode, final String getName, final long matrectransid)
    '''
def updateInventoryIssueDetails():
    '''    public void updateInventoryIssueDetails(final Date issDate, final double quantity)
    '''
def updateInventoryLastCost():
    '''    public void updateInventoryLastCost(final double unitcost)
    public void updateInventoryLastCost(final double unitcost, final double exr)
    public void updateInventoryLastCost(final double unitcost, final double exr, InvCost invcost)
    '''
def updateInventoryDeliveryTime():
    '''    public void updateInventoryDeliveryTime(final double deliveryTime)
    '''
def adjustAverageCost():
    '''    public MboRemote adjustAverageCost(final double newcost, final String conditionCode)
    '''
def changeStockCategory():
    '''    public void changeStockCategory(final String newcat)
    '''
def adjustStandardCost():
    '''    public MboRemote adjustStandardCost(final double newcost, final String conditionCode)
    '''
def getDefaultAverageCost():
    '''    public double getDefaultAverageCost()
    '''
def zeroYTDQuantities():
    '''    public void zeroYTDQuantities()
    '''
def reconcileBalances():
    '''    public void reconcileBalances()
    public void reconcileBalances(final String controlacc, final String shrinkageacc, final String remark)
    public MboRemote reconcileBalances(final String binnum, final String lotnum)
    '''
def getCurrentBalance():
    '''    public double getCurrentBalance(final String binnum, final String lotnum)
    public double getCurrentBalance(final String binnum, final String lotnum, final String conditionCode)
    '''
def getPhysicalCount():
    '''    public double getPhysicalCount(final String binnum, final String lotnum)
    public double getPhysicalCount(final String binnum, final String lotnum, final String conditionCode)
    '''
def addInvBalancesRecord():
    '''    public InvBalancesRemote addInvBalancesRecord(final String binnum, final String lotnum, final double curbal)
    public InvBalancesRemote addInvBalancesRecord(String binnum, String lotnum, final double curbal, String conditionCode)
    '''
def canDelete():
    '''    public void canDelete()
    '''
def delete():
    '''    public void delete(final long access)
    '''
def getInvBalanceRecord():
    '''    public InvBalances getInvBalanceRecord(final String binnum, final String lotnum, final String conditionCode)
    public InvBalances getInvBalanceRecord(String binnum, String lotnum, String conditionCode, String storeLoc, String storeSite)
    '''
def getInvBalancesSetForKitComponent():
    '''    public MboSetRemote getInvBalancesSetForKitComponent(String binnum)
    '''
def createIssue():
    '''    public MboRemote createIssue()
    '''
def isStocked():
    '''    public boolean isStocked()
    '''
def isNonStocked():
    '''    public boolean isNonStocked()
    '''
def isSpecialOrder():
    '''    public boolean isSpecialOrder()
    '''
def changeCapitalizedStatus():
    '''    public void changeCapitalizedStatus(final boolean capitalized)
    public void changeCapitalizedStatus(final boolean capitalized, final String capitalacc, final String memo)
    '''
def calculateCurrentBalance():
    '''    public double calculateCurrentBalance()
    '''
def calculateRQtyNotStaged():
    '''    public double calculateRQtyNotStaged()
    '''
def calculateStagedQty():
    '''    public double calculateStagedQty()
    '''
def calculatePickedQty():
    '''    public double calculatePickedQty()
    '''
def calculateShippedQty():
    '''    public double calculateShippedQty()
    '''
def calculateReceivedQty():
    '''    public double calculateReceivedQty()
    '''
def calculateHardShippedQty():
    '''    public double calculateHardShippedQty()
    '''
def calculateAvailableQty():
    '''    public double calculateAvailableQty()
    '''
def calculateOverShippedQty():
    '''    public double calculateOverShippedQty()
    '''
def setAutoCreateInvCost():
    '''    public void setAutoCreateInvCost(final boolean flag)
    '''
def setAutoCreateInvBalances():
    '''    public void setAutoCreateInvBalances(final boolean flag)
    '''
def canTransferCurrentItem():
    '''    public void canTransferCurrentItem()
    '''
def canIssueCurrentItem():
    '''    public void canIssueCurrentItem()
    '''
def getInventoryStatus():
    '''    public String getInventoryStatus()
    '''
def canAdjustStdCost():
    '''    public void canAdjustStdCost()
    '''
def canAdjustAvgCost():
    '''    public void canAdjustAvgCost()
    '''
def canAdjustBalance():
    '''    public void canAdjustBalance()
    '''
def canReconcileBalances():
    '''    public void canReconcileBalances()
    '''
def updateCurrentBalance():
    '''    public MboRemote updateCurrentBalance(final String binnum, final String lotnum, final String conditionCode, final double toIncrement)
    '''
def getErrorMsg():
    '''    public MXApplicationException getErrorMsg()
    '''
def canDoAction():
    '''    public void canDoAction()
    '''
def siteReceiptsAndTransfers():
    '''    public MboSetRemote siteReceiptsAndTransfers()
    '''
def setKitAction():
    '''    public void setKitAction(final String makeOrBreak)
    '''
def getKitAction():
    '''    public String getKitAction()
    '''
def kitMakeOrBreak():
    '''    public void kitMakeOrBreak(final KitRemote kit)
    public void kitMakeOrBreak(final KitRemote kit, final boolean useSourceBinForInvKitAction)
    '''
def canKit():
    '''    public void canKit()
    '''
def refreshCountDate():
    '''    public void refreshCountDate()
    '''
def copyAssetsForIssue():
    '''    public void copyAssetsForIssue(final MboSetRemote assetSet, final MboRemote issueItemToAssetMbo)
    '''
def checkRequestAgainstItemMaxIssue():
    '''    public void checkRequestAgainstItemMaxIssue(final String assetnum, final double qtyRequested)
    '''
def checkWOExists():
    '''    public boolean checkWOExists()
    '''
def checkInvBalancesExists():
    '''    public boolean checkInvBalancesExists()
    '''
def checkAssetExists():
    '''    public boolean checkAssetExists()
    '''
def checkJPExists():
    '''    public boolean checkJPExists()
    '''
def checkMRExists():
    '''    public boolean checkMRExists()
    '''
def checkPRExists():
    '''    public boolean checkPRExists()
    '''
def checkPOExists():
    '''    public boolean checkPOExists()
    '''
def checkContractExists():
    '''    public boolean checkContractExists()
    '''
def checkCIExists():
    '''    public boolean checkCIExists()
    '''
def changeStatus():
    '''    public void changeStatus(final String status, final Date date, final String memo, final long accessModifier)
    '''
def validateChangeStatus():
    '''    public void validateChangeStatus(final String status, final Date date, final String memo)
    '''
def isPendobs():
    '''    public boolean isPendobs()
    '''
def isObsolete():
    '''    public boolean isObsolete()
    '''
def isPlanning():
    '''    public boolean isPlanning()
    '''
def checkInvUseStatusForPlanning():
    '''    public boolean checkInvUseStatusForPlanning()
    '''
def checkInvUseStatusForPndObs():
    '''    public boolean checkInvUseStatusForPndObs()
    '''
def getStatus():
    '''    public String getStatus()
    '''
def getCostType():
    '''    public String getCostType()
    '''
def getInvLifoFifoCostRecordSetSorted():
    '''    public MboSetRemote getInvLifoFifoCostRecordSetSorted(final String conditionCode)
    '''
def getInvLifoFifoCostRecordSet():
    '''    public MboSetRemote getInvLifoFifoCostRecordSet(final String conditionCode)
    public MboSetRemote getInvLifoFifoCostRecordSet(final String conditionCode, final long transid)
    '''
def consumeInvLifoFifoCostRecord():
    '''    public void consumeInvLifoFifoCostRecord(final double quantity, final String conditionCode)
    public void consumeInvLifoFifoCostRecord(final double quantity, final String conditionCode, final long transid)
    '''
def consumeInvLifoFifoCostRecordRemaining():
    '''    public void consumeInvLifoFifoCostRecordRemaining(final double quantity, final String conditionCode, final long transid)
    '''
def getAverageCost():
    '''    public double getAverageCost(final MboSetRemote invLifoFifoCostSet)
    '''
def setAutoCreateInvLifoFifoCost():
    '''    public void setAutoCreateInvLifoFifoCost(final boolean flag)
    '''
def getAutoCreateInvLifoFifoCost():
    '''    public boolean getAutoCreateInvLifoFifoCost()
    '''
def getInvLifoFifoCostRecord():
    '''    public MboRemote getInvLifoFifoCostRecord(final String conditionCode)
    '''
def setNextInvoiceDate():
    '''    public void setNextInvoiceDate()
    '''
def getNextDate():
    '''    public Date getNextDate()
    '''
def addMonths():
    '''    public Date addMonths(final int addMonths, final Date fromDate)
    '''
def addYears():
    '''    public Date addYears(final int addYears, final Date fromDate)
    '''
def isConsignment():
    '''    public boolean isConsignment()
    '''
def updateConsignment():
    '''    public void updateConsignment()
    '''
def checkReconcileFlag():
    '''    public boolean checkReconcileFlag()
    '''
def POPRExists():
    '''    public boolean POPRExists()
    '''
def pendingTransactionExists():
    '''    public boolean pendingTransactionExists(final MboSetRemote transSet)
    '''
def getInvGenType():
    '''    public String getInvGenType()
    '''
def invUpdateCostType():
    '''    public void invUpdateCostType()
    '''
def checkBalandPOPR():
    '''    public void checkBalandPOPR()
    '''
def setEditabilityFlags():
    '''    public void setEditabilityFlags()
    '''
def increaseAccumulativeTotalCurBal():
    '''    public void increaseAccumulativeTotalCurBal(final double currentReceiptQty)
    '''
def getAccumulativeTotalCurBal():
    '''    public double getAccumulativeTotalCurBal()
    '''
def checkComponentCostType():
    '''    public void checkComponentCostType(final MboSetRemote itemStructKitSet)
    '''
def getStatusSetByMaxvarFlag():
    '''    public boolean getStatusSetByMaxvarFlag()
    '''
def calculateRQtyNotStagedForAvailBal():
    '''    public double calculateRQtyNotStagedForAvailBal()
    '''
def calculateBinCnt():
    '''    public String calculateBinCnt()
    '''
def calculateLotCnt():
    '''    public String calculateLotCnt()
    '''
def hasMultipleInvBalance():
    '''    public Boolean hasMultipleInvBalance()
    '''
def previewReconcileBalances():
    '''    public MboRemote previewReconcileBalances(final String controlacc, final String shrinkageacc, final String remark)
    '''
def updateGLAccount():
    '''    public void updateGLAccount(final String controlacc, final String shrinkageacc)
    '''
def calculateConditionCodeCnt():
    '''    public String calculateConditionCodeCnt()
    '''
