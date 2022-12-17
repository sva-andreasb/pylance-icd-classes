SEGMENT_MANAGER_FIELD = "String  \"_SM\""
DEFAULT_SEGMENT_MANAGER = "String  \"SEGMENTS\""
def ():
    '''returns MXSegmentManager\n\n
    (final String prefix, final String countField, final String seqenceField, final Map<String, String> segmentFieldsToActivityFields)\n
    '''
def pushSegmentMapToParentRow():
    '''returns None\n\n
    pushSegmentMapToParentRow(final MXGanttModel model, final MXActivity parent)\n
    '''
def updateParent():
    '''returns None\n\n
    updateParent(final MXActivity parent, final MXActivity childActivity, final int seq)\n
    '''
def buildSegmentActivityChildrenFromParentMap():
    '''returns None\n\n
    buildSegmentActivityChildrenFromParentMap(final MXGanttModel model, final MXActivity parent)\n
    '''
def pushChildSegmentsToParentMap():
    '''returns None\n\n
    pushChildSegmentsToParentMap(final MXGanttModel model, final MXActivity parent)\n
    '''
def compare():
    '''returns int\n\n
    compare(final MXSegmentActivity o1, final MXSegmentActivity o2)\n
    '''
def updateSegmentMapFromParentRowSegmentFields():
    '''returns None\n\n
    updateSegmentMapFromParentRowSegmentFields(final MXGanttModel model, final MXActivity parent)\n
    '''
def removeSegment():
    '''returns None\n\n
    removeSegment(final MXGanttModel model, final MXActivity parentSegmentActivity, final MXSegmentActivity act)\n
    '''
def addSegment():
    '''returns None\n\n
    addSegment(final MXGanttModel model, final MXActivity newParentSegmentActivity, final MXSegmentActivity act)\n
    '''
