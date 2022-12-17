def ():
    '''returns SCCDChatAuthenticator\n\n
    (final Oort oort)\n
    '''
def canHandshake():
    '''returns boolean\n\n
    canHandshake(final BayeuxServer server, final ServerSession session, final ServerMessage message)\n
    '''
def canCreate():
    '''returns boolean\n\n
    canCreate(final BayeuxServer server, final ServerSession session, final String channelId, final ServerMessage message)\n
    '''
def canPublish():
    '''returns boolean\n\n
    canPublish(final BayeuxServer server, final ServerSession session, final ServerChannel channel, final ServerMessage message)\n
    '''
def canSubscribe():
    '''returns boolean\n\n
    canSubscribe(final BayeuxServer server, final ServerSession session, final ServerChannel channel, final ServerMessage message)\n
    '''
def removed():
    '''returns None\n\n
    removed(final ServerSession session, final boolean expired)\n
    '''
