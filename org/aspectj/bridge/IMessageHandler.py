SYSTEM_ERR = "IMessageHandler  new MessageWriter(new PrintWriter(System.err, true), true)"
SYSTEM_OUT = "IMessageHandler  new MessageWriter(new PrintWriter(System.out, true), false)"
def handleMessage():
    '''    public boolean handleMessage(final IMessage message)
    '''
def isIgnoring():
    '''    public boolean isIgnoring(final IMessage.Kind kind)
    '''
def dontIgnore():
    '''    public void dontIgnore(final IMessage.Kind kind)
    '''
def ignore():
    '''    public void ignore(final IMessage.Kind kind)
    '''
