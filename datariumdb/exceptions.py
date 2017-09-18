class DatariumDBError(Exception):
    """Base class for DatariumDB exceptions."""


class CriticalDoubleSpend(DatariumDBError):
    """Data integrity error that requires attention"""


class CriticalDoubleInclusion(DatariumDBError):
    """Data integrity error that requires attention"""


class CriticalDuplicateVote(DatariumDBError):
    """Data integrity error that requires attention"""
