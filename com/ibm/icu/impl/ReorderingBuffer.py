def ReorderingBuffer():
    '''    public ReorderingBuffer(final Normalizer2Impl ni, final Appendable dest, final int destCapacity)
    '''
def isEmpty():
    '''    public boolean isEmpty()
    '''
def length():
    '''    public int length()
    '''
def getLastCC():
    '''    public int getLastCC()
    '''
def getStringBuilder():
    '''    public StringBuilder getStringBuilder()
    '''
def equals():
    '''    public boolean equals(final CharSequence s, final int start, final int limit)
    '''
def append():
    '''    public void append(final int c, final int cc)
    public void append(final CharSequence s, int start, final int limit, final boolean isNFD, int leadCC, final int trailCC)
    public ReorderingBuffer append(final char c)
    public ReorderingBuffer append(final CharSequence s)
    public ReorderingBuffer append(final CharSequence s, final int start, final int limit)
    '''
def appendZeroCC():
    '''    public void appendZeroCC(final int c)
    '''
def flush():
    '''    public void flush()
    '''
def flushAndAppendZeroCC():
    '''    public ReorderingBuffer flushAndAppendZeroCC(final CharSequence s, final int start, final int limit)
    '''
def remove():
    '''    public void remove()
    '''
def removeSuffix():
    '''    public void removeSuffix(final int suffixLength)
    '''
