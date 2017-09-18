from datariumdb.voting import Voting


class BaseConsensusRules():
    """Base consensus rules for Datarium.

    A consensus plugin must expose a class inheriting from this one via an entry_point.

    All methods listed below must be implemented.

    """
    voting = Voting

    @staticmethod
    def validate_transaction(datarium, transaction):
        """See :meth:`datariumdb.models.Transaction.validate`
        for documentation."""
        return transaction.validate(datarium)

    @staticmethod
    def validate_block(datarium, block):
        """See :meth:`datariumdb.models.Block.validate` for documentation."""
        return block.validate(datarium)
