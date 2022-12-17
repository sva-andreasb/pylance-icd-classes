COL_MODEL_INDEX = "String  \"__midx\""
COL_SCENARIO_NAME = "String  \"__scenarioname\""
def ():
    '''returns CompareID\n\n
    ()\n
    (final String id)\n
    '''
def COMPARE():
    '''returns int\n\n
    COMPARE()\n
    '''
def processChange():
    '''returns None\n\n
    processChange(final Future<MXGanttModel> model, final JSONObject change, final WebClientSession sess, final ReplyBuilder reply)\n
    '''
def updateCompareData():
    '''returns None\n\n
    updateCompareData(final WebClientSession sess, @MXEventParam("compare") final JSONObject compareJsonData)\n
    '''
def loadCompareData():
    '''returns None\n\n
    loadCompareData(final WebClientSession sess, @MXEventParam("compare") JSONObject compareJsonData)\n
    '''
def loadCompareUI():
    '''returns None\n\n
    loadCompareUI(final WebClientSession sess, @MXEventParam("appname") final String appName, @MXEventParam("compare") final JSONObject compareJsonData)\n
    '''
def onReset():
    '''returns None\n\n
    onReset()\n
    '''
def getTooltip():
    '''returns DynamicTooltip\n\n
    getTooltip(final WebClientSession sess, @MXEventParam("projectid") String projectid, @MXEventParam("col") final String col, @MXEventParam("id") final String id)\n
    '''
