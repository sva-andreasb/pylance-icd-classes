DOMAIN_BIMIMPORTSTATUS = "String  BIMIMPORTSTATUS""
DOMAIN_BIMLOGLEVEL = "String  BIMLOGLEVEL""
FIELD_DELETEFILES = "String  DELETEFILES""
FIELD_ERRORCOUNT = "String  ERRORCOUNT""
FIELD_WARNINGCOUNT = "String  WARNINGCOUNT""
FIELD_IMPORTEDBY = "String  IMPORTEDBY""
FIELD_LOG = "String  LOG""
FIELD_LOGLEVEL = "String  LOGLEVEL""
FIELD_ORGID = "String  ORGID""
FIELD_PERCENTCOMP = "String  PERCENTCOMP""
FIELD_SITEID = "String  SITEID""
FIELD_STATUS = "String  STATUS""
FIELD_UPLOADTIME = "String  UPLOADTIME""
LOG_ERRORS = "long  1L"
LOG_WARNINGS = "long  2L"
LOG_MESSAGES = "long  4L"
LOG_VALIDATE = "long  256L"
LOG_ALL = "long  255L"
STATUS_NEW = "int  1"
STATUS_WORKING = "int  2"
STATUS_IMPORTING = "int  3"
STATUS_EXPORTING = "int  4"
STATUS_VALIDATING = "int  5"
STATUS_COMPLETE = "int  6"
STATUS_FAILED = "int  7"
STATUS_UPDATING = "int  8"
STATUS_MERGING = "int  9"
def ImportBase():
'''public ImportBase(final MboSet ms)
'''
pass
def add():
'''public void add()
'''
pass
def getLogLevel():
'''public long getLogLevel()
'''
pass
def isStatusCompelete():
'''public boolean isStatusCompelete()
'''
pass
def isStatusNew():
'''public boolean isStatusNew()
public boolean isStatusNew(final String value)
'''
pass
def setOptionsReadOnly():
'''public void setOptionsReadOnly()
'''
pass
def setStatus():
'''public void setStatus(final int status)
'''
pass
