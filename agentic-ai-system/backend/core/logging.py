import logging
import json
import sys

from datetime import datetime


class JSONFormatter(logging.Formatter):

    def format(self, record):

        log = {
            "time": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "module": record.module,
            "message": record.getMessage()
        }

        if hasattr(record, "session_id"):
            log["session_id"] = record.session_id

        if hasattr(record, "tokens"):
            log["tokens"] = record.tokens

        return json.dumps(log)


def setup_logging():

    handler = logging.StreamHandler(sys.stdout)

    handler.setFormatter(JSONFormatter())

    logging.basicConfig(
        level=logging.INFO,
        handlers=[handler],
        force=True
    )


setup_logging()

logger = logging.getLogger(__name__)