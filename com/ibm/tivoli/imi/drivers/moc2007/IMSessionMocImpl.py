def ():
    '''returns IMSessionMocImpl\n\n
    ()\n
    '''
def getListenedUsers():
    '''returns List<String>\n\n
    getListenedUsers()\n
    '''
def setListenedUsers():
    '''returns None\n\n
    setListenedUsers(final List<String> listenedUsers)\n
    '''
def getReceiveMessage():
    '''returns ReceiveMessage\n\n
    getReceiveMessage()\n
    '''
def setReceiveMessage():
    '''returns None\n\n
    setReceiveMessage(final ReceiveMessage receiveMessage)\n
    '''
def getRid():
    '''returns int\n\n
    getRid()\n
    '''
def setRid():
    '''returns None\n\n
    setRid(final int rid)\n
    '''
def getTicket():
    '''returns String\n\n
    getTicket()\n
    '''
def setTicket():
    '''returns None\n\n
    setTicket(final String ticket)\n
    '''
def getSid():
    '''returns String\n\n
    getSid()\n
    '''
def setSid():
    '''returns None\n\n
    setSid(final String sid)\n
    '''
def changeUserStatus():
    '''returns None\n\n
    changeUserStatus(final IMUser.IMUserStatus newStatus)\n
    '''
def open():
    '''returns None\n\n
    open()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def removeMessageHandlerList():
    '''returns None\n\n
    removeMessageHandlerList(final String anObject)\n
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
def createMessageHandler():
    '''returns IMMessageHandler\n\n
    createMessageHandler(final IMUser imUser)\n
    '''
def createResolveHandler():
    '''returns IMResolveHandler\n\n
    createResolveHandler(final boolean b, final boolean b2)\n
    '''
def getMessageHandler():
    '''returns IMMessageHandlerMocImpl\n\n
    getMessageHandler(final String anObject)\n
    '''
def createUserStatusHandler():
    '''returns IMUserStatusHandler\n\n
    createUserStatusHandler()\n
    '''
def getConnectionTimeout():
    '''returns long\n\n
    getConnectionTimeout()\n
    '''
def getDefaultConnectionTimeout():
    '''returns long\n\n
    getDefaultConnectionTimeout()\n
    '''
def getDefaultResolveTimeout():
    '''returns long\n\n
    getDefaultResolveTimeout()\n
    '''
def getResolveTimeout():
    '''returns long\n\n
    getResolveTimeout()\n
    '''
def isOpened():
    '''returns boolean\n\n
    isOpened()\n
    '''
def resolve():
    '''returns IMUser\n\n
    resolve(final String s, final boolean b, final boolean b2)\n
    resolve(final String anObject)\n
    '''
def setConnectionTimeout():
    '''returns None\n\n
    setConnectionTimeout(final long connectionTimeout)\n
    '''
def setResolveTimeout():
    '''returns None\n\n
    setResolveTimeout(final long resolveTimeout)\n
    '''
def getUserStatusHandler():
    '''returns IMUserStatusHandler\n\n
    getUserStatusHandler()\n
    '''
def setUserStatusHandler():
    '''returns None\n\n
    setUserStatusHandler(final IMUserStatusHandler userStatusHandler)\n
    '''
def getAckId():
    '''returns int\n\n
    getAckId()\n
    '''
def setAckId():
    '''returns None\n\n
    setAckId(final int ackId)\n
    '''
def registerIMSingleListener():
    '''returns None\n\n
    registerIMSingleListener(final IMSingleListener imSingleListener)\n
    '''
def removeIMSingleListener():
    '''returns None\n\n
    removeIMSingleListener(final IMSingleListener imSingleListener)\n
    '''
def getPartnerConferenceId():
    '''returns String\n\n
    getPartnerConferenceId(final String key)\n
    '''
def removePartnerConferenceId():
    '''returns None\n\n
    removePartnerConferenceId(final String key)\n
    '''
def addPartnerConferenceId():
    '''returns None\n\n
    addPartnerConferenceId(final String key, final String value)\n
    '''
def getPartnerHandlerByConferenceId():
    '''returns IMMessageHandlerMocImpl\n\n
    getPartnerHandlerByConferenceId(final String anObject)\n
    '''
