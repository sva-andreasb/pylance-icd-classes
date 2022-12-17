COPYRIGHT = "String  \"IBM Confidential OCO Source Material\n5725-E24 (C) COPYRIGHT International Business Machines Corp. 2007, 2017\nThe source code for this program is not published or otherwise divested\nof its trade secrets, irrespective of what has been deposited with the\nU.S. Copyright Office.\""
DEFAULT_APPID = "String  \"srmssctr\""
SELF_SERVICE_CENTER_APP_NAME = "String  \"SRMSSCTR\""
OFFERINGS_APP_NAME = "String  \"PMSCOFFER\""
VIEW_APPROVAL_APP = "String  \"VIEWAPPRSR\""
def ():
    '''returns PmScInputSpecBean\n\n
    ()\n
    '''
def setupBean():
    '''returns None\n\n
    setupBean(final WebClientSession wcs)\n
    '''
def setMboSet():
    '''returns None\n\n
    setMboSet(final MboSetRemote mboSet)\n
    setMboSet(final PmScCRSpecSetRemote specSet)\n
    '''
def callMethod():
    '''returns int\n\n
    callMethod(final WebClientEvent event)\n
    '''
def cancelClicked():
    '''returns int\n\n
    cancelClicked()\n
    '''
def okClicked():
    '''returns int\n\n
    okClicked()\n
    '''
def shippingInfo():
    '''returns int\n\n
    shippingInfo()\n
    '''
def quickorder():
    '''returns int\n\n
    quickorder()\n
    '''
def opencrdr():
    '''returns int\n\n
    opencrdr()\n
    '''
def addtocart():
    '''returns None\n\n
    addtocart(final boolean submitCart, PmScCRSpecRemote crSpec)\n
    '''
def setValue():
    '''returns None\n\n
    setValue(final int row, final String attribute, final MboRemote mboRemote)\n
    '''
def submit():
    '''returns None\n\n
    submit(final PmScCRRemote cr)\n
    '''
def execute():
    '''returns int\n\n
    execute()\n
    '''
def launchActionServices():
    '''returns None\n\n
    launchActionServices(final OfferingRemote off, final CatalogRemote catmbo)\n
    '''
def launchWF():
    '''returns None\n\n
    launchWF(final OfferingRemote off, final long crid)\n
    '''
def deletefav():
    '''returns int\n\n
    deletefav()\n
    '''
def deleteFromFavorites():
    '''returns None\n\n
    deleteFromFavorites(final UserInfo userInfo, final OfferingRemote offering)\n
    '''
def addtofav():
    '''returns int\n\n
    addtofav()\n
    '''
def addToFavorites():
    '''returns None\n\n
    addToFavorites(final UserInfo userInfo, final OfferingRemote offering)\n
    '''
def cancelDialog():
    '''returns int\n\n
    cancelDialog()\n
    '''
def checkForAppError():
    '''returns None\n\n
    checkForAppError()\n
    '''
def validateTemplateOffering():
    '''returns String\n\n
    validateTemplateOffering(final MboRemote offering, final PageInstance dialog, final String dialogId, final SRRemote sr, final boolean findAll)\n
    '''
def getTicketSpec():
    '''returns int\n\n
    getTicketSpec(final String offeringattr)\n
    '''
def getERMAttr():
    '''returns UIERMAttribute\n\n
    getERMAttr(final String offeringattr, final int ticketspecid, final PmScCRSpecRemote crSpec)\n
    '''
def getExtendedToolTip():
    '''returns JSONObject\n\n
    getExtendedToolTip(final JSONObject definition)\n
    '''
