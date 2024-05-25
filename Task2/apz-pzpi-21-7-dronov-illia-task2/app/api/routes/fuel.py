from fastapi import APIRouter, Depends
from app.api.dependencies.services import get_fuel_service
from app.api.dependencies.user import get_current_user
from app.models.db.user import User
from app.services.fuel import FuelService


router = APIRouter(prefix="/fuel", tags=["Fuel"])

# TODO
@router.get("/fuel_suppliers/", response_model=None)
async def get_fuel_suppliers(
    current_user: User = Depends(get_current_user),
    fuel_service: FuelService = Depends(get_fuel_service),
) -> None:
    return await fuel_service.get_fuel_suppliers(current_user)

# TODO
@router.post("/fuel_suppliers/", response_model=None)
async def create_fuel_supplier(
    data: None,
    current_user: User = Depends(get_current_user),
    fuel_service: FuelService = Depends(get_fuel_service),
) -> None:
    return await fuel_service.create_fuel_supplier(data, current_user)

# TODO
@router.patch("/fuel_suppliers/{fuel_supplier_id}/update/", response_model=None)
async def update_fuel_supplier(
    data: None,
    fuel_supplier_id: int,
    current_user: User = Depends(get_current_user),
    fuel_service: FuelService = Depends(get_fuel_service),
) -> None:
    return await fuel_service.update_fuel_supplier(data, fuel_supplier_id, current_user)

# TODO
@router.delete("/fuel_suppliers/{fuel_supplier_id}/delete/", response_model=None)
async def delete_fuel_supplier(
    fuel_supplier_id: int,
    current_user: User = Depends(get_current_user),
    fuel_service: FuelService = Depends(get_fuel_service),
) -> None:
    return await fuel_service.delete_fuel_supplier(fuel_supplier_id, current_user)


# TODO
@router.get("/fuel_storages/", response_model=None)
async def get_fuel_storages(
    current_user: User = Depends(get_current_user),
    fuel_service: FuelService = Depends(get_fuel_service),
) -> None:
    return await fuel_service.get_fuel_storages(current_user)

# TODO
@router.post("/fuel_storages/", response_model=None)
async def create_fuel_storage(
    data: None,
    current_user: User = Depends(get_current_user),
    fuel_service: FuelService = Depends(get_fuel_service),
) -> None:
    return await fuel_service.create_fuel_storage(data, current_user)

# TODO
@router.patch("/fuel_storages/{fuel_storage_id}/update/", response_model=None)
async def update_fuel_storage(
    data: None,
    fuel_storage_id: int,
    current_user: User = Depends(get_current_user),
    fuel_service: FuelService = Depends(get_fuel_service),
) -> None:
    return await fuel_service.update_fuel_storage(data, fuel_storage_id, current_user)

# TODO
@router.delete("/fuel_storages/{fuel_storage_id}/delete/", response_model=None)
async def delete_fuel_storage(
    fuel_storage_id: int,
    current_user: User = Depends(get_current_user),
    fuel_service: FuelService = Depends(get_fuel_service),
) -> None:
    return await fuel_service.delete_fuel_storage(fuel_storage_id, current_user)

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