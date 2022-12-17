ROOT_NODE = "String  \"ROOT\""
WO_INTERNAL_STATUS_APPR = "String  \"APPR\""
PROPERTY_READ_ONLY_MODEL = "String  \"__READ_ONLY_MODEL\""
def visit():
    '''returns None\n\n
    visit(final IlvActivity item, final IlvGanttModel model, final Set<String> state)\n
    visit(final IlvActivity item, final IlvGanttModel model, final HasCancelled state)\n
    visit(final IlvActivity item, final IlvGanttModel model, final Void state)\n
    visit(final IlvHierarchyNode item, final IlvGanttModel model, final Void state)\n
    visit(final IlvActivity item, final IlvGanttModel model, final HasCancelled state)\n
    visit(final IlvHierarchyNode type, final IlvGanttModel model, final Void state)\n
    '''
def compare():
    '''returns int\n\n
    compare(final MXActivity o1, final MXActivity o2)\n
    '''
def ():
    '''returns CountingVisitor\n\n
    (final String id)\n
    (final String id)\n
    (final String fld, final Object value)\n
    (final List<String> flds, final List<Object> values)\n
    (final String fld, final Object value)\n
    (final String id)\n
    (final IFilter<IlvActivity> filter)\n
    (final IFilter<IlvHierarchyNode> filter)\n
    (final List<String> objectNames)\n
    ()\n
    '''
def test():
    '''returns boolean\n\n
    test(final IlvActivity in)\n
    test(final IlvResource in)\n
    test(final IlvActivity in)\n
    test(final IlvActivity in)\n
    test(final IlvResource in)\n
    '''
def isCancelled():
    '''returns boolean\n\n
    isCancelled()\n
    isCancelled()\n
    '''
def cancel():
    '''returns None\n\n
    cancel()\n
    cancel()\n
    '''
def getActivity():
    '''returns IlvActivity\n\n
    getActivity()\n
    '''
def getActivities():
    '''returns List<IlvActivity>\n\n
    getActivities()\n
    '''
def getNodes():
    '''returns List<IlvHierarchyNode>\n\n
    getNodes()\n
    '''
def isValid():
    '''returns boolean\n\n
    isValid()\n
    '''
def canAccept():
    '''returns boolean\n\n
    canAccept(final IlvActivity act)\n
    '''
def getCount():
    '''returns long\n\n
    getCount()\n
    '''
