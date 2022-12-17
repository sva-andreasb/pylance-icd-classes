def ():
    '''returns JMSQueueConsumer\n\n
    (final String destinationName, final String conFactoryName, final String selector, final int txMode, final Properties env)\n
    (final String destinationName, final String selector, final Session session, final Properties env)\n
    (final String destinationName, final String conFactoryName, final String selector, final int txMode, final Properties env, final String providerUserName, final String providerPassword)\n
    (final String destinationName, final String conFactoryName, final String selector, final int txMode, final int receiveMode, final long waitTimeOut, final Properties env)\n
    (final String destinationName, final String conFactoryName, final String selector, final int txMode, final int receiveMode, final long waitTimeOut, final Properties env, final String providerUserName, final String providerPassword)\n
    '''
def deleteMessage():
    '''returns String\n\n
    deleteMessage(final boolean autocommit)\n
    '''
def deleteAllMessages():
    '''returns int\n\n
    deleteAllMessages()\n
    '''
def createClientInSession():
    '''returns JMSClient\n\n
    createClientInSession()\n
    '''
