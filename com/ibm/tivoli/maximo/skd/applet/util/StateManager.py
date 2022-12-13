EVENT_SAVE_STATE = "String  save_state""
EVENT_RESTORE_STATE = "String  restore_state""
def getInstance():
'''public static StateManager getInstance()
'''
pass
def getState():
'''public AppState getState(final String project)
'''
pass
def hasState():
'''public boolean hasState(final String project)
'''
pass
def clearState():
'''public void clearState(final String project)
'''
pass
def saveTableState():
'''public void saveTableState(final JTable table, final TableState state)
'''
pass
def compare():
'''public int compare(final TableColState o1, final TableColState o2)
'''
pass
def saveState():
'''public void saveState(final IlvGanttChart chart, final GanttState state)
public AppState saveState(final IlvGanttChart chart, final String project)
public void saveState(final IlvScheduleChart chart, final AppState state, final String resId)
'''
pass
def restoreTableState():
'''public void restoreTableState(final JTable table, final TableState state)
'''
pass
def restoreState():
'''public void restoreState(final IlvGanttChart chart, final GanttState state)
public AppState restoreState(final IlvGanttChart chart, final String project)
public void restoreState(final IlvScheduleChart chart, final AppState state, final String resId)
'''
pass
def StateManager():
'''public StateManager()
'''
pass
def setPreviousState():
'''public void setPreviousState(final AppState state)
'''
pass
def getPreviousState():
'''public AppState getPreviousState(final String projectId)
'''
pass
def putState():
'''public void putState(final AppState state)
'''
pass
def visit():
'''public void visit(final IlvActivity item, final IlvGanttChart chart, final GanttState state)
public void visit(final IlvActivity item, final IlvGanttChart chart, final GanttState state)
public void visit(final IlvResource item, final IlvHierarchyChart chart, final GanttState state)
public void visit(final IlvResource item, final IlvHierarchyChart chart, final GanttState state)
'''
pass
def TableState():
'''public TableState()
'''
pass
def GanttState():
'''public GanttState()
'''
pass
def AppState():
'''public AppState()
public AppState(final String projectid)
'''
pass
