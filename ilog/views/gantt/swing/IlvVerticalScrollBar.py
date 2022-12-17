UNIT_PIXELS = "int  0"
UNIT_ROWS = "int  1"
BLOCK_PIXELS = "int  0"
BLOCK_PAGE_PIXELS = "int  1"
BLOCK_ROWS = "int  2"
BLOCK_PAGE_ROWS = "int  3"
def ():
    '''returns IlvVerticalScrollBar\n\n
    ()\n
    '''
def componentResized():
    '''returns None\n\n
    componentResized(final ComponentEvent componentEvent)\n
    '''
def getGanttConfiguration():
    '''returns IlvGanttConfiguration\n\n
    getGanttConfiguration()\n
    '''
def setGanttConfiguration():
    '''returns None\n\n
    setGanttConfiguration(final IlvGanttConfiguration a)\n
    '''
def getUnitIncrementMode():
    '''returns int\n\n
    getUnitIncrementMode()\n
    '''
def setUnitIncrementMode():
    '''returns None\n\n
    setUnitIncrementMode(final int c)\n
    '''
def getUnitIncrement():
    '''returns int\n\n
    getUnitIncrement(final int n)\n
    '''
def getBlockIncrementMode():
    '''returns int\n\n
    getBlockIncrementMode()\n
    '''
def setBlockIncrementMode():
    '''returns None\n\n
    setBlockIncrementMode(final int d)\n
    '''
def getBlockIncrement():
    '''returns int\n\n
    getBlockIncrement(final int direction)\n
    '''
def setValue():
    '''returns None\n\n
    setValue(int value)\n
    '''
def rowsInserted():
    '''returns None\n\n
    rowsInserted(final RowsInsertedEvent rowsInsertedEvent)\n
    '''
def rowsRemoved():
    '''returns None\n\n
    rowsRemoved(final RowsRemovedEvent rowsRemovedEvent)\n
    '''
def rowMoved():
    '''returns None\n\n
    rowMoved(final RowMovedEvent rowMovedEvent)\n
    '''
def rowExpanded():
    '''returns None\n\n
    rowExpanded(final RowExpandedEvent rowExpandedEvent)\n
    '''
def rowCollapsed():
    '''returns None\n\n
    rowCollapsed(final RowCollapsedEvent rowCollapsedEvent)\n
    '''
def rowHeightChanged():
    '''returns None\n\n
    rowHeightChanged(final RowHeightChangedEvent rowHeightChangedEvent)\n
    '''
def rootRowVisibilityChanged():
    '''returns None\n\n
    rootRowVisibilityChanged(final RootRowVisibilityChangedEvent rootRowVisibilityChangedEvent)\n
    '''
def ganttModelChanged():
    '''returns None\n\n
    ganttModelChanged(final GanttModelChangedEvent ganttModelChangedEvent)\n
    '''
