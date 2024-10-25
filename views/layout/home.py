import flet as ft

# from .my_calendar import my_cal
from tools.calendar.my_calendar import MyCalendar

calendar = MyCalendar()


def home(page: ft.Page):

    home_page = ft.Container(
        content=ft.Column(
            controls=[
                calendar.get_month_year_row(),
                calendar.get_week_days_row(),
                ft.Divider(),
                ft.Row(
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.ADD,
                            on_click=lambda e: page.go(f"/gig_add"),
                            tooltip="Add Gig",
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.END,
                ),
            ]
        ),
        padding=ft.padding.all(10),
    )

    return home_page
