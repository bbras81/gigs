import flet as ft
from datetime import datetime

#TODO Refatoraro calendario por classes para ser mais facial a reutilização
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

    def get_month_days_row(self, month):
        return ft.ResponsiveRow(
            columns=7,
            controls=[
                ft.Container(
                    height=48,
                    col=1,
                    border_radius=ft.border_radius.all(25),
                    bgcolor=(
                        ft.colors.BLUE_100
                        if self.selected_day == i and month == self.current_month
                        else None
                    ),  # Muda o fundo se o dia for selecionado e for o mês atual
                    border=(
                        ft.border.all(1, ft.colors.BLUE)
                        if i == self.current_day and month == datetime.today().month
                        else None
                    ),
                    alignment=ft.alignment.center,
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                str(i),
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
                        spacing=0,
                    ),
                    on_click=lambda e, day=i: add_gig(e, day),  # Define o dia clicado
                )
                for i in range(1, self.month_range[1] + 1)
            ],
        )
        # Preenchendo os dias vazios no início do mês

    for i in range(first_day_weekday):
        calendario_days.controls.insert(
            0,
            ft.Container(
                height=48,
                col=1,
                border_radius=ft.border_radius.all(25),
                alignment=ft.alignment.center,
            ),
        )
