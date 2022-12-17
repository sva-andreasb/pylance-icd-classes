def ():
    '''returns AppSetupService\n\n
    ()\n
    (final MXServer mxServer)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def getMainTbname():
    '''returns String\n\n
    getMainTbname(final String app, final UserInfo userInfo)\n
    '''
def getCondPropCache():
    '''returns CtrlCondPropCache\n\n
    getCondPropCache()\n
    '''
def getPresentationCache():
    '''returns PresentationCache\n\n
    getPresentationCache()\n
    '''
def overridePropValue():
    '''returns None\n\n
    overridePropValue(@WSMboKey("APPPROPCFG") final MboRemote propCfg, final String userAlnValue, final Long userLongVal, final Boolean userBoolValue)\n
    '''
def resetPropValue():
    '''returns None\n\n
    resetPropValue(@WSMboKey("APPPROPCFG") final MboRemote propCfg)\n
    '''
def publishWorkCenter():
    '''returns None\n\n
    publishWorkCenter(@WSMboKey("MAXWORKCENTER") final MboRemote maxWorkcenterMbo, final String revisionDate, final String workcenter, final String comments, final String headerString)\n
    '''
