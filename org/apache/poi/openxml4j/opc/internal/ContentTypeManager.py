CONTENT_TYPES_PART_NAME = "String  \"[Content_Types].xml\""
TYPES_NAMESPACE_URI = "String  \"http://schemas.openxmlformats.org/package/2006/content-types\""
def ContentTypeManager():
    '''public ContentTypeManager(final InputStream in, final OPCPackage pkg)
    '''
def addContentType():
    '''public void addContentType(final PackagePartName partName, final String contentType)
    '''
def removeContentType():
    '''public void removeContentType(final PackagePartName partName)
    '''
def isContentTypeRegister():
    '''public boolean isContentTypeRegister(final String contentType)
    '''
def getContentType():
    '''public String getContentType(final PackagePartName partName)
    '''
def clearAll():
    '''public void clearAll()
    '''
def clearOverrideContentTypes():
    '''public void clearOverrideContentTypes()
    '''
def save():
    '''public boolean save(final OutputStream outStream)
    '''
