def MIFMsgHubMXTransactable():
    '''public MIFMsgHubMXTransactable()
    '''
def setSyntheticNotf():
    '''public void setSyntheticNotf(final boolean syntheticNotf)
    '''
def setMessages():
    '''public void setMessages(final Map<String, JMSData> mapOfMessages)
    '''
def setUserInfo():
    '''public void setUserInfo(final UserInfo userInfo)
    '''
def getMessages():
    '''public Map getMessages()
    '''
def saveTransaction():
    '''public void saveTransaction(final MXTransaction txn)
    '''
def commitTransaction():
    '''public void commitTransaction(final MXTransaction txn)
    '''
def rollbackTransaction():
    '''public void rollbackTransaction(final MXTransaction txn)
    '''
def undoTransaction():
    '''public void undoTransaction(final MXTransaction txn)
    '''
def validateTransaction():
    '''public boolean validateTransaction(final MXTransaction txn)
    '''
def fireEventsBeforeDB():
    '''public void fireEventsBeforeDB(final MXTransaction txn)
    '''
def fireEventsAfterDB():
    '''public void fireEventsAfterDB(final MXTransaction txn)
    '''
def fireEventsAfterDBCommit():
    '''public void fireEventsAfterDBCommit(final MXTransaction txn)
    '''
def isEvent():
    '''public boolean isEvent()
    '''
def setIsEvent():
    '''public void setIsEvent(final boolean isEvent)
    '''
def deleteMesage():
    '''public void deleteMesage(final JMSData messageData, final String queueName, final UserInfo info)
    '''
def sendEmail():
    '''public boolean sendEmail(final QueueConfig config, final Connection conn, final Exception e)
    '''
