import flet as ft
from datetime import datetime
import calendar


# TODO Refatorar o calendario por classes para ser mais facial a reutilização
class MyCalendar:

    def __init__(self):
        self.current_day = datetime.today().day
        self.current_month = datetime.today().month
        self.current_year = datetime.today().year
        self.month_portuguese = [
            "Janeiro",
            "Fevereiro",
            "Março",
            "Abril",
            "Maio",
            "Junho",
            "Julho",
            "Agosto",
            "Setembro",
            "Outubro",
            "Novembro",
            "Dezembro",
        ]
        self.week_header = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"]
        self.selected_day = None
        self.month_range = calendar.monthrange(self.current_year, self.current_month)
        self.first_day_weekday = calendar.weekday(
            self.current_year, self.current_month, 1
        )

    def get_month_year_row(self):
        return ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Text(
                    self.month_portuguese[self.current_month - 1],
                    size=23,
                    weight=ft.FontWeight.W_900,
                    text_align=ft.TextAlign.CENTER,
                    col=1,
                ),
                ft.Text(
                    self.current_year,
                    size=18,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                    col=1,
                ),
            ],
        )

    def get_week_days_row(self):
        return ft.ResponsiveRow(
            columns=7,
            controls=[
                ft.Text(
                    self.week_header[day],
                    size=18,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                    col=1,
                )
                for day in range(len(self.week_header))
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            expand=True,
        )

    def days_month(self, day):
        day_col = ft.Column(
            controls=[
                ft.Text(
                    str(day),
                    size=18,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                    col=1,
                ),
                ft.Icon(
                    color=ft.colors.GREEN,
                    name=(ft.icons.CIRCLE),
                    size=10,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

        return ft.Container(
            height=48,
            col=1,
            border_radius=ft.border_radius.all(25),
            alignment=ft.alignment.center,
            content=day_col,
            on_click=lambda _: print(day),
        )

    def create_calendar(self, year, month):
        self.month_calendar = ft.ResponsiveRow(
            columns=7,
            alignment=ft.MainAxisAlignment.START,
        )
        for day in range(self.month_range[1]):
            self.month_calendar.controls.append(self.days_month(day + 1))

        for i in range(self.first_day_weekday):
            self.month_calendar.controls.insert(
                0,
                ft.Container(
                    height=48,
                    col=1,
                    border_radius=ft.border_radius.all(25),
                    alignment=ft.alignment.center,
                ),
            )

        return self.month_calendar

    def get_calendar(self): ...
