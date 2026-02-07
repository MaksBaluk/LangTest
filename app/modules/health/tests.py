import pytest

from app.modules.health import HealthResponse, get_health_service


@pytest.mark.anyio
async def test_health_check():
    assert await get_health_service().health_check() == HealthResponse(status="ok")
