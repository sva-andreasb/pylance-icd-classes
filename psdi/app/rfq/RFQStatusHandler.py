def ():
    '''returns RFQStatusHandler\n\n
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
    changeStatus(final String currentStatus, final String desiredStatus, Date asOfDate, final String memo)\n
    '''
def checkChargeValues():
    '''returns None\n\n
    checkChargeValues()\n
    '''
