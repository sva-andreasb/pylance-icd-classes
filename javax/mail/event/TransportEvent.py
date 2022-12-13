MESSAGE_DELIVERED = "int  1"
MESSAGE_NOT_DELIVERED = "int  2"
MESSAGE_PARTIALLY_DELIVERED = "int  3"
def getType():
    '''    public int getType()
    '''
def dispatch():
    '''    public void dispatch(final Object listener)
    '''
def getInvalidAddresses():
    '''    public Address[] getInvalidAddresses()
    '''
def getValidSentAddresses():
    '''    public Address[] getValidSentAddresses()
    '''
def getValidUnsentAddresses():
    '''    public Address[] getValidUnsentAddresses()
    '''
def getMessage():
    '''    public Message getMessage()
    '''
def TransportEvent():
    '''    public TransportEvent(final Transport transport, final int type, final Address[] validSent, final Address[] validUnsent, final Address[] invalid, final Message msg)
    '''
