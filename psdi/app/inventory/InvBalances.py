def InvBalances():
'''public InvBalances(final MboSet ms)
'''
pass
def updateCurrentBalance():
'''public void updateCurrentBalance(final double quantity)
'''
pass
def getPhysicalCount():
'''public double getPhysicalCount()
'''
pass
def getCurrentBalance():
'''public double getCurrentBalance()
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
def adjustPhysicalCount():
'''public MboRemote adjustPhysicalCount(final double quantity, final Date pCountDate)
'''
pass
def adjustCurrentBalance():
'''public MboRemote adjustCurrentBalance(final double newBalance)
public MboRemote adjustCurrentBalance(final double newBalance, final String controlacc, final String shrinkageacc)
'''
pass
def reconcileBalances():
'''public MboRemote reconcileBalances()
'''
pass
def canDelete():
'''public void canDelete()
'''
pass
def setAutoCreateInvLot():
'''public void setAutoCreateInvLot(final boolean flag)
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
def adjustLifoFifoCurrentBalance():
'''public void adjustLifoFifoCurrentBalance(final double newBalance)
'''
pass
def createInvTrans():
'''public MboRemote createInvTrans(final double quantity, final double unitcost, final boolean isreconcile)
'''
pass
def getNewBalanceForReconcile():
'''public double getNewBalanceForReconcile()
'''
pass
def reconcileBalancesLifoFifo():
'''public void reconcileBalancesLifoFifo(final String controlacc, final String shrinkageacc, final String remark)
'''
pass
def updateLifoFifoQtyAndCreateInvTrans():
'''public void updateLifoFifoQtyAndCreateInvTrans(final boolean isreconcile)
public void updateLifoFifoQtyAndCreateInvTrans(final HashMap<String, Vector<MboRemote>> condBalMap, final boolean isreconcile)
public void updateLifoFifoQtyAndCreateInvTrans(final Vector<MboRemote> invBalanceVec, final String conditionCode, final boolean isreconcile)
'''
pass
def reconcileLifoFifoCurrentBalance():
'''public void reconcileLifoFifoCurrentBalance(final double physcnt)
'''
pass
def checkWMATStatus():
'''public boolean checkWMATStatus()
'''
pass
def previewReconcileBalances():
'''public MboRemote previewReconcileBalances()
'''
pass
