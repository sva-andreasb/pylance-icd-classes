def ():
    '''returns RegistrarImpl_Stub\n\n
    (final RemoteRef ref)\n
    '''
def addAttributes():
    '''returns None\n\n
    addAttributes(final ServiceID serviceID, final long value, final EntryRep[] array)\n
    '''
def addLookupAttributes():
    '''returns None\n\n
    addLookupAttributes(final Entry[] array)\n
    '''
def addLookupGroups():
    '''returns None\n\n
    addLookupGroups(final String[] array)\n
    '''
def addLookupLocators():
    '''returns None\n\n
    addLookupLocators(final LookupLocator[] array)\n
    '''
def addMemberGroups():
    '''returns None\n\n
    addMemberGroups(final String[] array)\n
    '''
def cancelEventLease():
    '''returns None\n\n
    cancelEventLease(final long value, final long value2)\n
    '''
def cancelLeases():
    '''returns Exception[]\n\n
    cancelLeases(final Object[] array, final long[] array2)\n
    '''
def cancelServiceLease():
    '''returns None\n\n
    cancelServiceLease(final ServiceID serviceID, final long value)\n
    '''
def destroy():
    '''returns None\n\n
    destroy()\n
    '''
def getAdmin():
    '''returns Object\n\n
    getAdmin()\n
    '''
def getEntryClasses():
    '''returns EntryClassBase[]\n\n
    getEntryClasses(final Template template)\n
    '''
def getFieldValues():
    '''returns Object[]\n\n
    getFieldValues(final Template template, final int value, final int value2)\n
    '''
def getLocator():
    '''returns LookupLocator\n\n
    getLocator()\n
    '''
def getLogToSnapshotThreshold():
    '''returns int\n\n
    getLogToSnapshotThreshold()\n
    '''
def getLookupAttributes():
    '''returns Entry[]\n\n
    getLookupAttributes()\n
    '''
def getLookupGroups():
    '''returns String[]\n\n
    getLookupGroups()\n
    '''
def getLookupLocators():
    '''returns LookupLocator[]\n\n
    getLookupLocators()\n
    '''
def getMemberGroups():
    '''returns String[]\n\n
    getMemberGroups()\n
    '''
def getMinMaxEventLease():
    '''returns long\n\n
    getMinMaxEventLease()\n
    '''
def getMinMaxServiceLease():
    '''returns long\n\n
    getMinMaxServiceLease()\n
    '''
def getMinRenewalInterval():
    '''returns long\n\n
    getMinRenewalInterval()\n
    '''
def getServiceID():
    '''returns ServiceID\n\n
    getServiceID()\n
    '''
def getServiceTypes():
    '''returns ServiceTypeBase[]\n\n
    getServiceTypes(final Template template, final String s)\n
    '''
def getSnapshotWeight():
    '''returns float\n\n
    getSnapshotWeight()\n
    '''
def getStorageLocation():
    '''returns String\n\n
    getStorageLocation()\n
    '''
def getUnicastPort():
    '''returns int\n\n
    getUnicastPort()\n
    '''
def lookup():
    '''returns Matches\n\n
    lookup(final Template template)\n
    lookup(final Template template, final int value)\n
    '''
def modifyAttributes():
    '''returns None\n\n
    modifyAttributes(final ServiceID serviceID, final long value, final EntryRep[] array, final EntryRep[] array2)\n
    '''
def modifyLookupAttributes():
    '''returns None\n\n
    modifyLookupAttributes(final Entry[] array, final Entry[] array2)\n
    '''
def notify():
    '''returns EventRegistration\n\n
    notify(final Template template, final int value, final RemoteEventListener remoteEventListener, final MarshalledObject marshalledObject, final long value2)\n
    '''
def register():
    '''returns ServiceRegistration\n\n
    register(final Item item, final long value)\n
    '''
def removeLookupGroups():
    '''returns None\n\n
    removeLookupGroups(final String[] array)\n
    '''
def removeLookupLocators():
    '''returns None\n\n
    removeLookupLocators(final LookupLocator[] array)\n
    '''
def removeMemberGroups():
    '''returns None\n\n
    removeMemberGroups(final String[] array)\n
    '''
def renewEventLease():
    '''returns long\n\n
    renewEventLease(final long value, final long value2, final long value3)\n
    '''
def renewLeases():
    '''returns RenewResults\n\n
    renewLeases(final Object[] array, final long[] array2, final long[] array3)\n
    '''
def renewServiceLease():
    '''returns long\n\n
    renewServiceLease(final ServiceID serviceID, final long value, final long value2)\n
    '''
def setAttributes():
    '''returns None\n\n
    setAttributes(final ServiceID serviceID, final long value, final EntryRep[] array)\n
    '''
def setLogToSnapshotThreshold():
    '''returns None\n\n
    setLogToSnapshotThreshold(final int value)\n
    '''
def setLookupGroups():
    '''returns None\n\n
    setLookupGroups(final String[] array)\n
    '''
def setLookupLocators():
    '''returns None\n\n
    setLookupLocators(final LookupLocator[] array)\n
    '''
def setMemberGroups():
    '''returns None\n\n
    setMemberGroups(final String[] array)\n
    '''
def setMinMaxEventLease():
    '''returns None\n\n
    setMinMaxEventLease(final long value)\n
    '''
def setMinMaxServiceLease():
    '''returns None\n\n
    setMinMaxServiceLease(final long value)\n
    '''
def setMinRenewalInterval():
    '''returns None\n\n
    setMinRenewalInterval(final long value)\n
    '''
def setSnapshotWeight():
    '''returns None\n\n
    setSnapshotWeight(final float value)\n
    '''
def setStorageLocation():
    '''returns None\n\n
    setStorageLocation(final String s)\n
    '''
def setUnicastPort():
    '''returns None\n\n
    setUnicastPort(final int value)\n
    '''
