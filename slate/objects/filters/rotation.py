# Future
from __future__ import annotations

# Standard Library
from typing import TypedDict


__all__ = (
    "ObsidianRotationData",
    "LavalinkRotationData",
    "Rotation",
)

ObsidianRotationData = float


class LavalinkRotationData(TypedDict):
    rotationHz: float


class Rotation:

    def __init__(
        self,
        *,
        speed: float = 5.0
    ) -> None:
        self.speed: float = speed

    def __repr__(self) -> str:
        return f"<slate.Rotation speed={self.speed}>"

    def _construct_obsidian_payload(self) -> ObsidianRotationData:
        return self.speed

    def _construct_lavalink_payload(self) -> LavalinkRotationData:
        return {
            "rotationHz": self.speed,
        }