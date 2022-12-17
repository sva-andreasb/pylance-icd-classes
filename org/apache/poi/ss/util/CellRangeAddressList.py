def ():
    '''returns CellRangeAddressList\n\n
    ()\n
    (final int firstRow, final int lastRow, final int firstCol, final int lastCol)\n
    (final RecordInputStream in)\n
    '''
def countRanges():
    '''returns int\n\n
    countRanges()\n
    '''
def addCellRangeAddress():
    '''returns None\n\n
    addCellRangeAddress(final int firstRow, final int firstCol, final int lastRow, final int lastCol)\n
    addCellRangeAddress(final CellRangeAddress cra)\n
    '''
def remove():
    '''returns CellRangeAddress\n\n
    remove(final int rangeIndex)\n
    '''
def getCellRangeAddress():
    '''returns CellRangeAddress\n\n
    getCellRangeAddress(final int index)\n
    '''
def getSize():
    '''returns int\n\n
    getSize()\n
    '''
def serialize():
    '''returns None\n\n
    serialize(final int offset, final byte[] data)\n
    serialize(final LittleEndianOutput out)\n
    '''
def copy():
    '''returns CellRangeAddressList\n\n
    copy()\n
    '''
def getCellRangeAddresses():
    '''returns CellRangeAddress[]\n\n
    getCellRangeAddresses()\n
    '''
