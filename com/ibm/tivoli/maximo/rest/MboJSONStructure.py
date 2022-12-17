def ():
    '''returns MboJSONStructure\n\n
    (final boolean verbose, final boolean dropNulls, final boolean locale, final Set<String> cols, final boolean exclude, final boolean retainMbos, boolean generic, boolean metaData, final boolean compact, final boolean calculateEtag, final boolean useTotalCount, final boolean keys)\n
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
    serializeMboSetAsJSONObject(final OrderedJSONObject opOjo, final MboIterator mboSet, final int startIndex, int maxCount)\n
    '''
def getCalculatedEtag():
    '''returns String\n\n
    getCalculatedEtag()\n
    '''
def isKey():
    '''returns boolean\n\n
    isKey(final MboRemote mbo, final MboValueInfo mboValueInfo)\n
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
def setUseRowStamp():
    '''returns None\n\n
    setUseRowStamp(final boolean useRowStamp)\n
    '''
def setResolvedTotalCount():
    '''returns None\n\n
    setResolvedTotalCount(final int resolvedTotalCount)\n
    '''
def setResolvedStartCount():
    '''returns None\n\n
    setResolvedStartCount(final int resolvedStartCount)\n
    '''
def setInitialResolvedCount():
    '''returns None\n\n
    setInitialResolvedCount(final int initialResolvedCount)\n
    '''
