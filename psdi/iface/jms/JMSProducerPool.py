def closeAll():
    '''public static void closeAll()
    '''
def getInstance():
    '''public static JMSProducerPool getInstance(final String connectionFactoryName, final Properties env)
    '''
def getJMSProducer():
    '''public synchronized JMSProducer getJMSProducer(final String destinationName)
    public synchronized JMSProducer getJMSProducer(final String destinationName, final String providerUser, final String providerPassword)
    '''
def freeJMSProducer():
    '''public synchronized void freeJMSProducer(final JMSProducer producer)
    '''
