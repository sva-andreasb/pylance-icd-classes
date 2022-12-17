def ():
    '''returns JMSProducer\n\n
    (final String destinationName, final String conFactoryName, final int txMode, final Properties env, final String providerUserName, final String providerPassword)\n
    (final String destinationName, final String conFactoryName, final int txMode, final Properties env)\n
    (final String destinationName, final Session session, final Properties env)\n
    '''
def addMessage():
    '''returns None\n\n
    addMessage(final JMSData data)\n
    '''
def sendMessage():
    '''returns None\n\n
    sendMessage(final boolean autocommit)\n
    sendMessage(final List<JMSData> listData, final boolean autocommit)\n
    sendMessage(final JMSData data, final boolean autocommit)\n
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
def createJMSConsumerInSession():
    '''returns JMSConsumer\n\n
    createJMSConsumerInSession(final String selector)\n
    '''
