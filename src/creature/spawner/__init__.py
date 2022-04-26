from src.engine.physics.utils.joint.Joint import Joint
from src.engine.atoms.cell.Cell import Cell


class CreatureSpawner:
	def __init__(self) -> None:
		self._cells: dict[str, Cell] = dict[str, Cell]()
		self._joints: dict[str, Joint] = dict[str, Joint]()
