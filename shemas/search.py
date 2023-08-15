from pydantic import BaseModel


class SearchQuery(BaseModel):
    key: str
    value: str
