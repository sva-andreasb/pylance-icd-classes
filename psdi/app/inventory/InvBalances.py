def InvBalances():
    '''public InvBalances(final MboSet ms)
    '''
def updateCurrentBalance():
    '''public void updateCurrentBalance(final double quantity)
    '''
def getPhysicalCount():
    '''public double getPhysicalCount()
    '''
def getCurrentBalance():
    '''public double getCurrentBalance()
    '''
def init():
    '''public void init()
    '''
def add():
    '''public void add()
    '''
def adjustPhysicalCount():
    '''public MboRemote adjustPhysicalCount(final double quantity, final Date pCountDate)
    '''
def adjustCurrentBalance():
    '''public MboRemote adjustCurrentBalance(final double newBalance)
    public MboRemote adjustCurrentBalance(final double newBalance, final String controlacc, final String shrinkageacc)
    '''
def reconcileBalances():
    '''public MboRemote reconcileBalances()
    '''
def canDelete():
    '''public void canDelete()
    '''
def setAutoCreateInvLot():
    '''public void setAutoCreateInvLot(final boolean flag)
    '''
def appValidate():
    '''public void appValidate()
    '''
def save():
    '''public void save()
    '''
def adjustLifoFifoCurrentBalance():
    '''public void adjustLifoFifoCurrentBalance(final double newBalance)
    '''
def createInvTrans():
    '''public MboRemote createInvTrans(final double quantity, final double unitcost, final boolean isreconcile)
    '''
def getNewBalanceForReconcile():
    '''public double getNewBalanceForReconcile()
    '''
def reconcileBalancesLifoFifo():
    '''public void reconcileBalancesLifoFifo(final String controlacc, final String shrinkageacc, final String remark)
    '''
def updateLifoFifoQtyAndCreateInvTrans():
    '''public void updateLifoFifoQtyAndCreateInvTrans(final boolean isreconcile)
    public void updateLifoFifoQtyAndCreateInvTrans(final HashMap<String, Vector<MboRemote>> condBalMap, final boolean isreconcile)
    public void updateLifoFifoQtyAndCreateInvTrans(final Vector<MboRemote> invBalanceVec, final String conditionCode, final boolean isreconcile)
    '''
def reconcileLifoFifoCurrentBalance():
    '''public void reconcileLifoFifoCurrentBalance(final double physcnt)
    '''
def checkWMATStatus():
    '''public boolean checkWMATStatus()
    '''
def previewReconcileBalances():
    '''public MboRemote previewReconcileBalances()
    '''
