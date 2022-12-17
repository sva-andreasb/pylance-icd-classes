def ():
    '''returns XSSFEventBasedExcelExtractor\n\n
    (final String path)\n
    (final OPCPackage container)\n
    '''
def setIncludeSheetNames():
    '''returns None\n\n
    setIncludeSheetNames(final boolean includeSheetNames)\n
    '''
def getIncludeSheetNames():
    '''returns boolean\n\n
    getIncludeSheetNames()\n
    '''
def setFormulasNotResults():
    '''returns None\n\n
    setFormulasNotResults(final boolean formulasNotResults)\n
    '''
def getFormulasNotResults():
    '''returns boolean\n\n
    getFormulasNotResults()\n
    '''
def setIncludeHeadersFooters():
    '''returns None\n\n
    setIncludeHeadersFooters(final boolean includeHeadersFooters)\n
    '''
def getIncludeHeadersFooters():
    '''returns boolean\n\n
    getIncludeHeadersFooters()\n
    '''
def setIncludeTextBoxes():
    '''returns None\n\n
    setIncludeTextBoxes(final boolean includeTextBoxes)\n
    '''
def getIncludeTextBoxes():
    '''returns boolean\n\n
    getIncludeTextBoxes()\n
    '''
def setIncludeCellComments():
    '''returns None\n\n
    setIncludeCellComments(final boolean includeCellComments)\n
    '''
def getIncludeCellComments():
    '''returns boolean\n\n
    getIncludeCellComments()\n
    '''
def setConcatenatePhoneticRuns():
    '''returns None\n\n
    setConcatenatePhoneticRuns(final boolean concatenatePhoneticRuns)\n
    '''
def setLocale():
    '''returns None\n\n
    setLocale(final Locale locale)\n
    '''
def getLocale():
    '''returns Locale\n\n
    getLocale()\n
    '''
def getPackage():
    '''returns OPCPackage\n\n
    getPackage()\n
    '''
def processSheet():
    '''returns None\n\n
    processSheet(final XSSFSheetXMLHandler.SheetContentsHandler sheetContentsExtractor, final StylesTable styles, final CommentsTable comments, final ReadOnlySharedStringsTable strings, final InputStream sheetInputStream)\n
    '''
def getText():
    '''returns String\n\n
    getText()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def startRow():
    '''returns None\n\n
    startRow(final int rowNum)\n
    '''
def endRow():
    '''returns None\n\n
    endRow(final int rowNum)\n
    '''
def cell():
    '''returns None\n\n
    cell(final String cellRef, final String formattedValue, final XSSFComment comment)\n
    '''
def headerFooter():
    '''returns None\n\n
    headerFooter(final String text, final boolean isHeader, final String tagName)\n
    '''
