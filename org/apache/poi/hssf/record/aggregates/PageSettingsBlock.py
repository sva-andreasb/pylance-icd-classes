def ():
    '''returns PLSAggregate\n\n
    (final RecordStream rs)\n
    ()\n
    (final RecordStream rs)\n
    '''
def setColumnBreak():
    '''returns None\n\n
    setColumnBreak(final short column, final short fromRow, final short toRow)\n
    '''
def removeColumnBreak():
    '''returns None\n\n
    removeColumnBreak(final int column)\n
    '''
def visitContainedRecords():
    '''returns None\n\n
    visitContainedRecords(final RecordVisitor rv)\n
    visitContainedRecords(final RecordVisitor rv)\n
    '''
def getHeader():
    '''returns HeaderRecord\n\n
    getHeader()\n
    '''
def setHeader():
    '''returns None\n\n
    setHeader(final HeaderRecord newHeader)\n
    '''
def getFooter():
    '''returns FooterRecord\n\n
    getFooter()\n
    '''
def setFooter():
    '''returns None\n\n
    setFooter(final FooterRecord newFooter)\n
    '''
def getPrintSetup():
    '''returns PrintSetupRecord\n\n
    getPrintSetup()\n
    '''
def setPrintSetup():
    '''returns None\n\n
    setPrintSetup(final PrintSetupRecord newPrintSetup)\n
    '''
def getMargin():
    '''returns double\n\n
    getMargin(final short margin)\n
    '''
def setMargin():
    '''returns None\n\n
    setMargin(final short margin, final double size)\n
    '''
def setRowBreak():
    '''returns None\n\n
    setRowBreak(final int row, final short fromCol, final short toCol)\n
    '''
def removeRowBreak():
    '''returns None\n\n
    removeRowBreak(final int row)\n
    '''
def isRowBroken():
    '''returns boolean\n\n
    isRowBroken(final int row)\n
    '''
def isColumnBroken():
    '''returns boolean\n\n
    isColumnBroken(final int column)\n
    '''
def shiftRowBreaks():
    '''returns None\n\n
    shiftRowBreaks(final int startingRow, final int endingRow, final int count)\n
    '''
def shiftColumnBreaks():
    '''returns None\n\n
    shiftColumnBreaks(final short startingCol, final short endingCol, final short count)\n
    '''
def getRowBreaks():
    '''returns int[]\n\n
    getRowBreaks()\n
    '''
def getNumRowBreaks():
    '''returns int\n\n
    getNumRowBreaks()\n
    '''
def getColumnBreaks():
    '''returns int[]\n\n
    getColumnBreaks()\n
    '''
def getNumColumnBreaks():
    '''returns int\n\n
    getNumColumnBreaks()\n
    '''
def getVCenter():
    '''returns VCenterRecord\n\n
    getVCenter()\n
    '''
def getHCenter():
    '''returns HCenterRecord\n\n
    getHCenter()\n
    '''
def addLateHeaderFooter():
    '''returns None\n\n
    addLateHeaderFooter(final HeaderFooterRecord rec)\n
    '''
def addLateRecords():
    '''returns None\n\n
    addLateRecords(final RecordStream rs)\n
    '''
def positionRecords():
    '''returns None\n\n
    positionRecords(final List<RecordBase> sheetRecords)\n
    '''
def visitRecord():
    '''returns None\n\n
    visitRecord(final Record r)\n
    '''
