def ():
    '''returns StAXStructure\n\n
    ()\n
    (final boolean dropNullCols)\n
    (final boolean dropNullCols, final boolean retainMbos)\n
    '''
def isUseRowStamp():
    '''returns boolean\n\n
    isUseRowStamp()\n
    '''
def setUseRowStamp():
    '''returns None\n\n
    setUseRowStamp(final boolean useRowStamp)\n
    '''
def setAllowBinaryText():
    '''returns None\n\n
    setAllowBinaryText(final boolean binaryText)\n
    '''
def serializeMbo():
    '''returns None\n\n
    serializeMbo(final MboRemote mbo)\n
    serializeMbo(final XMLStreamWriter writer, final MboRemote mbo)\n
    '''
def serializeMboAsSet():
    '''returns None\n\n
    serializeMboAsSet(final MboRemote mbo)\n
    serializeMboAsSet(final XMLStreamWriter writer, final MboRemote mbo)\n
    '''
def serializeMboSet():
    '''returns None\n\n
    serializeMboSet(final MboSetRemote mboSet, final int startIndex, final int maxCount)\n
    serializeMboSet(final MboSetRemote mboSet)\n
    serializeMboSet(final XMLStreamWriter writer, final MboSetRemote mboSet)\n
    '''
def serializeMboIterator():
    '''returns byte[]\n\n
    serializeMboIterator(final XMLStreamWriter writer, final MboIterator mboSet)\n
    serializeMboIterator(final MboIterator mboSet, final int startIndex, final int maxCount)\n
    serializeMboIterator(final MboIterator mboSet)\n
    '''
def serializeMboList():
    '''returns None\n\n
    serializeMboList(final List<MboRemote> mboList, final int startIndex, final int maxCount)\n
    serializeMboList(final List<MboRemote> mboList)\n
    serializeMboList(final XMLStreamWriter writer, final List<MboRemote> mboList)\n
    '''
def serializeMboArray():
    '''returns byte[]\n\n
    serializeMboArray(final XMLStreamWriter writer, final MboRemote[] mboArray)\n
    serializeMboArray(final MboRemote[] mboArray, final int startIndex, final int maxCount)\n
    serializeMboArray(final MboRemote[] mboArray)\n
    '''
