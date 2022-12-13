def JMSQueueBrowser():
    '''public JMSQueueBrowser(final String destinationName, final String conFactoryName, final String selector, final Properties env)
    public JMSQueueBrowser(final String destinationName, final String conFactoryName, final String selector, final Properties env, final String providerUserName, final String providerPassword)
    public JMSQueueBrowser(final String destinationName, final String selector, final Session session, final Properties env)
    '''
def close():
    '''public void close()
    '''
def waitTillMessageInQueue():
    '''public void waitTillMessageInQueue(final long sleepFrequency)
    '''
def isMessageInQueue():
    '''public boolean isMessageInQueue()
    '''
def getAllMessages():
    '''public List<JMSData> getAllMessages()
    '''
def getMessages():
    '''public List<JMSData> getMessages(final int n)
    '''
def createClientInSession():
    '''public JMSClient createClientInSession()
    public JMSClient createClientInSession(final String destinationName, final Properties env)
    '''
