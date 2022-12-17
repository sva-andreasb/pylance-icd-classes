def ():
    '''returns PingJMSQueueResourceHandler\n\n
    (final BusResourceInfo resInfo, final String contextURI)\n
    '''
def handleRequest():
    '''returns BusResource\n\n
    handleRequest(final ResourceContext resCtx, final BusRequest request)\n
    '''
def browseMessages():
    '''returns BusResourceCollection\n\n
    browseMessages(final String queueURI, final String queueName, final BusRequest request)\n
    '''
def testConnection():
    '''returns BusResource\n\n
    testConnection(final String queueURI, final String queueName)\n
    '''
def testReadMessage():
    '''returns BusResource\n\n
    testReadMessage(final String queueURI, final String queueName)\n
    '''
def testWriteMessage():
    '''returns BusResource\n\n
    testWriteMessage(final String queueURI, final String queueName)\n
    '''
