def StatusHandler():
    '''public StatusHandler(final StatefulMbo sm)
    '''
def changeStatus():
    '''public void changeStatus(final String currentStatus, final String desiredStatus, final Date date, final String memo)
    '''
def canChangeStatus():
    '''public void canChangeStatus(final String currentStatus, final String desiredStatus, final long accessModifier)
    '''
def updateMboForStatus():
    '''public void updateMboForStatus(final String status)
    '''
def preStatusChange():
    '''public void preStatusChange(final String currentStatus, final String status, final Date asOfDate, final String memo)
    '''
def postStatusChange():
    '''public void postStatusChange(final String currentStatus, final String status, final Date asOfDate, final String memo)
    '''
