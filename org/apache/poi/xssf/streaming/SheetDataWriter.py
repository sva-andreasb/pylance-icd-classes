def ():
    '''returns SheetDataWriter\n\n
    ()\n
    (final SharedStringsTable sharedStringsTable)\n
    '''
def createTempFile():
    '''returns File\n\n
    createTempFile()\n
    '''
def createWriter():
    '''returns Writer\n\n
    createWriter(final File fd)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def getWorksheetXMLInputStream():
    '''returns InputStream\n\n
    getWorksheetXMLInputStream()\n
    '''
def getNumberOfFlushedRows():
    '''returns int\n\n
    getNumberOfFlushedRows()\n
    '''
def getNumberOfCellsOfLastFlushedRow():
    '''returns int\n\n
    getNumberOfCellsOfLastFlushedRow()\n
    '''
def getLowestIndexOfFlushedRows():
    '''returns int\n\n
    getLowestIndexOfFlushedRows()\n
    '''
def getLastFlushedRow():
    '''returns int\n\n
    getLastFlushedRow()\n
    '''
def writeRow():
    '''returns None\n\n
    writeRow(final int rownum, final SXSSFRow row)\n
    '''
def writeCell():
    '''returns None\n\n
    writeCell(final int columnIndex, final Cell cell)\n
    '''
