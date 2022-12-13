def JMSProducer():
    '''    public JMSProducer(final String destinationName, final String conFactoryName, final int txMode, final Properties env, final String providerUserName, final String providerPassword)
    public JMSProducer(final String destinationName, final String conFactoryName, final int txMode, final Properties env)
    public JMSProducer(final String destinationName, final Session session, final Properties env)
    '''
def addMessage():
    '''    public void addMessage(final JMSData data)
    '''
def sendMessage():
    '''    public void sendMessage(final boolean autocommit)
    public void sendMessage(final List<JMSData> listData, final boolean autocommit)
    public void sendMessage(final JMSData data, final boolean autocommit)
    '''
def close():
    '''    public void close()
    '''
def createClientInSession():
    '''    public JMSClient createClientInSession()
    public JMSClient createClientInSession(final String destinationName, final Properties env)
    '''
def createJMSConsumerInSession():
    '''    public JMSConsumer createJMSConsumerInSession(final String selector)
    '''
