MESSAGE_DELIVERED = "int  1"
MESSAGE_NOT_DELIVERED = "int  2"
MESSAGE_PARTIALLY_DELIVERED = "int  3"
def getType():
'''public int getType()
'''
pass
def dispatch():
'''public void dispatch(final Object listener)
'''
pass
def getInvalidAddresses():
'''public Address[] getInvalidAddresses()
'''
pass
def getValidSentAddresses():
'''public Address[] getValidSentAddresses()
'''
pass
def getValidUnsentAddresses():
'''public Address[] getValidUnsentAddresses()
'''
pass
def getMessage():
'''public Message getMessage()
'''
pass
def TransportEvent():
'''public TransportEvent(final Transport transport, final int type, final Address[] validSent, final Address[] validUnsent, final Address[] invalid, final Message msg)
'''
pass
