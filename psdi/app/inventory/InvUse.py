def InvUse():
    '''public InvUse(final MboSet ms)
    '''
def getProcess():
    '''public String getProcess()
    '''
def getMeterMap():
    '''public HashMap<String, DeployedMeterRemote> getMeterMap()
    '''
def getStatusListName():
    '''public String getStatusListName()
    '''
def init():
    '''public void init()
    '''
def initFieldFlagsOnMbo():
    '''public void initFieldFlagsOnMbo(final String attrName)
    '''
def add():
    '''public void add()
    '''
def getStatus():
    '''public String getStatus()
    '''
def addInvUseLine():
    '''public InvUseLineRemote addInvUseLine(final MboRemote owner)
    '''
def changeStatus():
    '''public void changeStatus(final String status, final Date date, final String memo, final long accessModifier)
    public void changeStatus(final String status, final Date date, final String memo, final String binflag, final String stagingbin, final boolean listtab, final long accessModifier)
    '''
def validateStatus():
    '''public void validateStatus(final String status, final Date date, final String memo, final String binflag, final String stagingbin, final boolean listtab)
    '''
def chkPickListMbo():
    '''public boolean chkPickListMbo(final MboRemote owner)
    '''
def checkReservationandSetBin():
    '''public void checkReservationandSetBin(final String binflag, final String stagebin, final String status)
    '''
def validateLineReservationandSetBin():
    '''public boolean validateLineReservationandSetBin(final boolean listtab, final String binflag, final String stagebin, final String status)
    '''
def processInvUseLines():
    '''public boolean processInvUseLines()
    '''
def deleteInvUseLines():
    '''public void deleteInvUseLines()
    '''
def cancelInvUseLines():
    '''public void cancelInvUseLines()
    '''
def getInvUseLineNum():
    '''public String getInvUseLineNum()
    '''
def allReservationDeletedInSet():
    '''public boolean allReservationDeletedInSet()
    '''
def isEntered():
    '''public boolean isEntered()
    '''
def isStaged():
    '''public boolean isStaged()
    '''
def isShipped():
    '''public boolean isShipped()
    '''
def isCompleted():
    '''public boolean isCompleted()
    '''
def isCancelled():
    '''public boolean isCancelled()
    '''
def copyInvUseLineSetForReturn():
    '''public void copyInvUseLineSetForReturn(final MboSetRemote matUseTransSet)
    '''
def copyInvReserveSetForInvUse():
    '''public void copyInvReserveSetForInvUse(final MboSetRemote invReserveSet)
    '''
def copySparePartSetForInvUse():
    '''public void copySparePartSetForInvUse(final MboSetRemote sparePartSet)
    '''
def copyInvBalancesSetForItems():
    '''public void copyInvBalancesSetForItems(final MboSetRemote invBalancesSet)
    '''
def isTransfer():
    '''public boolean isTransfer()
    '''
def isIssue():
    '''public boolean isIssue()
    '''
def staged():
    '''public void staged()
    '''
def complete():
    '''public void complete(final String currentMaxStatus)
    '''
def shipped():
    '''public void shipped(final String currentMaxStatus)
    '''
def getInvUseLineSplitRecordsMap():
    '''public HashMap<Long, ArrayList<InvUseLineSplitRemote>> getInvUseLineSplitRecordsMap()
    '''
def cancelled():
    '''public void cancelled()
    '''
def isSplitNeeded():
    '''public void isSplitNeeded(final MboRemote invUseLine)
    '''
def isListSelected():
    '''public boolean isListSelected()
    '''
def setListSelected():
    '''public void setListSelected(final boolean isListSelected)
    '''
def validateLines():
    '''public void validateLines(final String status)
    '''
def checkNegativeBalanace():
    '''public void checkNegativeBalanace(final MboRemote invuseline)
    '''
def validateRotatingAssets():
    '''public void validateRotatingAssets(final MboRemote invUseLine)
    '''
def validateGLAccounts():
    '''public void validateGLAccounts(final MboRemote invuseline)
    '''
def modify():
    '''public void modify()
    '''
def getUseType():
    '''public String getUseType()
    '''
def validatedata():
    '''public void validatedata()
    '''
def checkReturnLinesinSet():
    '''public boolean checkReturnLinesinSet()
    '''
def getQtyMap():
    '''public HashMap<Long, Double> getQtyMap()
    '''
def setQtyMap():
    '''public void setQtyMap(final Long invBalId, final Double qty)
    '''
def removeQtyMap():
    '''public void removeQtyMap(final Long invBalId)
    '''
def getUsedRotAssetNSMap():
    '''public HashMap<String, String> getUsedRotAssetNSMap()
    '''
def setUsedRotAssetNSMap():
    '''public void setUsedRotAssetNSMap(final String keyid, final String rotassetnum)
    '''
def removeUsedRotAssetNSMap():
    '''public void removeUsedRotAssetNSMap(final String keyid)
    '''
def getUsedRotAssetSMap():
    '''public HashMap<String, String> getUsedRotAssetSMap()
    '''
def setUsedRotAssetSMap():
    '''public void setUsedRotAssetSMap(final String keyid, final String rotassetnum)
    '''
def removeUsedRotAssetSMap():
    '''public void removeUsedRotAssetSMap(final String keyid)
    '''
def getRotQtyMap():
    '''public HashMap<Long, Double> getRotQtyMap()
    '''
def setRotQtyMap():
    '''public void setRotQtyMap(final Long keyid, final Double qty)
    '''
def removeRotQtyMap():
    '''public void removeRotQtyMap(final Long keyid)
    '''
def getDeletedInvUseLineList():
    '''public ArrayList<Long> getDeletedInvUseLineList()
    '''
def getInvBalQtyNSMap():
    '''public HashMap<Long, Double> getInvBalQtyNSMap()
    '''
def setInvBalQtyNSMap():
    '''public void setInvBalQtyNSMap(final Long invBalId, final Double qty)
    '''
def removeInvBalQtyNSMap():
    '''public void removeInvBalQtyNSMap(final Long invBalId)
    '''
def getUsedRotAssetList():
    '''public ArrayList<String> getUsedRotAssetList()
    '''
def addToUsedRotAssetList():
    '''public void addToUsedRotAssetList(final String rotassetnum)
    '''
def checkRotAssetNumList():
    '''public void checkRotAssetNumList(final String key, final String rotassetnum, final boolean newasset)
    '''
def canDelete():
    '''public void canDelete()
    '''
def setShipmentLines():
    '''public MboRemote setShipmentLines()
    '''
def addShipmentLines():
    '''public void addShipmentLines(final MboRemote shipment)
    '''
def validateForShipped():
    '''public void validateForShipped(final MboRemote invUseLine)
    '''
def getClearingAcct():
    '''public String getClearingAcct()
    '''
def getShipmentLineMap():
    '''public HashMap<Long, MboRemote> getShipmentLineMap()
    '''
def save():
    '''public void save()
    '''
def updateInvUseReceipts():
    '''public void updateInvUseReceipts(final InvUseLineRemote invUseLine)
    '''
def getExchangeRate():
    '''public double getExchangeRate(final Date date)
    '''
def getExchangeRate2():
    '''public double getExchangeRate2(final Date date)
    '''
def getInvUseLineMap():
    '''public HashMap<Long, MboRemote> getInvUseLineMap()
    '''
def validateHardReservation():
    '''public void validateHardReservation(final MboRemote invUseLine)
    '''
def getEvaluateSplitFlag():
    '''public int getEvaluateSplitFlag()
    '''
def setEvaluateSplitFlag():
    '''public int setEvaluateSplitFlag(final int split)
    '''
def setValidateStatusHasBeenCalled():
    '''public void setValidateStatusHasBeenCalled(final boolean hasBeenCalled)
    '''
def getValidateStatusHasBeenCalled():
    '''public boolean getValidateStatusHasBeenCalled()
    '''
def createInvUsageForPartialIssues():
    '''public MboRemote createInvUsageForPartialIssues(final MboSetRemote invReserveSet)
    '''
def duplicate():
    '''public MboRemote duplicate()
    '''
def selectAllInSet():
    '''public void selectAllInSet(final MboSetRemote invReserveSet)
    '''
def appValidate():
    '''public void appValidate()
    '''
def validateFinancialPeriods():
    '''public void validateFinancialPeriods(final String newStatus)
    '''
def canUseNextFinancialPeriod():
    '''public Boolean canUseNextFinancialPeriod()
    '''
def getValidateFinancialPeriodsHasBeenCalled():
    '''public boolean getValidateFinancialPeriodsHasBeenCalled()
    '''
def setValidateFinancialPeriodsCalled():
    '''public void setValidateFinancialPeriodsCalled(final boolean hasBeenCalled)
    '''
