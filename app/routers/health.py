from typing import Annotated

from fastapi import APIRouter, Depends, status

from app.modules.health import HealthResponse, HealthService, get_health_service

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("/", status_code=status.HTTP_200_OK, response_model=HealthResponse)
async def get_health(
    service: Annotated[HealthService, Depends(get_health_service)],
) -> HealthResponse:
    return await service.health_check()
