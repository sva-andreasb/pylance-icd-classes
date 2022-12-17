MAP_ACCESSOR_ID = "String  \"MAP_CONTROL_ACCESSOR_ID\""
def ():
    '''returns MapControlAccessor\n\n
    (final MapControlCallbacks instance)\n
    (final MapControlCallbacks instance, final LatLngBounds bounds)\n
    '''
def setRecordsToLayer():
    '''returns None\n\n
    setRecordsToLayer(final String layerName, final MboSetRemote records)\n
    '''
def addRecordsToLayer():
    '''returns None\n\n
    addRecordsToLayer(final String layerName, final MboSetRemote records)\n
    '''
def removeRecordsFromLayer():
    '''returns None\n\n
    removeRecordsFromLayer(final String layerName, final MboSetRemote records)\n
    '''
def getBounds():
    '''returns LatLngBounds\n\n
    getBounds()\n
    '''
def setMapBounds():
    '''returns None\n\n
    setMapBounds(final LatLngBounds bounds)\n
    '''
def createMapCallback():
    '''returns None\n\n
    createMapCallback(final String action, final JSONObject data)\n
    '''
def getMainRecordMbo():
    '''returns MboRemote\n\n
    getMainRecordMbo()\n
    '''
