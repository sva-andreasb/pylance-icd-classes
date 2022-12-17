def ():
    '''returns JingleSession\n\n
    (final FullJid initiator, final FullJid responder, final Role role, final String sid)\n
    (final FullJid initiator, final FullJid responder, final Role role, final String sid, final List<JingleContent> contents)\n
    '''
def getInitiator():
    '''returns FullJid\n\n
    getInitiator()\n
    '''
def isInitiator():
    '''returns boolean\n\n
    isInitiator()\n
    '''
def getResponder():
    '''returns FullJid\n\n
    getResponder()\n
    '''
def isResponder():
    '''returns boolean\n\n
    isResponder()\n
    '''
def getRemote():
    '''returns FullJid\n\n
    getRemote()\n
    '''
def getLocal():
    '''returns FullJid\n\n
    getLocal()\n
    '''
def getSessionId():
    '''returns String\n\n
    getSessionId()\n
    '''
def getFullJidAndSessionId():
    '''returns FullJidAndSessionId\n\n
    getFullJidAndSessionId()\n
    '''
def getContents():
    '''returns List<JingleContent>\n\n
    getContents()\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object other)\n
    '''
def handleJingleSessionRequest():
    '''returns IQ\n\n
    handleJingleSessionRequest(final Jingle jingle)\n
    '''
