def InvUseLine():
    '''public InvUseLine(final MboSet ms)
    '''
def init():
    '''public void init()
    '''
def add():
    '''public void add()
    '''
def isIssue():
    '''public boolean isIssue()
    '''
def isReturn():
    '''public boolean isReturn()
    '''
def isMixed():
    '''public boolean isMixed()
    '''
def isTransfer():
    '''public boolean isTransfer()
    '''
def isRotating():
    '''public boolean isRotating()
    '''
def isLotted():
    '''public boolean isLotted()
    '''
def isTool():
    '''public boolean isTool()
    '''
def getSharedInventory():
    '''public MboRemote getSharedInventory()
    public MboRemote getSharedInventory(final String storeLoc, final String siteid)
    '''
def getSharedInvBalance():
    '''public MboRemote getSharedInvBalance()
    public MboRemote getSharedInvBalance(final String binnum, final String lotnum)
    public MboRemote getSharedInvBalance(final String binnum, final String lotnum, final boolean sameBin)
    public MboRemote getSharedInvBalance(final String binnum, final String lotnum, final String storeloc, final String siteid)
    '''
def setIssueForThisReturn():
    '''public void setIssueForThisReturn(final MboRemote issue)
    '''
def getWO():
    '''public MboRemote getWO()
    '''
def validateInvUseLine():
    '''public void validateInvUseLine(final ArrayList<InvUseLineSplitRemote> splitList)
    '''
def preValidateLine():
    '''public void preValidateLine()
    '''
def validateLine():
    '''public void validateLine()
    '''
def checkInvBal():
    '''public void checkInvBal(final MboRemote invBal, final String parentInvUseStatus)
    '''
def checkLotExpiry():
    '''public void checkLotExpiry(final MboRemote invBal, final ItemRemote item)
    '''
def checkAssetWOLocValidate():
    '''public void checkAssetWOLocValidate()
    '''
def appValidate():
    '''public void appValidate()
    '''
def getBinNumFlag():
    '''public boolean getBinNumFlag()
    '''
def setBinNumFlag():
    '''public void setBinNumFlag(final boolean binNumFlag)
    '''
def addUpdateInvUseLineSplit():
    '''public MboRemote addUpdateInvUseLineSplit()
    '''
def save():
    '''public void save()
    '''
def setPickListStatus():
    '''public void setPickListStatus(final MboRemote owner)
    '''
def setInvUseStatus():
    '''public void setInvUseStatus(final MboRemote owner)
    '''
def isPLActionApplied():
    '''public boolean isPLActionApplied(final String action)
    '''
def chkPickListMbo():
    '''public boolean chkPickListMbo(final MboRemote owner)
    '''
def updateAutoCreatedInvUseLineSplit():
    '''public MboRemote updateAutoCreatedInvUseLineSplit()
    '''
def restockPickedQty():
    '''public void restockPickedQty()
    '''
def restockStagedQty():
    '''public void restockStagedQty()
    '''
def setStagingBin():
    '''public void setStagingBin(final String binflag, final String stagingBin)
    '''
def checkForNegativeBalance():
    '''public void checkForNegativeBalance(final MboRemote invBal, final MboRemote invuselinesplit)
    '''
def checkForNegativeAvlBalanceBeforeSplitting():
    '''public void checkForNegativeAvlBalanceBeforeSplitting()
    '''
def getSharedInvReserveSet():
    '''public MboSetRemote getSharedInvReserveSet()
    '''
def updateInvBalances():
    '''public void updateInvBalances(final MboRemote mbo, final double quantity, final String status)
    '''
def updateStagedInvBalances():
    '''public void updateStagedInvBalances(final String status)
    public void updateStagedInvBalances(final String status, final MboRemote mbo)
    '''
def updateInvReservePendingQty():
    '''public void updateInvReservePendingQty()
    '''
def updateInvReserveStagedQty():
    '''public void updateInvReserveStagedQty()
    public void updateInvReserveStagedQty(final MboRemote mbo)
    '''
def updateInvReservePickedQty():
    '''public void updateInvReservePickedQty(final MboRemote mbo)
    '''
def updateInvReserveActualQty():
    '''public void updateInvReserveActualQty()
    public void updateInvReserveActualQty(final boolean toUpdateWithNoRequestnum)
    public void updateInvReserveActualQty(final boolean toUpdateWithNoRequestnum, final MboRemote mbo)
    '''
def updateInvReserveShippedQty():
    '''public void updateInvReserveShippedQty()
    '''
def updateInvReserveForCancel():
    '''public void updateInvReserveForCancel()
    '''
def canDelete():
    '''public void canDelete()
    '''
def delete():
    '''public void delete(final long accessModifier)
    '''
def undelete():
    '''public void undelete()
    '''
def checkReservationExist():
    '''public boolean checkReservationExist()
    '''
def checkReservationExistForInfo():
    '''public void checkReservationExistForInfo()
    '''
def checkIssueExist():
    '''public boolean checkIssueExist()
    '''
def checkIssueExistForInfo():
    '''public void checkIssueExistForInfo()
    '''
def updateInvUseLineForReservation():
    '''public void updateInvUseLineForReservation(final MboRemote reservation)
    '''
def updateInvUseLineForReturn():
    '''public void updateInvUseLineForReturn(final MboRemote issuedItemForReturn)
    '''
def addRecordForStageTransfer():
    '''public void addRecordForStageTransfer(final MboSetRemote matrecMboSet, final ArrayList<InvUseLineSplitRemote> splitLineSplit)
    '''
def addMatRecTransRecordForPickTransfer():
    '''public MboRemote addMatRecTransRecordForPickTransfer(final MboSetRemote matrecMboSet, final MboRemote mbo)
    '''
def addMatRecTransRecordForRestockTransfer():
    '''public MboRemote addMatRecTransRecordForRestockTransfer(final MboSetRemote matrecMboSet, final MboRemote mbo)
    '''
def addMatRecTransRecordForStageTransfer():
    '''public MboRemote addMatRecTransRecordForStageTransfer(final MboSetRemote matrecMboSet, final MboRemote mbo)
    '''
def addRecordForShipTransfer():
    '''public void addRecordForShipTransfer(final MboSetRemote matrecMboSet, final ArrayList<InvUseLineSplitRemote> splitLineSplit)
    '''
def addMatRecTransRecordForShipTransfer():
    '''public MboRemote addMatRecTransRecordForShipTransfer(final MboSetRemote matrecMboSet, final MboRemote mbo)
    '''
def addTransferRecordForComplete():
    '''public void addTransferRecordForComplete(final MboSetRemote matrecMboSet, final ArrayList<InvUseLineSplitRemote> splitLineSplit)
    '''
def addMatRecTransRecordForComplete():
    '''public MboRemote addMatRecTransRecordForComplete(final MboSetRemote matrecMboSet, final MboRemote mbo)
    '''
def addIssueReturnRecordForComplete():
    '''public void addIssueReturnRecordForComplete(final MboSetRemote matrecMboSet, final ArrayList<InvUseLineSplitRemote> splitLineSplit)
    '''
def addMatUseTransRecordForComplete():
    '''public MboRemote addMatUseTransRecordForComplete(final MboSetRemote matuseMboSet, final MboRemote mbo)
    '''
def addMatRecTransRecordForCancelStageTransfer():
    '''public MboRemote addMatRecTransRecordForCancelStageTransfer()
    '''
def addMatRecTransRecordForCancelShipTransfer():
    '''public MboRemote addMatRecTransRecordForCancelShipTransfer()
    '''
def getPO():
    '''public MboRemote getPO()
    '''
def setOwnerPO():
    '''public void setOwnerPO(final MboRemote po)
    '''
def getPOLine():
    '''public MboRemote getPOLine()
    '''
def getTotalCurBalance():
    '''public double getTotalCurBalance()
    '''
def getInvUseLineQtyForReturn():
    '''public double getInvUseLineQtyForReturn(final long matusetransid)
    '''
def getQtyForReturn():
    '''public double getQtyForReturn()
    '''
def updateUnitCost():
    '''public void updateUnitCost()
    '''
def validateQty():
    '''public boolean validateQty()
    '''
def needsSplitting():
    '''public boolean needsSplitting()
    '''
def getDefaultLotNum():
    '''public String getDefaultLotNum()
    '''
def canGoNegative():
    '''public void canGoNegative(final UserInfo userInfo, final double toBeIssued, final double curbal, final double totalAvailable, final MboRemote sourceMbo)
    public void canGoNegative(final UserInfo userInfo, final double toBeIssued, final double totalAvailable, final MboRemote sourceMbo)
    '''
def modify():
    '''public void modify()
    '''
def checkItemStatus():
    '''public void checkItemStatus()
    '''
def setReservationUserPref():
    '''public void setReservationUserPref()
    '''
def setReturnUserPref():
    '''public void setReturnUserPref()
    '''
def setUserPref():
    '''public void setUserPref(final MboRemote mbo)
    '''
def getPendingQty():
    '''public double getPendingQty(final String requestnum, final String siteid)
    '''
def smartFindByObjectName():
    '''public MboSetRemote smartFindByObjectName(final String sourceObj, final String targetAttrName, final String value, final boolean exact)
    '''
def checkRotatingAssetExistInToSite():
    '''public boolean checkRotatingAssetExistInToSite(final String rotassetnum, final MboRemote mbo)
    '''
def updateAssetStatus():
    '''public void updateAssetStatus(final String rotassetnum, final String status)
    '''
def updateReceiptsComplete():
    '''public void updateReceiptsComplete()
    '''
def updateReceivedQty():
    '''public void updateReceivedQty(final double receivedQty)
    '''
def updateReturnedQty():
    '''public void updateReturnedQty(final double returnedQty)
    '''
def isInspectionRequired():
    '''public boolean isInspectionRequired()
    '''
def initFieldFlagsOnMbo():
    '''public void initFieldFlagsOnMbo(final String attrName)
    '''
def setDisplayUnitCost():
    '''public void setDisplayUnitCost()
    '''
def updateLifoFifoTable():
    '''public void updateLifoFifoTable(final MboRemote invUseLineSplit)
    '''
def updateLifoFifoForCancelled():
    '''public void updateLifoFifoForCancelled(final MboRemote useLine)
    '''
def addTransactionRecordsLIFOFIFO():
    '''public void addTransactionRecordsLIFOFIFO(final MboSetRemote transMboSet, final ArrayList<InvUseLineSplitRemote> splitLineSplit, final String status)
    '''
def updateInvLifoFifoCostSet():
    '''public double updateInvLifoFifoCostSet(final MboSetRemote transMboSet, MboRemote invUseLineSplit, final MboSetRemote invlifofifocostset, final String status)
    '''
def setAttributesEditibiltyForReturn():
    '''public void setAttributesEditibiltyForReturn()
    '''
def allKitComponentsAreInTransferToStore():
    '''public void allKitComponentsAreInTransferToStore()
    '''
def updateMR():
    '''public void updateMR(final MboRemote invReserve)
    '''
def getPhyscntDate():
    '''public Date getPhyscntDate(Date phyCntDate, final Date actualDate)
    '''
def getInvReserveInVector():
    '''public InvReserveRemote getInvReserveInVector(final Vector v, final MboRemote thisInvReserve)
    '''
def isSameStoreTransfer():
    '''public boolean isSameStoreTransfer()
    '''
def getInvUse():
    '''public MboRemote getInvUse()
    '''
def setCancelInvUseLines():
    '''public void setCancelInvUseLines(final boolean hasBeenCalled)
    '''
def setValue():
    '''public void setValue(final String attributeName, final String val, final long accessModifier)
    '''
