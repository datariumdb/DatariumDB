"""Generic backend database interfaces expected by DatariumDB.

The interfaces in this module allow DatariumDB to be agnostic about its
database backend. One can configure DatariumDB to use different databases as
its data store by setting the ``database.backend`` property in the
configuration or the ``DATARIUMDB_DATABASE_BACKEND`` environment variable.
"""

# Include the backend interfaces
from datariumdb.backend import admin, changefeed, schema, query  # noqa

from datariumdb.backend.connection import connect  # noqa
from datariumdb.backend.changefeed import get_changefeed  # noqa
