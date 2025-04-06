from manim import *

class Jank(Scene):
    def construct(self):
        
        x = 'GuhuG'
        y = 84

        text = Text(f"fuck this is so jank hopefully it works")
        self.play(Write(text))
        self.play(FadeOut(text))
        test = Text(f"{x}, {y}")
        self.play(Write(test))
        self.wait(1)