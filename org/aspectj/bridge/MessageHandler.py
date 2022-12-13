def MessageHandler():
    '''public MessageHandler()
    public MessageHandler(final boolean accumulateOnly)
    '''
def init():
    '''public void init()
    public void init(final boolean accumulateOnly)
    '''
def clearMessages():
    '''public void clearMessages()
    '''
def handleMessage():
    '''public boolean handleMessage(final IMessage message)
    '''
def isIgnoring():
    '''public boolean isIgnoring(final IMessage.Kind kind)
    '''
def ignore():
    '''public void ignore(final IMessage.Kind kind)
    '''
def dontIgnore():
    '''public void dontIgnore(final IMessage.Kind kind)
    '''
def hasAnyMessage():
    '''public boolean hasAnyMessage(final IMessage.Kind kind, final boolean orGreater)
    '''
def numMessages():
    '''public int numMessages(final IMessage.Kind kind, final boolean orGreater)
    '''
def getUnmodifiableListView():
    '''public List<IMessage> getUnmodifiableListView()
    '''
def getMessages():
    '''public IMessage[] getMessages(final IMessage.Kind kind, final boolean orGreater)
    '''
def getErrors():
    '''public IMessage[] getErrors()
    '''
def getWarnings():
    '''public IMessage[] getWarnings()
    '''
def setInterceptor():
    '''public void setInterceptor(final IMessageHandler interceptor)
    '''
def toString():
    '''public String toString()
    '''
