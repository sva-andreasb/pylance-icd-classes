CONTENT_TYPES_PART_NAME = "String  \"[Content_Types].xml\""
TYPES_NAMESPACE_URI = "String  \"http://schemas.openxmlformats.org/package/2006/content-types\""
def ():
    '''returns ContentTypeManager\n\n
    (final InputStream in, final OPCPackage pkg)\n
    '''
def addContentType():
    '''returns None\n\n
    addContentType(final PackagePartName partName, final String contentType)\n
    '''
def removeContentType():
    '''returns None\n\n
    removeContentType(final PackagePartName partName)\n
    '''
def isContentTypeRegister():
    '''returns boolean\n\n
    isContentTypeRegister(final String contentType)\n
    '''
def getContentType():
    '''returns String\n\n
    getContentType(final PackagePartName partName)\n
    '''
def clearAll():
    '''returns None\n\n
    clearAll()\n
    '''
def clearOverrideContentTypes():
    '''returns None\n\n
    clearOverrideContentTypes()\n
    '''
def save():
    '''returns boolean\n\n
    save(final OutputStream outStream)\n
    '''
