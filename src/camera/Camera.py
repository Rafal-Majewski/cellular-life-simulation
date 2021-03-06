from abc import ABC, abstractmethod
from src.engine.world.World import World


class Camera(ABC):
	@abstractmethod
	def display(self, world: World) -> None:
		pass
