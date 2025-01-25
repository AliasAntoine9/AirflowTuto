import logging
logger = logging.getLogger()


class ETL:
    @staticmethod
    def run() -> None:
        logger.warning("Airflow is running the Fake ETL!")


if __name__ == "__main__":
    ETL().run()
