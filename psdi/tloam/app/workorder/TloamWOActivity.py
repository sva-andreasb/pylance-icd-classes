def ():
    '''returns TloamWOActivity\n\n
    (final MboSet ms)\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def canDelete():
    '''returns None\n\n
    canDelete()\n
    '''
def delete():
    '''returns None\n\n
    delete(final long accessModifier)\n
    '''
def undelete():
    '''returns None\n\n
    undelete()\n
    '''
def editHistory():
    '''returns None\n\n
    editHistory()\n
    '''
def canEditRelatedSet():
    '''returns None\n\n
    canEditRelatedSet(final String relationName)\n
    '''
def copy():
    '''returns MboRemote\n\n
    copy(final MboSetRemote mboset, final long mboAddFlags)\n
    '''
def incrActLicCost():
    '''returns None\n\n
    incrActLicCost(final double incrAmount, final boolean isOutsideCost)\n
    '''
def incrEstLicCost():
    '''returns None\n\n
    incrEstLicCost(final double incrAmount)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def getMboSet():
    '''returns MboSetRemote\n\n
    getMboSet(String name)\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(final String status, final Date date, final String memo, final long accessModifier, final boolean comingFromReceiving)\n
    '''
def copyJobPlanToWorkPlan():
    '''returns None\n\n
    copyJobPlanToWorkPlan()\n
    '''
def createJPFromWO():
    '''returns MboRemote\n\n
    createJPFromWO(final Date date, final String jpnum, final String description, final String longdescription)\n
    '''
def isNewDuplicatedItem():
    '''returns boolean\n\n
    isNewDuplicatedItem()\n
    '''
def duplicate():
    '''returns MboRemote\n\n
    duplicate()\n
    '''
