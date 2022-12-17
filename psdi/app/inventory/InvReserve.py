def ():
    '''returns InvReserve\n\n
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
def appValidate():
    '''returns None\n\n
    appValidate()\n
    '''
def save():
    '''returns None\n\n
    save()\n
    '''
def incrActualQty():
    '''returns None\n\n
    incrActualQty(final double incrValue)\n
    '''
def copy():
    '''returns MboRemote\n\n
    copy()\n
    copy(final MboSetRemote mboset)\n
    '''
def issue():
    '''returns MboRemote\n\n
    issue(MboSetRemote newIssueSet, final String bin, final String lot, final String rotasset, final double qty)\n
    '''
def canDelete():
    '''returns None\n\n
    canDelete()\n
    '''
def smartFindByObjectName():
    '''returns MboSetRemote\n\n
    smartFindByObjectName(final String sourceObj, final String targetAttrName, final String value, final boolean exact)\n
    '''
def delete():
    '''returns None\n\n
    delete(final long accessModifier)\n
    '''
def deleteInvUseLines():
    '''returns None\n\n
    deleteInvUseLines()\n
    '''
def undelete():
    '''returns None\n\n
    undelete()\n
    '''
def isHardReservation():
    '''returns boolean\n\n
    isHardReservation()\n
    '''
def isBackOrdered():
    '''returns boolean\n\n
    isBackOrdered()\n
    '''
def setInvResType():
    '''returns None\n\n
    setInvResType(final String displayResType)\n
    setInvResType(final String displayResType, final int resbuffer)\n
    setInvResType(final String displayResType, final boolean disallowNegAvailBal)\n
    setInvResType(final String displayResType, final int resbuffer, final boolean disallowNegAvailBal)\n
    '''
def checkWMATStatus():
    '''returns boolean\n\n
    checkWMATStatus(final String itemnum, final String location, final String itemsetid, final String siteid)\n
    '''
def setMRUpdated():
    '''returns None\n\n
    setMRUpdated()\n
    '''
def setInvReserveValQtyFlag():
    '''returns None\n\n
    setInvReserveValQtyFlag()\n
    '''
def getInvReserveValQtyFlag():
    '''returns boolean\n\n
    getInvReserveValQtyFlag()\n
    '''
