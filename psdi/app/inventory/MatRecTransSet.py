def clearVector():
    '''public void clearVector()
    '''
def addWarnings():
    '''public void addWarnings(final MXException mx)
    '''
def MatRecTransSet():
    '''public MatRecTransSet(final MboServerInterface ms)
    '''
def validateOrderQty():
    '''public void validateOrderQty()
    '''
def deleteUnSelected():
    '''public void deleteUnSelected()
    '''
def copyInvReserveSet():
    '''public void copyInvReserveSet(final MboSetRemote invReserveSet, final String inOrOut)
    '''
def copySparePartSet():
    '''public void copySparePartSet(final MboSetRemote sparePartSet, final String inOrOut)
    '''
def copyInvBalancesSet():
    '''public void copyInvBalancesSet(final MboSetRemote invBalancesSet, final String inOrOut)
    '''
def copyPOLineSet():
    '''public void copyPOLineSet(final MboSetRemote poLineSet, final String inOrOut)
    '''
def warningsFromCopyPOItems():
    '''public void warningsFromCopyPOItems()
    '''
def copyMatRecTransSet():
    '''public void copyMatRecTransSet(final MboSetRemote matRecTransSet, final String inOrOut)
    '''
def warningsFromCopyMatRecTransItems():
    '''public void warningsFromCopyMatRecTransItems()
    '''
def setLocation():
    '''public void setLocation(final String loc)
    '''
def getLocation():
    '''public String getLocation()
    '''
def setPONum():
    '''public void setPONum(final String po)
    '''
def getPONum():
    '''public String getPONum()
    '''
def approveReceipts():
    '''public Vector approveReceipts(final Date todaysDate)
    '''
def canAdd():
    '''public void canAdd()
    '''
def setQbe():
    '''public void setQbe(final String attribute, final String expression)
    '''
def getUserWhere():
    '''public String getUserWhere(final String alias)
    '''
def resetQbe():
    '''public void resetQbe()
    '''
def createAssets():
    '''public void createAssets(final String ponum, final int polinenum, final String ownersysid, final String siteid)
    '''
def createReturnsForAssets():
    '''public void createReturnsForAssets(final PO po, final MboSetRemote matRecTransAssetSetRemote)
    '''
def checkInspectedTotal():
    '''public void checkInspectedTotal()
    '''
def returnIPCParts():
    '''public void returnIPCParts(final IpcSelectedPartsSetRemote partset)
    '''
def preValidateIpcBom():
    '''public void preValidateIpcBom(final IpcBomSetRemote bomset)
    '''
def setToExecuteCompleteAdd():
    '''public void setToExecuteCompleteAdd(final boolean toset)
    '''
def toExecuteCompleteAdd():
    '''public boolean toExecuteCompleteAdd()
    '''
def getNumberOfActualDateExceptions():
    '''public int getNumberOfActualDateExceptions()
    '''
def incrNumberOfActualDateExceptions():
    '''public void incrNumberOfActualDateExceptions(final int i)
    '''
def setCrossOrgExchangeRate():
    '''public void setCrossOrgExchangeRate(final MboRemote newMatRec, final MboRemote transferOutMatRec)
    '''
def getLineNumAssetMap():
    '''public HashMap<String, String> getLineNumAssetMap()
    '''
def setLineNumAssetMap():
    '''public void setLineNumAssetMap(final String linenum, final String rotassetnum)
    '''
def getShipReceiptCountMap():
    '''public HashMap<String, Long> getShipReceiptCountMap()
    '''
def setShipReceiptCountMap():
    '''public void setShipReceiptCountMap(final String linenum, final long count)
    '''
def getVoidShipReceiptCountMap():
    '''public HashMap<String, Long> getVoidShipReceiptCountMap()
    '''
def setVoidShipReceiptCountMap():
    '''public void setVoidShipReceiptCountMap(final String linenum, final long count)
    '''
