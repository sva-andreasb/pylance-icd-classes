def ():
    '''returns POStatusHandler\n\n
    (final StatefulMbo sm)\n
    '''
def canChangeStatus():
    '''returns None\n\n
    canChangeStatus(final String currentStatus, final String desiredStatus, final long accessModifier)\n
    '''
def checkStatusChangeAuthorization():
    '''returns None\n\n
    checkStatusChangeAuthorization(final String desiredExternalStatus)\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(final String currentStatus, final String desiredStatus, final Date date, final String memo)\n
    '''
def approve():
    '''returns None\n\n
    approve(final Date date)\n
    '''
def updateMboForStatus():
    '''returns None\n\n
    updateMboForStatus(final String status)\n
    '''
def revise():
    '''returns None\n\n
    revise()\n
    '''
def hold():
    '''returns None\n\n
    hold()\n
    '''
def pndrev():
    '''returns None\n\n
    pndrev()\n
    '''
def canPndRev():
    '''returns None\n\n
    canPndRev(final String currentMaxStatus)\n
    '''
def canRevise():
    '''returns None\n\n
    canRevise(final String currentMaxStatus)\n
    '''
def canHold():
    '''returns None\n\n
    canHold(final String currentMaxStatus)\n
    '''
def isPOFromPR():
    '''returns boolean\n\n
    isPOFromPR()\n
    '''
def isPOFromRFQ():
    '''returns boolean\n\n
    isPOFromRFQ()\n
    '''
def updatePRPRLine():
    '''returns None\n\n
    updatePRPRLine()\n
    '''
def updateRFQRFQLine():
    '''returns None\n\n
    updateRFQRFQLine()\n
    '''
def checkPndRevLines():
    '''returns None\n\n
    checkPndRevLines(final MboRemote poRemote, final MboSetRemote poLines)\n
    '''
def updatePndRevLines():
    '''returns None\n\n
    updatePndRevLines(final MboRemote poRemote, final MboSetRemote poLines)\n
    '''
def samePOlineOnTwoVersions():
    '''returns boolean\n\n
    samePOlineOnTwoVersions(final MboRemote prLineRemote)\n
    '''
