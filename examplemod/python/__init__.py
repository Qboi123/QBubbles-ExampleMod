import json
import os
import time

from qbubbles.events import PreInitializeEvent, PostInitializeEvent, InitializeEvent
from qbubbles.resources import ModelLoader, Resources
from qbubbles.modloader import Mod, ModSkeleton
from qbubbles.registry import Registry

from python.bubbles import init_bubbles
from python.globals import MODID, MODNAME, VERSION


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
        try:
            data = self.zipimport.get_data("assets/models/bubble/example_bubble.json")
        except AttributeError:
            with open(os.path.join(self.modPath, "../assets/models/bubble/example_bubble.json"), "r") as file:
                data = file.read()
        models = {}
        models["example_bubble"] = json.loads(data)
        bubbles = init_bubbles()
        modelLoader = ModelLoader()
        evt.canvas.itemconfig(evt.t2, text="Initialize bubbles")
        for bubble in bubbles:
            for i in range(50):
                evt.canvas.itemconfig(evt.t2, text=f"Initialize bubble: '{bubble.get_uname()}' {i}/50")
                evt.canvas.update()
                time.sleep(0.05)
            uname = f"{self.modID}:{bubble.get_uname()}"
            images = modelLoader.generate_bubble_images(bubble.minRadius, bubble.maxRadius, models[bubble.get_uname()])
            Registry.register_bubble(uname, bubble)
            Registry.register_bubresource(uname, "images", images)
        print(f"Initialized mod {self.modID}")

    def post_initialize(self, evt: PostInitializeEvent):
        print(f"Post initialized mod {self.modID}")


print(os.listdir("."))
