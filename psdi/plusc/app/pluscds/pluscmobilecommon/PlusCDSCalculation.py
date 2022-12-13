INPUT_FROM = "int  0"
INPUT_TO = "int  1"
OUTPUT_FROM = "int  2"
OUTPUT_TO = "int  3"
DEVIATION_N = "int  1"
DEVIATION_N_MINUS_1 = "int  2"
def PlusCDSCalculation():
    '''public PlusCDSCalculation(final HashMap dsConfig)
    '''
def getTolPrecision():
    '''public int getTolPrecision(final int minOutputPrecision, final int actualOutputPrecision, final int actualInputPrecision)
    '''
def getAssetPrecision():
    '''public int getAssetPrecision(final int minOutputPrecision, final int actualOutputPrecision, final int actualInputPrecision)
    '''
def getTolError():
    '''public int getTolError()
    '''
def getAssetError():
    '''public int getAssetError()
    '''
def getTolNPlaces():
    '''public int getTolNPlaces()
    '''
def getAssetNPlaces():
    '''public int getAssetNPlaces()
    '''
def getTolTruncate():
    '''public boolean getTolTruncate()
    '''
def getAssetTruncate():
    '''public boolean getAssetTruncate()
    '''
def getDesiredOutputTruncate():
    '''public boolean getDesiredOutputTruncate()
    '''
def getStdDeviationType():
    '''public int getStdDeviationType()
    '''
def summedToleranceEquationsTightesWidest():
    '''public double[] summedToleranceEquationsTightesWidest(final PlusCMboRemote owner, final String fieldName, final int tol, final boolean[] summedCalcTypes)
    '''
def squaredDesiredOutputValue():
    '''public String squaredDesiredOutputValue(final PlusCMboRemote owner)
    '''
def squareRootDesiredOutputValue():
    '''public String squareRootDesiredOutputValue(final PlusCMboRemote owner)
    '''
def squareRootOutputValueNegative():
    '''public static String squareRootOutputValueNegative(final Locale locale, final String instrcalrangeto, final String instroutrangefrom, final String instrOutputSpan, final String invalue)
    '''
def squaredOutputValueNegative():
    '''public static String squaredOutputValueNegative(final Locale locale, final String instrcalrangefrom, final String instrcalrangeto, final String instroutrangefrom, final String instrOutputSpan, final String invalue, final int precision)
    '''
def squaredOutputValue():
    '''public static String squaredOutputValue(final Locale locale, final String instrcalrangefrom, final String instrcalrangeto, final String instroutrangefrom, final String instrOutputSpan, final String invalue, final double sign, final int precision)
    '''
def calculateToleranceRangeSquareRoot():
    '''public boolean calculateToleranceRangeSquareRoot(final PlusCMboRemote owner, final String fieldName)
    '''
def calculateToleranceRangeSquared():
    '''public boolean calculateToleranceRangeSquared(final PlusCMboRemote owner, final String fieldName)
    '''
def calcPointRangeLimits():
    '''public void calcPointRangeLimits(final PlusCMboRemote mboRemote)
    '''
def getRangeLimitsTruncate():
    '''public boolean getRangeLimitsTruncate()
    '''
def summedToleranceEquations():
    '''public boolean summedToleranceEquations(final PlusCMboRemote owner, final String fieldName, final int tol, final boolean[] summedCalcTypes)
    '''
def directionCheck():
    '''public static double[] directionCheck(final PlusCMboRemote owner, final Locale locale)
    '''
def doUpdateOutputValue():
    '''public void doUpdateOutputValue(final PlusCMboRemote mboRemote, final boolean bValidateWhenSetting)
    '''
def doWOUpdateOutputValue():
    '''public String doWOUpdateOutputValue(final PlusCMboRemote owner, final String sPrefix)
    '''
def doUpdateRonValues():
    '''public void doUpdateRonValues(final PlusCMboRemote mboRemote)
    '''
def doUpdateTolValues():
    '''public boolean doUpdateTolValues(final PlusCMboRemote mboRemote, String fieldName)
    '''
def doUpdateErrorValues():
    '''public boolean doUpdateErrorValues(final PlusCMboRemote mboRemote, final String asFoundOrLeft, final boolean bShowOutOfTolMsg)
    '''
def checkAndAdjustFldValueSize():
    '''public String checkAndAdjustFldValueSize(String value, final DecimalFormatSymbols df, final int minFraction, final Locale locale)
    public String checkAndAdjustFldValueSize(String value, final DecimalFormatSymbols df, final Locale locale, final boolean shouldRound)
    '''
def calculateAveragesAndStdDevs():
    '''public boolean calculateAveragesAndStdDevs(final PlusCMboRemote[] groupPoints, final PlusCMboRemote groupAveragePoint, final String fieldName)
    '''
