FIRST_SPECIAL_CP = "int  1114112"
INITIAL_VALUE_CP = "int  1114112"
ERROR_VALUE_CP = "int  1114113"
MAX_CP = "int  1114113"
INITIAL_ROWS = "int  4096"
MEDIUM_ROWS = "int  65536"
MAX_ROWS = "int  1114114"
def ():
    '''returns DefaultGetFoldedValue\n\n
    (final int numOfColumns)\n
    (final IntTrieBuilder inBuilder)\n
    '''
def setValue():
    '''returns None\n\n
    setValue(final int start, final int end, int column, int value, int mask)\n
    '''
def getValue():
    '''returns int\n\n
    getValue(final int c, final int column)\n
    '''
def getRow():
    '''returns int[]\n\n
    getRow(final int rowIndex)\n
    '''
def getRowStart():
    '''returns int\n\n
    getRowStart(final int rowIndex)\n
    '''
def getRowEnd():
    '''returns int\n\n
    getRowEnd(final int rowIndex)\n
    '''
def compact():
    '''returns None\n\n
    compact(final CompactHandler compactor)\n
    '''
def compare():
    '''returns int\n\n
    compare(final Integer o1, final Integer o2)\n
    '''
def getCompactedArray():
    '''returns int[]\n\n
    getCompactedArray()\n
    '''
def getCompactedRows():
    '''returns int\n\n
    getCompactedRows()\n
    '''
def getCompactedColumns():
    '''returns int\n\n
    getCompactedColumns()\n
    '''
def compactToTrieWithRowIndexes():
    '''returns IntTrie\n\n
    compactToTrieWithRowIndexes()\n
    '''
def getFoldingOffset():
    '''returns int\n\n
    getFoldingOffset(final int value)\n
    '''
def getFoldedValue():
    '''returns int\n\n
    getFoldedValue(int start, final int offset)\n
    '''
