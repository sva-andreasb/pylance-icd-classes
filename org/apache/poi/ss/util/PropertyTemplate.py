def ():
    '''returns PropertyTemplate\n\n
    ()\n
    (final PropertyTemplate template)\n
    '''
def drawBorders():
    '''returns None\n\n
    drawBorders(final CellRangeAddress range, final BorderStyle borderType, final BorderExtent extent)\n
    drawBorders(final CellRangeAddress range, final BorderStyle borderType, final short color, final BorderExtent extent)\n
    '''
def applyBorders():
    '''returns None\n\n
    applyBorders(final Sheet sheet)\n
    '''
def drawBorderColors():
    '''returns None\n\n
    drawBorderColors(final CellRangeAddress range, final short color, final BorderExtent extent)\n
    '''
def getNumBorders():
    '''returns int\n\n
    getNumBorders(final CellAddress cell)\n
    getNumBorders(final int row, final int col)\n
    '''
def getNumBorderColors():
    '''returns int\n\n
    getNumBorderColors(final CellAddress cell)\n
    getNumBorderColors(final int row, final int col)\n
    '''
def getBorderStyle():
    '''returns BorderStyle\n\n
    getBorderStyle(final CellAddress cell, final String property)\n
    getBorderStyle(final int row, final int col, final String property)\n
    '''
def getTemplateProperty():
    '''returns short\n\n
    getTemplateProperty(final CellAddress cell, final String property)\n
    getTemplateProperty(final int row, final int col, final String property)\n
    '''
