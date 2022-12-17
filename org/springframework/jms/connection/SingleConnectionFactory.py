def ():
    '''returns SingleConnectionFactory\n\n
    ()\n
    (final Connection target)\n
    (final ConnectionFactory targetConnectionFactory)\n
    '''
def setTargetConnectionFactory():
    '''returns None\n\n
    setTargetConnectionFactory(final ConnectionFactory targetConnectionFactory)\n
    '''
def getTargetConnectionFactory():
    '''returns ConnectionFactory\n\n
    getTargetConnectionFactory()\n
    '''
def afterPropertiesSet():
    '''returns None\n\n
    afterPropertiesSet()\n
    '''
def destroy():
    '''returns None\n\n
    destroy()\n
    '''
def createConnection():
    '''returns Connection\n\n
    createConnection()\n
    createConnection(final String username, final String password)\n
    '''
def createQueueConnection():
    '''returns QueueConnection\n\n
    createQueueConnection()\n
    createQueueConnection(final String username, final String password)\n
    '''
def createTopicConnection():
    '''returns TopicConnection\n\n
    createTopicConnection()\n
    createTopicConnection(final String username, final String password)\n
    '''
def invoke():
    '''returns Object\n\n
    invoke(final Object proxy, final Method method, final Object[] args)\n
    '''
