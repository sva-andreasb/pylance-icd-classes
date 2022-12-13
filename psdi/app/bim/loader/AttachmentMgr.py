PROP_MAX_FILE_SIZE = "String  mxe.doclink.maxfilesize""
PROP_DEF_PATH = "String  mxe.doclink.doctypes.defpath""
PROP_ALLOWED_EXTENSIONS = "String  mxe.doclink.doctypes.allowedFileExtensions""
PROP_PRINT_WITH_REPORT = "String  mxe.doclink.defaultPrintDocWithReport""
TABLE_DOCINFO = "String  DOCINFO""
RELATIONSHIP_DOCINFO = "String  DOCINFO""
RELATIONSHIP_DOCLINKS = "String  DOCLINKS""
FIELD_DESCRIPTION = "String  DESCRIPTION""
FIELD_DOCINFOID = "String  DOCINFOID""
FIELD_DOCUMENT = "String  DOCUMENT""
FIELD_DOCTYPE = "String  DOCTYPE""
FIELD_NEWURLNAME = "String  NEWURLNAME""
FIELD_PRINTTHRULINKDFLT = "String  PRINTTHRULINKDFLT""
FIELD_PRINTTHRULINK = "String  PRINTTHRULINK""
FIELD_URLNAME = "String  URLNAME""
FIELD_URLTYPE = "String  URLTYPE""
FIELD_WEBURL = "String  WEBURL""
FIELD_ADDINFO = "String  ADDINFO""
FIELD_OWNERTABLE = "String  OWNERTABLE""
FIELD_GETLATESTVERSION = "String  GETLATESTVERSION""
DOCTYPE_ATTACHMENTS = "String  Attachments""
DOCTYPE_DIAGRAMS = "String  Diagrams""
DOCTYPE_IMAGES = "String  Images""
URL_TYPE_FILE = "String  FILE""
FILE_DOES_NOT_EXIST = "int  0"
FILE_EXISTS_AND_MATCHES = "int  1"
FILE_EXISTS_AND_DOES_NOT_MATCH = "int  2"
TABLE_DOCTYPES = "String  DOCTYPES""
FIELD_APP = "String  APP""
FIELD_DEFAULTFILEPATH = "String  DEFAULTFILEPATH""
def AttachmentMgr():
'''public AttachmentMgr(final ProgressLogger<ItemFACILITY> logger, final MboRemote projectMbo)
'''
pass
def getOwningTable():
'''public String getOwningTable(final Item item)
'''
pass
def getPathForDocType():
'''public String getPathForDocType(final String name)
'''
pass
def getRootDir():
'''public String getRootDir()
'''
pass
def getProjectDocDir():
'''public String getProjectDocDir()
'''
pass
def getAllowedExtensions():
'''public String[] getAllowedExtensions()
'''
pass
def getMaxFileSize():
'''public long getMaxFileSize()
'''
pass
def isPrintWithReport():
'''public boolean isPrintWithReport()
'''
pass
def getAttachmentFileName():
'''public String getAttachmentFileName(final Item item, final ItemDOCUMENT doc)
'''
pass
def testFileMatch():
'''public int testFileMatch(final String cobieFileName, final String maximoFileName)
'''
pass
def copyFile():
'''public void copyFile(final Item item, final String source, final String destination)
public void copyFile(final String source, final String destination)
'''
pass
def deleteFiles():
'''public void deleteFiles()
'''
pass
def findDocInfo():
'''public MboRemote findDocInfo(final String maximoFileName, final String docName)
'''
pass
def getMD5Checksum():
'''public static String getMD5Checksum(final String filename)
'''
pass
def getApp():
'''public String getApp()
'''
pass
def getDescription():
'''public String getDescription()
'''
pass
def getPath():
'''public String getPath()
'''
pass
def getType():
'''public String getType()
'''
pass
