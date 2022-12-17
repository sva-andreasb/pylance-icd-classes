def ():
    '''returns JMSQueueBrowser\n\n
    (final String destinationName, final String conFactoryName, final String selector, final Properties env)\n
    (final String destinationName, final String conFactoryName, final String selector, final Properties env, final String providerUserName, final String providerPassword)\n
    (final String destinationName, final String selector, final Session session, final Properties env)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def waitTillMessageInQueue():
    '''returns None\n\n
    waitTillMessageInQueue(final long sleepFrequency)\n
    '''
def isMessageInQueue():
    '''returns boolean\n\n
    isMessageInQueue()\n
    '''
def getAllMessages():
    '''returns List<JMSData>\n\n
    getAllMessages()\n
    '''
def getMessages():
    '''returns List<JMSData>\n\n
    getMessages(final int n)\n
    '''
def createClientInSession():
    '''returns JMSClient\n\n
    createClientInSession()\n
    createClientInSession(final String destinationName, final Properties env)\n
    '''
