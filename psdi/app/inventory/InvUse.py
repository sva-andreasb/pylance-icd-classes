def InvUse():
'''public InvUse(final MboSet ms)
'''
pass
def getProcess():
'''public String getProcess()
'''
pass
def getMeterMap():
'''public HashMap<String, DeployedMeterRemote> getMeterMap()
'''
pass
def getStatusListName():
'''public String getStatusListName()
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
def getStatus():
'''public String getStatus()
'''
pass
def addInvUseLine():
'''public InvUseLineRemote addInvUseLine(final MboRemote owner)
'''
pass
def changeStatus():
'''public void changeStatus(final String status, final Date date, final String memo, final long accessModifier)
public void changeStatus(final String status, final Date date, final String memo, final String binflag, final String stagingbin, final boolean listtab, final long accessModifier)
'''
pass
def validateStatus():
'''public void validateStatus(final String status, final Date date, final String memo, final String binflag, final String stagingbin, final boolean listtab)
'''
pass
def chkPickListMbo():
'''public boolean chkPickListMbo(final MboRemote owner)
'''
pass
def checkReservationandSetBin():
'''public void checkReservationandSetBin(final String binflag, final String stagebin, final String status)
'''
pass
def validateLineReservationandSetBin():
'''public boolean validateLineReservationandSetBin(final boolean listtab, final String binflag, final String stagebin, final String status)
'''
pass
def processInvUseLines():
'''public boolean processInvUseLines()
'''
pass
def deleteInvUseLines():
'''public void deleteInvUseLines()
'''
pass
def cancelInvUseLines():
'''public void cancelInvUseLines()
'''
pass
def getInvUseLineNum():
'''public String getInvUseLineNum()
'''
pass
def allReservationDeletedInSet():
'''public boolean allReservationDeletedInSet()
'''
pass
def isEntered():
'''public boolean isEntered()
'''
pass
def isStaged():
'''public boolean isStaged()
'''
pass
def isShipped():
'''public boolean isShipped()
'''
pass
def isCompleted():
'''public boolean isCompleted()
'''
pass
def isCancelled():
'''public boolean isCancelled()
'''
pass
def copyInvUseLineSetForReturn():
'''public void copyInvUseLineSetForReturn(final MboSetRemote matUseTransSet)
'''
pass
def copyInvReserveSetForInvUse():
'''public void copyInvReserveSetForInvUse(final MboSetRemote invReserveSet)
'''
pass
def copySparePartSetForInvUse():
'''public void copySparePartSetForInvUse(final MboSetRemote sparePartSet)
'''
pass
def copyInvBalancesSetForItems():
'''public void copyInvBalancesSetForItems(final MboSetRemote invBalancesSet)
'''
pass
def isTransfer():
'''public boolean isTransfer()
'''
pass
def isIssue():
'''public boolean isIssue()
'''
pass
def staged():
'''public void staged()
'''
pass
def complete():
'''public void complete(final String currentMaxStatus)
'''
pass
def shipped():
'''public void shipped(final String currentMaxStatus)
'''
pass
def getInvUseLineSplitRecordsMap():
'''public HashMap<Long, ArrayList<InvUseLineSplitRemote>> getInvUseLineSplitRecordsMap()
'''
pass
def cancelled():
'''public void cancelled()
'''
pass
def isSplitNeeded():
'''public void isSplitNeeded(final MboRemote invUseLine)
'''
pass
def isListSelected():
'''public boolean isListSelected()
'''
pass
def setListSelected():
'''public void setListSelected(final boolean isListSelected)
'''
pass
def validateLines():
'''public void validateLines(final String status)
'''
pass
def checkNegativeBalanace():
'''public void checkNegativeBalanace(final MboRemote invuseline)
'''
pass
def validateRotatingAssets():
'''public void validateRotatingAssets(final MboRemote invUseLine)
'''
pass
def validateGLAccounts():
'''public void validateGLAccounts(final MboRemote invuseline)
'''
pass
def modify():
'''public void modify()
'''
pass
def getUseType():
'''public String getUseType()
'''
pass
def validatedata():
'''public void validatedata()
'''
pass
def checkReturnLinesinSet():
'''public boolean checkReturnLinesinSet()
'''
pass
def getQtyMap():
'''public HashMap<Long, Double> getQtyMap()
'''
pass
def setQtyMap():
'''public void setQtyMap(final Long invBalId, final Double qty)
'''
pass
def removeQtyMap():
'''public void removeQtyMap(final Long invBalId)
'''
pass
def getUsedRotAssetNSMap():
'''public HashMap<String, String> getUsedRotAssetNSMap()
'''
pass
def setUsedRotAssetNSMap():
'''public void setUsedRotAssetNSMap(final String keyid, final String rotassetnum)
'''
pass
def removeUsedRotAssetNSMap():
'''public void removeUsedRotAssetNSMap(final String keyid)
'''
pass
def getUsedRotAssetSMap():
'''public HashMap<String, String> getUsedRotAssetSMap()
'''
pass
def setUsedRotAssetSMap():
'''public void setUsedRotAssetSMap(final String keyid, final String rotassetnum)
'''
pass
def removeUsedRotAssetSMap():
'''public void removeUsedRotAssetSMap(final String keyid)
'''
pass
def getRotQtyMap():
'''public HashMap<Long, Double> getRotQtyMap()
'''
pass
def setRotQtyMap():
'''public void setRotQtyMap(final Long keyid, final Double qty)
'''
pass
def removeRotQtyMap():
'''public void removeRotQtyMap(final Long keyid)
'''
pass
def getDeletedInvUseLineList():
'''public ArrayList<Long> getDeletedInvUseLineList()
'''
pass
def getInvBalQtyNSMap():
'''public HashMap<Long, Double> getInvBalQtyNSMap()
'''
pass
def setInvBalQtyNSMap():
'''public void setInvBalQtyNSMap(final Long invBalId, final Double qty)
'''
pass
def removeInvBalQtyNSMap():
'''public void removeInvBalQtyNSMap(final Long invBalId)
'''
pass
def getUsedRotAssetList():
'''public ArrayList<String> getUsedRotAssetList()
'''
pass
def addToUsedRotAssetList():
'''public void addToUsedRotAssetList(final String rotassetnum)
'''
pass
def checkRotAssetNumList():
'''public void checkRotAssetNumList(final String key, final String rotassetnum, final boolean newasset)
'''
pass
def canDelete():
'''public void canDelete()
'''
pass
def setShipmentLines():
'''public MboRemote setShipmentLines()
'''
pass
def addShipmentLines():
'''public void addShipmentLines(final MboRemote shipment)
'''
pass
def validateForShipped():
'''public void validateForShipped(final MboRemote invUseLine)
'''
pass
def getClearingAcct():
'''public String getClearingAcct()
'''
pass
def getShipmentLineMap():
'''public HashMap<Long, MboRemote> getShipmentLineMap()
'''
pass
def save():
'''public void save()
'''
pass
def updateInvUseReceipts():
'''public void updateInvUseReceipts(final InvUseLineRemote invUseLine)
'''
pass
def getExchangeRate():
'''public double getExchangeRate(final Date date)
'''
pass
def getExchangeRate2():
'''public double getExchangeRate2(final Date date)
'''
pass
def getInvUseLineMap():
'''public HashMap<Long, MboRemote> getInvUseLineMap()
'''
pass
def validateHardReservation():
'''public void validateHardReservation(final MboRemote invUseLine)
'''
pass
def getEvaluateSplitFlag():
'''public int getEvaluateSplitFlag()
'''
pass
def setEvaluateSplitFlag():
'''public int setEvaluateSplitFlag(final int split)
'''
pass
def setValidateStatusHasBeenCalled():
'''public void setValidateStatusHasBeenCalled(final boolean hasBeenCalled)
'''
pass
def getValidateStatusHasBeenCalled():
'''public boolean getValidateStatusHasBeenCalled()
'''
pass
def createInvUsageForPartialIssues():
'''public MboRemote createInvUsageForPartialIssues(final MboSetRemote invReserveSet)
'''
pass
def duplicate():
'''public MboRemote duplicate()
'''
pass
def selectAllInSet():
'''public void selectAllInSet(final MboSetRemote invReserveSet)
'''
pass
def appValidate():
'''public void appValidate()
'''
pass
def validateFinancialPeriods():
'''public void validateFinancialPeriods(final String newStatus)
'''
pass
def canUseNextFinancialPeriod():
'''public Boolean canUseNextFinancialPeriod()
'''
pass
def getValidateFinancialPeriodsHasBeenCalled():
'''public boolean getValidateFinancialPeriodsHasBeenCalled()
'''
pass
def setValidateFinancialPeriodsCalled():
'''public void setValidateFinancialPeriodsCalled(final boolean hasBeenCalled)
'''
pass
