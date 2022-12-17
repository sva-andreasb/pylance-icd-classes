def ():
    '''returns ColumnHelper\n\n
    (final CTWorksheet worksheet)\n
    '''
def cleanColumns():
    '''returns None\n\n
    cleanColumns()\n
    '''
def addCleanColIntoCols():
    '''returns CTCols\n\n
    addCleanColIntoCols(final CTCols cols, final CTCol newCol)\n
    '''
def cloneCol():
    '''returns CTCol\n\n
    cloneCol(final CTCols cols, final CTCol col)\n
    '''
def getColumn():
    '''returns CTCol\n\n
    getColumn(final long index, final boolean splitColumns)\n
    '''
def getColumn1Based():
    '''returns CTCol\n\n
    getColumn1Based(final long index1, final boolean splitColumns)\n
    '''
def columnExists():
    '''returns boolean\n\n
    columnExists(final CTCols cols, final long index)\n
    '''
def setColumnAttributes():
    '''returns None\n\n
    setColumnAttributes(final CTCol fromCol, final CTCol toCol)\n
    '''
def setColBestFit():
    '''returns None\n\n
    setColBestFit(final long index, final boolean bestFit)\n
    '''
def setCustomWidth():
    '''returns None\n\n
    setCustomWidth(final long index, final boolean bestFit)\n
    '''
def setColWidth():
    '''returns None\n\n
    setColWidth(final long index, final double width)\n
    '''
def setColHidden():
    '''returns None\n\n
    setColHidden(final long index, final boolean hidden)\n
    '''
def setColDefaultStyle():
    '''returns None\n\n
    setColDefaultStyle(final long index, final CellStyle style)\n
    setColDefaultStyle(final long index, final int styleId)\n
    '''
def getColDefaultStyle():
    '''returns int\n\n
    getColDefaultStyle(final long index)\n
    '''
def getIndexOfColumn():
    '''returns int\n\n
    getIndexOfColumn(final CTCols cols, final CTCol searchCol)\n
    '''
