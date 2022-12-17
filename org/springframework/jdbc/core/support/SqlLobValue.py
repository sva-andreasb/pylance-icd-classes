def ():
    '''returns SqlLobValue\n\n
    (final byte[] bytes)\n
    (final byte[] bytes, final LobHandler lobHandler)\n
    (final String content)\n
    (final String content, final LobHandler lobHandler)\n
    (final InputStream stream, final int length)\n
    (final InputStream stream, final int length, final LobHandler lobHandler)\n
    (final Reader reader, final int length)\n
    (final Reader reader, final int length, final LobHandler lobHandler)\n
    '''
def setTypeValue():
    '''returns None\n\n
    setTypeValue(final PreparedStatement ps, final int paramIndex, final int sqlType, final String typeName)\n
    '''
def cleanup():
    '''returns None\n\n
    cleanup()\n
    '''
