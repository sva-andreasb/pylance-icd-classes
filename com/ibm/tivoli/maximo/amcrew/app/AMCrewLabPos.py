def ():
    '''returns LaborStatusCompare\n\n
    (final MboSet ms)\n
    (final MboRemote currentLabor)\n
    '''
def init():
    '''returns None\n\n
    init()\n
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
def deleteAssociatedQuals():
    '''returns None\n\n
    deleteAssociatedQuals(final String position)\n
    '''
def deleteAssociatedLabor():
    '''returns None\n\n
    deleteAssociatedLabor(final String position)\n
    '''
def setRequirementStatus():
    '''returns None\n\n
    setRequirementStatus(final String amcrew, final String orgid, final Date crewShiftStart, final Date crewShiftEnd, final Date crewDate)\n
    '''
def setStatusFromAssignedLabor():
    '''returns None\n\n
    setStatusFromAssignedLabor(final MboSet laborSet, final Date crewShiftStart, final Date crewShiftEnd, final Date crewDate)\n
    '''
def sortLaborWithModAvail():
    '''returns ArrayList<LaborStatusCompare>\n\n
    sortLaborWithModAvail(final MboSet laborSet, final Date crewDate)\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final LaborStatusCompare compareLabor)\n
    '''
