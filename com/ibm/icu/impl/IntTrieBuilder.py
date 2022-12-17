def ():
    '''returns IntTrieBuilder\n\n
    (final IntTrieBuilder table)\n
    (final int[] aliasdata, final int maxdatalength, final int initialvalue, final int leadunitvalue, final boolean latin1linear)\n
    '''
def getValue():
    '''returns int\n\n
    getValue(final int ch)\n
    getValue(final int ch, final boolean[] inBlockZero)\n
    '''
def setValue():
    '''returns boolean\n\n
    setValue(final int ch, final int value)\n
    '''
def serialize():
    '''returns int\n\n
    serialize(final DataManipulate datamanipulate, final Trie.DataManipulate triedatamanipulate)\n
    serialize(final OutputStream os, final boolean reduceTo16Bits, final DataManipulate datamanipulate)\n
    '''
def setRange():
    '''returns boolean\n\n
    setRange(int start, int limit, final int value, final boolean overwrite)\n
    '''
