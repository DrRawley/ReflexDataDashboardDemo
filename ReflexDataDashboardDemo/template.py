from typing import Callable

import reflex as rx

from ReflexDataDashboardDemo.navigation import dashboard_sidebar
from ReflexDataDashboardDemo.styles import BACKGROUND_COLOR, FONT_FAMILY


def template(page: Callable[[], rx.Component]) -> rx.Component:
    return rx.box(
        dashboard_sidebar,
        page(),
        rx.logo(),
        background_color=BACKGROUND_COLOR,
        font_family=FONT_FAMILY,
        padding_bottom="4em",
    )
