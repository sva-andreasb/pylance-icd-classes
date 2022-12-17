RECEIVEMODE_NOWAIT = "int  1"
RECEIVEMODE_WAIT = "int  2"
def ():
    '''returns JMSConsumer\n\n
    (final String destinationName, final String conFactoryName, final String selector, final int txMode, final Properties env)\n
    (final String destinationName, final String conFactoryName, final String selector, final int txMode, final Properties env, final String providerUserName, final String providerPassword)\n
    (final String destinationName, final String conFactoryName, final String selector, final int txMode, final int receiveMode, final long waitTimeOut, final Properties env)\n
    (final String destinationName, final String conFactoryName, final String selector, final int txMode, final int receiveMode, final long waitTimeOut, final Properties env, final String providerUserName, final String providerPassword)\n
    (final String destinationName, final String conFactoryName, final String selector, final int txMode, final String subscriptionName, final Properties env, final String providerUserName, final String providerPassword)\n
    (final String destinationName, final String conFactoryName, final String selector, final int txMode, final String subscriptionName, final Properties env)\n
    (final String destinationName, final String selector, final Session session, final Properties env)\n
    (final String destinationName, final String selector, final Session session, final String subscriptionName, final Properties env)\n
    '''
def getMessage():
    '''returns JMSData\n\n
    getMessage(final boolean autocommit)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def createClientInSession():
    '''returns JMSClient\n\n
    createClientInSession()\n
    createClientInSession(final String destinationName, final Properties env)\n
    '''
def createJMSProducerInSession():
    '''returns JMSProducer\n\n
    createJMSProducerInSession()\n
    '''
