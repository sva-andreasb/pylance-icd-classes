CONTENT_TYPE = "String  \"text/html\""
def ():
    '''returns HtmlDocWriter\n\n
    (final Configuration configuration, final DocPath docPath)\n
    '''
def getHyperLink():
    '''returns Content\n\n
    getHyperLink(final DocPath docPath, final String s)\n
    getHyperLink(final String s, final Content content)\n
    getHyperLink(final SectionName sectionName, final Content content)\n
    getHyperLink(final SectionName sectionName, final String s, final Content content)\n
    getHyperLink(final DocPath docPath, final Content content)\n
    getHyperLink(final DocLink docLink, final Content content)\n
    getHyperLink(final DocPath docPath, final Content content, final boolean b, final String s, final String s2, final String s3)\n
    getHyperLink(final DocLink docLink, final Content content, final boolean b, final String s, final String s2, final String s3)\n
    getHyperLink(final DocPath docPath, final Content content, final String s, final String s2)\n
    getHyperLink(final DocLink docLink, final Content content, final String s, final String s2)\n
    '''
def getDocLink():
    '''returns DocLink\n\n
    getDocLink(final String s)\n
    getDocLink(final SectionName sectionName)\n
    getDocLink(final SectionName sectionName, final String s)\n
    '''
def getName():
    '''returns String\n\n
    getName(final String s)\n
    '''
def getPkgName():
    '''returns String\n\n
    getPkgName(final ClassDoc classDoc)\n
    '''
def getMemberDetailsListPrinted():
    '''returns boolean\n\n
    getMemberDetailsListPrinted()\n
    '''
def printFramesetDocument():
    '''returns None\n\n
    printFramesetDocument(final String s, final boolean b, final Content content)\n
    '''
