def ():
    '''returns InspectionService\n\n
    ()\n
    (final MXServer mxServer)\n
    '''
def changeFormStatus():
    '''returns None\n\n
    changeFormStatus(@WSMboKey("INSPECTIONFORM") final InspectionFormRemote inspForm, final String status)\n
    '''
def changeResultStatus():
    '''returns None\n\n
    changeResultStatus(@WSMboKey("INSPECTIONRESULT") final InspectionResultRemote inspResult, final String status)\n
    '''
def changeResultStatusMobile():
    '''returns None\n\n
    changeResultStatusMobile(@WSMboKey("INSPECTIONRESULT") final InspectionResultRemote inspResult, final String status)\n
    '''
def updateAssetLocMeter():
    '''returns None\n\n
    updateAssetLocMeter(@WSMboKey("INSPECTIONRESULT") final InspectionResultRemote inspResult, final String referenceobject, final String referenceobjectid, final String asset, final String location, final String siteid, final String orgid, final String inspformnum, final String resultnum)\n
    '''
def getRevision():
    '''returns MboRemote\n\n
    getRevision(@WSMboKey("INSPECTIONFORM") final InspectionFormRemote inspForm)\n
    '''
