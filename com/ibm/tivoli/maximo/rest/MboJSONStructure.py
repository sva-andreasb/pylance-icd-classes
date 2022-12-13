def MboJSONStructure():
    '''    public MboJSONStructure(final boolean verbose, final boolean dropNulls, final boolean locale, final Set<String> cols, final boolean exclude, final boolean retainMbos, boolean generic, boolean metaData, final boolean compact, final boolean calculateEtag, final boolean useTotalCount, final boolean keys)
    '''
def serializeMboSet():
    '''    public byte[] serializeMboSet(final MboSetRemote mboSet)
    public byte[] serializeMboSet(final MboIterator mboSet)
    public byte[] serializeMboSet(final OrderedJSONObject opOjo, final MboIterator mboSet)
    public byte[] serializeMboSet(final MboSetRemote mboSet, final int startIndex, final int maxCount)
    public byte[] serializeMboSet(final MboIterator mboSet, final int startIndex, final int maxCount)
    public byte[] serializeMboSet(final OrderedJSONObject opOjo, final MboIterator mboSet, final int startIndex, final int maxCount)
    '''
def serializeMboSetAsJSONObject():
    '''    public OrderedJSONObject serializeMboSetAsJSONObject(final MboSetRemote mboSet, final int startIndex, final int maxCount)
    public OrderedJSONObject serializeMboSetAsJSONObject(final MboIterator mboSet, final int startIndex, final int maxCount)
    public OrderedJSONObject serializeMboSetAsJSONObject(final OrderedJSONObject opOjo, final MboIterator mboSet, final int startIndex, int maxCount)
    '''
def getCalculatedEtag():
    '''    public String getCalculatedEtag()
    '''
def isKey():
    '''    public boolean isKey(final MboRemote mbo, final MboValueInfo mboValueInfo)
    '''
def covertJSONObjectToBytes():
    '''    public byte[] covertJSONObjectToBytes(final OrderedJSONObject ojo)
    '''
def serializeMbo():
    '''    public byte[] serializeMbo(final MboRemote mbo)
    public byte[] serializeMbo(final OrderedJSONObject opOjo, final MboRemote mbo)
    '''
def setUseRowStamp():
    '''    public void setUseRowStamp(final boolean useRowStamp)
    '''
def setResolvedTotalCount():
    '''    public void setResolvedTotalCount(final int resolvedTotalCount)
    '''
def setResolvedStartCount():
    '''    public void setResolvedStartCount(final int resolvedStartCount)
    '''
def setInitialResolvedCount():
    '''    public void setInitialResolvedCount(final int initialResolvedCount)
    '''
