def JMSProducer():
'''public JMSProducer(final String destinationName, final String conFactoryName, final int txMode, final Properties env, final String providerUserName, final String providerPassword)
public JMSProducer(final String destinationName, final String conFactoryName, final int txMode, final Properties env)
public JMSProducer(final String destinationName, final Session session, final Properties env)
'''
pass
def addMessage():
'''public void addMessage(final JMSData data)
'''
pass
def sendMessage():
'''public void sendMessage(final boolean autocommit)
public void sendMessage(final List<JMSData> listData, final boolean autocommit)
public void sendMessage(final JMSData data, final boolean autocommit)
'''
pass
def close():
'''public void close()
'''
pass
def createClientInSession():
'''public JMSClient createClientInSession()
public JMSClient createClientInSession(final String destinationName, final Properties env)
'''
pass
def createJMSConsumerInSession():
'''public JMSConsumer createJMSConsumerInSession(final String selector)
'''
pass
