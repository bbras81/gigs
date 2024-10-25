import flet as ft

from gigs.gigs_data import Gigs


gigs_info = Gigs


def gigs_add_c(page: ft.Page):
    page.title = "Add Gig"

    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Add Gig"),
                gigs_info.
            ]
        )
    )
