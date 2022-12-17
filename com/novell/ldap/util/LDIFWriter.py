def ():
    '''returns LDIFWriter\n\n
    (final OutputStream outputStream)\n
    (final OutputStream outputStream, final String s, final boolean value)\n
    '''
def writeEntry():
    '''returns None\n\n
    writeEntry(final LDAPEntry ldapEntry)\n
    writeEntry(final LDAPEntry ldapEntry, final LDAPControl[] array)\n
    '''
def writeMessage():
    '''returns None\n\n
    writeMessage(final LDAPMessage ldapMessage)\n
    '''
def writeComments():
    '''returns None\n\n
    writeComments(final String s)\n
    '''
def writeError():
    '''returns None\n\n
    writeError(final Exception ex)\n
    '''
def getVersion():
    '''returns String\n\n
    getVersion()\n
    '''
def isRequest():
    '''returns boolean\n\n
    isRequest()\n
    '''
def isPrintable():
    '''returns boolean\n\n
    isPrintable(final byte[] array)\n
    '''
def finish():
    '''returns None\n\n
    finish()\n
    '''
