def validate():
    '''    public void validate(final long chatIdentifier)
    '''
def isNewChatHelper():
    '''    public synchronized boolean isNewChatHelper()
    '''
def isNewRecord():
    '''    public boolean isNewRecord()
    '''
def sendMessage():
    '''    public synchronized void sendMessage(final String message)
    '''
def popMessageBuffer():
    '''    public synchronized String popMessageBuffer()
    '''
def messageReceived():
    '''    public synchronized void messageReceived(final IMMessageEvent messageEvent)
    '''
def conversationClosed():
    '''    public synchronized void conversationClosed(final String reason)
    '''
def closeConversation():
    '''    public synchronized boolean closeConversation(final WebClientSession webClientSession)
    public synchronized boolean closeConversation(final HttpServletRequest request)
    '''
def abortConversation():
    '''    public synchronized boolean abortConversation(final boolean saveFlag, final WebClientSession webClientSession)
    public synchronized boolean abortConversation(final boolean saveFlag, final HttpServletRequest request)
    '''
def isOpened():
    '''    public boolean isOpened()
    '''
