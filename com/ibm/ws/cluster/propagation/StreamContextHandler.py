MAX_SERVER_WEIGHT = "int  20"
def parseVersion1():
    '''returns None\n\n
    parseVersion1(final DataInput datai)\n
    '''
def parseVersion2():
    '''returns None\n\n
    parseVersion2(final ObjectInput ois, final boolean isPull, final DescriptionKey clusterKey, final boolean publish)\n
    parseVersion2(final ObjectInput ois, final boolean isPull, final DescriptionKey clusterKey)\n
    '''
def exportVersion1():
    '''returns byte[]\n\n
    exportVersion1(final ClusterDescription cd, final String clusterName)\n
    '''
def exportVersion2():
    '''returns byte[]\n\n
    exportVersion2(final boolean createDataOutputStream, final ClusterDescription[] cd, final boolean isPull, final boolean isTriggerPropagation)\n
    '''
def parseVersion2IIOPClusterMemberDescription():
    '''returns None\n\n
    parseVersion2IIOPClusterMemberDescription(final IIOPClusterMemberDescription iiopMember, final ObjectInput in)\n
    '''
def parseVersion2LSDClusterMemberDescription():
    '''returns None\n\n
    parseVersion2LSDClusterMemberDescription(final LSDClusterMemberDescription lsdMember, final ObjectInput in)\n
    '''
def parseVersion2SelectionClusterMemberDescription():
    '''returns None\n\n
    parseVersion2SelectionClusterMemberDescription(final SelectionClusterMemberDescription selectionMember, final ObjectInput in)\n
    '''
def run():
    '''returns Object\n\n
    run()\n
    '''
