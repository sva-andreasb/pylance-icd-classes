EVENT_SAVE_STATE = "String  \"save_state\""
EVENT_RESTORE_STATE = "String  \"restore_state\""
def getState():
    '''returns AppState\n\n
    getState(final String project)\n
    '''
def hasState():
    '''returns boolean\n\n
    hasState(final String project)\n
    '''
def clearState():
    '''returns None\n\n
    clearState(final String project)\n
    '''
def saveTableState():
    '''returns None\n\n
    saveTableState(final JTable table, final TableState state)\n
    '''
def compare():
    '''returns int\n\n
    compare(final TableColState o1, final TableColState o2)\n
    '''
def saveState():
    '''returns None\n\n
    saveState(final IlvGanttChart chart, final GanttState state)\n
    saveState(final IlvGanttChart chart, final String project)\n
    saveState(final IlvScheduleChart chart, final AppState state, final String resId)\n
    '''
def restoreTableState():
    '''returns None\n\n
    restoreTableState(final JTable table, final TableState state)\n
    '''
def restoreState():
    '''returns None\n\n
    restoreState(final IlvGanttChart chart, final GanttState state)\n
    restoreState(final IlvGanttChart chart, final String project)\n
    restoreState(final IlvScheduleChart chart, final AppState state, final String resId)\n
    '''
def ():
    '''returns AppState\n\n
    ()\n
    ()\n
    ()\n
    ()\n
    (final String projectid)\n
    '''
def setPreviousState():
    '''returns None\n\n
    setPreviousState(final AppState state)\n
    '''
def getPreviousState():
    '''returns AppState\n\n
    getPreviousState(final String projectId)\n
    '''
def putState():
    '''returns None\n\n
    putState(final AppState state)\n
    '''
def visit():
    '''returns None\n\n
    visit(final IlvActivity item, final IlvGanttChart chart, final GanttState state)\n
    visit(final IlvActivity item, final IlvGanttChart chart, final GanttState state)\n
    visit(final IlvResource item, final IlvHierarchyChart chart, final GanttState state)\n
    visit(final IlvResource item, final IlvHierarchyChart chart, final GanttState state)\n
    '''
