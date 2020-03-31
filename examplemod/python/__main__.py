import os
import time

from qbubbles.events import PreInitializeEvent, PostInitializeEvent, InitializeEvent
from qbubbles.resources import ModelLoader, Resources
from qbubbles.modloader import Mod, ModSkeleton
from qbubbles.registry import Registry

from .bubbles import init_bubbles
from .globals import MODID, MODNAME, VERSION


@Mod(modid=MODID, name=MODNAME, version=VERSION)
class ExampleMod(ModSkeleton):
    def __init__(self):
        print(f"Loaded Mod {self.modID}")
        PreInitializeEvent.bind(self.pre_initialize)
        InitializeEvent.bind(self.initialize)
        PostInitializeEvent.bind(self.post_initialize)

    def pre_initialize(self, evt: PreInitializeEvent):
        print(f"Pre initialized mod {self.modID}")

    def initialize(self, evt: InitializeEvent):
        self.zipimport.get_data("assets/models/bubble/example_bubble.json")
        bubbles = init_bubbles()
        evt.canvas.itemconfig(evt.t2, text="Initialize bubbles")
        for bubble in bubbles:
            for i in range(50):
                evt.canvas.itemconfig(evt.t2, text=f"Initialize bubble: '{bubble.get_uname()}'")
                evt.canvas.update()
                time.sleep(0.05)
            Registry.register_bubble(f"{self.modID}:{bubble.get_uname()}", bubble)
        print(f"Initialized mod {self.modID}")

    def post_initialize(self, evt: PostInitializeEvent):
        print(f"Post initialized mod {self.modID}")


print(os.listdir("."))
