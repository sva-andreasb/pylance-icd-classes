FIRST_CUSTOM_STYLE_ID = "int  165"
def setMaxNumberOfDataFormats():
    '''returns None\n\n
    setMaxNumberOfDataFormats(final int num)\n
    '''
def getMaxNumberOfDataFormats():
    '''returns int\n\n
    getMaxNumberOfDataFormats()\n
    '''
def ():
    '''returns StylesTable\n\n
    ()\n
    (final PackagePart part)\n
    '''
def setWorkbook():
    '''returns None\n\n
    setWorkbook(final XSSFWorkbook wb)\n
    '''
def getTheme():
    '''returns ThemesTable\n\n
    getTheme()\n
    '''
def setTheme():
    '''returns None\n\n
    setTheme(final ThemesTable theme)\n
    '''
def ensureThemesTable():
    '''returns None\n\n
    ensureThemesTable()\n
    '''
def readFrom():
    '''returns None\n\n
    readFrom(final InputStream is)\n
    '''
def getNumberFormatAt():
    '''returns String\n\n
    getNumberFormatAt(final short fmtId)\n
    '''
def putNumberFormat():
    '''returns None\n\n
    putNumberFormat(final String fmt)\n
    putNumberFormat(final short index, final String fmt)\n
    '''
def removeNumberFormat():
    '''returns boolean\n\n
    removeNumberFormat(final short index)\n
    removeNumberFormat(final String fmt)\n
    '''
def getFontAt():
    '''returns XSSFFont\n\n
    getFontAt(final int idx)\n
    '''
def putFont():
    '''returns int\n\n
    putFont(final XSSFFont font, final boolean forceRegistration)\n
    putFont(final XSSFFont font)\n
    '''
def getStyleAt():
    '''returns XSSFCellStyle\n\n
    getStyleAt(final int idx)\n
    '''
def putStyle():
    '''returns int\n\n
    putStyle(final XSSFCellStyle style)\n
    '''
def getBorderAt():
    '''returns XSSFCellBorder\n\n
    getBorderAt(final int idx)\n
    '''
def putBorder():
    '''returns int\n\n
    putBorder(final XSSFCellBorder border)\n
    '''
def getFillAt():
    '''returns XSSFCellFill\n\n
    getFillAt(final int idx)\n
    '''
def getBorders():
    '''returns List<XSSFCellBorder>\n\n
    getBorders()\n
    '''
def getFills():
    '''returns List<XSSFCellFill>\n\n
    getFills()\n
    '''
def getFonts():
    '''returns List<XSSFFont>\n\n
    getFonts()\n
    '''
def putFill():
    '''returns int\n\n
    putFill(final XSSFCellFill fill)\n
    '''
def getCellXfAt():
    '''returns CTXf\n\n
    getCellXfAt(final int idx)\n
    '''
def putCellXf():
    '''returns int\n\n
    putCellXf(final CTXf cellXf)\n
    '''
def replaceCellXfAt():
    '''returns None\n\n
    replaceCellXfAt(final int idx, final CTXf cellXf)\n
    '''
def getCellStyleXfAt():
    '''returns CTXf\n\n
    getCellStyleXfAt(final int idx)\n
    '''
def putCellStyleXf():
    '''returns int\n\n
    putCellStyleXf(final CTXf cellStyleXf)\n
    '''
def getNumCellStyles():
    '''returns int\n\n
    getNumCellStyles()\n
    '''
def getNumDataFormats():
    '''returns int\n\n
    getNumDataFormats()\n
    '''
def _getStyleXfsSize():
    '''returns int\n\n
    _getStyleXfsSize()\n
    '''
def getCTStylesheet():
    '''returns CTStylesheet\n\n
    getCTStylesheet()\n
    '''
def _getDXfsSize():
    '''returns int\n\n
    _getDXfsSize()\n
    '''
def writeTo():
    '''returns None\n\n
    writeTo(final OutputStream out)\n
    '''
def getDxfAt():
    '''returns CTDxf\n\n
    getDxfAt(final int idx)\n
    '''
def putDxf():
    '''returns int\n\n
    putDxf(final CTDxf dxf)\n
    '''
def getExplicitTableStyle():
    '''returns TableStyle\n\n
    getExplicitTableStyle(final String name)\n
    '''
def getExplicitTableStyleNames():
    '''returns Set<String>\n\n
    getExplicitTableStyleNames()\n
    '''
def getTableStyle():
    '''returns TableStyle\n\n
    getTableStyle(final String name)\n
    '''
def createCellStyle():
    '''returns XSSFCellStyle\n\n
    createCellStyle()\n
    '''
def findFont():
    '''returns XSSFFont\n\n
    findFont(final boolean bold, final short color, final short fontHeight, final String name, final boolean italic, final boolean strikeout, final short typeOffset, final byte underline)\n
    '''
def getIndexedColors():
    '''returns IndexedColorMap\n\n
    getIndexedColors()\n
    '''
