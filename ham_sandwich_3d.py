from manim import *
import numpy as np

class HamSandwich3D(ThreeDScene):
    def construct(self):
        self.camera.background_color = WHITE
        self.set_camera_orientation(phi=65 * DEGREES, theta=-120 * DEGREES)

        # invisible axes (used only for coordinate mapping)
        axes = ThreeDAxes(
            x_range=[-5, 5, 1], y_range=[-5, 5, 1], z_range=[-4, 4, 1],
            x_length=10, y_length=10, z_length=8,
            axis_config={"stroke_opacity": 0, "include_ticks": False},
        )

        # Object 1: blob (left)
        # plane at x=-3, y=0: z = 0.55*(-3) - 0.35*(0) = -1.65
        def blob1_func(u, v):
            r = 0.9 + 0.15 * np.sin(4*u) * np.cos(3*v) + 0.1 * np.cos(2*u + v)
            return axes.c2p(
                -3 + r * np.cos(u) * np.cos(v),
                0 + r * np.sin(u) * np.cos(v),
                -1.65 + r * np.sin(v),
            )

        blob1 = Surface(
            blob1_func,
            u_range=[0, TAU], v_range=[-PI/2, PI/2],
            resolution=(40, 22),
            fill_opacity=0.85, stroke_width=0.2, stroke_color="#C06010",
        )
        blob1.set_color("#E08030")

        # Object 2: blob (back-right)
        # plane at x=2, y=3: z = 0.55*2 - 0.35*3 = 0.05
        def blob2_func(u, v):
            r_base = 0.6 + 0.12 * np.sin(3*u) * np.cos(2*v) + 0.08 * np.cos(5*u)
            return axes.c2p(
                2 + r_base * np.cos(u) * np.cos(v),
                3 + r_base * np.sin(u) * np.cos(v),
                0.05 + (1.8 + 0.2 * np.sin(4*u)) * np.sin(v),
            )

        blob2 = Surface(
            blob2_func,
            u_range=[0, TAU], v_range=[-PI/2, PI/2],
            resolution=(40, 22),
            fill_opacity=0.85, stroke_width=0.2, stroke_color="#105858",
        )
        blob2.set_color("#18897A")

        # Object 3: bumpy blob (front-right), split into upper and lower
        # plane at x=2, y=-3: z = 0.55*2 - 0.35*(-3) = 2.15
        def blob3_func(u, v):
            r = 1.2 + 0.25 * np.sin(3*u) * np.cos(2*v) + 0.15 * np.cos(5*u)
            return axes.c2p(
                2 + r * np.cos(u) * np.cos(v),
                -3 + r * np.sin(u) * np.cos(v),
                2.15 + r * 0.7 * np.sin(v),
            )

        # upper half (above plane) - full opacity
        blob3_top = Surface(
            blob3_func,
            u_range=[0, TAU], v_range=[0, PI/2],
            resolution=(48, 12),
            fill_opacity=0.85, stroke_width=0.2, stroke_color="#8A1535",
        )
        blob3_top.set_color("#C42050")

        # lower half (below plane) - translucent
        blob3_bot = Surface(
            blob3_func,
            u_range=[0, TAU], v_range=[-PI/2, 0],
            resolution=(48, 12),
            fill_opacity=0.3, stroke_width=0.15, stroke_color="#8A1535",
        )
        blob3_bot.set_color("#C42050")

        # Bisecting plane
        plane = Surface(
            lambda u, v: axes.c2p(u, v, 0.55 * u - 0.35 * v),
            u_range=[-5, 5], v_range=[-5, 5],
            resolution=(2, 2),
            fill_opacity=0.5, stroke_width=1.8, stroke_color="#666666",
        )
        plane.set_color("#B0B0B0")

        # Labels
        l1 = MathTex("A_1", font_size=42, color="#E08030")
        l1.move_to(axes.c2p(-3, 0, -0.3))
        l2 = MathTex("A_2", font_size=42, color="#18897A")
        l2.move_to(axes.c2p(2, 3, 2.5))
        l3 = MathTex("A_3", font_size=42, color="#C42050")
        l3.move_to(axes.c2p(2, -3, 3.8))
        lp = MathTex(r"\Pi(\mathbf{n}^*)", font_size=38, color="#555555")
        lp.move_to(axes.c2p(4, -4, 0.5))
        for lbl in [l1, l2, l3, lp]:
            self.add_fixed_orientation_mobjects(lbl)

        self.add(plane, blob1, blob2, blob3_bot, blob3_top,
                 l1, l2, l3, lp)
