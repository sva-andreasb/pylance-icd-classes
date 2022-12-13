def JMSQueueBrowser():
'''public JMSQueueBrowser(final String destinationName, final String conFactoryName, final String selector, final Properties env)
public JMSQueueBrowser(final String destinationName, final String conFactoryName, final String selector, final Properties env, final String providerUserName, final String providerPassword)
public JMSQueueBrowser(final String destinationName, final String selector, final Session session, final Properties env)
'''
pass
def close():
'''public void close()
'''
pass
def waitTillMessageInQueue():
'''public void waitTillMessageInQueue(final long sleepFrequency)
'''
pass
def isMessageInQueue():
'''public boolean isMessageInQueue()
'''
pass
def getAllMessages():
'''public List<JMSData> getAllMessages()
'''
pass
def getMessages():
'''public List<JMSData> getMessages(final int n)
'''
pass
def createClientInSession():
'''public JMSClient createClientInSession()
public JMSClient createClientInSession(final String destinationName, final Properties env)
'''
pass
