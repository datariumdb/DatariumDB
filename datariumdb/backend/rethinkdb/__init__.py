"""RethinkDB backend implementation.

Contains a RethinkDB-specific implementation of the
:mod:`~datariumdb.backend.changefeed`, :mod:`~datariumdb.backend.query`, and
:mod:`~datariumdb.backend.schema` interfaces.

You can specify DatariumDB to use RethinkDB as its database backend by either
setting ``database.backend`` to ``'rethinkdb'`` in your configuration file, or
setting the ``DATARIUMDB_DATABASE_BACKEND`` environment variable to
``'rethinkdb'``.

If configured to use RethinkDB, DatariumDB will automatically return instances
of :class:`~datariumdb.backend.rethinkdb.RethinkDBConnection` for
:func:`~datariumdb.backend.connection.connect` and dispatch calls of the
generic backend interfaces to the implementations in this module.
"""

# Register the single dispatched modules on import.
from datariumdb.backend.rethinkdb import admin, changefeed, schema, query  # noqa

# RethinkDBConnection should always be accessed via
# ``datariumdb.backend.connect()``.
