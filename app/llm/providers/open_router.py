from langchain_openai import ChatOpenAI

from app.core.config import settings

model = ChatOpenAI(
    model=settings.openapi.model,
    base_url=settings.openapi.base_url,
    api_key=settings.openapi.api_key,
)
