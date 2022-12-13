def OslcMboJsonSerializer():
'''public OslcMboJsonSerializer(final OslcRequest oslcRequest, final Map<String, OslcResourceProperty> resourceProperties)
public OslcMboJsonSerializer(final OslcRequest oslcRequest)
public OslcMboJsonSerializer(final String selectExp, final OslcRequest oslcRequest)
'''
pass
def setRetainMbos():
'''public void setRetainMbos(final boolean retainMbos)
'''
pass
def setDropNulls():
'''public void setDropNulls(final boolean dropNulls)
'''
pass
def serializeResolvedResource():
'''public OslcResourceResponse serializeResolvedResource(final LocalURIResolver.ResolvedResource rr)
'''
pass
def serializeMboSet():
'''public JSONObject serializeMboSet(final MboSetRemote mboSet)
public JSONObject serializeMboSet(final JSONObject rootOjo, final MboSetRemote mboSet, final String collectionURI)
'''
pass
def serializeMbo():
'''public JSONObject serializeMbo(final MboRemote mbo)
public void serializeMbo(final JSONObject mboOjo, final MboRemote mbo, final String collectionURI)
'''
pass
def setObjectID():
'''public void setObjectID(final JSONObject mboOjo, final MboRemote mbo)
'''
pass
