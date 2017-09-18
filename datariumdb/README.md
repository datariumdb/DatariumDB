# Overview

A high-level description of the files and subdirectories of DatariumDB.

There are three database tables which underpin DatariumDB: `backlog`, where incoming transactions are held temporarily until they can be consumed; `datarium`, where blocks of transactions are written permanently; and `votes`, where votes are written permanently.  It is the votes in the `votes` table which must be queried to determine block validity and order. For more in-depth explanation, see [the whitepaper](https://www.datariumdb.com/whitepaper/).

## Files

### [`core.py`](./core.py)

The `Datarium` class is defined here.  Most operations outlined in the [whitepaper](https://www.datariumdb.com/whitepaper/) as well as database interactions are found in this file.  This is the place to start if you are interested in implementing a server API, since many of these class methods concern DatariumDB interacting with the outside world.

### [`models.py`](./models.py)

`Block`, `Transaction`, and `Asset` classes are defined here.  The classes mirror the block and transaction structure from the [documentation](https://docs.datariumdb.com/projects/server/en/latest/data-models/index.html), but also include methods for validation and signing.

### [`consensus.py`](./consensus.py)

Base class for consensus methods (verification of votes, blocks, and transactions).  The actual logic is mostly found in `transaction` and `block` models, defined in [`models.py`](./models.py).

### [`processes.py`](./processes.py)

Entry point for the DatariumDB process, after initialization.  All subprocesses are started here: processes to handle new blocks, votes, etc.

### [`config_utils.py`](./config_utils.py)

Methods for managing the configuration, including loading configuration files, automatically generating the configuration, and keeping the configuration consistent across DatariumDB instances.

## Folders

### [`pipelines`](./pipelines)

Structure and implementation of various subprocesses started in [`processes.py`](./processes.py).

### [`commands`](./commands)

Contains code for the [CLI](https://docs.datariumdb.com/projects/server/en/latest/server-reference/datariumdb-cli.html) for DatariumDB.

### [`db`](./db)

Code for building the database connection, creating indexes, and other database setup tasks.
