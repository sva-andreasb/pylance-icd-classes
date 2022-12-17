def clearAllCachedResultValues():
    '''returns None\n\n
    clearAllCachedResultValues()\n
    '''
def createName():
    '''returns HSSFName\n\n
    createName()\n
    '''
def getExternalSheetIndex():
    '''returns int\n\n
    getExternalSheetIndex(final String sheetName)\n
    getExternalSheetIndex(final String workbookName, final String sheetName)\n
    '''
def get3DReferencePtg():
    '''returns Ptg\n\n
    get3DReferencePtg(final CellReference cr, final SheetIdentifier sheet)\n
    get3DReferencePtg(final AreaReference areaRef, final SheetIdentifier sheet)\n
    '''
def getNameXPtg():
    '''returns NameXPtg\n\n
    getNameXPtg(final String name, final SheetIdentifier sheet)\n
    '''
def getName():
    '''returns EvaluationName\n\n
    getName(final String name, final int sheetIndex)\n
    getName(final NamePtg namePtg)\n
    '''
def getSheetIndex():
    '''returns int\n\n
    getSheetIndex(final EvaluationSheet evalSheet)\n
    getSheetIndex(final String sheetName)\n
    '''
def getSheetName():
    '''returns String\n\n
    getSheetName(final int sheetIndex)\n
    '''
def getSheet():
    '''returns EvaluationSheet\n\n
    getSheet(final int sheetIndex)\n
    '''
def convertFromExternSheetIndex():
    '''returns int\n\n
    convertFromExternSheetIndex(final int externSheetIndex)\n
    '''
def getExternalSheet():
    '''returns ExternalSheet\n\n
    getExternalSheet(final int externSheetIndex)\n
    getExternalSheet(final String firstSheetName, final String lastSheetName, final int externalWorkbookNumber)\n
    '''
def getExternalName():
    '''returns ExternalName\n\n
    getExternalName(final int externSheetIndex, final int externNameIndex)\n
    getExternalName(final String nameName, final String sheetName, final int externalWorkbookNumber)\n
    '''
def resolveNameXText():
    '''returns String\n\n
    resolveNameXText(final NameXPtg n)\n
    '''
def getSheetFirstNameByExternSheet():
    '''returns String\n\n
    getSheetFirstNameByExternSheet(final int externSheetIndex)\n
    '''
def getSheetLastNameByExternSheet():
    '''returns String\n\n
    getSheetLastNameByExternSheet(final int externSheetIndex)\n
    '''
def getNameText():
    '''returns String\n\n
    getNameText(final NamePtg namePtg)\n
    getNameText()\n
    '''
def getFormulaTokens():
    '''returns Ptg[]\n\n
    getFormulaTokens(final EvaluationCell evalCell)\n
    '''
def getUDFFinder():
    '''returns UDFFinder\n\n
    getUDFFinder()\n
    '''
def getSpreadsheetVersion():
    '''returns SpreadsheetVersion\n\n
    getSpreadsheetVersion()\n
    '''
def getTable():
    '''returns Table\n\n
    getTable(final String name)\n
    '''
def ():
    '''returns Name\n\n
    (final NameRecord nameRecord, final int index)\n
    '''
def getNameDefinition():
    '''returns Ptg[]\n\n
    getNameDefinition()\n
    '''
def hasFormula():
    '''returns boolean\n\n
    hasFormula()\n
    '''
def isFunctionName():
    '''returns boolean\n\n
    isFunctionName()\n
    '''
def isRange():
    '''returns boolean\n\n
    isRange()\n
    '''
def createPtg():
    '''returns NamePtg\n\n
    createPtg()\n
    '''
