def ():
    '''returns AcknowledgedMessagesClientExtension\n\n
    (final ServerSession session)\n
    '''
def rcv():
    '''returns boolean\n\n
    rcv(final ServerSession from, final ServerMessage.Mutable message)\n
    '''
def rcvMeta():
    '''returns boolean\n\n
    rcvMeta(final ServerSession session, final ServerMessage.Mutable message)\n
    '''
def send():
    '''returns ServerMessage\n\n
    send(final ServerSession to, final ServerMessage message)\n
    '''
def sendMeta():
    '''returns boolean\n\n
    sendMeta(final ServerSession to, final ServerMessage.Mutable message)\n
    '''
