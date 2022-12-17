def ():
    '''returns ConstraintMaxDataManager\n\n
    (final MXServer mxServer)\n
    '''
def populateDataObjects():
    '''returns None\n\n
    populateDataObjects(final MboRemote projectMbo, final Map<String, ArrayList<String>> queryMap)\n
    '''
def loadDataObjects():
    '''returns JSONArray\n\n
    loadDataObjects(final Schedule schedule, final Activity activity, final MboRemote projectMbo, final DataSpec dataSpec, final Long offsetRecord)\n
    loadDataObjects(final Schedule schedule, final JSONArray activities, final MboRemote projectMbo, final DataSpec dataSpec, final Long offsetRecord)\n
    loadDataObjects(final Schedule schedule, final DataSpec dataSpec, final List<String> ids)\n
    loadDataObjects(final Schedule schedule, final DataSpec dataSpec, final Long offsetRecord, final boolean parentOnly)\n
    '''
def processChanges():
    '''returns None\n\n
    processChanges(final MboRemote projectMbo, final List<Constraint> constraintChanges)\n
    '''
def commitChanges():
    '''returns None\n\n
    commitChanges(final MboRemote projectMbo, final MboSetRemote constraintSet, final String selectedIDs)\n
    '''
def getPageCount():
    '''returns int\n\n
    getPageCount(final Schedule schedule, final DataSpec dataSpec, final boolean parentOnly)\n
    '''
def getRowCount():
    '''returns int\n\n
    getRowCount(final Schedule schedule, final DataSpec dataSpec, final boolean parentOnly)\n
    '''
def bulkLoadDataObjects():
    '''returns JSONArray\n\n
    bulkLoadDataObjects(final Schedule schedule, final DataSpec dataSpec, final Long offsetRecord)\n
    '''
