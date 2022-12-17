DOMAIN = "String  \"domain\""
PATH = "String  \"path\""
PORT = "String  \"port\""
VERSION = "String  \"version\""
SECURE = "String  \"secure\""
MAXAGE = "String  \"max-age\""
COMMENT = "String  \"comment\""
COMMENTURL = "String  \"commenturl\""
DISCARD = "String  \"discard\""
def ():
    '''returns Cookie2\n\n
    ()\n
    (final String domain, final String name, final String value)\n
    (final String domain, final String name, final String value, final String path, final Date expires, final boolean secure)\n
    (final String domain, final String name, final String value, final String path, final Date expires, final boolean secure, final int[] ports)\n
    '''
def getCommentURL():
    '''returns String\n\n
    getCommentURL()\n
    '''
def setCommentURL():
    '''returns None\n\n
    setCommentURL(final String commentURL)\n
    '''
def getPorts():
    '''returns int[]\n\n
    getPorts()\n
    '''
def setPorts():
    '''returns None\n\n
    setPorts(final int[] ports)\n
    '''
def setDiscard():
    '''returns None\n\n
    setDiscard(final boolean toDiscard)\n
    '''
def isPersistent():
    '''returns boolean\n\n
    isPersistent()\n
    '''
def setPortAttributeSpecified():
    '''returns None\n\n
    setPortAttributeSpecified(final boolean value)\n
    '''
def isPortAttributeSpecified():
    '''returns boolean\n\n
    isPortAttributeSpecified()\n
    '''
def setPortAttributeBlank():
    '''returns None\n\n
    setPortAttributeBlank(final boolean value)\n
    '''
def isPortAttributeBlank():
    '''returns boolean\n\n
    isPortAttributeBlank()\n
    '''
def setVersionAttributeSpecified():
    '''returns None\n\n
    setVersionAttributeSpecified(final boolean value)\n
    '''
def isVersionAttributeSpecified():
    '''returns boolean\n\n
    isVersionAttributeSpecified()\n
    '''
def toExternalForm():
    '''returns String\n\n
    toExternalForm()\n
    '''
