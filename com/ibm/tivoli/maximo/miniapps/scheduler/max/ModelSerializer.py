def ():
    '''returns ModelSerializer\n\n
    (final Supplier<UIOptions> optionsSupplier, final MaxSerializationHelper helper)\n
    '''
def serializeChildren():
    '''returns JSONObject\n\n
    serializeChildren(final Schedule schedule, final String activityID)\n
    serializeChildren(final Schedule schedule, final String activityID, final int level)\n
    '''
def serializePage():
    '''returns JSONObject\n\n
    serializePage(final Schedule schedule, final int p)\n
    '''
def serializeHierarchy():
    '''returns JSONObject\n\n
    serializeHierarchy(final Schedule schedule, String activityID)\n
    '''
def serializeCircularDependencies():
    '''returns JSONObject\n\n
    serializeCircularDependencies(final Schedule schedule, final List<String> activityIDs)\n
    '''
def serializeCompareRootPages():
    '''returns JSONObject\n\n
    serializeCompareRootPages(final Schedule leftSchedule, final Schedule rightSchedule)\n
    '''
def serializeRootPages():
    '''returns JSONObject\n\n
    serializeRootPages(final Schedule schedule)\n
    '''
def serializeAllRecords():
    '''returns JSONObject\n\n
    serializeAllRecords(final Schedule schedule)\n
    '''
