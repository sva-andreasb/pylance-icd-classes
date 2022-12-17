def ():
    '''returns CountingMessageHandler\n\n
    (final IMessageHandler delegate)\n
    '''
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
def toString():
    '''returns String\n\n
    toString()\n
    '''
def numMessages():
    '''returns int\n\n
    numMessages(final IMessage.Kind kind, final boolean orGreater)\n
    '''
def hasErrors():
    '''returns boolean\n\n
    hasErrors()\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
