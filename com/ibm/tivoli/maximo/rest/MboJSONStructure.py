def MboJSONStructure():
'''public MboJSONStructure(final boolean verbose, final boolean dropNulls, final boolean locale, final Set<String> cols, final boolean exclude, final boolean retainMbos, boolean generic, boolean metaData, final boolean compact, final boolean calculateEtag, final boolean useTotalCount, final boolean keys)
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
public OrderedJSONObject serializeMboSetAsJSONObject(final OrderedJSONObject opOjo, final MboIterator mboSet, final int startIndex, int maxCount)
'''
pass
def getCalculatedEtag():
'''public String getCalculatedEtag()
'''
pass
def isKey():
'''public boolean isKey(final MboRemote mbo, final MboValueInfo mboValueInfo)
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
def setUseRowStamp():
'''public void setUseRowStamp(final boolean useRowStamp)
'''
pass
def setResolvedTotalCount():
'''public void setResolvedTotalCount(final int resolvedTotalCount)
'''
pass
def setResolvedStartCount():
'''public void setResolvedStartCount(final int resolvedStartCount)
'''
pass
def setInitialResolvedCount():
'''public void setInitialResolvedCount(final int initialResolvedCount)
'''
pass
