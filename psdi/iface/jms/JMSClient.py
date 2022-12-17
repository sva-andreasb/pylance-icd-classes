NO_TX = "int  0"
SESSION_TX = "int  1"
QUEUE = "String  \"javax.jms.Queue\""
TOPIC = "String  \"javax.jms.Topic\""
JMS_LOGGER = "String  \"maximo.jms\""
def getProviderUserName():
    '''returns String\n\n
    getProviderUserName()\n
    '''
def getProviderPassword():
    '''returns String\n\n
    getProviderPassword()\n
    '''
def getSession():
    '''returns Session\n\n
    getSession()\n
    '''
def getEnvironment():
    '''returns Properties\n\n
    getEnvironment()\n
    '''
def getDestinationName():
    '''returns String\n\n
    getDestinationName()\n
    '''
def isValid():
    '''returns boolean\n\n
    isValid()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def rollbackTx():
    '''returns None\n\n
    rollbackTx()\n
    '''
def commitTx():
    '''returns None\n\n
    commitTx()\n
    '''
