from typing import Any

import requests

from config import get_base_url, get_jwt

JWT: str = get_jwt()
BASE_URL: str = get_base_url()


def get_storages() -> list[dict]:
    response = requests.get(
        f"{BASE_URL}/storages/", headers={"Authorization": f"Bearer {JWT}"}
    )
    return response.json()



def get_storages_ids() -> list[int]:
    storages: list[dict] = get_storages()
    return [storage["id"] for storage in storages]


def get_storage_critical_lvl(storage_id: int) -> int:
    response = requests.get(
        f"{BASE_URL}/storages/", headers={"Authorization": f"Bearer {JWT}"}
    )
    data: dict[str, Any] = response.json()

    return [storage["id"] for storage in data]


def get_storage_current_lvl(storage_id: int) -> int:
    response = requests.get(
        f"{BASE_URL}/storages/", headers={"Authorization": f"Bearer {JWT}"}
    )
    data: dict[str, Any] = response.json()

    return [storage["id"] for storage in data]


# def change_current_
