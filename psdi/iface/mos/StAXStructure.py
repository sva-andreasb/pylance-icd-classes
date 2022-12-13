def StAXStructure():
    '''public StAXStructure()
    public StAXStructure(final boolean dropNullCols)
    public StAXStructure(final boolean dropNullCols, final boolean retainMbos)
    '''
def isUseRowStamp():
    '''public boolean isUseRowStamp()
    '''
def setUseRowStamp():
    '''public void setUseRowStamp(final boolean useRowStamp)
    '''
def setAllowBinaryText():
    '''public void setAllowBinaryText(final boolean binaryText)
    '''
def serializeMbo():
    '''public byte[] serializeMbo(final MboRemote mbo)
    public void serializeMbo(final XMLStreamWriter writer, final MboRemote mbo)
    '''
def serializeMboAsSet():
    '''public byte[] serializeMboAsSet(final MboRemote mbo)
    public void serializeMboAsSet(final XMLStreamWriter writer, final MboRemote mbo)
    '''
def serializeMboSet():
    '''public byte[] serializeMboSet(final MboSetRemote mboSet, final int startIndex, final int maxCount)
    public byte[] serializeMboSet(final MboSetRemote mboSet)
    public void serializeMboSet(final XMLStreamWriter writer, final MboSetRemote mboSet)
    '''
def serializeMboIterator():
    '''public void serializeMboIterator(final XMLStreamWriter writer, final MboIterator mboSet)
    public byte[] serializeMboIterator(final MboIterator mboSet, final int startIndex, final int maxCount)
    public byte[] serializeMboIterator(final MboIterator mboSet)
    '''
def serializeMboList():
    '''public byte[] serializeMboList(final List<MboRemote> mboList, final int startIndex, final int maxCount)
    public byte[] serializeMboList(final List<MboRemote> mboList)
    public void serializeMboList(final XMLStreamWriter writer, final List<MboRemote> mboList)
    '''
def serializeMboArray():
    '''public void serializeMboArray(final XMLStreamWriter writer, final MboRemote[] mboArray)
    public byte[] serializeMboArray(final MboRemote[] mboArray, final int startIndex, final int maxCount)
    public byte[] serializeMboArray(final MboRemote[] mboArray)
    '''
