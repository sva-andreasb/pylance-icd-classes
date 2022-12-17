ST_AUTH_TYPE_PLAIN_PASSWD = "short  0"
ST_AUTH_TYPE_PLAIN_NOTES_TOKEN = "short  1"
ST_AUTH_TYPE_ENC_PASSWORD = "short  2"
ST_AUTH_TYPE_ANON = "short  3"
ST_AUTH_TYPE_ENC_DH_PASSWORD = "short  4"
ST_AUTH_TYPE_ENC_DH_NOTES_TOKEN = "short  5"
def ():
    '''returns VpkAuthInfo\n\n
    (final short type, final byte[] data)\n
    '''
def dump():
    '''returns None\n\n
    dump(final NdrOutputStream ndrOutputStream)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
