def ():
    '''returns MOSJSONStructure\n\n
    (final String mosName, final String operation, final boolean verbose, final boolean dropNulls, final boolean locale, final boolean retainMbos, final boolean generic, final boolean keys, final boolean rootOnly, final boolean metaData, final boolean compact, final boolean calculateEtag, final boolean useTotalCount)\n
    (final MosInfo mosInfo, final String operation, final boolean verbose, final boolean dropNulls, final boolean locale, final boolean retainMbos, boolean generic, final boolean keys, final boolean rootOnly, boolean metaData, final boolean compact, final boolean calculateEtag, final boolean useTotalCount)\n
    '''
def getCalculatedEtag():
    '''returns String\n\n
    getCalculatedEtag()\n
    '''
def isUseRowStamp():
    '''returns boolean\n\n
    isUseRowStamp()\n
    '''
def setUseRowStamp():
    '''returns None\n\n
    setUseRowStamp(final boolean useRowStamp)\n
    '''
def serializeMboSet():
    '''returns byte[]\n\n
    serializeMboSet(final MboSetRemote mboSet)\n
    serializeMboSet(final MboIterator mboSet)\n
    serializeMboSet(final OrderedJSONObject opOjo, final MboIterator mboSet)\n
    serializeMboSet(final MboSetRemote mboSet, final int startIndex, final int maxCount)\n
    serializeMboSet(final MboIterator mboSet, final int startIndex, final int maxCount)\n
    serializeMboSet(final OrderedJSONObject opOjo, final MboIterator mboSet, final int startIndex, final int maxCount)\n
    '''
def serializeMboSetAsJSONObject():
    '''returns OrderedJSONObject\n\n
    serializeMboSetAsJSONObject(final MboSetRemote mboSet, final int startIndex, final int maxCount)\n
    serializeMboSetAsJSONObject(final MboIterator mboSet, final int startIndex, final int maxCount)\n
    serializeMboSetAsJSONObject(final OrderedJSONObject opOjo, final MboIterator mboSet, final int startIndex, final int maxCount)\n
    '''
def covertJSONObjectToBytes():
    '''returns byte[]\n\n
    covertJSONObjectToBytes(final OrderedJSONObject ojo)\n
    '''
def serializeMbo():
    '''returns byte[]\n\n
    serializeMbo(final MboRemote mbo)\n
    serializeMbo(final OrderedJSONObject opOjo, final MboRemote mbo)\n
    '''
def serializeMboAsJSONObject():
    '''returns OrderedJSONObject\n\n
    serializeMboAsJSONObject(final MboRemote mbo)\n
    serializeMboAsJSONObject(final OrderedJSONObject opOjo, final MboRemote mbo)\n
    '''
def isKey():
    '''returns boolean\n\n
    isKey(final MboRemote mbo, final String mboAttrName)\n
    '''
def setResolvedTotalCount():
    '''returns None\n\n
    setResolvedTotalCount(final int resolvedTotalCount)\n
    '''
def setInitialResolvedCount():
    '''returns None\n\n
    setInitialResolvedCount(final int initialResolvedCount)\n
    '''
def setResolvedStartCount():
    '''returns None\n\n
    setResolvedStartCount(final int resolvedStartCount)\n
    '''
