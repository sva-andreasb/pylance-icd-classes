def ():
    '''returns InvUseLineSet\n\n
    (final MboServerInterface ms)\n
    '''
def copyInvUseLineSet():
    '''returns None\n\n
    copyInvUseLineSet(final MboSetRemote matUseTransSet)\n
    '''
def sameMatUseTransFound():
    '''returns boolean\n\n
    sameMatUseTransFound(final MboRemote selectedIssue)\n
    '''
def copyInvReserveSet():
    '''returns None\n\n
    copyInvReserveSet(final MboSetRemote invReserveSet)\n
    '''
def addInvUseLineFromInvReserve():
    '''returns MboRemote\n\n
    addInvUseLineFromInvReserve(final MboRemote invRes)\n
    '''
def copySparePartSet():
    '''returns None\n\n
    copySparePartSet(final MboSetRemote sparePartSet)\n
    '''
def copyInvBalancesSet():
    '''returns None\n\n
    copyInvBalancesSet(final MboSetRemote invBalancesSet)\n
    '''
def addInvUseLineFromMatUseTrans():
    '''returns MboRemote\n\n
    addInvUseLineFromMatUseTrans(final MboRemote matUseTrans)\n
    '''
def getInvBalMap():
    '''returns MboRemote\n\n
    getInvBalMap(final String key)\n
    '''
def putInvBalMap():
    '''returns None\n\n
    putInvBalMap(final String key, final MboRemote invBalMbo)\n
    '''
def clearInvBalMap():
    '''returns None\n\n
    clearInvBalMap()\n
    '''
def clearinvBalQtyMap():
    '''returns None\n\n
    clearinvBalQtyMap()\n
    '''
def validateInvUseData():
    '''returns None\n\n
    validateInvUseData()\n
    '''
def canAdd():
    '''returns None\n\n
    canAdd()\n
    '''
def getQtyForReservationinSet():
    '''returns double\n\n
    getQtyForReservationinSet(final String requestnum, final long invuselineid)\n
    '''
def getPhyscntdateList():
    '''returns ArrayList<String>\n\n
    getPhyscntdateList()\n
    '''
def returnIPCParts():
    '''returns None\n\n
    returnIPCParts(final IpcSelectedPartsSetRemote partset)\n
    '''
def preValidateIpcBom():
    '''returns None\n\n
    preValidateIpcBom(final IpcBomSetRemote bomset)\n
    '''
def getInvReserveVector():
    '''returns Vector\n\n
    getInvReserveVector()\n
    '''
