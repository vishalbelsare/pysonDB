import json
import os
from typing import Any
from typing import Dict
from uuid import uuid4

from .errors import DataError


def verify_data(data: Dict[str, Any], db: Dict[str, Dict[str, Any]]) -> bool:
    if db:
        if sorted(list(db.values())[0]) == sorted(list(data)):
            return True

        else:
            raise DataError(
                "The data provided does not comply with the schema of the intially provided data"
            )

    return True


def get_id(db: Dict[str, Dict[str, Any]]) -> str:
    """Generates a new uuid and then checks whether it exists in the DB"""

    def get_id() -> str:
        _id = str(uuid4().int)[:18]
        if _id in db:
            return get_id()

        else:
            return _id

    return get_id()


def create_db(filename: str, create_file: bool = True) -> None:
    def create(filename: str, data: str) -> None:
        with open(filename, "w") as db_file:
            db_file.write(data)

    if filename.endswith(".json"):
        if create_file and not os.path.exists(filename):
            create(filename, json.dumps({}))  # just simply write empty data
