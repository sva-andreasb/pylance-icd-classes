def ():
    '''returns OslcMboJsonSerializer\n\n
    (final OslcRequest oslcRequest, final Map<String, OslcResourceProperty> resourceProperties)\n
    (final OslcRequest oslcRequest)\n
    (final String selectExp, final OslcRequest oslcRequest)\n
    '''
def setRetainMbos():
    '''returns None\n\n
    setRetainMbos(final boolean retainMbos)\n
    '''
def setDropNulls():
    '''returns None\n\n
    setDropNulls(final boolean dropNulls)\n
    '''
def serializeResolvedResource():
    '''returns OslcResourceResponse\n\n
    serializeResolvedResource(final LocalURIResolver.ResolvedResource rr)\n
    '''
def serializeMboSet():
    '''returns JSONObject\n\n
    serializeMboSet(final MboSetRemote mboSet)\n
    serializeMboSet(final JSONObject rootOjo, final MboSetRemote mboSet, final String collectionURI)\n
    '''
def serializeMbo():
    '''returns None\n\n
    serializeMbo(final MboRemote mbo)\n
    serializeMbo(final JSONObject mboOjo, final MboRemote mbo, final String collectionURI)\n
    '''
def setObjectID():
    '''returns None\n\n
    setObjectID(final JSONObject mboOjo, final MboRemote mbo)\n
    '''
