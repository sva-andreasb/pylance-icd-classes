RECEIVEMODE_NOWAIT = "int  1"
RECEIVEMODE_WAIT = "int  2"
def JMSConsumer():
    '''public JMSConsumer(final String destinationName, final String conFactoryName, final String selector, final int txMode, final Properties env)
    public JMSConsumer(final String destinationName, final String conFactoryName, final String selector, final int txMode, final Properties env, final String providerUserName, final String providerPassword)
    public JMSConsumer(final String destinationName, final String conFactoryName, final String selector, final int txMode, final int receiveMode, final long waitTimeOut, final Properties env)
    public JMSConsumer(final String destinationName, final String conFactoryName, final String selector, final int txMode, final int receiveMode, final long waitTimeOut, final Properties env, final String providerUserName, final String providerPassword)
    public JMSConsumer(final String destinationName, final String conFactoryName, final String selector, final int txMode, final String subscriptionName, final Properties env, final String providerUserName, final String providerPassword)
    public JMSConsumer(final String destinationName, final String conFactoryName, final String selector, final int txMode, final String subscriptionName, final Properties env)
    public JMSConsumer(final String destinationName, final String selector, final Session session, final Properties env)
    public JMSConsumer(final String destinationName, final String selector, final Session session, final String subscriptionName, final Properties env)
    '''
def getMessage():
    '''public JMSData getMessage(final boolean autocommit)
    '''
def close():
    '''public void close()
    '''
def createClientInSession():
    '''public JMSClient createClientInSession()
    public JMSClient createClientInSession(final String destinationName, final Properties env)
    '''
def createJMSProducerInSession():
    '''public JMSProducer createJMSProducerInSession()
    '''
