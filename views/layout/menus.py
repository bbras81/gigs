import flet as ft


def menu_appbar(page: ft.Page):
    app_bar_title = ft.Text("Gig's App")
    appbar = ft.AppBar(
        center_title=True,
        leading_width=40,
        title=app_bar_title,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.PopupMenuButton(
                icon=ft.icons.MENU,
                menu_position=ft.PopupMenuPosition.UNDER,
                items=[
                    ft.PopupMenuItem(
                        text="Clients",
                        icon=ft.icons.PEOPLE,
                        on_click=lambda _: page.go("/client_add"),
                    ),
                    ft.PopupMenuItem(
                        text="Settings",
                        icon=ft.icons.SETTINGS,
                    ),
                ],
            ),
        ],
    )

    return appbar
