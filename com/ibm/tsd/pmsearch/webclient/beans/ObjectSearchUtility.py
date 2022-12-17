ORACLEDB = "int  1"
SQLSERVERDB = "int  2"
DB2DB = "int  3"
def ():
    '''returns ObjectSearchUtility\n\n
    ()\n
    '''
def newincidentsearch():
    '''returns int\n\n
    newincidentsearch(final AppInstance app, final MboRemote mbo, final MXSession session)\n
    '''
def newsrsearch():
    '''returns int\n\n
    newsrsearch(final AppInstance app, final MboRemote mbo, final MXSession session)\n
    '''
def newproblemsearch():
    '''returns int\n\n
    newproblemsearch(final AppInstance app, final MboRemote mbo, final MXSession session)\n
    '''
def newsolutionsearch():
    '''returns int\n\n
    newsolutionsearch(final AppInstance app, final MboRemote mbo, final MXSession session)\n
    '''
def newkmsearch():
    '''returns int\n\n
    newkmsearch(final WebClientSession session, final AppInstance app)\n
    '''
def setQbe():
    '''returns None\n\n
    setQbe(final WebClientSession clientSession, final AppInstance app, final DataBean bean, final String attribute, final String expression, final boolean propagateQbe)\n
    setQbe(final WebClientSession clientSession, final AppInstance app, final DataBean bean, final String attribute, final MboSetRemote expression, final boolean propagateQbe)\n
    '''
