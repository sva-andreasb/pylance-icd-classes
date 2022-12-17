def ():
    '''returns ReorderingBuffer\n\n
    (final Normalizer2Impl ni, final Appendable dest, final int destCapacity)\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty()\n
    '''
def length():
    '''returns int\n\n
    length()\n
    '''
def getLastCC():
    '''returns int\n\n
    getLastCC()\n
    '''
def getStringBuilder():
    '''returns StringBuilder\n\n
    getStringBuilder()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final CharSequence s, final int start, final int limit)\n
    '''
def append():
    '''returns ReorderingBuffer\n\n
    append(final int c, final int cc)\n
    append(final CharSequence s, int start, final int limit, final boolean isNFD, int leadCC, final int trailCC)\n
    append(final char c)\n
    append(final CharSequence s)\n
    append(final CharSequence s, final int start, final int limit)\n
    '''
def appendZeroCC():
    '''returns None\n\n
    appendZeroCC(final int c)\n
    '''
def flush():
    '''returns None\n\n
    flush()\n
    '''
def flushAndAppendZeroCC():
    '''returns ReorderingBuffer\n\n
    flushAndAppendZeroCC(final CharSequence s, final int start, final int limit)\n
    '''
def remove():
    '''returns None\n\n
    remove()\n
    '''
def removeSuffix():
    '''returns None\n\n
    removeSuffix(final int suffixLength)\n
    '''
