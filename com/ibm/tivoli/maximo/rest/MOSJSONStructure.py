def MOSJSONStructure():
    '''public MOSJSONStructure(final String mosName, final String operation, final boolean verbose, final boolean dropNulls, final boolean locale, final boolean retainMbos, final boolean generic, final boolean keys, final boolean rootOnly, final boolean metaData, final boolean compact, final boolean calculateEtag, final boolean useTotalCount)
    public MOSJSONStructure(final MosInfo mosInfo, final String operation, final boolean verbose, final boolean dropNulls, final boolean locale, final boolean retainMbos, boolean generic, final boolean keys, final boolean rootOnly, boolean metaData, final boolean compact, final boolean calculateEtag, final boolean useTotalCount)
    '''
def getCalculatedEtag():
    '''public String getCalculatedEtag()
    '''
def isUseRowStamp():
    '''public boolean isUseRowStamp()
    '''
def setUseRowStamp():
    '''public void setUseRowStamp(final boolean useRowStamp)
    '''
def serializeMboSet():
    '''public byte[] serializeMboSet(final MboSetRemote mboSet)
    public byte[] serializeMboSet(final MboIterator mboSet)
    public byte[] serializeMboSet(final OrderedJSONObject opOjo, final MboIterator mboSet)
    public byte[] serializeMboSet(final MboSetRemote mboSet, final int startIndex, final int maxCount)
    public byte[] serializeMboSet(final MboIterator mboSet, final int startIndex, final int maxCount)
    public byte[] serializeMboSet(final OrderedJSONObject opOjo, final MboIterator mboSet, final int startIndex, final int maxCount)
    '''
def serializeMboSetAsJSONObject():
    '''public OrderedJSONObject serializeMboSetAsJSONObject(final MboSetRemote mboSet, final int startIndex, final int maxCount)
    public OrderedJSONObject serializeMboSetAsJSONObject(final MboIterator mboSet, final int startIndex, final int maxCount)
    public OrderedJSONObject serializeMboSetAsJSONObject(final OrderedJSONObject opOjo, final MboIterator mboSet, final int startIndex, final int maxCount)
    '''
def covertJSONObjectToBytes():
    '''public byte[] covertJSONObjectToBytes(final OrderedJSONObject ojo)
    '''
def serializeMbo():
    '''public byte[] serializeMbo(final MboRemote mbo)
    public byte[] serializeMbo(final OrderedJSONObject opOjo, final MboRemote mbo)
    '''
def serializeMboAsJSONObject():
    '''public OrderedJSONObject serializeMboAsJSONObject(final MboRemote mbo)
    public OrderedJSONObject serializeMboAsJSONObject(final OrderedJSONObject opOjo, final MboRemote mbo)
    '''
def isKey():
    '''public boolean isKey(final MboRemote mbo, final String mboAttrName)
    '''
def setResolvedTotalCount():
    '''public void setResolvedTotalCount(final int resolvedTotalCount)
    '''
def setInitialResolvedCount():
    '''public void setInitialResolvedCount(final int initialResolvedCount)
    '''
def setResolvedStartCount():
    '''public void setResolvedStartCount(final int resolvedStartCount)
    '''
