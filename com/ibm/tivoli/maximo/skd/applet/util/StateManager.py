EVENT_SAVE_STATE = "String  \"save_state\""
EVENT_RESTORE_STATE = "String  \"restore_state\""
def getInstance():
    '''    public static StateManager getInstance()
    '''
def getState():
    '''    public AppState getState(final String project)
    '''
def hasState():
    '''    public boolean hasState(final String project)
    '''
def clearState():
    '''    public void clearState(final String project)
    '''
def saveTableState():
    '''    public void saveTableState(final JTable table, final TableState state)
    '''
def compare():
    '''    public int compare(final TableColState o1, final TableColState o2)
    '''
def saveState():
    '''    public void saveState(final IlvGanttChart chart, final GanttState state)
    public AppState saveState(final IlvGanttChart chart, final String project)
    public void saveState(final IlvScheduleChart chart, final AppState state, final String resId)
    '''
def restoreTableState():
    '''    public void restoreTableState(final JTable table, final TableState state)
    '''
def restoreState():
    '''    public void restoreState(final IlvGanttChart chart, final GanttState state)
    public AppState restoreState(final IlvGanttChart chart, final String project)
    public void restoreState(final IlvScheduleChart chart, final AppState state, final String resId)
    '''
def StateManager():
    '''    public StateManager()
    '''
def setPreviousState():
    '''    public void setPreviousState(final AppState state)
    '''
def getPreviousState():
    '''    public AppState getPreviousState(final String projectId)
    '''
def putState():
    '''    public void putState(final AppState state)
    '''
def visit():
    '''    public void visit(final IlvActivity item, final IlvGanttChart chart, final GanttState state)
    public void visit(final IlvActivity item, final IlvGanttChart chart, final GanttState state)
    public void visit(final IlvResource item, final IlvHierarchyChart chart, final GanttState state)
    public void visit(final IlvResource item, final IlvHierarchyChart chart, final GanttState state)
    '''
def TableState():
    '''    public TableState()
    '''
def GanttState():
    '''    public GanttState()
    '''
def AppState():
    '''    public AppState()
    public AppState(final String projectid)
    '''
