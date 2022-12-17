OK = "int  2"
CANCEL = "int  4"
YES = "int  8"
NO = "int  16"
NULL = "int  -1"
def ():
    '''returns MXApplicationYesNoCancelException\n\n
    (final String id, final String eg, final String ek)\n
    (final String id, final String eg, final String ek, final Object[] params)\n
    (final String id, final String eg, final String ek, final Throwable t)\n
    (final String id, final String eg, final String ek, final Object[] p, final Throwable t)\n
    '''
def getId():
    '''returns String\n\n
    getId()\n
    '''
def postUserInput():
    '''returns None\n\n
    postUserInput(final MXServerRemote server, final int answer, final UserInfo ui)\n
    '''
def setContinueEvents():
    '''returns None\n\n
    setContinueEvents(final int responses)\n
    '''
def getContinueEvents():
    '''returns int\n\n
    getContinueEvents()\n
    '''
def getUserClickedValue():
    '''returns int\n\n
    getUserClickedValue()\n
    '''
