INPUT_FROM = "int  0"
INPUT_TO = "int  1"
OUTPUT_FROM = "int  2"
OUTPUT_TO = "int  3"
DEVIATION_N = "int  1"
DEVIATION_N_MINUS_1 = "int  2"
def ():
    '''returns PlusCDSCalculation\n\n
    (final HashMap dsConfig)\n
    '''
def getTolPrecision():
    '''returns int\n\n
    getTolPrecision(final int minOutputPrecision, final int actualOutputPrecision, final int actualInputPrecision)\n
    '''
def getAssetPrecision():
    '''returns int\n\n
    getAssetPrecision(final int minOutputPrecision, final int actualOutputPrecision, final int actualInputPrecision)\n
    '''
def getTolError():
    '''returns int\n\n
    getTolError()\n
    '''
def getAssetError():
    '''returns int\n\n
    getAssetError()\n
    '''
def getTolNPlaces():
    '''returns int\n\n
    getTolNPlaces()\n
    '''
def getAssetNPlaces():
    '''returns int\n\n
    getAssetNPlaces()\n
    '''
def getTolTruncate():
    '''returns boolean\n\n
    getTolTruncate()\n
    '''
def getAssetTruncate():
    '''returns boolean\n\n
    getAssetTruncate()\n
    '''
def getDesiredOutputTruncate():
    '''returns boolean\n\n
    getDesiredOutputTruncate()\n
    '''
def getStdDeviationType():
    '''returns int\n\n
    getStdDeviationType()\n
    '''
def summedToleranceEquationsTightesWidest():
    '''returns double[]\n\n
    summedToleranceEquationsTightesWidest(final PlusCMboRemote owner, final String fieldName, final int tol, final boolean[] summedCalcTypes)\n
    '''
def squaredDesiredOutputValue():
    '''returns String\n\n
    squaredDesiredOutputValue(final PlusCMboRemote owner)\n
    '''
def squareRootDesiredOutputValue():
    '''returns String\n\n
    squareRootDesiredOutputValue(final PlusCMboRemote owner)\n
    '''
def calculateToleranceRangeSquareRoot():
    '''returns boolean\n\n
    calculateToleranceRangeSquareRoot(final PlusCMboRemote owner, final String fieldName)\n
    '''
def calculateToleranceRangeSquared():
    '''returns boolean\n\n
    calculateToleranceRangeSquared(final PlusCMboRemote owner, final String fieldName)\n
    '''
def calcPointRangeLimits():
    '''returns None\n\n
    calcPointRangeLimits(final PlusCMboRemote mboRemote)\n
    '''
def getRangeLimitsTruncate():
    '''returns boolean\n\n
    getRangeLimitsTruncate()\n
    '''
def summedToleranceEquations():
    '''returns boolean\n\n
    summedToleranceEquations(final PlusCMboRemote owner, final String fieldName, final int tol, final boolean[] summedCalcTypes)\n
    '''
def doUpdateOutputValue():
    '''returns None\n\n
    doUpdateOutputValue(final PlusCMboRemote mboRemote, final boolean bValidateWhenSetting)\n
    '''
def doWOUpdateOutputValue():
    '''returns String\n\n
    doWOUpdateOutputValue(final PlusCMboRemote owner, final String sPrefix)\n
    '''
def doUpdateRonValues():
    '''returns None\n\n
    doUpdateRonValues(final PlusCMboRemote mboRemote)\n
    '''
def doUpdateTolValues():
    '''returns boolean\n\n
    doUpdateTolValues(final PlusCMboRemote mboRemote, String fieldName)\n
    '''
def doUpdateErrorValues():
    '''returns boolean\n\n
    doUpdateErrorValues(final PlusCMboRemote mboRemote, final String asFoundOrLeft, final boolean bShowOutOfTolMsg)\n
    '''
def checkAndAdjustFldValueSize():
    '''returns String\n\n
    checkAndAdjustFldValueSize(String value, final DecimalFormatSymbols df, final int minFraction, final Locale locale)\n
    checkAndAdjustFldValueSize(String value, final DecimalFormatSymbols df, final Locale locale, final boolean shouldRound)\n
    '''
def calculateAveragesAndStdDevs():
    '''returns boolean\n\n
    calculateAveragesAndStdDevs(final PlusCMboRemote[] groupPoints, final PlusCMboRemote groupAveragePoint, final String fieldName)\n
    '''
