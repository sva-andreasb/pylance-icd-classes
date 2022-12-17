def ():
    '''returns MatUseTrans\n\n
    (final MboSet ms)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def getTotalQtyForReturn():
    '''returns double\n\n
    getTotalQtyForReturn()\n
    '''
def getQtyForReturn():
    '''returns double\n\n
    getQtyForReturn()\n
    '''
def setQtyForReturn():
    '''returns None\n\n
    setQtyForReturn(final double qty)\n
    '''
def getIssueForThisReturn():
    '''returns MatUseTransRemote\n\n
    getIssueForThisReturn()\n
    '''
def getTotalQty():
    '''returns double\n\n
    getTotalQty()\n
    '''
def setTotalQtyForThisReturn():
    '''returns None\n\n
    setTotalQtyForThisReturn(final double qty)\n
    '''
def canDelete():
    '''returns None\n\n
    canDelete()\n
    '''
def appValidate():
    '''returns None\n\n
    appValidate()\n
    '''
def getWO():
    '''returns MboRemote\n\n
    getWO()\n
    '''
def save():
    '''returns None\n\n
    save()\n
    '''
def createInvoiceOnConsumption():
    '''returns None\n\n
    createInvoiceOnConsumption()\n
    '''
def getSharedInventory():
    '''returns MboRemote\n\n
    getSharedInventory()\n
    '''
def getSharedAssetSet():
    '''returns MboSetRemote\n\n
    getSharedAssetSet()\n
    '''
def getSharedInvBalance():
    '''returns MboRemote\n\n
    getSharedInvBalance()\n
    '''
def getInvBalancesRecord():
    '''returns MboRemote\n\n
    getInvBalancesRecord(final MboRemote inventory)\n
    '''
def setIgnoreLocationAssetMismatch():
    '''returns None\n\n
    setIgnoreLocationAssetMismatch(final boolean value)\n
    '''
def setIgnoreLocationOccupied():
    '''returns None\n\n
    setIgnoreLocationOccupied(final boolean value)\n
    '''
def setUpdateWorkOrdersOnMoveAsset():
    '''returns None\n\n
    setUpdateWorkOrdersOnMoveAsset(final boolean value)\n
    '''
def getSharedInvReserveSet():
    '''returns MboSetRemote\n\n
    getSharedInvReserveSet()\n
    '''
def canBeReturned():
    '''returns boolean\n\n
    canBeReturned()\n
    '''
def returnIssue():
    '''returns MboRemote\n\n
    returnIssue(final String bin, final String lot, final double qty)\n
    returnIssue()\n
    returnIssue(final MboSetRemote newMatUseSet)\n
    '''
def setIssueForThisReturn():
    '''returns None\n\n
    setIssueForThisReturn(final MboRemote issue)\n
    '''
def setRotatingAssetnum():
    '''returns None\n\n
    setRotatingAssetnum(final String rotAssetnum)\n
    '''
def isReturn():
    '''returns boolean\n\n
    isReturn()\n
    '''
def isIssue():
    '''returns boolean\n\n
    isIssue()\n
    '''
def getValidateOrder():
    '''returns String[]\n\n
    getValidateOrder()\n
    '''
def delete():
    '''returns None\n\n
    delete(final long accessModifier)\n
    '''
def undelete():
    '''returns None\n\n
    undelete()\n
    '''
def isUncommitted():
    '''returns boolean\n\n
    isUncommitted()\n
    '''
def setUncommitted():
    '''returns None\n\n
    setUncommitted(final boolean uncommitted)\n
    '''
def setSharedInvBalancesUpdatedFlag():
    '''returns None\n\n
    setSharedInvBalancesUpdatedFlag(final boolean updated)\n
    '''
def setInvReserveUpdatedFlag():
    '''returns None\n\n
    setInvReserveUpdatedFlag(final boolean updated)\n
    '''
def setCheckNegBalanceFlag():
    '''returns None\n\n
    setCheckNegBalanceFlag(final boolean flag)\n
    '''
def createMatUseTransRecordforLifoFifo():
    '''returns None\n\n
    createMatUseTransRecordforLifoFifo(final MboRemote inv)\n
    '''
def setWorkOrderUpdatedFlag():
    '''returns None\n\n
    setWorkOrderUpdatedFlag(final boolean updated)\n
    '''
def getInvReserveInVector():
    '''returns InvReserveRemote\n\n
    getInvReserveInVector(final Vector v, final MboRemote thisInvReserve)\n
    '''
def isInvoice():
    '''returns boolean\n\n
    isInvoice()\n
    '''
def isVoidReceipt():
    '''returns boolean\n\n
    isVoidReceipt()\n
    '''
def storeTheLifoFifoUpdated():
    '''returns None\n\n
    storeTheLifoFifoUpdated(final Hashtable lifofifoHash, final String invlifofifoID, final MboRemote invlifofifocost)\n
    '''
def isReceipt():
    '''returns boolean\n\n
    isReceipt()\n
    '''
def getPossibleInvLifofo():
    '''returns MboRemote\n\n
    getPossibleInvLifofo()\n
    '''
