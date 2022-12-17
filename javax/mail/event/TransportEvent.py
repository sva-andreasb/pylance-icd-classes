MESSAGE_DELIVERED = "int  1"
MESSAGE_NOT_DELIVERED = "int  2"
MESSAGE_PARTIALLY_DELIVERED = "int  3"
def getType():
    '''returns int\n\n
    getType()\n
    '''
def dispatch():
    '''returns None\n\n
    dispatch(final Object listener)\n
    '''
def getInvalidAddresses():
    '''returns Address[]\n\n
    getInvalidAddresses()\n
    '''
def getValidSentAddresses():
    '''returns Address[]\n\n
    getValidSentAddresses()\n
    '''
def getValidUnsentAddresses():
    '''returns Address[]\n\n
    getValidUnsentAddresses()\n
    '''
def getMessage():
    '''returns Message\n\n
    getMessage()\n
    '''
def ():
    '''returns TransportEvent\n\n
    (final Transport transport, final int type, final Address[] validSent, final Address[] validUnsent, final Address[] invalid, final Message msg)\n
    '''
