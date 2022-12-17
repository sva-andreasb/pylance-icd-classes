def ():
    '''returns InvBalances\n\n
    (final MboSet ms)\n
    '''
def updateCurrentBalance():
    '''returns None\n\n
    updateCurrentBalance(final double quantity)\n
    '''
def getPhysicalCount():
    '''returns double\n\n
    getPhysicalCount()\n
    '''
def getCurrentBalance():
    '''returns double\n\n
    getCurrentBalance()\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def adjustPhysicalCount():
    '''returns MboRemote\n\n
    adjustPhysicalCount(final double quantity, final Date pCountDate)\n
    '''
def adjustCurrentBalance():
    '''returns MboRemote\n\n
    adjustCurrentBalance(final double newBalance)\n
    adjustCurrentBalance(final double newBalance, final String controlacc, final String shrinkageacc)\n
    '''
def reconcileBalances():
    '''returns MboRemote\n\n
    reconcileBalances()\n
    '''
def canDelete():
    '''returns None\n\n
    canDelete()\n
    '''
def setAutoCreateInvLot():
    '''returns None\n\n
    setAutoCreateInvLot(final boolean flag)\n
    '''
def appValidate():
    '''returns None\n\n
    appValidate()\n
    '''
def save():
    '''returns None\n\n
    save()\n
    '''
def adjustLifoFifoCurrentBalance():
    '''returns None\n\n
    adjustLifoFifoCurrentBalance(final double newBalance)\n
    '''
def createInvTrans():
    '''returns MboRemote\n\n
    createInvTrans(final double quantity, final double unitcost, final boolean isreconcile)\n
    '''
def getNewBalanceForReconcile():
    '''returns double\n\n
    getNewBalanceForReconcile()\n
    '''
def reconcileBalancesLifoFifo():
    '''returns None\n\n
    reconcileBalancesLifoFifo(final String controlacc, final String shrinkageacc, final String remark)\n
    '''
def updateLifoFifoQtyAndCreateInvTrans():
    '''returns None\n\n
    updateLifoFifoQtyAndCreateInvTrans(final boolean isreconcile)\n
    updateLifoFifoQtyAndCreateInvTrans(final HashMap<String, Vector<MboRemote>> condBalMap, final boolean isreconcile)\n
    updateLifoFifoQtyAndCreateInvTrans(final Vector<MboRemote> invBalanceVec, final String conditionCode, final boolean isreconcile)\n
    '''
def reconcileLifoFifoCurrentBalance():
    '''returns None\n\n
    reconcileLifoFifoCurrentBalance(final double physcnt)\n
    '''
def checkWMATStatus():
    '''returns boolean\n\n
    checkWMATStatus()\n
    '''
def previewReconcileBalances():
    '''returns MboRemote\n\n
    previewReconcileBalances()\n
    '''
