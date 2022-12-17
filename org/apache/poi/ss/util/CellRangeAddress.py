ENCODED_SIZE = "int  8"
def ():
    '''returns CellRangeAddress\n\n
    (final int firstRow, final int lastRow, final int firstCol, final int lastCol)\n
    (final RecordInputStream in)\n
    '''
def serialize():
    '''returns None\n\n
    serialize(final LittleEndianOutput out)\n
    '''
def copy():
    '''returns CellRangeAddress\n\n
    copy()\n
    '''
def formatAsString():
    '''returns String\n\n
    formatAsString()\n
    formatAsString(final String sheetName, final boolean useAbsoluteAddress)\n
    '''
