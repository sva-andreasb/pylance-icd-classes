def createEntry():
    '''returns int\n\n
    createEntry(final Connection connection, final String source, final String sourcefile)\n
    createEntry(final Connection connection, final String source, final String sourcefile, final byte[] content, final int content_length)\n
    createEntry(final Connection connection, final String source, final String sourcefile, final byte[] content, final int content_length, final long time)\n
    '''
def setContent():
    '''returns None\n\n
    setContent(final Connection connection, final int n, final InputStream inputStream)\n
    setContent(final Connection connection, final int n, final InputStream inputStream, final int n2)\n
    '''
def setContentFrom():
    '''returns int\n\n
    setContentFrom(final Connection connection, final int n, final int value)\n
    '''
def replaceEntry():
    '''returns int\n\n
    replaceEntry(final Connection connection, final int value, final String s, final String s2, final byte[] array, final int value2)\n
    replaceEntry(final Connection connection, final String s, final String s2, final char c, final char c2, final String s3, final String s4, final byte[] array, final int value)\n
    '''
def removeEntry():
    '''returns int\n\n
    removeEntry(final Connection connection, final int n)\n
    '''
def removeEntriesForApp():
    '''returns None\n\n
    removeEntriesForApp(final Connection connection, final String s, final String s2, final boolean b)\n
    '''
def removeOrphanedEntries():
    '''returns None\n\n
    removeOrphanedEntries(final Connection connection)\n
    '''
def removeEntriesForProject():
    '''returns None\n\n
    removeEntriesForProject(final Connection connection, final String s)\n
    '''
def removeEntriesForGroup():
    '''returns int\n\n
    removeEntriesForGroup(final Connection connection, final String s, final String s2)\n
    '''
