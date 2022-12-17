def ():
    '''returns InvUseService\n\n
    ()\n
    (final MXServer mxServer)\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(@WSMboKey("INVUSE") final InvUseRemote invuse, final String status, final Date date, final String memo)\n
    '''
def createShipmentReceipt():
    '''returns MboRemote\n\n
    createShipmentReceipt(final UserInfo userInfo, final MboSetRemote receiptSet, final String shipmentnum, final long shipmentlinenum, final String ownersysid, final String siteid)\n
    '''
def createShipmentReturn():
    '''returns MboRemote\n\n
    createShipmentReturn(final UserInfo userInfo, final MboSetRemote receiptSet, final String shipmentnum, final long shipmentlinenum, final String ownersysid, final String siteid)\n
    '''
