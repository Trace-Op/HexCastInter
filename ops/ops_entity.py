from typing import Union, List
import core
from core import VMFrame


class GetPlayer(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="PLAYER",
            signature="-> Entity",
            name="Get player entity",
            game_name="Mind's Reflection",
            parameters=[],
            output=[core.Entity]
        )
    def execute(self, frame: VMFrame):
        frame.stack.append(frame.player.copy())

class ToPosition(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="TO_POS",
            signature="Entity -> Vec",
            name="Transform Entity to Position (eyes)",
            game_name="Compass' Purification",
            parameters=[core.Entity],
            output=[core.Vector]
        )
    def execute(self, frame: VMFrame):
        e = frame.stack.pop()
        r = e.position_eyes
        frame.stack.append(r)

class ToPositionStanding(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="TO_POS_FEET",
            signature="Entity -> Vec",
            name="Transform Entity to Position (feet)",
            game_name="Compass' Purification II",
            parameters=[core.Entity],
            output=[core.Vector]
        )
    def execute(self, frame: VMFrame):
        e = frame.stack.pop()
        r = e.position
        frame.stack.append(r)

class ToFacing(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="TO_FACING",
            signature="Entity -> Vec",
            name="Transform Entity to Facing Vector",
            game_name="Alidade's Purification",
            parameters=[core.Entity],
            output=[core.Vector]
        )
    def execute(self, frame: VMFrame):
        e = frame.stack.pop()
        r = e.facing
        frame.stack.append(r)

# The list of entity filters because I guess an EntityType flags attribute was too much.
# these all are (Pos -> Entity|Null)
# they are in here for the benefit of the analysis tools. and won't be supported until an entity framework is set up
class GetEntity(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="GETENTITY",
            signature="Vec -> Entity",
            name="Get Entity At",
            game_name="Entity Purification",
            parameters=[core.Vector],
            output=[Union[core.Entity, None]]
        )
    def execute(self, frame: VMFrame):
        raise NotImplementedError("please hold for proper entity management subsystem to online.")

class GetEntityAnimal(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="GETENTITY_ANIMAL",
            signature="Vec -> Entity",
            name="Get (Animal) Entity At",
            game_name="Entity Purification Animal",
            parameters=[core.Vector],
            output=[Union[core.Entity, None]]
        )
    def execute(self, frame: VMFrame):
        raise NotImplementedError("please hold for proper entity management subsystem to online.")

class GetEntityMonster(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="GETENTITY_MONSTER",
            signature="Vec -> Entity",
            name="Get (Monster) Entity At",
            game_name="Entity Purification Monster",
            parameters=[core.Vector],
            output=[Union[core.Entity, None]]
        )
    def execute(self, frame: VMFrame):
        raise NotImplementedError("please hold for proper entity management subsystem to online.")

class GetEntityItem(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="GETENTITY_ITEM",
            signature="Vec -> Entity",
            name="Get (Item) Entity At",
            game_name="Entity Purification Item",
            parameters=[core.Vector],
            output=[Union[core.Entity, None]]
        )
    def execute(self, frame: VMFrame):
        raise NotImplementedError("please hold for proper entity management subsystem to online.")

class GetEntityPlayer(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="GETENTITY_PLAYER",
            signature="Vec -> Entity",
            name="Get (Player) Entity At",
            game_name="Entity Purification Player",
            parameters=[core.Vector],
            output=[Union[core.Entity, None]]
        )
    def execute(self, frame: VMFrame):
        raise NotImplementedError("please hold for proper entity management subsystem to online.")

class GetEntityLiving(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="GETENTITY_LIVING",
            signature="Vec -> Entity",
            name="Get Entity At",
            game_name="Entity Purification",
            parameters=[core.Vector],
            output=[Union[core.Entity, None]]
        )
    def execute(self, frame: VMFrame):
        raise NotImplementedError("please hold for proper entity management subsystem to online.")

# Zone Filters, same as Entity filters but grab List[Entity] around a radius
# we will put in GetEntityZoneAny because that one makes sense.
# if there is one suggestion for upstream it is to have an "Entity Type Purification (Entity -> EntityTypesFlag (int maybe?))"
# there is also in the spec:
#  monster/non-monster
#  living/non-living
#  player/non-player
#  item/non-item
#  animal/non-animal
class GetEntityZoneAny(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="GETENTITY_ZONE_ANY",
            signature="Vec, Num -> List[Entity]",
            name="Get Entities Near",
            game_name="Zone Distillation: Any",
            parameters=[core.Vector, Union[int, float]],
            output=[List[core.Entity]]
        )
    def execute(self, frame: VMFrame):
        raise NotImplementedError("please hold for proper entity management subsystem to online.")