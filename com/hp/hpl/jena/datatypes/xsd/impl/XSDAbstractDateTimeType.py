YEAR_MASK = "short  1"
MONTH_MASK = "short  2"
DAY_MASK = "short  4"
TIME_MASK = "short  8"
FULL_MASK = "short  15"
def ():
    '''returns XSDAbstractDateTimeType\n\n
    (final String typename)\n
    '''
def isEqual():
    '''returns boolean\n\n
    isEqual(final LiteralLabel value1, final LiteralLabel value2)\n
    '''
def dateToString():
    '''returns String\n\n
    dateToString(final int[] date)\n
    '''
def normalizeSubType():
    '''returns RDFDatatype\n\n
    normalizeSubType(final Object value, final RDFDatatype dt)\n
    '''
