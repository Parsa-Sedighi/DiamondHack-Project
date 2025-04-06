from manim import *
import math

class Sine(Scene):
    def construct(self):
        r_val = -2
        r_val = float(r_val)

        x = math.cos(r_val)
        y = math.sin(r_val)

        # Zoomed-in axes for bigger visual scale
        axes = Axes(
            x_range=[-3.6, 3.6],
            y_range=[-1.8, 1.8],
            x_length=12,  # width in scene units
            y_length=6,  # height in scene units
            tips=True,
            axis_config={"include_numbers": False},
        )
        self.play(Create(axes))

        # Larger-looking unit circle on same axes
        circle = Circle(radius=axes.x_axis.unit_size, color=BLUE)  # 1 unit radius, scaled to axes
        circle.move_to(axes.c2p(0, 0))
        self.play(Create(circle))

        # Compute important points
        origin = axes.c2p(0, 0)
        circle_point = axes.c2p(x, y)

        # Radius
        radius_line = Line(origin, circle_point, color=YELLOW)
        point_dot = Dot(circle_point, color=YELLOW)

        # Triangle legs
        base = Line(origin, axes.c2p(x, 0), color=GREEN)
        vertical = DashedLine(axes.c2p(x, 0), circle_point, color=RED)

        # Angle arc and label
        angle_arc = Arc(radius=0.3, start_angle=0, angle=r_val, color=ORANGE).move_arc_center_to(origin)
        angle_label = MathTex(f"\\theta = {round(r_val, 2)}").next_to(angle_arc, RIGHT, buff=0.2)

        # Sine label
        sine_label = MathTex(f"\\sin({round(r_val, 2)}) = {round(y, 2)}")
        sine_label.next_to(vertical, RIGHT)

        # Sine curve on the same axes
        sine_curve = axes.plot(lambda x: math.sin(x), color=GREY_D)

        # Dot on sine curve
        sine_dot = Dot(axes.c2p(r_val, y), color=RED)
        sine_projection = DashedLine(circle_point, axes.c2p(r_val, y), color=WHITE, stroke_opacity=0.6)

        # Animate
        self.play(Create(sine_curve))
        self.play(Create(radius_line), FadeIn(point_dot))
        self.play(Create(base), Create(vertical))
        self.play(Create(angle_arc), Write(angle_label))
        self.play(Write(sine_label))
        self.play(Create(sine_projection), FadeIn(sine_dot))
        self.wait(2)