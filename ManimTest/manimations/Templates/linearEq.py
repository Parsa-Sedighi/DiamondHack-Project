from manim import *

class Linear(Scene):
    def construct(self):
        
        y = ++y
        m = ++m
        b = ++b

        text = Text(f"Linear Template Test")
        self.play(Write(text))
        self.play(FadeOut(text))
        test = Text(f"{y}, {m}, {b}")
        self.play(Write(test))
        self.wait(1)