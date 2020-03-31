from qbubbles.bubbles import Bubble


class ExampleBubble(Bubble):
    def __init__(self):
        super(ExampleBubble, self).__init__()

        self.priority = 250000
        self.minRadius = 21
        self.maxRadius = 80
        self.minSpeed = 10
        self.maxSpeec = 25
        self.hardness = 1

        self.set_uname("example_bubble")
