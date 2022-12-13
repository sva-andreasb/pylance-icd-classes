def MessageHandler():
'''public MessageHandler()
public MessageHandler(final boolean accumulateOnly)
'''
pass
def init():
'''public void init()
public void init(final boolean accumulateOnly)
'''
pass
def clearMessages():
'''public void clearMessages()
'''
pass
def handleMessage():
'''public boolean handleMessage(final IMessage message)
'''
pass
def isIgnoring():
'''public boolean isIgnoring(final IMessage.Kind kind)
'''
pass
def ignore():
'''public void ignore(final IMessage.Kind kind)
'''
pass
def dontIgnore():
'''public void dontIgnore(final IMessage.Kind kind)
'''
pass
def hasAnyMessage():
'''public boolean hasAnyMessage(final IMessage.Kind kind, final boolean orGreater)
'''
pass
def numMessages():
'''public int numMessages(final IMessage.Kind kind, final boolean orGreater)
'''
pass
def getUnmodifiableListView():
'''public List<IMessage> getUnmodifiableListView()
'''
pass
def getMessages():
'''public IMessage[] getMessages(final IMessage.Kind kind, final boolean orGreater)
'''
pass
def getErrors():
'''public IMessage[] getErrors()
'''
pass
def getWarnings():
'''public IMessage[] getWarnings()
'''
pass
def setInterceptor():
'''public void setInterceptor(final IMessageHandler interceptor)
'''
pass
def toString():
'''public String toString()
'''
pass
