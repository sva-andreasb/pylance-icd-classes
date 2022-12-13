def MatRecTrans():
'''public MatRecTrans(final MboSet ms)
'''
pass
def init():
'''public void init()
'''
pass
def getBinNumFlag():
'''public boolean getBinNumFlag()
'''
pass
def setBinNumFlag():
'''public void setBinNumFlag(final boolean binNumFlag)
'''
pass
def add():
'''public void add()
'''
pass
def canDelete():
'''public void canDelete()
'''
pass
def isTransfer():
'''public boolean isTransfer()
'''
pass
def isPicksTransfer():
'''public boolean isPicksTransfer()
'''
pass
def isPickRestock():
'''public boolean isPickRestock()
'''
pass
def isShipReceipt():
'''public boolean isShipReceipt()
'''
pass
def isTransferNoPO():
'''public boolean isTransferNoPO()
'''
pass
def isReceipt():
'''public boolean isReceipt()
'''
pass
def isReturn():
'''public boolean isReturn()
'''
pass
def isInvoice():
'''public boolean isInvoice()
'''
pass
def isMisclReceipt():
'''public boolean isMisclReceipt()
'''
pass
def isVoidReceipt():
'''public boolean isVoidReceipt()
'''
pass
def hasVoidReceipt():
'''public boolean hasVoidReceipt()
'''
pass
def isHolding():
'''public boolean isHolding()
'''
pass
def getHoldingLocationForSite():
'''public MboRemote getHoldingLocationForSite(final String siteid)
'''
pass
def isReject():
'''public boolean isReject()
'''
pass
def isShipReject():
'''public boolean isShipReject()
'''
pass
def getReceiptStatus():
'''public String getReceiptStatus()
'''
pass
def getClearingAcct():
'''public MboRemote getClearingAcct()
'''
pass
def approve():
'''public void approve(Date statusDate)
public void approve(final MboSetRemote assetInputSet)
'''
pass
def updateInventory():
'''public void updateInventory(final InventoryRemote invmbo, final PORemote poMbo, final InvCost invcost)
'''
pass
def addRotatingAsset():
'''public void addRotatingAsset(final String assetnum)
'''
pass
def appValidate():
'''public void appValidate()
'''
pass
def save():
'''public void save()
'''
pass
def createInvoiceOnConsumption():
'''public void createInvoiceOnConsumption()
'''
pass
def updateInvReserveActualQty():
'''public void updateInvReserveActualQty(final MboRemote invUseLine)
'''
pass
def getReceiptForThisReturn():
'''public MboRemote getReceiptForThisReturn()
'''
pass
def getshipTransferForThisShipReceipt():
'''public MboRemote getshipTransferForThisShipReceipt()
'''
pass
def setAproveAfterCreatingAssets():
'''public void setAproveAfterCreatingAssets(final boolean flag)
'''
pass
def getApproveAfterCreatingAssets():
'''public boolean getApproveAfterCreatingAssets()
'''
pass
def rejectsForRotatingShipments():
'''public void rejectsForRotatingShipments()
'''
pass
def transferForRotatingShipments():
'''public void transferForRotatingShipments()
'''
pass
def approveShipReceipt():
'''public void approveShipReceipt()
'''
pass
def approveCrossSiteShipment():
'''public void approveCrossSiteShipment(final MboSetRemote assetInputSet, final MboRemote oneAssetInput)
'''
pass
def setInspectionRequiredEditibilityFlags():
'''public void setInspectionRequiredEditibilityFlags(final boolean flag)
'''
pass
def canApprove():
'''public void canApprove()
'''
pass
def onlyPayOnReceipt():
'''public void onlyPayOnReceipt(final PORemote poMbo, final POLineRemote poLineMbo)
'''
pass
def setToInvBalUpdated():
'''public void setToInvBalUpdated()
'''
pass
def setFromInvBalUpdated():
'''public void setFromInvBalUpdated()
'''
pass
def getCourierLaborTransientMatRec():
'''public MboRemote getCourierLaborTransientMatRec()
'''
pass
def getSharedInventory():
'''public MboRemote getSharedInventory(final String storeLoc, final String siteid)
'''
pass
def calculateUnInvoicedQtyCost():
'''public double[] calculateUnInvoicedQtyCost()
'''
pass
def createReturn():
'''public void createReturn(final MatRecTransRemote matrec)
'''
pass
def getInvCostRecord():
'''public MboRemote getInvCostRecord(final MboRemote toInventory)
'''
pass
def updateInventoryCostAndBalances():
'''public void updateInventoryCostAndBalances()
'''
pass
def isSwitchoffWOUpdate():
'''public boolean isSwitchoffWOUpdate()
'''
pass
def setSwitchoffWOUpdate():
'''public void setSwitchoffWOUpdate(final boolean switchoffWOUpdate)
'''
pass
def setInvReserveUpdatedFlag():
'''public void setInvReserveUpdatedFlag(final boolean updated)
'''
pass
def setCheckNegBalance():
'''public void setCheckNegBalance(final boolean updated)
'''
pass
def getPOLineUpdated():
'''public boolean getPOLineUpdated()
'''
pass
def setPOLineUpdated():
'''public void setPOLineUpdated()
'''
pass
def isStageTransfer():
'''public boolean isStageTransfer()
'''
pass
def isShipTransfer():
'''public boolean isShipTransfer()
'''
pass
def isShipCancel():
'''public boolean isShipCancel()
'''
pass
def isShipReturn():
'''public boolean isShipReturn()
'''
pass
def isVoidShipReceipt():
'''public boolean isVoidShipReceipt()
'''
pass
def createMatRecTransRecordforLifoFifo():
'''public void createMatRecTransRecordforLifoFifo(final MboRemote inv)
'''
pass
def canBeReturned():
'''public boolean canBeReturned()
'''
pass
def setShipmentMap():
'''public void setShipmentMap()
'''
pass
def isDirectIssueConversion():
'''public boolean isDirectIssueConversion()
public boolean isDirectIssueConversion(final boolean includeStoreroom)
'''
pass
def getDirectIssueConversion():
'''public double getDirectIssueConversion()
'''
pass
def createStdRecAdjOnRotAssetTransferIn():
'''public void createStdRecAdjOnRotAssetTransferIn()
'''
pass
def isSameStoreTransfer():
'''public boolean isSameStoreTransfer()
'''
pass
def setOriginalCostDate():
'''public void setOriginalCostDate(final Date costDate)
'''
pass
def getOriginalCostDate():
'''public Date getOriginalCostDate()
'''
pass
def setWorkOrderUpdatedFlag():
'''public void setWorkOrderUpdatedFlag(final boolean updated)
'''
pass
def getWorkOrderUpdatedFlag():
'''public boolean getWorkOrderUpdatedFlag()
'''
pass
def isRejectedReturn():
'''public boolean isRejectedReturn()
'''
pass
def createShipReceiptRecordsforLifoFifo():
'''public void createShipReceiptRecordsforLifoFifo()
'''
pass
