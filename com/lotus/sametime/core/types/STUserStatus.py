ST_USER_STATUS_OFFLINE = "short  0"
ST_USER_STATUS_ACTIVE = "short  32"
ST_USER_STATUS_NOT_USING = "short  64"
ST_USER_STATUS_AWAY = "short  96"
ST_USER_STATUS_DND = "short  128"
ST_USER_STATUS_MOBILE = "short  512"
ST_USER_STATUS_ACTIVE_MOBILE = "short  544"
ST_USER_STATUS_UNKNOWN = "short  Short.MIN_VALUE"
ST_USER_STATUS_DONTCARE = "short  16384"
ST_USER_STATUS_IN_MEETING = "short  8"
def ():
    '''returns STUserStatus\n\n
    (final short type, final int time, final String description)\n
    (final NdrInputStream ndrInputStream)\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
def dump():
    '''returns None\n\n
    dump(final NdrOutputStream ndrOutputStream)\n
    '''
def load():
    '''returns None\n\n
    load(final NdrInputStream ndrInputStream)\n
    '''
def isStatus():
    '''returns boolean\n\n
    isStatus(final short n)\n
    '''
