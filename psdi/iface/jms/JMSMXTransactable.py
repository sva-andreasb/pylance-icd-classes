def JMSMXTransactable():
'''public JMSMXTransactable()
'''
pass
def setSyntheticNotf():
'''public void setSyntheticNotf(final boolean syntheticNotf)
'''
pass
def setMessages():
'''public void setMessages(final Map<String, JMSData> mapOfMessages)
'''
pass
def setUserInfo():
'''public void setUserInfo(final UserInfo userInfo)
'''
pass
def getMessages():
'''public Map getMessages()
'''
pass
def saveTransaction():
'''public void saveTransaction(final MXTransaction txn)
'''
pass
def commitTransaction():
'''public void commitTransaction(final MXTransaction txn)
'''
pass
def rollbackTransaction():
'''public void rollbackTransaction(final MXTransaction txn)
'''
pass
def undoTransaction():
'''public void undoTransaction(final MXTransaction txn)
'''
pass
def validateTransaction():
'''public boolean validateTransaction(final MXTransaction txn)
'''
pass
def fireEventsBeforeDB():
'''public void fireEventsBeforeDB(final MXTransaction txn)
'''
pass
def fireEventsAfterDB():
'''public void fireEventsAfterDB(final MXTransaction txn)
'''
pass
def fireEventsAfterDBCommit():
'''public void fireEventsAfterDBCommit(final MXTransaction txn)
'''
pass
def isEvent():
'''public boolean isEvent()
'''
pass
def setIsEvent():
'''public void setIsEvent(final boolean isEvent)
'''
pass
def storeMesage():
'''public void storeMesage(final String status, final JMSData messageData, final String queueName, final Exception e, final UserInfo info)
'''
pass
def deleteMesage():
'''public void deleteMesage(final JMSData messageData, final String queueName, final UserInfo info)
'''
pass
def sendEmail():
'''public boolean sendEmail(final QueueConfig config, final Connection conn, final Exception e)
'''
pass
