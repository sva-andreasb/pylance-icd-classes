def ():
    '''returns IMSessionXMPPImpl\n\n
    ()\n
    '''
def configure():
    '''returns None\n\n
    configure(final Properties properties)\n
    '''
def getServerHostName():
    '''returns String\n\n
    getServerHostName()\n
    '''
def getServerPort():
    '''returns int\n\n
    getServerPort()\n
    '''
def getServiceName():
    '''returns String\n\n
    getServiceName()\n
    '''
def getSessionName():
    '''returns String\n\n
    getSessionName()\n
    '''
def getUserId():
    '''returns String\n\n
    getUserId()\n
    '''
def getUserPassword():
    '''returns String\n\n
    getUserPassword()\n
    '''
def getIMUser():
    '''returns IMUser\n\n
    getIMUser()\n
    '''
def open():
    '''returns None\n\n
    open()\n
    '''
def changeUserStatus():
    '''returns None\n\n
    changeUserStatus(final IMUser.IMUserStatus imUserStatus)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def isOpened():
    '''returns boolean\n\n
    isOpened()\n
    '''
def createResolveHandler():
    '''returns IMResolveHandler\n\n
    createResolveHandler(final boolean b, final boolean b2)\n
    '''
def createUserStatusHandler():
    '''returns IMUserStatusHandler\n\n
    createUserStatusHandler()\n
    '''
def createMessageHandler():
    '''returns IMMessageHandler\n\n
    createMessageHandler(final IMUser imUser)\n
    '''
def resolve():
    '''returns IMUser\n\n
    resolve(final String s, final boolean b, final boolean b2)\n
    resolve(final String s)\n
    '''
def getDefaultConnectionTimeout():
    '''returns long\n\n
    getDefaultConnectionTimeout()\n
    '''
def setConnectionTimeout():
    '''returns None\n\n
    setConnectionTimeout(final long connectionTimeout)\n
    '''
def getConnectionTimeout():
    '''returns long\n\n
    getConnectionTimeout()\n
    '''
def getDefaultResolveTimeout():
    '''returns long\n\n
    getDefaultResolveTimeout()\n
    '''
def registerIMSingleListener():
    '''returns None\n\n
    registerIMSingleListener(final IMSingleListener imSingleListener)\n
    '''
def removeIMSingleListener():
    '''returns None\n\n
    removeIMSingleListener(final IMSingleListener imSingleListener)\n
    '''
def removeMessageHandlerList():
    '''returns None\n\n
    removeMessageHandlerList(final String anObject)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
