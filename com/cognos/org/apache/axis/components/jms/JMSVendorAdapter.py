SEND_ACTION = "int  0"
CONNECT_ACTION = "int  1"
SUBSCRIBE_ACTION = "int  2"
RECEIVE_ACTION = "int  3"
ON_EXCEPTION_ACTION = "int  4"
def getVendorId():
    '''returns String\n\n
    getVendorId()\n
    '''
def getJMSConnectorProperties():
    '''returns HashMap\n\n
    getJMSConnectorProperties(final JMSURLHelper jmsurl)\n
    '''
def getJMSConnectionFactoryProperties():
    '''returns HashMap\n\n
    getJMSConnectionFactoryProperties(final JMSURLHelper jmsurl)\n
    '''
def getQueue():
    '''returns Queue\n\n
    getQueue(final QueueSession session, final String name)\n
    '''
def getTopic():
    '''returns Topic\n\n
    getTopic(final TopicSession session, final String name)\n
    '''
def isRecoverable():
    '''returns boolean\n\n
    isRecoverable(final Throwable thrown, final int action)\n
    '''
def setProperties():
    '''returns None\n\n
    setProperties(final Message message, final HashMap props)\n
    '''
def setupMessageContext():
    '''returns None\n\n
    setupMessageContext(final MessageContext context, final Call call, final JMSURLHelper jmsurl)\n
    '''
def setupApplicationProperties():
    '''returns None\n\n
    setupApplicationProperties(final MessageContext context, final Call call, final JMSURLHelper jmsurl)\n
    '''
