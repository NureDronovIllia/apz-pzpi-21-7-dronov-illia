from fastapi import APIRouter, Depends

from app.api.dependencies.services import get_vehicle_service
from app.api.dependencies.user import get_current_user
from app.models.db.user import User
from app.services.vehicle import VehicleService

router = APIRouter(prefix="/vehicles", tags=["Vehicles"])

# TODO
@router.get("/", response_model=None)
async def get_vehicles(
     current_user: User = Depends(get_current_user),
    vehicle_service: VehicleService = Depends(get_vehicle_service),
) -> None:
    return await vehicle_service.get_vehicles(current_user)

# TODO
@router.get("/get_current_status", response_model=None)
async def get_current_status(
    vehicle_id: int,
    current_user: User = Depends(get_current_user),
    vehicle_service: VehicleService = Depends(get_vehicle_service),
) -> None:
    return await vehicle_service.get_current_status(vehicle_id, current_user)

# TODO
@router.post("/set_current_status", response_model=None)
async def set_current_status(
    vehicle_id: int,
    current_user: User = Depends(get_current_user),
    vehicle_service: VehicleService = Depends(get_vehicle_service),
) -> None:
    return await vehicle_service.set_current_status(vehicle_id, current_user)

# TODO
@router.post("/create/", response_model=None, status_code=201)
async def create_vehicle(
    data: None,
    current_user: User = Depends(get_current_user),
    vehicle_service: VehicleService = Depends(get_vehicle_service),
) -> None:
    return await vehicle_service.create_vehicle(data, current_user)

# TODO
@router.patch("/{vehicle_id}/update/", response_model=None)
async def update_vehicle(
    vehicle_id: int, 
    data: None,
    current_user: User = Depends(get_current_user),
    vehicle_service: VehicleService = Depends(get_vehicle_service),
) -> None:
    return await vehicle_service.update_vehicle(vehicle_id, data, current_user)

# TODO
@router.delete("/{vehicle_id}/delete/", response_model=None, status_code=204)
async def delete_vehicle(
    vehicle_id: int, 
    current_user: User = Depends(get_current_user),
    vehicle_service: VehicleService = Depends(get_vehicle_service),
) -> None:
    return await vehicle_service.delete_vehicle(vehicle_id, current_user)

# TODO
@router.get("/inspections/", response_model=None)
async def get_inspections(
    current_user: User = Depends(get_current_user),
    vehicle_service: VehicleService = Depends(get_vehicle_service),
) -> None:
    return await vehicle_service.get_inspections(current_user)

# TODO
@router.post("/inspections/start/", response_model=None)
async def start_inspection(
    vehicle_id: int, 
    current_user: User = Depends(get_current_user),
    vehicle_service: VehicleService = Depends(get_vehicle_service),
) -> None:
    return await vehicle_service.start_inspection(vehicle_id, current_user)


# TODO
@router.post("/inspections/{inspection_id}/end/", response_model=None)
async def end_inspection(
    inspection_id: int, 
    current_user: User = Depends(get_current_user),
    vehicle_service: VehicleService = Depends(get_vehicle_service),
) -> None:
    return await vehicle_service.end_inspection(inspection_id, current_user)