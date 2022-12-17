def createEntry():
    '''returns int\n\n
    createEntry(final Connection connection, final String group_name, final String group_version, final byte[] content, final int content_length)\n
    createEntry(final Connection connection, final String group_name, final String group_version, final byte[] content, final int content_length, final long time, final String state, final Long n)\n
    '''
def replaceEntry():
    '''returns int\n\n
    replaceEntry(final Connection connection, final int value, final byte[] array, final int n)\n
    '''
def removeEntry():
    '''returns int\n\n
    removeEntry(final Connection connection, final int n, final int value)\n
    '''
def updateState():
    '''returns int\n\n
    updateState(final Connection connection, final int value, final String s, final int value2)\n
    '''
