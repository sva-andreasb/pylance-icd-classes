def validate():
'''public void validate(final long chatIdentifier)
'''
pass
def isNewChatHelper():
'''public synchronized boolean isNewChatHelper()
'''
pass
def isNewRecord():
'''public boolean isNewRecord()
'''
pass
def sendMessage():
'''public synchronized void sendMessage(final String message)
'''
pass
def popMessageBuffer():
'''public synchronized String popMessageBuffer()
'''
pass
def messageReceived():
'''public synchronized void messageReceived(final IMMessageEvent messageEvent)
'''
pass
def conversationClosed():
'''public synchronized void conversationClosed(final String reason)
'''
pass
def closeConversation():
'''public synchronized boolean closeConversation(final WebClientSession webClientSession)
public synchronized boolean closeConversation(final HttpServletRequest request)
'''
pass
def abortConversation():
'''public synchronized boolean abortConversation(final boolean saveFlag, final WebClientSession webClientSession)
public synchronized boolean abortConversation(final boolean saveFlag, final HttpServletRequest request)
'''
pass
def isOpened():
'''public boolean isOpened()
'''
pass
