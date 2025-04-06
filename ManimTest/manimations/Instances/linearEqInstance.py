from manim import *

class Linear(Scene):
    def construct(self):
        # Define values (replace these with actual numbers later)
        y_val = 7
        m_val = 4
        b_val = 1

        yb_val = y_val - b_val
        ybm_val = yb_val / m_val

        # Show the original equation
        equation = MathTex("y = mx + b").move_to([0, 2, 0])
        self.play(Write(equation))
        self.wait(1)

        # Substitute values into the equation
        substituted = MathTex(
            f"{y_val} = {m_val}x + {b_val}"
        ).next_to(equation, DOWN, buff=0.5)
        self.play(TransformFromCopy(equation, substituted))
        self.wait(1)

        # Step 1: Subtract b from both sides
        step1 = MathTex(
            f"{y_val} - {b_val} = {m_val}x"
        ).next_to(substituted, DOWN, buff=0.5)
        self.play(TransformFromCopy(substituted, step1))
        #simplify
        step1Simp = MathTex(
            f"{yb_val} = {m_val}x"
        ).move_to(step1)
        self.play(Transform(step1, step1Simp))
        self.wait(1)

        # Step 2: Divide both sides by m
        step2 = MathTex(
            f"x = \\frac{{{yb_val}}}{{{m_val}}}"
        ).next_to(step1, DOWN, buff=0.5)
        self.play(TransformFromCopy(step1Simp, step2))
        #simplify
        if (yb_val % m_val == 0):
            step2Simp = MathTex(
                f"x = {int(ybm_val)}"
            ).move_to(step2)
            self.play(Transform(step2, step2Simp))
        self.wait(1)

        # Final message
        conclusion = Text("Solved for x!", font_size=36).next_to(step2, DOWN, buff=0.5)
        self.play(Write(conclusion))
        self.wait(2)