def ():
    '''returns StatusHandler\n\n
    (final StatefulMbo sm)\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(final String currentStatus, final String desiredStatus, final Date date, final String memo)\n
    '''
def canChangeStatus():
    '''returns None\n\n
    canChangeStatus(final String currentStatus, final String desiredStatus, final long accessModifier)\n
    '''
def updateMboForStatus():
    '''returns None\n\n
    updateMboForStatus(final String status)\n
    '''
def preStatusChange():
    '''returns None\n\n
    preStatusChange(final String currentStatus, final String status, final Date asOfDate, final String memo)\n
    '''
def postStatusChange():
    '''returns None\n\n
    postStatusChange(final String currentStatus, final String status, final Date asOfDate, final String memo)\n
    '''
