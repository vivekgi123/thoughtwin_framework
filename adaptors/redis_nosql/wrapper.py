import redis_om

from redis_om import get_redis_connection, Migrator


class AdaptorWrapper:
    """_summary_

    Returns:
        _type_: _description_
    """

    @classmethod
    def connetion_agent(cls):
        """_summary_

        Returns:
            _type_: _description_
        """
        return get_redis_connection()

    @classmethod
    def setting_agent(cls):
        """_summary_

        Returns:
            _type_: _description_
        """
        return Migrator
