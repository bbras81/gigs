import flet as ft
from .my_calendar import my_cal


def home(page: ft.Page):

    home_page = ft.Container(
        content=ft.Column(
            controls=[
                my_cal(page),
                ft.Divider(),
                ft.Row(
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.ADD,
                            on_click=lambda e: page.go("/gigs_add"),
                            tooltip="Add Gig",
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.END,
                ),
            ]
        )
    )

    return home_page
