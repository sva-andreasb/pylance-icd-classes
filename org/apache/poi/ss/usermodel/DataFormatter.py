def ():
    '''returns ConstantStringFormat\n\n
    ()\n
    (final boolean emulateCSV)\n
    (final Locale locale)\n
    (final Locale locale, final boolean emulateCSV)\n
    (final String pattern, final DecimalFormatSymbols symbols)\n
    (final String s)\n
    '''
def createFormat():
    '''returns Format\n\n
    createFormat(final Cell cell)\n
    '''
def getDefaultFormat():
    '''returns Format\n\n
    getDefaultFormat(final Cell cell)\n
    '''
def formatRawCellContents():
    '''returns String\n\n
    formatRawCellContents(final double value, final int formatIndex, final String formatString)\n
    formatRawCellContents(final double value, final int formatIndex, final String formatString, final boolean use1904Windowing)\n
    '''
def formatCellValue():
    '''returns String\n\n
    formatCellValue(final Cell cell)\n
    formatCellValue(final Cell cell, final FormulaEvaluator evaluator)\n
    formatCellValue(final Cell cell, final FormulaEvaluator evaluator, final ConditionalFormattingEvaluator cfEvaluator)\n
    '''
def setDefaultNumberFormat():
    '''returns None\n\n
    setDefaultNumberFormat(final Format format)\n
    '''
def addFormat():
    '''returns None\n\n
    addFormat(final String excelFormatStr, final Format format)\n
    '''
def getLocaleChangedObservable():
    '''returns Observable\n\n
    getLocaleChangedObservable()\n
    '''
def update():
    '''returns None\n\n
    update(final Observable observable, final Object localeObj)\n
    '''
def format():
    '''returns StringBuffer\n\n
    format(Object obj, final StringBuffer toAppendTo, final FieldPosition pos)\n
    format(final Object obj, final StringBuffer toAppendTo, final FieldPosition pos)\n
    format(final Object obj, final StringBuffer toAppendTo, final FieldPosition pos)\n
    format(final Object obj, final StringBuffer toAppendTo, final FieldPosition pos)\n
    format(final Object obj, final StringBuffer toAppendTo, final FieldPosition pos)\n
    format(final Object obj, final StringBuffer toAppendTo, final FieldPosition pos)\n
    '''
def parseObject():
    '''returns Object\n\n
    parseObject(final String source, final ParsePosition pos)\n
    parseObject(final String source, final ParsePosition pos)\n
    parseObject(final String source, final ParsePosition pos)\n
    parseObject(final String source, final ParsePosition pos)\n
    parseObject(final String source, final ParsePosition pos)\n
    parseObject(final String source, final ParsePosition pos)\n
    '''
