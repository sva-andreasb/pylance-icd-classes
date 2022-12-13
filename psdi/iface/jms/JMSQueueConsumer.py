def JMSQueueConsumer():
'''public JMSQueueConsumer(final String destinationName, final String conFactoryName, final String selector, final int txMode, final Properties env)
public JMSQueueConsumer(final String destinationName, final String selector, final Session session, final Properties env)
public JMSQueueConsumer(final String destinationName, final String conFactoryName, final String selector, final int txMode, final Properties env, final String providerUserName, final String providerPassword)
public JMSQueueConsumer(final String destinationName, final String conFactoryName, final String selector, final int txMode, final int receiveMode, final long waitTimeOut, final Properties env)
public JMSQueueConsumer(final String destinationName, final String conFactoryName, final String selector, final int txMode, final int receiveMode, final long waitTimeOut, final Properties env, final String providerUserName, final String providerPassword)
'''
pass
def deleteMessage():
'''public Map<String, String> deleteMessage()
public String deleteMessage(final boolean autocommit)
'''
pass
def deleteAllMessages():
'''public int deleteAllMessages()
'''
pass
def createClientInSession():
'''public JMSClient createClientInSession()
'''
pass
