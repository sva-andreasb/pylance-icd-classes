PROP_MAX_FILE_SIZE = "String  \"mxe.doclink.maxfilesize\""
PROP_DEF_PATH = "String  \"mxe.doclink.doctypes.defpath\""
PROP_ALLOWED_EXTENSIONS = "String  \"mxe.doclink.doctypes.allowedFileExtensions\""
PROP_PRINT_WITH_REPORT = "String  \"mxe.doclink.defaultPrintDocWithReport\""
TABLE_DOCINFO = "String  \"DOCINFO\""
RELATIONSHIP_DOCINFO = "String  \"DOCINFO\""
RELATIONSHIP_DOCLINKS = "String  \"DOCLINKS\""
FIELD_DESCRIPTION = "String  \"DESCRIPTION\""
FIELD_DOCINFOID = "String  \"DOCINFOID\""
FIELD_DOCUMENT = "String  \"DOCUMENT\""
FIELD_DOCTYPE = "String  \"DOCTYPE\""
FIELD_NEWURLNAME = "String  \"NEWURLNAME\""
FIELD_PRINTTHRULINKDFLT = "String  \"PRINTTHRULINKDFLT\""
FIELD_PRINTTHRULINK = "String  \"PRINTTHRULINK\""
FIELD_URLNAME = "String  \"URLNAME\""
FIELD_URLTYPE = "String  \"URLTYPE\""
FIELD_WEBURL = "String  \"WEBURL\""
FIELD_ADDINFO = "String  \"ADDINFO\""
FIELD_OWNERTABLE = "String  \"OWNERTABLE\""
FIELD_GETLATESTVERSION = "String  \"GETLATESTVERSION\""
DOCTYPE_ATTACHMENTS = "String  \"Attachments\""
DOCTYPE_DIAGRAMS = "String  \"Diagrams\""
DOCTYPE_IMAGES = "String  \"Images\""
URL_TYPE_FILE = "String  \"FILE\""
FILE_DOES_NOT_EXIST = "int  0"
FILE_EXISTS_AND_MATCHES = "int  1"
FILE_EXISTS_AND_DOES_NOT_MATCH = "int  2"
TABLE_DOCTYPES = "String  \"DOCTYPES\""
FIELD_APP = "String  \"APP\""
FIELD_DEFAULTFILEPATH = "String  \"DEFAULTFILEPATH\""
def ():
    '''returns AttachmentMgr\n\n
    (final ProgressLogger<ItemFACILITY> logger, final MboRemote projectMbo)\n
    '''
def getOwningTable():
    '''returns String\n\n
    getOwningTable(final Item item)\n
    '''
def getPathForDocType():
    '''returns String\n\n
    getPathForDocType(final String name)\n
    '''
def getRootDir():
    '''returns String\n\n
    getRootDir()\n
    '''
def getProjectDocDir():
    '''returns String\n\n
    getProjectDocDir()\n
    '''
def getAllowedExtensions():
    '''returns String[]\n\n
    getAllowedExtensions()\n
    '''
def getMaxFileSize():
    '''returns long\n\n
    getMaxFileSize()\n
    '''
def isPrintWithReport():
    '''returns boolean\n\n
    isPrintWithReport()\n
    '''
def getAttachmentFileName():
    '''returns String\n\n
    getAttachmentFileName(final Item item, final ItemDOCUMENT doc)\n
    '''
def testFileMatch():
    '''returns int\n\n
    testFileMatch(final String cobieFileName, final String maximoFileName)\n
    '''
def copyFile():
    '''returns None\n\n
    copyFile(final Item item, final String source, final String destination)\n
    copyFile(final String source, final String destination)\n
    '''
def deleteFiles():
    '''returns None\n\n
    deleteFiles()\n
    '''
def findDocInfo():
    '''returns MboRemote\n\n
    findDocInfo(final String maximoFileName, final String docName)\n
    '''
def getApp():
    '''returns String\n\n
    getApp()\n
    '''
def getDescription():
    '''returns String\n\n
    getDescription()\n
    '''
def getPath():
    '''returns String\n\n
    getPath()\n
    '''
def getType():
    '''returns String\n\n
    getType()\n
    '''
