MAX_COUNT = "String  \"GlobalSearch.maxCount\""
ENABLE_UNPERSIST_FIELD = "String  \"GlobalSearch.enable.unpersist.field\""
DEFAULT_COUNT = "String  \"500\""
CONTENTS = "String  \"contents\""
FILE = "String  \"file\""
OFFER_MBO_CLASS = "String  \"offer\""
CATALOG_MBO_CLASS = "String  \"catalog\""
CATALOG_REQUEST_MBO_CLASS = "String  \"catalogRequest\""
TICKET_TEMPLATE_MBO_CLASS = "String  \"tktemplate\""
DEFAULT_ENCODING = "String  \"UTF-8\""
MAX_FILE_LENGTH_KEY = "String  \"PmObjSearchCron.maxFileLength\""
DEFAULT_MAX_FILE_LENGTH = "String  \"1000000\""
STATIC_STATE_COMMENTS = "String  \"This is an IBM generated file.  Do not modify this file.\""
STATE_FILENAME = "String  \"srm.properties\""
SR_LAST_SUCCESS_DATE = "String  \"sr.success.date\""
INC_LAST_SUCCESS_DATE = "String  \"incident.success.date\""
PRB_LAST_SUCCESS_DATE = "String  \"problem.success.date\""
SOLN_LAST_SUCCESS_DATE = "String  \"solution.success.date\""
BB_LAST_SUCCESS_DATE = "String  \"bb.success.date\""
TKTEMPLATE_LAST_SUCCESS_DATE = "String  \"tktemplate.success.date\""
CAT_LAST_SUCCESS_DATE = "String  \"catalog.success.date\""
CATREQ_LAST_SUCCESS_DATE = "String  \"catalogreq.success.date\""
LWDICT = "String  \"LWDICT\""
LUCENEOBJINDEX = "String  \"LUCENEOBJINDEX\""
LUCENEFLDCHG = "String  \"LUCENEFLDCHG\""
DESCRIPTION = "String  \"description\""
SOLUTIONID = "String  \"solutionid\""
SOLUTION = "String  \"solution\""
SUBJECT = "String  \"subject\""
MESSAGE = "String  \"message\""
BULLETINBOARDID = "String  \"bulletinboardid\""
BULLETINBOARDUID = "String  \"bulletinboarduid\""
INCIDENTID = "String  \"incidentid\""
INCIDENT = "String  \"incident\""
TYPE = "String  \"type\""
CLASSIFICATION = "String  \"classification\""
STATUS = "String  \"status\""
PROBLEMCODE = "String  \"problemcode_longdescription\""
FR1CODE = "String  \"fr1code_longdescription\""
FR2CODE = "String  \"fr2code_longdescription\""
DESCRIPTION_LD = "String  \"description_longdescription\""
TICKETID = "String  \"ticketid\""
TICKETUID = "String  \"ticketuid\""
CLASS_STR = "String  \"class\""
CLASSSTRUCTUREID = "String  \"classstructureid\""
OWNERID = "String  \"ownerid\""
ITEMID = "String  \"itemid\""
TEMPLATEID = "String  \"tktemplateid\""
ITEMNUM = "String  \"ITEMNUM\""
PMSCCRID = "String  \"PMSCCRID\""
PMSCCRID_OLD = "String  \"mrid\""
KEYWORD = "String  \"keyword\""
LANGUAGE_CODE_KEY = "String  \"langcode\""
EMPTY_STRING = "String  \"\""
ALLKEYWORDS = "String  \"allkeywords\""
def ():
    '''returns SrmSearchEngine\n\n
    (final MboRemote refMbo)\n
    (final MboRemote refMbo, final boolean useSpecialChars)\n
    '''
def createIndexingSearch():
    '''returns None\n\n
    createIndexingSearch()\n
    '''
def simpleSearch():
    '''returns String\n\n
    simpleSearch(final String textSearch, final SearchConfigValues mboSearched, final List<SearchConfigValues> attributesSearched)\n
    '''
def getLastUpdateDateWhereclause():
    '''returns String\n\n
    getLastUpdateDateWhereclause(final String luceneEntityKey)\n
    '''
def isOKToRun():
    '''returns boolean\n\n
    isOKToRun()\n
    '''
def getLanguageForSearch():
    '''returns String\n\n
    getLanguageForSearch()\n
    '''
def getAllSDAttrbts():
    '''returns List<String>\n\n
    getAllSDAttrbts()\n
    '''
def getAttributeTitle():
    '''returns String\n\n
    getAttributeTitle(final String attributeName)\n
    '''
def getSolutionAttrbtsList():
    '''returns List<String>\n\n
    getSolutionAttrbtsList()\n
    '''
def setSolutionAttrbtsList():
    '''returns None\n\n
    setSolutionAttrbtsList(final List<String> solutionAttrbtsList)\n
    '''
def getTicktAttrbts():
    '''returns List<String>\n\n
    getTicktAttrbts()\n
    '''
def setTicktAttrbts():
    '''returns None\n\n
    setTicktAttrbts(final List<String> ticktAttrbts)\n
    '''
def getBbAttrbts():
    '''returns List<String>\n\n
    getBbAttrbts()\n
    '''
def setBbAttrbts():
    '''returns None\n\n
    setBbAttrbts(final List<String> bbAttrbts)\n
    '''
def classifierSearch():
    '''returns List<ClassProb>\n\n
    classifierSearch(final String textSearch, final SrmClassifierFilter filter, final boolean addClass)\n
    '''
def getSession():
    '''returns MXSession\n\n
    getSession()\n
    '''
def setSession():
    '''returns None\n\n
    setSession(final MXSession session)\n
    '''
def getQualifiedWhere():
    '''returns String\n\n
    getQualifiedWhere(final String mboName)\n
    '''
def isUpgradedVersion():
    '''returns boolean\n\n
    isUpgradedVersion()\n
    '''
def checkOldMbo():
    '''returns boolean\n\n
    checkOldMbo(final String mboName)\n
    '''
def getAttachmentNameFromID():
    '''returns String\n\n
    getAttachmentNameFromID(final String mboName, final String id)\n
    '''
def setAttachmentFileName():
    '''returns None\n\n
    setAttachmentFileName(final MboSetRemote mboSet, final String mboName, final String mboIdName)\n
    '''
def setMboSetScore():
    '''returns None\n\n
    setMboSetScore(final MboSetRemote mboSet, final String keyName)\n
    '''
