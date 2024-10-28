import flet as ft

from gigs.gigs_data import Gigs


gigs_info = Gigs()


def gigs_add_c(page: ft.Page, gig_date: str):
    page.title = "Add Gig"
    gigs_info.gig_date.value = gig_date
    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Add Gig"),
                gigs_info.gig_date,
                gigs_info.gig_hour,
                gigs_info.gig_local,
                gigs_info.gig_cachet,
            ],
            scroll=ft.ScrollMode.HIDDEN,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )
