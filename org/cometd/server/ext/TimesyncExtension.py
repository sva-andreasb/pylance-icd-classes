LAG_ATTRIBUTE = "String  \"lag\""
def ():
    '''returns TimesyncExtension\n\n
    ()\n
    '''
def getAccuracyTarget():
    '''returns int\n\n
    getAccuracyTarget()\n
    '''
def setAccuracyTarget():
    '''returns None\n\n
    setAccuracyTarget(final int target)\n
    '''
def rcv():
    '''returns boolean\n\n
    rcv(final ServerSession from, final ServerMessage.Mutable message)\n
    '''
def rcvMeta():
    '''returns boolean\n\n
    rcvMeta(final ServerSession from, final ServerMessage.Mutable message)\n
    '''
def send():
    '''returns boolean\n\n
    send(final ServerSession from, final ServerSession to, final ServerMessage.Mutable message)\n
    '''
def sendMeta():
    '''returns boolean\n\n
    sendMeta(final ServerSession session, final ServerMessage.Mutable message)\n
    '''
