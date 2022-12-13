CONTEXT_FACTORY = "String  java.naming.factory.initial""
PROVIDER_URL = "String  java.naming.provider.url""
_CONNECTION_FACTORY_JNDI_NAME = "String  ConnectionFactoryJNDIName""
CONNECTION_FACTORY_JNDI_NAME = "String  transport.jms.ConnectionFactoryJNDIName""
def getQueueConnectionFactory():
'''public QueueConnectionFactory getQueueConnectionFactory(final HashMap cfConfig)
'''
pass
def getTopicConnectionFactory():
'''public TopicConnectionFactory getTopicConnectionFactory(final HashMap cfConfig)
'''
pass
def addVendorConnectionFactoryProperties():
'''public void addVendorConnectionFactoryProperties(final JMSURLHelper jmsurl, final HashMap cfConfig)
'''
pass
def isMatchingConnectionFactory():
'''public boolean isMatchingConnectionFactory(final ConnectionFactory cf, final JMSURLHelper originalJMSURL, final HashMap cfProps)
'''
pass
def getQueue():
'''public Queue getQueue(final QueueSession session, final String name)
'''
pass
def getTopic():
'''public Topic getTopic(final TopicSession session, final String name)
'''
pass
