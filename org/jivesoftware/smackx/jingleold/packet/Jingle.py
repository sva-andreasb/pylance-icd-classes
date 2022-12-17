NAMESPACE = "String  \"urn:xmpp:tmp:jingle\""
NODENAME = "String  \"jingle\""
def ():
    '''returns Jingle\n\n
    (final List<JingleContent> contents, final JingleContentInfo mi, final String sid)\n
    (final JingleContent content)\n
    (final JingleContentInfo info)\n
    (final JingleActionEnum action)\n
    (final String sid)\n
    ()\n
    '''
def getSid():
    '''returns String\n\n
    getSid()\n
    '''
def getContentInfo():
    '''returns JingleContentInfo\n\n
    getContentInfo()\n
    '''
def setContentInfo():
    '''returns None\n\n
    setContentInfo(final JingleContentInfo contentInfo)\n
    '''
def getContents():
    '''returns Iterator<JingleContent>\n\n
    getContents()\n
    '''
def getContentsList():
    '''returns List<JingleContent>\n\n
    getContentsList()\n
    '''
def addContent():
    '''returns None\n\n
    addContent(final JingleContent content)\n
    '''
def addContents():
    '''returns None\n\n
    addContents(final List<JingleContent> contentList)\n
    '''
def getAction():
    '''returns JingleActionEnum\n\n
    getAction()\n
    '''
def setAction():
    '''returns None\n\n
    setAction(final JingleActionEnum action)\n
    '''
def getInitiator():
    '''returns Jid\n\n
    getInitiator()\n
    '''
def setInitiator():
    '''returns None\n\n
    setInitiator(final Jid initiator)\n
    '''
def getResponder():
    '''returns Jid\n\n
    getResponder()\n
    '''
def setResponder():
    '''returns None\n\n
    setResponder(final Jid resp)\n
    '''
