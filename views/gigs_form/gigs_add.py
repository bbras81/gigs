import flet as ft
from gigs.gigs_data import Gigs


gigs_info = Gigs()


def gigs_add_c(page: ft.Page, gig_date: str):
    page.title = "Add Gig"

    gigs_info.gig_date.width = page.width / 2
    gigs_info.gig_date.value = gig_date

    hour_button = ft.CupertinoFilledButton(
        content=ft.Text("Hour", color=ft.colors.WHITE),
        on_click=hour_picker_view,
    )

    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Add Gig"),
                ft.Row(
                    controls=[
                        gigs_info.gig_date,
                        hour_button,
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                gigs_info.hour_picker,
                gigs_info.gig_local,
                gigs_info.gig_cachet,
                ft.ElevatedButton(
                    "Add gig",
                    on_click=lambda _: ...,
                    width=100,
                    height=40,
                ),
            ],
            scroll=ft.ScrollMode.HIDDEN,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )


def hour_picker_view(e):
    if gigs_info.hour_picker:
        gigs_info.hour_picker.visible = not gigs_info.hour_picker.visible
        if gigs_info.hour_picker:
            gigs_info.hour_picker.update()
