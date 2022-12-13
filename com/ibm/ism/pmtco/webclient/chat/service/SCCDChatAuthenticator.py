def SCCDChatAuthenticator():
    '''public SCCDChatAuthenticator(final Oort oort)
    '''
def canHandshake():
    '''public boolean canHandshake(final BayeuxServer server, final ServerSession session, final ServerMessage message)
    '''
def canCreate():
    '''public boolean canCreate(final BayeuxServer server, final ServerSession session, final String channelId, final ServerMessage message)
    '''
def canPublish():
    '''public boolean canPublish(final BayeuxServer server, final ServerSession session, final ServerChannel channel, final ServerMessage message)
    '''
def canSubscribe():
    '''public boolean canSubscribe(final BayeuxServer server, final ServerSession session, final ServerChannel channel, final ServerMessage message)
    '''
def removed():
    '''public void removed(final ServerSession session, final boolean expired)
    '''
def getPersonIDByClientID():
    '''public static String getPersonIDByClientID(final String clientID)
    '''
