def ():
    '''returns JMSTopicSubscriber\n\n
    (final String destinationName, final String conFactoryName, final String selector, final int txMode, final String subscriptionName, final Properties env)\n
    (final String destinationName, final String selector, final Session session, final String subscriptionName, final Properties env)\n
    (final String destinationName, final String conFactoryName, final String selector, final int txMode, final Properties env)\n
    (final String destinationName, final String selector, final Session session, final Properties env)\n
    (final String destinationName, final String conFactoryName, final String selector, final int txMode, final String subscriptionName, final Properties env, final String providerUserName, final String providerPassword)\n
    '''
def unsubscribe():
    '''returns None\n\n
    unsubscribe()\n
    '''
def createClientInSession():
    '''returns JMSClient\n\n
    createClientInSession()\n
    '''
