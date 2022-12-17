FIELD_TYPE_NONE = "int  0"
FIELD_TYPE_PUSHBUTTON = "int  1"
FIELD_TYPE_CHECKBOX = "int  2"
FIELD_TYPE_RADIOBUTTON = "int  3"
FIELD_TYPE_TEXT = "int  4"
FIELD_TYPE_LIST = "int  5"
FIELD_TYPE_COMBO = "int  6"
FIELD_TYPE_SIGNATURE = "int  7"
def getAppearanceStates():
    '''returns String[]\n\n
    getAppearanceStates(final String fieldName)\n
    '''
def getFieldType():
    '''returns int\n\n
    getFieldType(final String fieldName)\n
    '''
def exportAsFdf():
    '''returns None\n\n
    exportAsFdf(final FdfWriter writer)\n
    '''
def renameField():
    '''returns boolean\n\n
    renameField(final String oldName, String newName)\n
    '''
def getField():
    '''returns String\n\n
    getField(final String name)\n
    '''
def setFieldProperty():
    '''returns boolean\n\n
    setFieldProperty(final String field, final String name, final Object value, final int[] inst)\n
    setFieldProperty(final String field, final String name, final int value, final int[] inst)\n
    '''
def setFields():
    '''returns None\n\n
    setFields(final FdfReader fdf)\n
    setFields(final XfdfReader xfdf)\n
    '''
def setField():
    '''returns boolean\n\n
    setField(final String name, final String value)\n
    setField(final String name, String value, final String display)\n
    '''
def getFields():
    '''returns HashMap\n\n
    getFields()\n
    '''
def getFieldItem():
    '''returns Item\n\n
    getFieldItem(final String name)\n
    '''
def getFieldPositions():
    '''returns float[]\n\n
    getFieldPositions(final String name)\n
    '''
def removeFieldsFromPage():
    '''returns boolean\n\n
    removeFieldsFromPage(final int page)\n
    '''
def removeField():
    '''returns boolean\n\n
    removeField(final String name, final int page)\n
    removeField(final String name)\n
    '''
def isGenerateAppearances():
    '''returns boolean\n\n
    isGenerateAppearances()\n
    '''
def setGenerateAppearances():
    '''returns None\n\n
    setGenerateAppearances(final boolean generateAppearances)\n
    '''
def getSignatureNames():
    '''returns ArrayList\n\n
    getSignatureNames()\n
    '''
def getBlankSignatureNames():
    '''returns ArrayList\n\n
    getBlankSignatureNames()\n
    '''
def getSignatureDictionary():
    '''returns PdfDictionary\n\n
    getSignatureDictionary(final String name)\n
    '''
def signatureCoversWholeDocument():
    '''returns boolean\n\n
    signatureCoversWholeDocument(final String name)\n
    '''
def verifySignature():
    '''returns PdfPKCS7\n\n
    verifySignature(final String name)\n
    verifySignature(final String name, final String provider)\n
    '''
def getTotalRevisions():
    '''returns int\n\n
    getTotalRevisions()\n
    '''
def getRevision():
    '''returns int\n\n
    getRevision(final String field)\n
    '''
def extractRevision():
    '''returns InputStream\n\n
    extractRevision(final String field)\n
    '''
def getFieldCache():
    '''returns HashMap\n\n
    getFieldCache()\n
    '''
def setFieldCache():
    '''returns None\n\n
    setFieldCache(final HashMap fieldCache)\n
    '''
def ():
    '''returns InstHit\n\n
    ()\n
    (final int[] inst)\n
    '''
def isHit():
    '''returns boolean\n\n
    isHit(final int n)\n
    '''
def read():
    '''returns int\n\n
    read()\n
    read(final byte[] b, final int off, final int len)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def compare():
    '''returns int\n\n
    compare(final Object o1, final Object o2)\n
    '''
