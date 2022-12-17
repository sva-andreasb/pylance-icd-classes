SYSTEM_ERR = "IMessageHandler  new MessageWriter(new PrintWriter(System.err, true), true)"
SYSTEM_OUT = "IMessageHandler  new MessageWriter(new PrintWriter(System.out, true), false)"
def handleMessage():
    '''returns boolean\n\n
    handleMessage(final IMessage message)\n
    '''
def isIgnoring():
    '''returns boolean\n\n
    isIgnoring(final IMessage.Kind kind)\n
    '''
def dontIgnore():
    '''returns None\n\n
    dontIgnore(final IMessage.Kind kind)\n
    '''
def ignore():
    '''returns None\n\n
    ignore(final IMessage.Kind kind)\n
    '''
