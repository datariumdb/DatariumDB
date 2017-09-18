"""Module to store messages used in commands, such as error messages,
warnings, prompts, etc.

"""
CANNOT_START_KEYPAIR_NOT_FOUND = (
    "Can't start DatariumDB, no keypair found. "
    'Did you run `datariumdb configure`?'
)

RETHINKDB_STARTUP_ERROR = 'Error starting RethinkDB, reason is: {}'
