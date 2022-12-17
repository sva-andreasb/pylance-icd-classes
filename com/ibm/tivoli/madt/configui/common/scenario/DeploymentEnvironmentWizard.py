CONFIGURE_TPAE_SCENARIO = "int  1"
CONFIGURE_NEW_APP_SERVER_SCENARIO = "int  2"
MIDDLEWARE_ONLY_SCENARIO = "int  3"
DB2_LOCAL = "int  2"
DB2_BASE_CONFIGURATION_DONE = "int  4"
DATABASE_CONFIGURATION_DONE = "int  8"
WAS_LOCAL = "int  16"
WAS_BASE_CONFIGURATION_DONE = "int  32"
APP_SERVER_CONFIGURATION_DONE = "int  64"
ITDS_LOCAL = "int  128"
ITDS_BASE_CONFIGURATION_DONE = "int  256"
CONFIGURE_75_UPGRADE_SCENARIO = "int  96"
def ():
    '''returns DeploymentEnvironmentWizard\n\n
    (final int scenario, final int state)\n
    '''
def dispose():
    '''returns None\n\n
    dispose()\n
    '''
