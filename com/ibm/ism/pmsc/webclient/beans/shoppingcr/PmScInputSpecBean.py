COPYRIGHT = "String  IBM Confidential OCO Source Material\n5725-E24 (C) COPYRIGHT International Business Machines Corp. 2007, 2017\nThe source code for this program is not published or otherwise divested\nof its trade secrets, irrespective of what has been deposited with the\nU.S. Copyright Office.""
DEFAULT_APPID = "String  srmssctr""
SELF_SERVICE_CENTER_APP_NAME = "String  SRMSSCTR""
OFFERINGS_APP_NAME = "String  PMSCOFFER""
VIEW_APPROVAL_APP = "String  VIEWAPPRSR""
def PmScInputSpecBean():
'''public PmScInputSpecBean()
'''
pass
def setupBean():
'''public void setupBean(final WebClientSession wcs)
'''
pass
def setMboSet():
'''public void setMboSet(final MboSetRemote mboSet)
public void setMboSet(final PmScCRSpecSetRemote specSet)
'''
pass
def callMethod():
'''public int callMethod(final WebClientEvent event)
'''
pass
def cancelClicked():
'''public int cancelClicked()
'''
pass
def okClicked():
'''public int okClicked()
'''
pass
def shippingInfo():
'''public int shippingInfo()
'''
pass
def quickorder():
'''public int quickorder()
'''
pass
def opencrdr():
'''public int opencrdr()
'''
pass
def addtocart():
'''public void addtocart(final boolean submitCart, PmScCRSpecRemote crSpec)
'''
pass
def setValue():
'''public void setValue(final int row, final String attribute, final MboRemote mboRemote)
public synchronized void setValue(final int nRow, final String attribute, final String value, final long accessModifier)
public synchronized void setValue(final String attribute, final MboRemote mboRemote)
'''
pass
def submit():
'''public void submit(final PmScCRRemote cr)
'''
pass
def execute():
'''public int execute()
'''
pass
def launchActionServices():
'''public void launchActionServices(final OfferingRemote off, final CatalogRemote catmbo)
'''
pass
def launchWF():
'''public void launchWF(final OfferingRemote off, final long crid)
'''
pass
def deletefav():
'''public int deletefav()
'''
pass
def deleteFromFavorites():
'''public void deleteFromFavorites(final UserInfo userInfo, final OfferingRemote offering)
'''
pass
def addtofav():
'''public int addtofav()
'''
pass
def addToFavorites():
'''public void addToFavorites(final UserInfo userInfo, final OfferingRemote offering)
'''
pass
def cancelDialog():
'''public int cancelDialog()
'''
pass
def checkForAppError():
'''public void checkForAppError()
'''
pass
def validateTemplateOffering():
'''public String validateTemplateOffering(final MboRemote offering, final PageInstance dialog, final String dialogId, final SRRemote sr, final boolean findAll)
'''
pass
def getTicketSpec():
'''public int getTicketSpec(final String offeringattr)
'''
pass
def getERMAttr():
'''public UIERMAttribute getERMAttr(final String offeringattr, final int ticketspecid, final PmScCRSpecRemote crSpec)
'''
pass
def getExtendedToolTip():
'''public JSONObject getExtendedToolTip(final JSONObject definition)
'''
pass
