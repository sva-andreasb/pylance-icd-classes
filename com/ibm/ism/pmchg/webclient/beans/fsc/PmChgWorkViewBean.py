COPYRIGHT = "String  \"\n\nLicensed Materials - Property of IBM\n5725-E24\n(C)Copyright IBM Corporation 2007, 2013.\nAll Rights Reserved.\nUS Government Users Restricted Rights - Use, duplication \nor disclosure restricted by GSA ADP Schedule Contract with IBM Corp.\n\n\""
def ():
    '''returns PmChgWorkViewBean\n\n
    ()\n
    '''
def onReset():
    '''returns None\n\n
    onReset()\n
    '''
def createGanttModel():
    '''returns Future<MXGanttModel>\n\n
    createGanttModel()\n
    '''
def REFRESH():
    '''returns int\n\n
    REFRESH()\n
    '''
def addActionMenuItems():
    '''returns None\n\n
    addActionMenuItems(final TMenu popupmenu, final String[] selectedactivitys, final Future<MXGanttModel> modelFutre, final IMXActivityPropertyInfo actproptinfo, final String projectId, final String propName, final String propValue, final String frame)\n
    '''
def getLayoutUI():
    '''returns JSONObject\n\n
    getLayoutUI(final WebClientSession sess, @MXEventParam("appname") final String appName, @MXEventParam("projectid") final String projectId)\n
    '''
def loadSchedulerProject():
    '''returns None\n\n
    loadSchedulerProject(final WebClientSession sess)\n
    '''
def processChange():
    '''returns None\n\n
    processChange(final Future<MXGanttModel> model, final JSONObject change, final WebClientSession sess, final ReplyBuilder reply)\n
    '''
def markAssignmentDelete():
    '''returns None\n\n
    markAssignmentDelete(final Future<MXGanttModel> modelFuture, final JSONObject obj, final MXActivity act)\n
    '''
def getLastKnownState():
    '''returns String\n\n
    getLastKnownState()\n
    '''
def async_upload_state():
    '''returns JSONObject\n\n
    async_upload_state(final WebClientSession sess, @MXEventParam("cfgid") final String cfgid, @MXEventParam("cookie") final String cookie)\n
    '''
