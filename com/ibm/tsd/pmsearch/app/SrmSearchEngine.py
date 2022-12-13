MAX_COUNT = "String GlobalSearch.maxCount""
ENABLE_UNPERSIST_FIELD = "String GlobalSearch.enable.unpersist.field""
DEFAULT_COUNT = "String 500""
CONTENTS = "String contents""
FILE = "String file""
OFFER_MBO_CLASS = "String offer""
CATALOG_MBO_CLASS = "String catalog""
CATALOG_REQUEST_MBO_CLASS = "String catalogRequest""
TICKET_TEMPLATE_MBO_CLASS = "String tktemplate""
DEFAULT_ENCODING = "String UTF-8""
MAX_FILE_LENGTH_KEY = "String PmObjSearchCron.maxFileLength""
DEFAULT_MAX_FILE_LENGTH = "String 1000000""
STATIC_STATE_COMMENTS = "String This is an IBM generated file.  Do not modify this file.""
STATE_FILENAME = "String srm.properties""
SR_LAST_SUCCESS_DATE = "String sr.success.date""
INC_LAST_SUCCESS_DATE = "String incident.success.date""
PRB_LAST_SUCCESS_DATE = "String problem.success.date""
SOLN_LAST_SUCCESS_DATE = "String solution.success.date""
BB_LAST_SUCCESS_DATE = "String bb.success.date""
TKTEMPLATE_LAST_SUCCESS_DATE = "String tktemplate.success.date""
CAT_LAST_SUCCESS_DATE = "String catalog.success.date""
CATREQ_LAST_SUCCESS_DATE = "String catalogreq.success.date""
LWDICT = "String LWDICT""
LUCENEOBJINDEX = "String LUCENEOBJINDEX""
LUCENEFLDCHG = "String LUCENEFLDCHG""
DESCRIPTION = "String description""
SOLUTIONID = "String solutionid""
SOLUTION = "String solution""
SUBJECT = "String subject""
MESSAGE = "String message""
BULLETINBOARDID = "String bulletinboardid""
BULLETINBOARDUID = "String bulletinboarduid""
INCIDENTID = "String incidentid""
INCIDENT = "String incident""
TYPE = "String type""
CLASSIFICATION = "String classification""
STATUS = "String status""
PROBLEMCODE = "String problemcode_longdescription""
FR1CODE = "String fr1code_longdescription""
FR2CODE = "String fr2code_longdescription""
DESCRIPTION_LD = "String description_longdescription""
TICKETID = "String ticketid""
TICKETUID = "String ticketuid""
CLASS_STR = "String class""
CLASSSTRUCTUREID = "String classstructureid""
OWNERID = "String ownerid""
ITEMID = "String itemid""
TEMPLATEID = "String tktemplateid""
ITEMNUM = "String ITEMNUM""
PMSCCRID = "String PMSCCRID""
PMSCCRID_OLD = "String mrid""
KEYWORD = "String keyword""
LANGUAGE_CODE_KEY = "String langcode""
EMPTY_STRING = "String "
ALLKEYWORDS = "String allkeywords""
def SrmSearchEngine():
'''public SrmSearchEngine(final MboRemote refMbo)
public SrmSearchEngine(final MboRemote refMbo, final boolean useSpecialChars)
'''
pass
def isCatalogInstalled():
'''public static boolean isCatalogInstalled(final MboRemote refMbo)
'''
pass
def isDeskInstalled():
'''public static boolean isDeskInstalled(final MboRemote refMbo)
'''
pass
def isSolutionInstalled():
'''public static boolean isSolutionInstalled(final MboRemote refMbo)
'''
pass
def isServiceProviderInstalled():
'''public static boolean isServiceProviderInstalled(final MboRemote refMbo)
'''
pass
def createIndexingSearch():
'''public void createIndexingSearch()
'''
pass
def simpleSearch():
'''public String simpleSearch(final String textSearch, final SearchConfigValues mboSearched, final List<SearchConfigValues> attributesSearched)
'''
pass
def searchAttachments():
'''public Map<SearchConfigValues, String> searchAttachments(final String textSearch, final long tktuid)
'''
pass
def searchStoringAttachments():
'''public Map<SearchConfigValues, String> searchStoringAttachments(final String textSearch, final List<String> configSearch, final long tktuid)
'''
pass
def search():
'''public Map<SearchConfigValues, String> search(final String textSearch, final List<String> configSearch, final int tktuid)
'''
pass
def searchFull():
'''public Map<SearchConfigValues, String> searchFull(String textSearch, final List<String> configSearch, final int tktuid)
'''
pass
def getLastUpdateDateWhereclause():
'''public String getLastUpdateDateWhereclause(final String luceneEntityKey)
'''
pass
def isOKToRun():
'''public boolean isOKToRun()
'''
pass
def getLanguageForSearch():
'''public String getLanguageForSearch()
'''
pass
def getErrorMessageForThrowable():
'''public static final String getErrorMessageForThrowable(final Throwable t)
'''
pass
def getAllSDAttrbts():
'''public List<String> getAllSDAttrbts()
'''
pass
def getAttributeTitle():
'''public String getAttributeTitle(final String attributeName)
'''
pass
def getSolutionAttrbtsList():
'''public List<String> getSolutionAttrbtsList()
'''
pass
def setSolutionAttrbtsList():
'''public void setSolutionAttrbtsList(final List<String> solutionAttrbtsList)
'''
pass
def getTicktAttrbts():
'''public List<String> getTicktAttrbts()
'''
pass
def setTicktAttrbts():
'''public void setTicktAttrbts(final List<String> ticktAttrbts)
'''
pass
def getBbAttrbts():
'''public List<String> getBbAttrbts()
'''
pass
def setBbAttrbts():
'''public void setBbAttrbts(final List<String> bbAttrbts)
'''
pass
def classifierSearch():
'''public List<ClassProb> classifierSearch(final String textSearch, final SrmClassifierFilter filter, final boolean addClass)
'''
pass
def getSession():
'''public MXSession getSession()
'''
pass
def setSession():
'''public void setSession(final MXSession session)
'''
pass
def getQualifiedWhere():
'''public String getQualifiedWhere(final String mboName)
'''
pass
def isUpgradedVersion():
'''public boolean isUpgradedVersion()
'''
pass
def checkOldMbo():
'''public boolean checkOldMbo(final String mboName)
'''
pass
def getAttachmentNameFromID():
'''public String getAttachmentNameFromID(final String mboName, final String id)
'''
pass
def setAttachmentFileName():
'''public void setAttachmentFileName(final MboSetRemote mboSet, final String mboName, final String mboIdName)
'''
pass
def setMboSetScore():
'''public void setMboSetScore(final MboSetRemote mboSet, final String keyName)
'''
pass
