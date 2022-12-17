def ():
    '''returns MRStatusHandler\n\n
    (final MR sm)\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(final String currentStatus, final String desiredStatus, final Date date, final String memo)\n
    '''
def canChangeStatus():
    '''returns None\n\n
    canChangeStatus(final String currentStatus, final String desiredStatus, final long accessModifier)\n
    '''
def canUnapprove():
    '''returns None\n\n
    canUnapprove(final String currentInternalStatus)\n
    '''
def canApprove():
    '''returns None\n\n
    canApprove(final String currentInternalStatus)\n
    '''
def canClose():
    '''returns None\n\n
    canClose(final String currentInternalStatus)\n
    '''
def canCancel():
    '''returns None\n\n
    canCancel(final String currentInternalStatus)\n
    '''
def checkStatusChangeAuthorization():
    '''returns None\n\n
    checkStatusChangeAuthorization(final String desiredExternalStatus)\n
    '''
def checkUserSecurity():
    '''returns None\n\n
    checkUserSecurity(final String desiredMaxStatus)\n
    '''
def updateMboForStatus():
    '''returns None\n\n
    updateMboForStatus(final String status)\n
    '''
def canAddInvReserve():
    '''returns boolean\n\n
    canAddInvReserve(final MboRemote mrlineMbo)\n
    '''
