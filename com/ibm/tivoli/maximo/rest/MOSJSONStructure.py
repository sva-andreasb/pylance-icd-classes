def MOSJSONStructure():
'''public MOSJSONStructure(final String mosName, final String operation, final boolean verbose, final boolean dropNulls, final boolean locale, final boolean retainMbos, final boolean generic, final boolean keys, final boolean rootOnly, final boolean metaData, final boolean compact, final boolean calculateEtag, final boolean useTotalCount)
public MOSJSONStructure(final MosInfo mosInfo, final String operation, final boolean verbose, final boolean dropNulls, final boolean locale, final boolean retainMbos, boolean generic, final boolean keys, final boolean rootOnly, boolean metaData, final boolean compact, final boolean calculateEtag, final boolean useTotalCount)
'''
pass
def getCalculatedEtag():
'''public String getCalculatedEtag()
'''
pass
def isUseRowStamp():
'''public boolean isUseRowStamp()
'''
pass
def setUseRowStamp():
'''public void setUseRowStamp(final boolean useRowStamp)
'''
pass
def serializeMboSet():
'''public byte[] serializeMboSet(final MboSetRemote mboSet)
public byte[] serializeMboSet(final MboIterator mboSet)
public byte[] serializeMboSet(final OrderedJSONObject opOjo, final MboIterator mboSet)
public byte[] serializeMboSet(final MboSetRemote mboSet, final int startIndex, final int maxCount)
public byte[] serializeMboSet(final MboIterator mboSet, final int startIndex, final int maxCount)
public byte[] serializeMboSet(final OrderedJSONObject opOjo, final MboIterator mboSet, final int startIndex, final int maxCount)
'''
pass
def serializeMboSetAsJSONObject():
'''public OrderedJSONObject serializeMboSetAsJSONObject(final MboSetRemote mboSet, final int startIndex, final int maxCount)
public OrderedJSONObject serializeMboSetAsJSONObject(final MboIterator mboSet, final int startIndex, final int maxCount)
public OrderedJSONObject serializeMboSetAsJSONObject(final OrderedJSONObject opOjo, final MboIterator mboSet, final int startIndex, final int maxCount)
'''
pass
def covertJSONObjectToBytes():
'''public byte[] covertJSONObjectToBytes(final OrderedJSONObject ojo)
'''
pass
def serializeMbo():
'''public byte[] serializeMbo(final MboRemote mbo)
public byte[] serializeMbo(final OrderedJSONObject opOjo, final MboRemote mbo)
'''
pass
def serializeMboAsJSONObject():
'''public OrderedJSONObject serializeMboAsJSONObject(final MboRemote mbo)
public OrderedJSONObject serializeMboAsJSONObject(final OrderedJSONObject opOjo, final MboRemote mbo)
'''
pass
def isKey():
'''public boolean isKey(final MboRemote mbo, final String mboAttrName)
'''
pass
def setResolvedTotalCount():
'''public void setResolvedTotalCount(final int resolvedTotalCount)
'''
pass
def setInitialResolvedCount():
'''public void setInitialResolvedCount(final int initialResolvedCount)
'''
pass
def setResolvedStartCount():
'''public void setResolvedStartCount(final int resolvedStartCount)
'''
pass
