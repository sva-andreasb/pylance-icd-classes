def ():
    '''returns MessageHandler\n\n
    ()\n
    (final boolean accumulateOnly)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    init(final boolean accumulateOnly)\n
    '''
def clearMessages():
    '''returns None\n\n
    clearMessages()\n
    '''
def handleMessage():
    '''returns boolean\n\n
    handleMessage(final IMessage message)\n
    '''
def isIgnoring():
    '''returns boolean\n\n
    isIgnoring(final IMessage.Kind kind)\n
    '''
def ignore():
    '''returns None\n\n
    ignore(final IMessage.Kind kind)\n
    '''
def dontIgnore():
    '''returns None\n\n
    dontIgnore(final IMessage.Kind kind)\n
    '''
def hasAnyMessage():
    '''returns boolean\n\n
    hasAnyMessage(final IMessage.Kind kind, final boolean orGreater)\n
    '''
def numMessages():
    '''returns int\n\n
    numMessages(final IMessage.Kind kind, final boolean orGreater)\n
    '''
def getUnmodifiableListView():
    '''returns List<IMessage>\n\n
    getUnmodifiableListView()\n
    '''
def getMessages():
    '''returns IMessage[]\n\n
    getMessages(final IMessage.Kind kind, final boolean orGreater)\n
    '''
def getErrors():
    '''returns IMessage[]\n\n
    getErrors()\n
    '''
def getWarnings():
    '''returns IMessage[]\n\n
    getWarnings()\n
    '''
def setInterceptor():
    '''returns None\n\n
    setInterceptor(final IMessageHandler interceptor)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
