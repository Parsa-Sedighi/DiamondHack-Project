from manim import *

class Jank(Scene):
    def construct(self):
        
        x = ++x
        y = ++y

        text = Text(f"fuck this is so jank hopefully it works")
        self.play(Write(text))
        self.play(FadeOut(text))
        test = Text(f"{x}, {y}")
        self.play(Write(test))
        self.wait(1)