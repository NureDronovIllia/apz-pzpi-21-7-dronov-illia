from fastapi import APIRouter, Depends

from app.api.dependencies.services import get_fuel_service
from app.api.dependencies.user import get_current_user
from app.models.db.user import User
from app.services.fuel import FuelService

router = APIRouter(prefix="/fuel", tags=["Fuel"])


# TODO
@router.get("/suppliers/", response_model=None)
async def get_suppliers(
    current_user: User = Depends(get_current_user),
    fuel_service: FuelService = Depends(get_fuel_service),
) -> None:
    return await fuel_service.get_suppliers(current_user)


# TODO
@router.post("/suppliers/", response_model=None)
async def create_supplier(
    data: None,
    current_user: User = Depends(get_current_user),
    fuel_service: FuelService = Depends(get_fuel_service),
) -> None:
    return await fuel_service.create_supplier(data, current_user)


# TODO
@router.patch("/suppliers/{supplier_id}/update/", response_model=None)
async def update_supplier(
    data: None,
    supplier_id: int,
    current_user: User = Depends(get_current_user),
    fuel_service: FuelService = Depends(get_fuel_service),
) -> None:
    return await fuel_service.update_supplier(data, supplier_id, current_user)


# TODO
@router.delete("/suppliers/{supplier_id}/delete/", response_model=None)
async def delete_supplier(
    supplier_id: int,
    current_user: User = Depends(get_current_user),
    fuel_service: FuelService = Depends(get_fuel_service),
) -> None:
    return await fuel_service.delete_supplier(supplier_id, current_user)


# TODO
@router.get("/storages/", response_model=None)
async def get_storages(
    current_user: User = Depends(get_current_user),
    fuel_service: FuelService = Depends(get_fuel_service),
) -> None:
    return await fuel_service.get_storages(current_user)


# TODO
@router.post("/storages/", response_model=None)
async def create_storage(
    data: None,
    current_user: User = Depends(get_current_user),
    fuel_service: FuelService = Depends(get_fuel_service),
) -> None:
    return await fuel_service.create_storage(data, current_user)


# TODO
@router.patch("/storages/{storage_id}/update/", response_model=None)
async def update_storage(
    data: None,
    storage_id: int,
    current_user: User = Depends(get_current_user),
    fuel_service: FuelService = Depends(get_fuel_service),
) -> None:
    return await fuel_service.update_storage(data, storage_id, current_user)


# TODO
@router.delete("/storages/{storage_id}/delete/", response_model=None)
async def delete_storage(
    storage_id: int,
    current_user: User = Depends(get_current_user),
    fuel_service: FuelService = Depends(get_fuel_service),
) -> None:
    return await fuel_service.delete_storage(storage_id, current_user)


# TODO
@router.get("/pucrhases/", response_model=None)
async def get_purchases(
    current_user: User = Depends(get_current_user),
    fuel_service: FuelService = Depends(get_fuel_service),
) -> None:
    return await fuel_service.get_purchases(current_user)


# TODO
@router.post("/purchases/", response_model=None)
async def create_purchase(
    data: None,
    current_user: User = Depends(get_current_user),
    fuel_service: FuelService = Depends(get_fuel_service),
) -> None:
    return await fuel_service.create_purchase(data, current_user)
