def setResumeOnError():
    '''returns None\n\n
    setResumeOnError(final boolean resumeOnError)\n
    '''
def ():
    '''returns DSMLWriter\n\n
    (final String name)\n
    (final OutputStream out)\n
    (final Writer out)\n
    '''
def writeError():
    '''returns None\n\n
    writeError(final Exception ex)\n
    '''
def finish():
    '''returns None\n\n
    finish()\n
    '''
def writeComments():
    '''returns None\n\n
    writeComments(final String str)\n
    '''
def writeMessage():
    '''returns None\n\n
    writeMessage(final LDAPMessage ldapMessage)\n
    '''
def writeEntry():
    '''returns None\n\n
    writeEntry(final LDAPEntry ldapEntry)\n
    writeEntry(final LDAPEntry ldapEntry, final LDAPControl[] array)\n
    writeEntry(final LDAPEntry ldapEntry, final LDAPControl[] array, final String str)\n
    '''
def getVersion():
    '''returns String\n\n
    getVersion()\n
    '''
def isRequest():
    '''returns boolean\n\n
    isRequest()\n
    '''
def useIndent():
    '''returns None\n\n
    useIndent(final boolean indent)\n
    '''
def setIndent():
    '''returns None\n\n
    setIndent(final int n)\n
    '''
