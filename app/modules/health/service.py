from app.modules.health.dto import HealthResponse


class HealthService:
    async def health_check(self) -> HealthResponse:
        return HealthResponse(status="ok")
