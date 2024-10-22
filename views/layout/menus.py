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
                        on_click=lambda _: page.go("/view_client"),
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


def menu_bottom_bar(page: ft.Page):

    bottom_bar = ft.BottomAppBar(
        content=ft.Row(
            controls=[
                ft.IconButton(
                    icon=ft.icons.ADD_CIRCLE_OUTLINE,
                    on_click=lambda _: page.go("/client_add"),
                    tooltip="Add Gig",
                    icon_size=40,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.END,
        ),
        shape=ft.NotchShape.CIRCULAR,
        height=100,
    )
    return bottom_bar
