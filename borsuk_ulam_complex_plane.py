from manim import *
import numpy as np


class BorsukUlamComplexPlane(ThreeDScene):
    def construct(self):
        self.camera.background_color = WHITE
        self.set_camera_orientation(phi=62 * DEGREES, theta=-55 * DEGREES, zoom=0.78)

        axis_color = "#3E4654"
        surface_blue = "#8DB7D9"
        surface_edge = "#2C6693"
        gold = "#D9A441"
        red = "#8C1D18"
        ink = "#11131A"

        title = Text("Borsuk-Ulam: a sphere maps to the complex plane", font_size=34, color=ink)
        title.to_edge(UP, buff=0.32)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title), run_time=0.9)

        axes = ThreeDAxes(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            z_range=[-2, 2, 1],
            x_length=4.0,
            y_length=4.0,
            z_length=4.0,
            axis_config={
                "stroke_color": axis_color,
                "stroke_width": 2,
                "include_ticks": False,
            },
        )
        axes.move_to(LEFT * 2.75)

        x_label = MathTex("x", font_size=28, color=axis_color)
        y_label = MathTex("y", font_size=28, color=axis_color)
        z_label_axis = MathTex("z", font_size=28, color=axis_color)
        x_label.move_to(axes.c2p(2.18, 0, 0))
        y_label.move_to(axes.c2p(0, 2.18, 0))
        z_label_axis.move_to(axes.c2p(0, 0, 2.18))
        self.add_fixed_orientation_mobjects(x_label, y_label, z_label_axis)

        sphere_surface = Surface(
            lambda u, v: axes.c2p(
                np.cos(u) * np.cos(v),
                np.sin(u) * np.cos(v),
                np.sin(v),
            ),
            u_range=[0, TAU],
            v_range=[-PI / 2, PI / 2],
            resolution=(42, 22),
            fill_opacity=0.42,
            stroke_width=0.35,
            stroke_color=surface_edge,
        )
        sphere_surface.set_color(surface_blue)

        sphere_label = MathTex("S^2", font_size=38, color=surface_edge)
        sphere_label.move_to(axes.c2p(0, 0, -1.35))
        self.add_fixed_orientation_mobjects(sphere_label)

        p = np.array([0.58, 0.43, 0.69])
        p = p / np.linalg.norm(p)
        p_u = np.arctan2(p[1], p[0]) % TAU
        p_v = np.arcsin(p[2])
        antipode_u = (p_u + PI) % TAU
        antipode_v = -p_v
        p_start = axes.c2p(p[0], p[1], p[2])
        antipode_start = axes.c2p(-p[0], -p[1], -p[2])

        p_dot = Dot(point=p_start, radius=0.115, color=gold)
        antipode_dot = Dot(point=antipode_start, radius=0.115, color=red)

        p_label = MathTex("P", font_size=40, color=gold)
        antipode_label = MathTex("-P", font_size=40, color=red)
        p_label.move_to(p_start + UP * 0.34 + RIGHT * 0.24)
        antipode_label.move_to(antipode_start + DOWN * 0.38 + LEFT * 0.24)
        self.add_fixed_orientation_mobjects(p_label, antipode_label)

        caption = Text("Start with a highlighted antipodal pair.", font_size=25, color=ink)
        caption.to_edge(DOWN, buff=0.35)
        self.add_fixed_in_frame_mobjects(caption)

        self.play(
            Create(axes),
            FadeIn(sphere_surface),
            FadeIn(sphere_label),
            FadeIn(x_label),
            FadeIn(y_label),
            FadeIn(z_label_axis),
            FadeIn(p_dot),
            FadeIn(antipode_dot),
            Write(p_label),
            Write(antipode_label),
            FadeIn(caption),
            run_time=1.8,
        )

        plane = NumberPlane(
            x_range=[-2.4, 2.4, 1],
            y_range=[-1.8, 1.8, 1],
            x_length=4.5,
            y_length=3.4,
            background_line_style={
                "stroke_color": "#D7DCE2",
                "stroke_width": 1,
                "stroke_opacity": 0.72,
            },
            axis_config={
                "stroke_color": axis_color,
                "stroke_width": 2,
                "include_ticks": False,
            },
        )
        plane.move_to(RIGHT * 2.55)
        plane_box = SurroundingRectangle(plane, color=axis_color, stroke_width=1.2, buff=0.05)

        re_label = MathTex(r"\operatorname{Re}", font_size=28, color=axis_color)
        im_label = MathTex(r"\operatorname{Im}", font_size=28, color=axis_color)
        plane_label = MathTex(r"\mathbb{C}\cong\mathbb{R}^2", font_size=36, color=axis_color)
        re_label.move_to(plane.c2p(2.65, 0))
        im_label.move_to(plane.c2p(0, 2.02))
        plane_label.move_to(plane.get_bottom() + DOWN * 0.35)
        self.add_fixed_orientation_mobjects(re_label, im_label, plane_label)

        map_label = MathTex(r"F:S^2\to\mathbb{C}", font_size=34, color=ink)
        map_label.to_corner(UR, buff=0.45)
        self.add_fixed_in_frame_mobjects(map_label)

        self.play(
            Create(plane),
            Create(plane_box),
            FadeIn(re_label),
            FadeIn(im_label),
            FadeIn(plane_label),
            Write(map_label),
            run_time=1.2,
        )

        self.collision_target = np.array([0.66, 0.42])
        self.collision_parameters = [(p_u, p_v), (antipode_u, antipode_v)]

        flat_surface = Surface(
            lambda u, v: plane.c2p(*self.flat_image_coordinate(u, v)),
            u_range=[0, TAU],
            v_range=[-PI / 2, PI / 2],
            resolution=(42, 22),
            fill_opacity=0.58,
            stroke_width=0.35,
            stroke_color=surface_edge,
        )
        flat_surface.set_color(surface_blue)

        z0 = plane.c2p(*self.flat_image_coordinate(p_u, p_v))

        def point_on_sphere(u, v):
            return axes.c2p(
                np.cos(u) * np.cos(v),
                np.sin(u) * np.cos(v),
                np.sin(v),
            )

        def point_on_flat_image(u, v):
            return plane.c2p(*self.flat_image_coordinate(u, v))

        def attach_markers(group, alpha):
            p_position = interpolate(point_on_sphere(p_u, p_v), point_on_flat_image(p_u, p_v), alpha)
            antipode_position = interpolate(
                point_on_sphere(antipode_u, antipode_v),
                point_on_flat_image(antipode_u, antipode_v),
                alpha,
            )
            p_dot.move_to(p_position)
            antipode_dot.move_to(antipode_position)
            p_label.move_to(p_position + interpolate(UP * 0.34 + RIGHT * 0.24, UP * 0.38 + LEFT * 0.32, alpha))
            antipode_label.move_to(
                antipode_position + interpolate(DOWN * 0.38 + LEFT * 0.24, DOWN * 0.38 + RIGHT * 0.36, alpha)
            )

        morph_caption = Text("The whole sphere surface becomes a planar image.", font_size=25, color=ink)
        morph_caption.to_edge(DOWN, buff=0.35)
        self.add_fixed_in_frame_mobjects(morph_caption)

        self.play(
            FadeOut(caption),
            FadeIn(morph_caption),
            FadeOut(sphere_label),
            FadeOut(x_label),
            FadeOut(y_label),
            FadeOut(z_label_axis),
            FadeOut(axes),
            Transform(sphere_surface, flat_surface),
            UpdateFromAlphaFunc(
                VGroup(p_dot, antipode_dot, p_label, antipode_label),
                attach_markers,
            ),
            run_time=3.2,
            rate_func=smooth,
        )

        target_ring = Circle(radius=0.19, color=ink, stroke_width=3.2)
        target_ring.move_to(z0)
        z0_label = MathTex("z_0", font_size=36, color=ink)
        z0_label.move_to(z0 + RIGHT * 0.48 + UP * 0.22)
        self.add_fixed_orientation_mobjects(z0_label)

        self.play(Create(target_ring), FadeIn(z0_label), run_time=0.8)

        equality = MathTex(r"F(P)=F(-P)=z_0", font_size=44, color=ink)
        equality.to_edge(DOWN, buff=0.35)
        self.add_fixed_in_frame_mobjects(equality)
        self.play(FadeOut(morph_caption), FadeIn(equality), run_time=0.8)
        self.wait(2.4)

    def flat_image_coordinate(self, u, v):
        base = self.base_flat_image_coordinate(u, v)
        if not hasattr(self, "collision_parameters"):
            return base[0], base[1], 0

        adjusted = base.copy()
        for center_u, center_v in self.collision_parameters:
            center_base = self.base_flat_image_coordinate(center_u, center_v)
            du = self.angle_distance(u, center_u)
            dv = v - center_v
            weight = np.exp(-(du * du / (2 * 0.18 ** 2) + dv * dv / (2 * 0.16 ** 2)))
            adjusted += weight * (self.collision_target - center_base)
        return adjusted[0], adjusted[1], 0

    def base_flat_image_coordinate(self, u, v):
        angle = u + 0.22 * np.sin(2 * v) + 0.10 * np.sin(3 * u)
        radial = abs(np.cos(v))
        boundary = 1.0 + 0.18 * np.sin(3 * angle) + 0.11 * np.cos(5 * angle)
        x = 1.10 * radial * boundary * np.cos(angle)
        y = 0.78 * radial * boundary * np.sin(angle)
        return np.array([x, y])

    def angle_distance(self, a, b):
        return np.arctan2(np.sin(a - b), np.cos(a - b))
