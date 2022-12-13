def InvUseLine():
'''public InvUseLine(final MboSet ms)
'''
pass
def init():
'''public void init()
'''
pass
def add():
'''public void add()
'''
pass
def isIssue():
'''public boolean isIssue()
'''
pass
def isReturn():
'''public boolean isReturn()
'''
pass
def isMixed():
'''public boolean isMixed()
'''
pass
def isTransfer():
'''public boolean isTransfer()
'''
pass
def isRotating():
'''public boolean isRotating()
'''
pass
def isLotted():
'''public boolean isLotted()
'''
pass
def isTool():
'''public boolean isTool()
'''
pass
def getSharedInventory():
'''public MboRemote getSharedInventory()
public MboRemote getSharedInventory(final String storeLoc, final String siteid)
'''
pass
def getSharedInvBalance():
'''public MboRemote getSharedInvBalance()
public MboRemote getSharedInvBalance(final String binnum, final String lotnum)
public MboRemote getSharedInvBalance(final String binnum, final String lotnum, final boolean sameBin)
public MboRemote getSharedInvBalance(final String binnum, final String lotnum, final String storeloc, final String siteid)
'''
pass
def setIssueForThisReturn():
'''public void setIssueForThisReturn(final MboRemote issue)
'''
pass
def getWO():
'''public MboRemote getWO()
'''
pass
def validateInvUseLine():
'''public void validateInvUseLine(final ArrayList<InvUseLineSplitRemote> splitList)
'''
pass
def preValidateLine():
'''public void preValidateLine()
'''
pass
def validateLine():
'''public void validateLine()
'''
pass
def checkInvBal():
'''public void checkInvBal(final MboRemote invBal, final String parentInvUseStatus)
'''
pass
def checkLotExpiry():
'''public void checkLotExpiry(final MboRemote invBal, final ItemRemote item)
'''
pass
def checkAssetWOLocValidate():
'''public void checkAssetWOLocValidate()
'''
pass
def appValidate():
'''public void appValidate()
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
def addUpdateInvUseLineSplit():
'''public MboRemote addUpdateInvUseLineSplit()
'''
pass
def save():
'''public void save()
'''
pass
def setPickListStatus():
'''public void setPickListStatus(final MboRemote owner)
'''
pass
def setInvUseStatus():
'''public void setInvUseStatus(final MboRemote owner)
'''
pass
def isPLActionApplied():
'''public boolean isPLActionApplied(final String action)
'''
pass
def chkPickListMbo():
'''public boolean chkPickListMbo(final MboRemote owner)
'''
pass
def updateAutoCreatedInvUseLineSplit():
'''public MboRemote updateAutoCreatedInvUseLineSplit()
'''
pass
def restockPickedQty():
'''public void restockPickedQty()
'''
pass
def restockStagedQty():
'''public void restockStagedQty()
'''
pass
def setStagingBin():
'''public void setStagingBin(final String binflag, final String stagingBin)
'''
pass
def checkForNegativeBalance():
'''public void checkForNegativeBalance(final MboRemote invBal, final MboRemote invuselinesplit)
'''
pass
def checkForNegativeAvlBalanceBeforeSplitting():
'''public void checkForNegativeAvlBalanceBeforeSplitting()
'''
pass
def getSharedInvReserveSet():
'''public MboSetRemote getSharedInvReserveSet()
'''
pass
def updateInvBalances():
'''public void updateInvBalances(final MboRemote mbo, final double quantity, final String status)
'''
pass
def updateStagedInvBalances():
'''public void updateStagedInvBalances(final String status)
public void updateStagedInvBalances(final String status, final MboRemote mbo)
'''
pass
def updateInvReservePendingQty():
'''public void updateInvReservePendingQty()
'''
pass
def updateInvReserveStagedQty():
'''public void updateInvReserveStagedQty()
public void updateInvReserveStagedQty(final MboRemote mbo)
'''
pass
def updateInvReservePickedQty():
'''public void updateInvReservePickedQty(final MboRemote mbo)
'''
pass
def updateInvReserveActualQty():
'''public void updateInvReserveActualQty()
public void updateInvReserveActualQty(final boolean toUpdateWithNoRequestnum)
public void updateInvReserveActualQty(final boolean toUpdateWithNoRequestnum, final MboRemote mbo)
'''
pass
def updateInvReserveShippedQty():
'''public void updateInvReserveShippedQty()
'''
pass
def updateInvReserveForCancel():
'''public void updateInvReserveForCancel()
'''
pass
def canDelete():
'''public void canDelete()
'''
pass
def delete():
'''public void delete(final long accessModifier)
'''
pass
def undelete():
'''public void undelete()
'''
pass
def checkReservationExist():
'''public boolean checkReservationExist()
'''
pass
def checkReservationExistForInfo():
'''public void checkReservationExistForInfo()
'''
pass
def checkIssueExist():
'''public boolean checkIssueExist()
'''
pass
def checkIssueExistForInfo():
'''public void checkIssueExistForInfo()
'''
pass
def updateInvUseLineForReservation():
'''public void updateInvUseLineForReservation(final MboRemote reservation)
'''
pass
def updateInvUseLineForReturn():
'''public void updateInvUseLineForReturn(final MboRemote issuedItemForReturn)
'''
pass
def addRecordForStageTransfer():
'''public void addRecordForStageTransfer(final MboSetRemote matrecMboSet, final ArrayList<InvUseLineSplitRemote> splitLineSplit)
'''
pass
def addMatRecTransRecordForPickTransfer():
'''public MboRemote addMatRecTransRecordForPickTransfer(final MboSetRemote matrecMboSet, final MboRemote mbo)
'''
pass
def addMatRecTransRecordForRestockTransfer():
'''public MboRemote addMatRecTransRecordForRestockTransfer(final MboSetRemote matrecMboSet, final MboRemote mbo)
'''
pass
def addMatRecTransRecordForStageTransfer():
'''public MboRemote addMatRecTransRecordForStageTransfer(final MboSetRemote matrecMboSet, final MboRemote mbo)
'''
pass
def addRecordForShipTransfer():
'''public void addRecordForShipTransfer(final MboSetRemote matrecMboSet, final ArrayList<InvUseLineSplitRemote> splitLineSplit)
'''
pass
def addMatRecTransRecordForShipTransfer():
'''public MboRemote addMatRecTransRecordForShipTransfer(final MboSetRemote matrecMboSet, final MboRemote mbo)
'''
pass
def addTransferRecordForComplete():
'''public void addTransferRecordForComplete(final MboSetRemote matrecMboSet, final ArrayList<InvUseLineSplitRemote> splitLineSplit)
'''
pass
def addMatRecTransRecordForComplete():
'''public MboRemote addMatRecTransRecordForComplete(final MboSetRemote matrecMboSet, final MboRemote mbo)
'''
pass
def addIssueReturnRecordForComplete():
'''public void addIssueReturnRecordForComplete(final MboSetRemote matrecMboSet, final ArrayList<InvUseLineSplitRemote> splitLineSplit)
'''
pass
def addMatUseTransRecordForComplete():
'''public MboRemote addMatUseTransRecordForComplete(final MboSetRemote matuseMboSet, final MboRemote mbo)
'''
pass
def addMatRecTransRecordForCancelStageTransfer():
'''public MboRemote addMatRecTransRecordForCancelStageTransfer()
'''
pass
def addMatRecTransRecordForCancelShipTransfer():
'''public MboRemote addMatRecTransRecordForCancelShipTransfer()
'''
pass
def getPO():
'''public MboRemote getPO()
'''
pass
def setOwnerPO():
'''public void setOwnerPO(final MboRemote po)
'''
pass
def getPOLine():
'''public MboRemote getPOLine()
'''
pass
def getTotalCurBalance():
'''public double getTotalCurBalance()
'''
pass
def getInvUseLineQtyForReturn():
'''public double getInvUseLineQtyForReturn(final long matusetransid)
'''
pass
def getQtyForReturn():
'''public double getQtyForReturn()
'''
pass
def updateUnitCost():
'''public void updateUnitCost()
'''
pass
def validateQty():
'''public boolean validateQty()
'''
pass
def needsSplitting():
'''public boolean needsSplitting()
'''
pass
def getDefaultLotNum():
'''public String getDefaultLotNum()
'''
pass
def canGoNegative():
'''public void canGoNegative(final UserInfo userInfo, final double toBeIssued, final double curbal, final double totalAvailable, final MboRemote sourceMbo)
public void canGoNegative(final UserInfo userInfo, final double toBeIssued, final double totalAvailable, final MboRemote sourceMbo)
'''
pass
def modify():
'''public void modify()
'''
pass
def checkItemStatus():
'''public void checkItemStatus()
'''
pass
def setReservationUserPref():
'''public void setReservationUserPref()
'''
pass
def setReturnUserPref():
'''public void setReturnUserPref()
'''
pass
def setUserPref():
'''public void setUserPref(final MboRemote mbo)
'''
pass
def getPendingQty():
'''public double getPendingQty(final String requestnum, final String siteid)
'''
pass
def smartFindByObjectName():
'''public MboSetRemote smartFindByObjectName(final String sourceObj, final String targetAttrName, final String value, final boolean exact)
'''
pass
def checkRotatingAssetExistInToSite():
'''public boolean checkRotatingAssetExistInToSite(final String rotassetnum, final MboRemote mbo)
'''
pass
def updateAssetStatus():
'''public void updateAssetStatus(final String rotassetnum, final String status)
'''
pass
def updateReceiptsComplete():
'''public void updateReceiptsComplete()
'''
pass
def updateReceivedQty():
'''public void updateReceivedQty(final double receivedQty)
'''
pass
def updateReturnedQty():
'''public void updateReturnedQty(final double returnedQty)
'''
pass
def isInspectionRequired():
'''public boolean isInspectionRequired()
'''
pass
def initFieldFlagsOnMbo():
'''public void initFieldFlagsOnMbo(final String attrName)
'''
pass
def setDisplayUnitCost():
'''public void setDisplayUnitCost()
'''
pass
def updateLifoFifoTable():
'''public void updateLifoFifoTable(final MboRemote invUseLineSplit)
'''
pass
def updateLifoFifoForCancelled():
'''public void updateLifoFifoForCancelled(final MboRemote useLine)
'''
pass
def addTransactionRecordsLIFOFIFO():
'''public void addTransactionRecordsLIFOFIFO(final MboSetRemote transMboSet, final ArrayList<InvUseLineSplitRemote> splitLineSplit, final String status)
'''
pass
def updateInvLifoFifoCostSet():
'''public double updateInvLifoFifoCostSet(final MboSetRemote transMboSet, MboRemote invUseLineSplit, final MboSetRemote invlifofifocostset, final String status)
'''
pass
def setAttributesEditibiltyForReturn():
'''public void setAttributesEditibiltyForReturn()
'''
pass
def allKitComponentsAreInTransferToStore():
'''public void allKitComponentsAreInTransferToStore()
'''
pass
def updateMR():
'''public void updateMR(final MboRemote invReserve)
'''
pass
def getPhyscntDate():
'''public Date getPhyscntDate(Date phyCntDate, final Date actualDate)
'''
pass
def getInvReserveInVector():
'''public InvReserveRemote getInvReserveInVector(final Vector v, final MboRemote thisInvReserve)
'''
pass
def isSameStoreTransfer():
'''public boolean isSameStoreTransfer()
'''
pass
def getInvUse():
'''public MboRemote getInvUse()
'''
pass
def setCancelInvUseLines():
'''public void setCancelInvUseLines(final boolean hasBeenCalled)
'''
pass
def setValue():
'''public void setValue(final String attributeName, final String val, final long accessModifier)
'''
pass
