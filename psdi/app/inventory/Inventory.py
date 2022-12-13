def Inventory():
'''public Inventory(final MboSet ms)
'''
pass
def getProcess():
'''public String getProcess()
'''
pass
def getStatusListName():
'''public String getStatusListName()
'''
pass
def setIsKitComponentToAddToStore():
'''public void setIsKitComponentToAddToStore(final boolean isKitComponentToAddToStore)
'''
pass
def init():
'''public void init()
'''
pass
def initFieldFlagsOnMbo():
'''public void initFieldFlagsOnMbo(final String attrName)
'''
pass
def add():
'''public void add()
'''
pass
def setCostType():
'''public void setCostType()
'''
pass
def appValidate():
'''public void appValidate()
'''
pass
def isKit():
'''public boolean isKit()
'''
pass
def isCapitalized():
'''public boolean isCapitalized()
'''
pass
def save():
'''public void save()
'''
pass
def addUpdateInvVendor():
'''public void addUpdateInvVendor()
'''
pass
def getPrimaryInvVendor():
'''public MboRemote getPrimaryInvVendor(final MboSetRemote invVendSet)
'''
pass
def doAdjustment():
'''public MboRemote doAdjustment(final NonPersistentMboRemote invAdj)
'''
pass
def adjustCurrentBalance():
'''public MboRemote adjustCurrentBalance(final String binnum, final String lotnum, final double newBalance, final String conditionCode)
'''
pass
def adjustPhysicalCount():
'''public MboRemote adjustPhysicalCount(final String binnum, final String lotnum, final double quantity, final Date pCountDate)
public MboRemote adjustPhysicalCount(final String binnum, final String lotnum, final double quantity, final Date pCountDate, final String ownersysid)
public MboRemote adjustPhysicalCount(final String binnum, final String lotnum, final double quantity, final Date pCountDate, final String ownersysid, final String conditionCode)
'''
pass
def getDefaultIssueCost():
'''public double getDefaultIssueCost(final AssetRemote assetRemote, final String conditionCode)
public double getDefaultIssueCost(final AssetRemote assetRemote)
public double getDefaultIssueCost()
public double getDefaultIssueCost(final String conditionCode)
public double getDefaultIssueCost(final ArrayList<InvLifoFifoCost> invLifoFifoCostList)
'''
pass
def updateInventoryAverageCost():
'''public void updateInventoryAverageCost(final double quantity, final double totalvalue)
public void updateInventoryAverageCost(final double quantity, final double totalvalue, final double exr)
public void updateInventoryAverageCost(final double quantity, final double totalvalue, final double exr, final InvCost invCost)
public void updateInventoryAverageCost(final double quantity, final double totalvalue, final double exr, InvCost invCost, final boolean transferWithinStore)
public void updateInventoryAverageCost(final double quantity, final double totalvalue, final double exr, final String conditionCode)
'''
pass
def getInvCostRecord():
'''public MboRemote getInvCostRecord(final String conditionCode)
'''
pass
def addInvLifoFifoCostRecord():
'''public MboRemote addInvLifoFifoCostRecord(final String conditioncode)
public MboRemote addInvLifoFifoCostRecord(final double quantity, final double unitcost, final String conditioncode, final String getName, final long matrectransid)
'''
pass
def updateInventoryIssueDetails():
'''public void updateInventoryIssueDetails(final Date issDate, final double quantity)
'''
pass
def updateInventoryLastCost():
'''public void updateInventoryLastCost(final double unitcost)
public void updateInventoryLastCost(final double unitcost, final double exr)
public void updateInventoryLastCost(final double unitcost, final double exr, InvCost invcost)
'''
pass
def updateInventoryDeliveryTime():
'''public void updateInventoryDeliveryTime(final double deliveryTime)
'''
pass
def adjustAverageCost():
'''public MboRemote adjustAverageCost(final double newcost, final String conditionCode)
'''
pass
def changeStockCategory():
'''public void changeStockCategory(final String newcat)
'''
pass
def adjustStandardCost():
'''public MboRemote adjustStandardCost(final double newcost, final String conditionCode)
'''
pass
def getDefaultAverageCost():
'''public double getDefaultAverageCost()
'''
pass
def zeroYTDQuantities():
'''public void zeroYTDQuantities()
'''
pass
def reconcileBalances():
'''public void reconcileBalances()
public void reconcileBalances(final String controlacc, final String shrinkageacc, final String remark)
public MboRemote reconcileBalances(final String binnum, final String lotnum)
'''
pass
def getCurrentBalance():
'''public double getCurrentBalance(final String binnum, final String lotnum)
public double getCurrentBalance(final String binnum, final String lotnum, final String conditionCode)
'''
pass
def getPhysicalCount():
'''public double getPhysicalCount(final String binnum, final String lotnum)
public double getPhysicalCount(final String binnum, final String lotnum, final String conditionCode)
'''
pass
def addInvBalancesRecord():
'''public InvBalancesRemote addInvBalancesRecord(final String binnum, final String lotnum, final double curbal)
public InvBalancesRemote addInvBalancesRecord(String binnum, String lotnum, final double curbal, String conditionCode)
'''
pass
def canDelete():
'''public void canDelete()
'''
pass
def delete():
'''public void delete(final long access)
'''
pass
def getInvBalanceRecord():
'''public InvBalances getInvBalanceRecord(final String binnum, final String lotnum, final String conditionCode)
public InvBalances getInvBalanceRecord(String binnum, String lotnum, String conditionCode, String storeLoc, String storeSite)
'''
pass
def getInvBalancesSetForKitComponent():
'''public MboSetRemote getInvBalancesSetForKitComponent(String binnum)
'''
pass
def createIssue():
'''public MboRemote createIssue()
'''
pass
def isStocked():
'''public boolean isStocked()
'''
pass
def isNonStocked():
'''public boolean isNonStocked()
'''
pass
def isSpecialOrder():
'''public boolean isSpecialOrder()
'''
pass
def changeCapitalizedStatus():
'''public void changeCapitalizedStatus(final boolean capitalized)
public void changeCapitalizedStatus(final boolean capitalized, final String capitalacc, final String memo)
'''
pass
def calculateCurrentBalance():
'''public double calculateCurrentBalance()
'''
pass
def calculateRQtyNotStaged():
'''public double calculateRQtyNotStaged()
'''
pass
def calculateStagedQty():
'''public double calculateStagedQty()
'''
pass
def calculatePickedQty():
'''public double calculatePickedQty()
'''
pass
def calculateShippedQty():
'''public double calculateShippedQty()
'''
pass
def calculateReceivedQty():
'''public double calculateReceivedQty()
'''
pass
def calculateHardShippedQty():
'''public double calculateHardShippedQty()
'''
pass
def calculateAvailableQty():
'''public double calculateAvailableQty()
'''
pass
def calculateOverShippedQty():
'''public double calculateOverShippedQty()
'''
pass
def setAutoCreateInvCost():
'''public void setAutoCreateInvCost(final boolean flag)
'''
pass
def setAutoCreateInvBalances():
'''public void setAutoCreateInvBalances(final boolean flag)
'''
pass
def canTransferCurrentItem():
'''public void canTransferCurrentItem()
'''
pass
def canIssueCurrentItem():
'''public void canIssueCurrentItem()
'''
pass
def getInventoryStatus():
'''public String getInventoryStatus()
'''
pass
def canAdjustStdCost():
'''public void canAdjustStdCost()
'''
pass
def canAdjustAvgCost():
'''public void canAdjustAvgCost()
'''
pass
def canAdjustBalance():
'''public void canAdjustBalance()
'''
pass
def canReconcileBalances():
'''public void canReconcileBalances()
'''
pass
def updateCurrentBalance():
'''public MboRemote updateCurrentBalance(final String binnum, final String lotnum, final String conditionCode, final double toIncrement)
'''
pass
def getErrorMsg():
'''public MXApplicationException getErrorMsg()
'''
pass
def canDoAction():
'''public void canDoAction()
'''
pass
def siteReceiptsAndTransfers():
'''public MboSetRemote siteReceiptsAndTransfers()
'''
pass
def setKitAction():
'''public void setKitAction(final String makeOrBreak)
'''
pass
def getKitAction():
'''public String getKitAction()
'''
pass
def kitMakeOrBreak():
'''public void kitMakeOrBreak(final KitRemote kit)
public void kitMakeOrBreak(final KitRemote kit, final boolean useSourceBinForInvKitAction)
'''
pass
def canKit():
'''public void canKit()
'''
pass
def refreshCountDate():
'''public void refreshCountDate()
'''
pass
def copyAssetsForIssue():
'''public void copyAssetsForIssue(final MboSetRemote assetSet, final MboRemote issueItemToAssetMbo)
'''
pass
def checkRequestAgainstItemMaxIssue():
'''public void checkRequestAgainstItemMaxIssue(final String assetnum, final double qtyRequested)
'''
pass
def checkWOExists():
'''public boolean checkWOExists()
'''
pass
def checkInvBalancesExists():
'''public boolean checkInvBalancesExists()
'''
pass
def checkAssetExists():
'''public boolean checkAssetExists()
'''
pass
def checkJPExists():
'''public boolean checkJPExists()
'''
pass
def checkMRExists():
'''public boolean checkMRExists()
'''
pass
def checkPRExists():
'''public boolean checkPRExists()
'''
pass
def checkPOExists():
'''public boolean checkPOExists()
'''
pass
def checkContractExists():
'''public boolean checkContractExists()
'''
pass
def checkCIExists():
'''public boolean checkCIExists()
'''
pass
def changeStatus():
'''public void changeStatus(final String status, final Date date, final String memo, final long accessModifier)
'''
pass
def validateChangeStatus():
'''public void validateChangeStatus(final String status, final Date date, final String memo)
'''
pass
def isPendobs():
'''public boolean isPendobs()
'''
pass
def isObsolete():
'''public boolean isObsolete()
'''
pass
def isPlanning():
'''public boolean isPlanning()
'''
pass
def checkInvUseStatusForPlanning():
'''public boolean checkInvUseStatusForPlanning()
'''
pass
def checkInvUseStatusForPndObs():
'''public boolean checkInvUseStatusForPndObs()
'''
pass
def getStatus():
'''public String getStatus()
'''
pass
def getCostType():
'''public String getCostType()
'''
pass
def getInvLifoFifoCostRecordSetSorted():
'''public MboSetRemote getInvLifoFifoCostRecordSetSorted(final String conditionCode)
'''
pass
def getInvLifoFifoCostRecordSet():
'''public MboSetRemote getInvLifoFifoCostRecordSet(final String conditionCode)
public MboSetRemote getInvLifoFifoCostRecordSet(final String conditionCode, final long transid)
'''
pass
def consumeInvLifoFifoCostRecord():
'''public void consumeInvLifoFifoCostRecord(final double quantity, final String conditionCode)
public void consumeInvLifoFifoCostRecord(final double quantity, final String conditionCode, final long transid)
'''
pass
def consumeInvLifoFifoCostRecordRemaining():
'''public void consumeInvLifoFifoCostRecordRemaining(final double quantity, final String conditionCode, final long transid)
'''
pass
def getAverageCost():
'''public double getAverageCost(final MboSetRemote invLifoFifoCostSet)
'''
pass
def setAutoCreateInvLifoFifoCost():
'''public void setAutoCreateInvLifoFifoCost(final boolean flag)
'''
pass
def getAutoCreateInvLifoFifoCost():
'''public boolean getAutoCreateInvLifoFifoCost()
'''
pass
def getInvLifoFifoCostRecord():
'''public MboRemote getInvLifoFifoCostRecord(final String conditionCode)
'''
pass
def setNextInvoiceDate():
'''public void setNextInvoiceDate()
'''
pass
def getNextDate():
'''public Date getNextDate()
'''
pass
def addMonths():
'''public Date addMonths(final int addMonths, final Date fromDate)
'''
pass
def addYears():
'''public Date addYears(final int addYears, final Date fromDate)
'''
pass
def isConsignment():
'''public boolean isConsignment()
'''
pass
def updateConsignment():
'''public void updateConsignment()
'''
pass
def checkReconcileFlag():
'''public boolean checkReconcileFlag()
'''
pass
def POPRExists():
'''public boolean POPRExists()
'''
pass
def pendingTransactionExists():
'''public boolean pendingTransactionExists(final MboSetRemote transSet)
'''
pass
def getInvGenType():
'''public String getInvGenType()
'''
pass
def invUpdateCostType():
'''public void invUpdateCostType()
'''
pass
def checkBalandPOPR():
'''public void checkBalandPOPR()
'''
pass
def setEditabilityFlags():
'''public void setEditabilityFlags()
'''
pass
def increaseAccumulativeTotalCurBal():
'''public void increaseAccumulativeTotalCurBal(final double currentReceiptQty)
'''
pass
def getAccumulativeTotalCurBal():
'''public double getAccumulativeTotalCurBal()
'''
pass
def checkComponentCostType():
'''public void checkComponentCostType(final MboSetRemote itemStructKitSet)
'''
pass
def getStatusSetByMaxvarFlag():
'''public boolean getStatusSetByMaxvarFlag()
'''
pass
def calculateRQtyNotStagedForAvailBal():
'''public double calculateRQtyNotStagedForAvailBal()
'''
pass
def calculateBinCnt():
'''public String calculateBinCnt()
'''
pass
def calculateLotCnt():
'''public String calculateLotCnt()
'''
pass
def hasMultipleInvBalance():
'''public Boolean hasMultipleInvBalance()
'''
pass
def previewReconcileBalances():
'''public MboRemote previewReconcileBalances(final String controlacc, final String shrinkageacc, final String remark)
'''
pass
def updateGLAccount():
'''public void updateGLAccount(final String controlacc, final String shrinkageacc)
'''
pass
def calculateConditionCodeCnt():
'''public String calculateConditionCodeCnt()
'''
pass
