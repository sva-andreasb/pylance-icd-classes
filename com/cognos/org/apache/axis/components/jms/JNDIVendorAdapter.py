CONTEXT_FACTORY = "String  \"java.naming.factory.initial\""
PROVIDER_URL = "String  \"java.naming.provider.url\""
_CONNECTION_FACTORY_JNDI_NAME = "String  \"ConnectionFactoryJNDIName\""
CONNECTION_FACTORY_JNDI_NAME = "String  \"transport.jms.ConnectionFactoryJNDIName\""
def getQueueConnectionFactory():
    '''returns QueueConnectionFactory\n\n
    getQueueConnectionFactory(final HashMap cfConfig)\n
    '''
def getTopicConnectionFactory():
    '''returns TopicConnectionFactory\n\n
    getTopicConnectionFactory(final HashMap cfConfig)\n
    '''
def addVendorConnectionFactoryProperties():
    '''returns None\n\n
    addVendorConnectionFactoryProperties(final JMSURLHelper jmsurl, final HashMap cfConfig)\n
    '''
def isMatchingConnectionFactory():
    '''returns boolean\n\n
    isMatchingConnectionFactory(final ConnectionFactory cf, final JMSURLHelper originalJMSURL, final HashMap cfProps)\n
    '''
def getQueue():
    '''returns Queue\n\n
    getQueue(final QueueSession session, final String name)\n
    '''
def getTopic():
    '''returns Topic\n\n
    getTopic(final TopicSession session, final String name)\n
    '''
