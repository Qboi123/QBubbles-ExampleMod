from typing import List

from qbubbles.bubbles import Bubble

from .exampleBubble import ExampleBubble

BUBBLES: List[Bubble] = []


def init_bubbles():
    BUBBLES.append(ExampleBubble())
    return BUBBLES
