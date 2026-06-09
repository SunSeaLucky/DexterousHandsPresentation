from dataclasses import dataclass


@dataclass(frozen=True)
class Reference:
    url: str
    title: str | None = None
    authors: list[str] | None = None
    date: str | None = None
    organization: str | None = None
    description: str | None = None
    notes: str | None = None
