METADATA_PATTERN = "String  \"META-INF/[^/]*|WEB-INF/[^/]*|.*wsdl|META-INF/wsdl/.*|WEB-INF/wsdl/.*\""
THISDIR_PATTERN = "String  \"/[^/]*\""
WHOLEDIR_PATTERN = "String  \"/.*\""
DelModules = "String  \"MetadataTask.deletedMods\""
AddedModules = "String  \"MetadataTask.addedMods\""
SAVE_BUFFER_SIZE = "int  8192"
def performTask():
    '''returns boolean\n\n
    performTask()\n
    '''
