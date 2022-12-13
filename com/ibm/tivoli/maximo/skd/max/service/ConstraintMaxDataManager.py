def ConstraintMaxDataManager():
'''public ConstraintMaxDataManager(final MXServer mxServer)
'''
pass
def populateDataObjects():
'''public void populateDataObjects(final MboRemote projectMbo, final Map<String, ArrayList<String>> queryMap)
'''
pass
def loadDataObjects():
'''public JSONArray loadDataObjects(final Schedule schedule, final Activity activity, final MboRemote projectMbo, final DataSpec dataSpec, final Long offsetRecord)
public JSONArray loadDataObjects(final Schedule schedule, final JSONArray activities, final MboRemote projectMbo, final DataSpec dataSpec, final Long offsetRecord)
public JSONArray loadDataObjects(final Schedule schedule, final DataSpec dataSpec, final List<String> ids)
public JSONArray loadDataObjects(final Schedule schedule, final DataSpec dataSpec, final Long offsetRecord, final boolean parentOnly)
'''
pass
def processChanges():
'''public void processChanges(final MboRemote projectMbo, final List<Constraint> constraintChanges)
'''
pass
def commitChanges():
'''public void commitChanges(final MboRemote projectMbo, final MboSetRemote constraintSet, final String selectedIDs)
'''
pass
def getPageCount():
'''public int getPageCount(final Schedule schedule, final DataSpec dataSpec, final boolean parentOnly)
'''
pass
def getRowCount():
'''public int getRowCount(final Schedule schedule, final DataSpec dataSpec, final boolean parentOnly)
'''
pass
def bulkLoadDataObjects():
'''public JSONArray bulkLoadDataObjects(final Schedule schedule, final DataSpec dataSpec, final Long offsetRecord)
'''
pass
