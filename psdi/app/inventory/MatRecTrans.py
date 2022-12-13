def MatRecTrans():
    '''    public MatRecTrans(final MboSet ms)
    '''
def init():
    '''    public void init()
    '''
def getBinNumFlag():
    '''    public boolean getBinNumFlag()
    '''
def setBinNumFlag():
    '''    public void setBinNumFlag(final boolean binNumFlag)
    '''
def add():
    '''    public void add()
    '''
def canDelete():
    '''    public void canDelete()
    '''
def isTransfer():
    '''    public boolean isTransfer()
    '''
def isPicksTransfer():
    '''    public boolean isPicksTransfer()
    '''
def isPickRestock():
    '''    public boolean isPickRestock()
    '''
def isShipReceipt():
    '''    public boolean isShipReceipt()
    '''
def isTransferNoPO():
    '''    public boolean isTransferNoPO()
    '''
def isReceipt():
    '''    public boolean isReceipt()
    '''
def isReturn():
    '''    public boolean isReturn()
    '''
def isInvoice():
    '''    public boolean isInvoice()
    '''
def isMisclReceipt():
    '''    public boolean isMisclReceipt()
    '''
def isVoidReceipt():
    '''    public boolean isVoidReceipt()
    '''
def hasVoidReceipt():
    '''    public boolean hasVoidReceipt()
    '''
def isHolding():
    '''    public boolean isHolding()
    '''
def getHoldingLocationForSite():
    '''    public MboRemote getHoldingLocationForSite(final String siteid)
    '''
def isReject():
    '''    public boolean isReject()
    '''
def isShipReject():
    '''    public boolean isShipReject()
    '''
def getReceiptStatus():
    '''    public String getReceiptStatus()
    '''
def getClearingAcct():
    '''    public MboRemote getClearingAcct()
    '''
def approve():
    '''    public void approve(Date statusDate)
    public void approve(final MboSetRemote assetInputSet)
    '''
def updateInventory():
    '''    public void updateInventory(final InventoryRemote invmbo, final PORemote poMbo, final InvCost invcost)
    '''
def addRotatingAsset():
    '''    public void addRotatingAsset(final String assetnum)
    '''
def appValidate():
    '''    public void appValidate()
    '''
def save():
    '''    public void save()
    '''
def createInvoiceOnConsumption():
    '''    public void createInvoiceOnConsumption()
    '''
def updateInvReserveActualQty():
    '''    public void updateInvReserveActualQty(final MboRemote invUseLine)
    '''
def getReceiptForThisReturn():
    '''    public MboRemote getReceiptForThisReturn()
    '''
def getshipTransferForThisShipReceipt():
    '''    public MboRemote getshipTransferForThisShipReceipt()
    '''
def setAproveAfterCreatingAssets():
    '''    public void setAproveAfterCreatingAssets(final boolean flag)
    '''
def getApproveAfterCreatingAssets():
    '''    public boolean getApproveAfterCreatingAssets()
    '''
def rejectsForRotatingShipments():
    '''    public void rejectsForRotatingShipments()
    '''
def transferForRotatingShipments():
    '''    public void transferForRotatingShipments()
    '''
def approveShipReceipt():
    '''    public void approveShipReceipt()
    '''
def approveCrossSiteShipment():
    '''    public void approveCrossSiteShipment(final MboSetRemote assetInputSet, final MboRemote oneAssetInput)
    '''
def setInspectionRequiredEditibilityFlags():
    '''    public void setInspectionRequiredEditibilityFlags(final boolean flag)
    '''
def canApprove():
    '''    public void canApprove()
    '''
def onlyPayOnReceipt():
    '''    public void onlyPayOnReceipt(final PORemote poMbo, final POLineRemote poLineMbo)
    '''
def setToInvBalUpdated():
    '''    public void setToInvBalUpdated()
    '''
def setFromInvBalUpdated():
    '''    public void setFromInvBalUpdated()
    '''
def getCourierLaborTransientMatRec():
    '''    public MboRemote getCourierLaborTransientMatRec()
    '''
def getSharedInventory():
    '''    public MboRemote getSharedInventory(final String storeLoc, final String siteid)
    '''
def calculateUnInvoicedQtyCost():
    '''    public double[] calculateUnInvoicedQtyCost()
    '''
def createReturn():
    '''    public void createReturn(final MatRecTransRemote matrec)
    '''
def getInvCostRecord():
    '''    public MboRemote getInvCostRecord(final MboRemote toInventory)
    '''
def updateInventoryCostAndBalances():
    '''    public void updateInventoryCostAndBalances()
    '''
def isSwitchoffWOUpdate():
    '''    public boolean isSwitchoffWOUpdate()
    '''
def setSwitchoffWOUpdate():
    '''    public void setSwitchoffWOUpdate(final boolean switchoffWOUpdate)
    '''
def setInvReserveUpdatedFlag():
    '''    public void setInvReserveUpdatedFlag(final boolean updated)
    '''
def setCheckNegBalance():
    '''    public void setCheckNegBalance(final boolean updated)
    '''
def getPOLineUpdated():
    '''    public boolean getPOLineUpdated()
    '''
def setPOLineUpdated():
    '''    public void setPOLineUpdated()
    '''
def isStageTransfer():
    '''    public boolean isStageTransfer()
    '''
def isShipTransfer():
    '''    public boolean isShipTransfer()
    '''
def isShipCancel():
    '''    public boolean isShipCancel()
    '''
def isShipReturn():
    '''    public boolean isShipReturn()
    '''
def isVoidShipReceipt():
    '''    public boolean isVoidShipReceipt()
    '''
def createMatRecTransRecordforLifoFifo():
    '''    public void createMatRecTransRecordforLifoFifo(final MboRemote inv)
    '''
def canBeReturned():
    '''    public boolean canBeReturned()
    '''
def setShipmentMap():
    '''    public void setShipmentMap()
    '''
def isDirectIssueConversion():
    '''    public boolean isDirectIssueConversion()
    public boolean isDirectIssueConversion(final boolean includeStoreroom)
    '''
def getDirectIssueConversion():
    '''    public double getDirectIssueConversion()
    '''
def createStdRecAdjOnRotAssetTransferIn():
    '''    public void createStdRecAdjOnRotAssetTransferIn()
    '''
def isSameStoreTransfer():
    '''    public boolean isSameStoreTransfer()
    '''
def setOriginalCostDate():
    '''    public void setOriginalCostDate(final Date costDate)
    '''
def getOriginalCostDate():
    '''    public Date getOriginalCostDate()
    '''
def setWorkOrderUpdatedFlag():
    '''    public void setWorkOrderUpdatedFlag(final boolean updated)
    '''
def getWorkOrderUpdatedFlag():
    '''    public boolean getWorkOrderUpdatedFlag()
    '''
def isRejectedReturn():
    '''    public boolean isRejectedReturn()
    '''
def createShipReceiptRecordsforLifoFifo():
    '''    public void createShipReceiptRecordsforLifoFifo()
    '''
