def ():
    '''returns MIFMsgHubMXTransactable\n\n
    ()\n
    '''
def setSyntheticNotf():
    '''returns None\n\n
    setSyntheticNotf(final boolean syntheticNotf)\n
    '''
def setMessages():
    '''returns None\n\n
    setMessages(final Map<String, JMSData> mapOfMessages)\n
    '''
def setUserInfo():
    '''returns None\n\n
    setUserInfo(final UserInfo userInfo)\n
    '''
def getMessages():
    '''returns Map\n\n
    getMessages()\n
    '''
def saveTransaction():
    '''returns None\n\n
    saveTransaction(final MXTransaction txn)\n
    '''
def commitTransaction():
    '''returns None\n\n
    commitTransaction(final MXTransaction txn)\n
    '''
def rollbackTransaction():
    '''returns None\n\n
    rollbackTransaction(final MXTransaction txn)\n
    '''
def undoTransaction():
    '''returns None\n\n
    undoTransaction(final MXTransaction txn)\n
    '''
def validateTransaction():
    '''returns boolean\n\n
    validateTransaction(final MXTransaction txn)\n
    '''
def fireEventsBeforeDB():
    '''returns None\n\n
    fireEventsBeforeDB(final MXTransaction txn)\n
    '''
def fireEventsAfterDB():
    '''returns None\n\n
    fireEventsAfterDB(final MXTransaction txn)\n
    '''
def fireEventsAfterDBCommit():
    '''returns None\n\n
    fireEventsAfterDBCommit(final MXTransaction txn)\n
    '''
def isEvent():
    '''returns boolean\n\n
    isEvent()\n
    '''
def setIsEvent():
    '''returns None\n\n
    setIsEvent(final boolean isEvent)\n
    '''
def deleteMesage():
    '''returns None\n\n
    deleteMesage(final JMSData messageData, final String queueName, final UserInfo info)\n
    '''
def sendEmail():
    '''returns boolean\n\n
    sendEmail(final QueueConfig config, final Connection conn, final Exception e)\n
    '''
