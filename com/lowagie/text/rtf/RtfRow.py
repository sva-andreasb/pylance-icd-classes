def ():
    '''returns RtfRow\n\n
    (final RtfWriter writer, final RtfTable mainTable)\n
    '''
def pregenerateRows():
    '''returns None\n\n
    pregenerateRows(final int columns)\n
    '''
def importRow():
    '''returns boolean\n\n
    importRow(final Row row, final float[] propWidths, final int tableWidth, final int pageWidth, final int cellpadding, final int cellspacing, final int borders, final Color borderColor, final float borderWidth, final int y)\n
    '''
def writeRow():
    '''returns boolean\n\n
    writeRow(final ByteArrayOutputStream os, final int rowNum, final Table table)\n
    '''
def setMerge():
    '''returns None\n\n
    setMerge(final int x, final int mergeType, final RtfCell mergeCell)\n
    '''
