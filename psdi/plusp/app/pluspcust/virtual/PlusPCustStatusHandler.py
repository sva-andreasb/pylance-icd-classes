CUSTOMER_STATUS_LIST = "String  \"PLUSPCUSTSTATUS\""
def ():
    '''returns PlusPCustStatusHandler\n\n
    (final StatefulMbo statefulMbo)\n
    '''
def checkStatusChangeAuthorization():
    '''returns None\n\n
    checkStatusChangeAuthorization(final String s)\n
    '''
def toInternalStatus():
    '''returns String\n\n
    toInternalStatus(final String value)\n
    '''
def possibleStatusChange():
    '''returns None\n\n
    possibleStatusChange(final String s, final String s2)\n
    '''
def verifyCustomerAssociation():
    '''returns boolean\n\n
    verifyCustomerAssociation(final DBShortcut dbShortcut, final SqlFormat sqlFormat)\n
    '''
def canChangeCustomerStatus():
    '''returns None\n\n
    canChangeCustomerStatus(final String currentStatus, final String desiredStatus, final long accessModifier)\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(final String currentStatus, final String s, final Date date, final String memo)\n
    '''
