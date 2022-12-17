def ():
    '''returns DataItem\n\n
    (final String id, final String label, final Locale locale)\n
    (final DataSet dataSet, final MboRemote mbo)\n
    '''
def updateFromMbo():
    '''returns None\n\n
    updateFromMbo(final DataSet dataSet, final MboRemote mbo)\n
    updateFromMbo(final DataSet dataSet, final MboRemote mbo, final String idSuffix)\n
    '''
def getId():
    '''returns String\n\n
    getId()\n
    '''
def getBaseId():
    '''returns String\n\n
    getBaseId()\n
    '''
def getLocale():
    '''returns Locale\n\n
    getLocale()\n
    '''
def getMbo():
    '''returns MboRemote\n\n
    getMbo()\n
    '''
def getElements():
    '''returns List<DataElement>\n\n
    getElements()\n
    '''
def cleanup():
    '''returns None\n\n
    cleanup()\n
    '''
def add():
    '''returns None\n\n
    add(final DataElement element)\n
    '''
def addElement():
    '''returns DataElement\n\n
    addElement(final DataSet dataSet, final MboRemote mbo, final CacheLvcMsgDesc lvcInfoMsgUtil)\n
    addElement(final DataSet dataSet, final MboRemote mbo, final String startMAttr, final String endMAttr, final CacheLvcMsgDesc lvcInfoMsgUtil)\n
    '''
def toJSON():
    '''returns JSONObject\n\n
    toJSON()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def hasOverlapWith():
    '''returns boolean\n\n
    hasOverlapWith(final DataSet dataSet, final MboRemote mbo)\n
    '''
