def ():
    '''returns HtmlDocletWriter\n\n
    (final ConfigurationImpl configuration, final DocPath path)\n
    '''
def replaceDocRootDir():
    '''returns String\n\n
    replaceDocRootDir(final String input)\n
    '''
def getAllClassesLinkScript():
    '''returns Content\n\n
    getAllClassesLinkScript(final String str)\n
    '''
def getTagletWriterInstance():
    '''returns TagletWriter\n\n
    getTagletWriterInstance(final boolean b)\n
    '''
def getTargetPackageLink():
    '''returns Content\n\n
    getTargetPackageLink(final PackageDoc packageDoc, final String s, final Content content)\n
    '''
def getTargetProfilePackageLink():
    '''returns Content\n\n
    getTargetProfilePackageLink(final PackageDoc packageDoc, final String s, final Content content, final String s2)\n
    '''
def getTargetProfileLink():
    '''returns Content\n\n
    getTargetProfileLink(final String s, final Content content, final String s2)\n
    '''
def getTypeNameForProfile():
    '''returns String\n\n
    getTypeNameForProfile(final ClassDoc classDoc)\n
    '''
def isTypeInProfile():
    '''returns boolean\n\n
    isTypeInProfile(final ClassDoc classDoc, final int n)\n
    '''
def addClassesSummary():
    '''returns None\n\n
    addClassesSummary(final ClassDoc[] a, final String s, final String s2, final String[] array, final Content content, final int n)\n
    '''
def printHtmlDocument():
    '''returns None\n\n
    printHtmlDocument(final String[] array, final boolean b, final Content content)\n
    '''
def getWindowTitle():
    '''returns String\n\n
    getWindowTitle(String string)\n
    '''
def getUserHeaderFooter():
    '''returns Content\n\n
    getUserHeaderFooter(final boolean b)\n
    '''
def addTop():
    '''returns None\n\n
    addTop(final Content content)\n
    '''
def addBottom():
    '''returns None\n\n
    addBottom(final Content content)\n
    '''
def getNavLinkPrevious():
    '''returns Content\n\n
    getNavLinkPrevious(final DocPath docPath)\n
    '''
def getNavLinkNext():
    '''returns Content\n\n
    getNavLinkNext(final DocPath docPath)\n
    '''
def getSummaryTableHeader():
    '''returns Content\n\n
    getSummaryTableHeader(final String[] array, final String s)\n
    '''
def getTableCaption():
    '''returns Content\n\n
    getTableCaption(final Content content)\n
    '''
def getMarkerAnchor():
    '''returns Content\n\n
    getMarkerAnchor(final String s)\n
    getMarkerAnchor(final SectionName sectionName)\n
    getMarkerAnchor(final SectionName sectionName, final String s)\n
    getMarkerAnchor(final String s, Content content)\n
    '''
def getPackageName():
    '''returns Content\n\n
    getPackageName(final PackageDoc packageDoc)\n
    '''
def getPackageLabel():
    '''returns Content\n\n
    getPackageLabel(final String s)\n
    '''
def getPackageLink():
    '''returns Content\n\n
    getPackageLink(final PackageDoc packageDoc, final String s)\n
    getPackageLink(final PackageDoc obj, final Content content)\n
    '''
def italicsClassName():
    '''returns Content\n\n
    italicsClassName(final ClassDoc classDoc, final boolean b)\n
    '''
def addSrcLink():
    '''returns None\n\n
    addSrcLink(final ProgramElementDoc programElementDoc, final Content content, final Content content2)\n
    '''
def getLink():
    '''returns Content\n\n
    getLink(final LinkInfoImpl linkInfoImpl)\n
    '''
def getTypeParameterLinks():
    '''returns Content\n\n
    getTypeParameterLinks(final LinkInfoImpl linkInfoImpl)\n
    '''
def getCrossClassLink():
    '''returns Content\n\n
    getCrossClassLink(final String s, final String s2, final Content content, final boolean b, final String s3, final boolean b2)\n
    '''
def isClassLinkable():
    '''returns boolean\n\n
    isClassLinkable(final ClassDoc classDoc)\n
    '''
def getCrossPackageLink():
    '''returns DocLink\n\n
    getCrossPackageLink(final String s)\n
    '''
def getQualifiedClassLink():
    '''returns Content\n\n
    getQualifiedClassLink(final LinkInfoImpl.Kind kind, final ClassDoc classDoc)\n
    '''
def addPreQualifiedClassLink():
    '''returns None\n\n
    addPreQualifiedClassLink(final LinkInfoImpl.Kind kind, final ClassDoc classDoc, final Content content)\n
    addPreQualifiedClassLink(final LinkInfoImpl.Kind kind, final ClassDoc classDoc, final boolean b, final Content content)\n
    '''
def getPreQualifiedClassLink():
    '''returns Content\n\n
    getPreQualifiedClassLink(final LinkInfoImpl.Kind kind, final ClassDoc classDoc, final boolean b)\n
    '''
def addPreQualifiedStrongClassLink():
    '''returns None\n\n
    addPreQualifiedStrongClassLink(final LinkInfoImpl.Kind kind, final ClassDoc classDoc, final Content content)\n
    '''
def getDocLink():
    '''returns Content\n\n
    getDocLink(final LinkInfoImpl.Kind kind, final MemberDoc memberDoc, final String s)\n
    getDocLink(final LinkInfoImpl.Kind kind, final MemberDoc memberDoc, final String s, final boolean b)\n
    getDocLink(final LinkInfoImpl.Kind kind, final ClassDoc classDoc, final MemberDoc memberDoc, final String s, final boolean b)\n
    getDocLink(final LinkInfoImpl.Kind kind, final ClassDoc classDoc, final MemberDoc memberDoc, final Content content, final boolean b)\n
    getDocLink(final LinkInfoImpl.Kind kind, final ClassDoc classDoc, final MemberDoc memberDoc, final String s, final boolean b, final boolean b2)\n
    getDocLink(final LinkInfoImpl.Kind kind, final ClassDoc classDoc, final MemberDoc memberDoc, final Content content, final boolean b, final boolean b2)\n
    getDocLink(final LinkInfoImpl.Kind kind, final ClassDoc classDoc, final MemberDoc memberDoc, final Content content)\n
    '''
def getAnchor():
    '''returns String\n\n
    getAnchor(final ExecutableMemberDoc executableMemberDoc)\n
    getAnchor(final ExecutableMemberDoc executableMemberDoc, final boolean b)\n
    '''
def seeTagToContent():
    '''returns Content\n\n
    seeTagToContent(final SeeTag seeTag)\n
    '''
def addInlineComment():
    '''returns None\n\n
    addInlineComment(final Doc doc, final Tag tag, final Content content)\n
    addInlineComment(final Doc doc, final Content content)\n
    '''
def addInlineDeprecatedComment():
    '''returns None\n\n
    addInlineDeprecatedComment(final Doc doc, final Tag tag, final Content content)\n
    '''
def addSummaryComment():
    '''returns None\n\n
    addSummaryComment(final Doc doc, final Content content)\n
    addSummaryComment(final Doc doc, final Tag[] array, final Content content)\n
    '''
def addSummaryDeprecatedComment():
    '''returns None\n\n
    addSummaryDeprecatedComment(final Doc doc, final Tag tag, final Content content)\n
    '''
def commentTagsToContent():
    '''returns Content\n\n
    commentTagsToContent(final Tag tag, final Doc doc, final Tag[] array, final boolean b)\n
    '''
def getStyleSheetProperties():
    '''returns HtmlTree\n\n
    getStyleSheetProperties()\n
    '''
def getScriptProperties():
    '''returns HtmlTree\n\n
    getScriptProperties()\n
    '''
def isCoreClass():
    '''returns boolean\n\n
    isCoreClass(final ClassDoc classDoc)\n
    '''
def addAnnotationInfo():
    '''returns boolean\n\n
    addAnnotationInfo(final PackageDoc packageDoc, final Content content)\n
    addAnnotationInfo(final ProgramElementDoc programElementDoc, final Content content)\n
    addAnnotationInfo(final int n, final Doc doc, final Parameter parameter, final Content content)\n
    '''
def addReceiverAnnotationInfo():
    '''returns None\n\n
    addReceiverAnnotationInfo(final ExecutableMemberDoc executableMemberDoc, final AnnotationDesc[] array, final Content content)\n
    '''
def getAnnotations():
    '''returns List<Content>\n\n
    getAnnotations(final int n, final AnnotationDesc[] array, final boolean b, final boolean b2)\n
    '''
def configuration():
    '''returns Configuration\n\n
    configuration()\n
    '''
