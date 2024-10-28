import flet as ft

# from .my_calendar import my_cal
from tools.calendar.my_calendar import MyCalendar


def home(page: ft.Page):
    my_calendar = MyCalendar(page)

    home_page = ft.Container(
        content=ft.Column(
            controls=[
                my_calendar.get_calendar(),
                ft.Divider(),
                ft.Row(
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.ADD,
                            on_click=lambda e: page.go(
                                f"/gig_add/{my_calendar.current_year}-{my_calendar.current_month}-{my_calendar.selected_day if my_calendar.selected_day else my_calendar.current_day}"
                            ),
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
