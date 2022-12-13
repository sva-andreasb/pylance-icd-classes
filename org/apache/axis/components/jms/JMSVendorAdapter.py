SEND_ACTION = "int  0"
CONNECT_ACTION = "int  1"
SUBSCRIBE_ACTION = "int  2"
RECEIVE_ACTION = "int  3"
ON_EXCEPTION_ACTION = "int  4"
def getVendorId():
    '''public String getVendorId()
    '''
def getJMSConnectorProperties():
    '''public HashMap getJMSConnectorProperties(final JMSURLHelper jmsurl)
    '''
def getJMSConnectionFactoryProperties():
    '''public HashMap getJMSConnectionFactoryProperties(final JMSURLHelper jmsurl)
    '''
def getQueue():
    '''public Queue getQueue(final QueueSession session, final String name)
    '''
def getTopic():
    '''public Topic getTopic(final TopicSession session, final String name)
    '''
def isRecoverable():
    '''public boolean isRecoverable(final Throwable thrown, final int action)
    '''
def setProperties():
    '''public void setProperties(final Message message, final HashMap props)
    '''
def setupMessageContext():
    '''public void setupMessageContext(final MessageContext context, final Call call, final JMSURLHelper jmsurl)
    '''
def setupApplicationProperties():
    '''public void setupApplicationProperties(final MessageContext context, final Call call, final JMSURLHelper jmsurl)
    '''
