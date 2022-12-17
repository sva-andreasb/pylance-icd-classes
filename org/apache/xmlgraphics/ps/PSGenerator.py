DEFAULT_LANGUAGE_LEVEL = "int  3"
LF = "char  '\n'"
def ():
    '''returns PSGenerator\n\n
    (final OutputStream out)\n
    '''
def isCompactMode():
    '''returns boolean\n\n
    isCompactMode()\n
    '''
def setCompactMode():
    '''returns None\n\n
    setCompactMode(final boolean value)\n
    '''
def isCommentsEnabled():
    '''returns boolean\n\n
    isCommentsEnabled()\n
    '''
def setCommentsEnabled():
    '''returns None\n\n
    setCommentsEnabled(final boolean value)\n
    '''
def getOutputStream():
    '''returns OutputStream\n\n
    getOutputStream()\n
    '''
def getPSLevel():
    '''returns int\n\n
    getPSLevel()\n
    '''
def setPSLevel():
    '''returns None\n\n
    setPSLevel(final int level)\n
    '''
def resolveURI():
    '''returns Source\n\n
    resolveURI(final String uri)\n
    '''
def formatDouble():
    '''returns String\n\n
    formatDouble(final double value)\n
    '''
def formatDouble5():
    '''returns String\n\n
    formatDouble5(final double value)\n
    '''
def write():
    '''returns None\n\n
    write(final String cmd)\n
    write(final int n)\n
    '''
def writeln():
    '''returns None\n\n
    writeln(final String cmd)\n
    '''
def commentln():
    '''returns None\n\n
    commentln(final String comment)\n
    '''
def mapCommand():
    '''returns String\n\n
    mapCommand(final String command)\n
    '''
def writeByteArr():
    '''returns None\n\n
    writeByteArr(final byte[] cmd)\n
    '''
def flush():
    '''returns None\n\n
    flush()\n
    '''
def writeDSCComment():
    '''returns None\n\n
    writeDSCComment(final String name)\n
    writeDSCComment(final String name, final Object param)\n
    writeDSCComment(final String name, final Object[] params)\n
    '''
def saveGraphicsState():
    '''returns None\n\n
    saveGraphicsState()\n
    '''
def restoreGraphicsState():
    '''returns boolean\n\n
    restoreGraphicsState()\n
    '''
def getCurrentState():
    '''returns PSState\n\n
    getCurrentState()\n
    '''
def showPage():
    '''returns None\n\n
    showPage()\n
    '''
def concatMatrix():
    '''returns None\n\n
    concatMatrix(final double a, final double b, final double c, final double d, final double e, final double f)\n
    concatMatrix(final double[] matrix)\n
    concatMatrix(final AffineTransform at)\n
    '''
def formatMatrix():
    '''returns String\n\n
    formatMatrix(final AffineTransform at)\n
    '''
def formatRectangleToArray():
    '''returns String\n\n
    formatRectangleToArray(final Rectangle2D rect)\n
    '''
def defineRect():
    '''returns None\n\n
    defineRect(final double x, final double y, final double w, final double h)\n
    '''
def useLineCap():
    '''returns None\n\n
    useLineCap(final int linecap)\n
    '''
def useLineJoin():
    '''returns None\n\n
    useLineJoin(final int linejoin)\n
    '''
def useMiterLimit():
    '''returns None\n\n
    useMiterLimit(final float miterlimit)\n
    '''
def useLineWidth():
    '''returns None\n\n
    useLineWidth(final double width)\n
    '''
def useDash():
    '''returns None\n\n
    useDash(String pattern)\n
    '''
def useRGBColor():
    '''returns None\n\n
    useRGBColor(final Color col)\n
    '''
def useColor():
    '''returns None\n\n
    useColor(final Color col)\n
    '''
def useFont():
    '''returns None\n\n
    useFont(final String name, final float size)\n
    '''
def getResourceTracker():
    '''returns ResourceTracker\n\n
    getResourceTracker()\n
    '''
def setResourceTracker():
    '''returns None\n\n
    setResourceTracker(final ResourceTracker resTracker)\n
    '''
def notifyStartNewPage():
    '''returns None\n\n
    notifyStartNewPage()\n
    '''
def notifyResourceUsage():
    '''returns None\n\n
    notifyResourceUsage(final PSResource res, final boolean needed)\n
    '''
def writeResources():
    '''returns None\n\n
    writeResources(final boolean pageLevel)\n
    '''
def isResourceSupplied():
    '''returns boolean\n\n
    isResourceSupplied(final PSResource res)\n
    '''
def embedIdentityH():
    '''returns boolean\n\n
    embedIdentityH()\n
    '''
def getIdentityHCMapResource():
    '''returns PSResource\n\n
    getIdentityHCMapResource()\n
    '''
def getProcsetCIDInitResource():
    '''returns PSResource\n\n
    getProcsetCIDInitResource()\n
    '''
def includeProcsetCIDInitResource():
    '''returns None\n\n
    includeProcsetCIDInitResource()\n
    '''
