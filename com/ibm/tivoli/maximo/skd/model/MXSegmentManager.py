SEGMENT_MANAGER_FIELD = "String  \"_SM\""
DEFAULT_SEGMENT_MANAGER = "String  \"SEGMENTS\""
def MXSegmentManager():
    '''    public MXSegmentManager(final String prefix, final String countField, final String seqenceField, final Map<String, String> segmentFieldsToActivityFields)
    '''
def pushSegmentMapToParentRow():
    '''    public void pushSegmentMapToParentRow(final MXGanttModel model, final MXActivity parent)
    '''
def updateParent():
    '''    public void updateParent(final MXActivity parent, final MXActivity childActivity, final int seq)
    '''
def buildSegmentActivityChildrenFromParentMap():
    '''    public void buildSegmentActivityChildrenFromParentMap(final MXGanttModel model, final MXActivity parent)
    '''
def pushChildSegmentsToParentMap():
    '''    public void pushChildSegmentsToParentMap(final MXGanttModel model, final MXActivity parent)
    '''
def compare():
    '''    public int compare(final MXSegmentActivity o1, final MXSegmentActivity o2)
    '''
def updateSegmentMapFromParentRowSegmentFields():
    '''    public void updateSegmentMapFromParentRowSegmentFields(final MXGanttModel model, final MXActivity parent)
    '''
def children():
    '''    public static List<MXSegmentActivity> children(final MXGanttModel model, final MXActivity parent)
    '''
def get():
    '''    public static <T> T get(final MXActivity parent, final String prefix, final int seq, final String fld)
    '''
def set():
    '''    public static void set(final MXActivity parent, final String prefix, final int seq, final String fld, final Object value)
    '''
def getManager():
    '''    public static MXSegmentManager getManager(final MXGanttModel model, final MXActivity parent)
    public static MXSegmentManager getManager(final MXGanttModel model, final String mgrId)
    '''
def setManager():
    '''    public static void setManager(final MXGanttModel model, final MXActivity parent, final MXSegmentManager mgr)
    public static void setManager(final MXGanttModel model, final String managerId, final MXSegmentManager mgr)
    '''
def updateMap():
    '''    public static void updateMap(final MXActivity mxActivity, final String property, final Object value)
    '''
def removeSegment():
    '''    public void removeSegment(final MXGanttModel model, final MXActivity parentSegmentActivity, final MXSegmentActivity act)
    '''
def addSegment():
    '''    public void addSegment(final MXGanttModel model, final MXActivity newParentSegmentActivity, final MXSegmentActivity act)
    '''
