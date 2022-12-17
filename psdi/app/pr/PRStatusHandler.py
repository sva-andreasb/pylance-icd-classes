def ():
    '''returns PRStatusHandler\n\n
    (final StatefulMbo sm)\n
    '''
def checkStatusChangeAuthorization():
    '''returns None\n\n
    checkStatusChangeAuthorization(final String desiredExternalStatus)\n
    '''
def canChangeStatus():
    '''returns None\n\n
    canChangeStatus(final String currentStatus, final String desiredStatus, final long accessModifier)\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(final String currentStatus, final String desiredStatus, final Date date, final String memo)\n
    '''
def updateMboForStatus():
    '''returns None\n\n
    updateMboForStatus(final String status)\n
    '''
def deletePRReferencesFromWO():
    '''returns None\n\n
    deletePRReferencesFromWO()\n
    '''
def postStatusChange():
    '''returns None\n\n
    postStatusChange(final String currentStatus, final String status, final Date asOfDate, final String memo)\n
    '''
