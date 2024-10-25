import flet as ft
from datetime import datetime
import calendar


class Calendar:
    def __init__(self, page=ft.Page()):
        self.page = page
        self.current_day = datetime.today().day
        self.current_month = datetime.today().month
        self.current_year = datetime.today().year
        self.selected_day = None  # Armazena o dia selecionado
        self.main_container = self.create_calendar(
            self.current_year, self.current_month
        )

    def create_calendar(self, year, month):
        month_range = calendar.monthrange(year, month)
        first_day_weekday = calendar.weekday(year, month, 1)

        month_and_year = self.create_month_and_year_header(month, year)
        calendar_header = self.create_calendar_header()
        calendario_days = self.create_calendar_days(
            month_range, first_day_weekday, month, year
        )

        # Container principal do calendário
        main_container = ft.Container(
            content=ft.Column(
                controls=[
                    month_and_year,
                    calendar_header,
                    ft.Divider(),
                    calendario_days,
                ],
                expand=True,
            ),
            bgcolor=ft.colors.TRANSPARENT,
            border_radius=ft.border_radius.all(10),
            expand=True,
        )
        return main_container

    def create_month_and_year_header(self, month, year):
        # Função para obter o nome do mês em português
        def get_month_name(month):
            month_portuguese = [
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
            return month_portuguese[month - 1]

        return ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Text(
                    get_month_name(month),
                    size=23,
                    weight=ft.FontWeight.W_900,
                    text_align=ft.TextAlign.CENTER,
                    col=1,
                ),
                ft.Text(
                    year,
                    size=18,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                    col=1,
                ),
            ],
        )

    def create_calendar_header(self):
        week_header = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"]
        return ft.ResponsiveRow(
            columns=7,
            controls=[
                ft.Text(
                    week_header[day],
                    size=18,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                    col=1,
                )
                for day in range(len(week_header))
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            expand=True,
        )

    def create_calendar_days(self, month_range, first_day_weekday, month, year):
        calendario_days = ft.ResponsiveRow(columns=7)

        for i in range(1, month_range[1] + 1):
            day_container = ft.Container(
                height=48,
                col=1,
                border_radius=ft.border_radius.all(25),
                bgcolor=(
                    ft.colors.BLUE_100
                    if self.selected_day == i and month == self.current_month
                    else None
                ),
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
                on_click=lambda e, day=i: self.add_gig(e, day, month, year),
            )
            calendario_days.controls.append(day_container)

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

        return calendario_days

    def add_gig(self, e, day, month, year):
        for control in self.main_container.content.controls[-1].controls:
            control.bgcolor = None  # Limpa o fundo de todos os dias
        clicked_container = self.main_container.content.controls[-1].controls[day - 1]
        clicked_container.bgcolor = ft.colors.BLUE_100  # Marca o dia clicado
        self.selected_day = f"{day}/{month}/{year}"
        self.page.update()

    def handle_swipe(self, e):
        self.selected_day = None  # Limpa a seleção do dia ao mudar de mês
        if e.primary_velocity > 0:  # Swipe para a direita (mês anterior)
            if self.current_month == 1:
                self.current_month = 12
                self.current_year -= 1
            else:
                self.current_month -= 1
        else:  # Swipe para a esquerda (próximo mês)
            if self.current_month == 12:
                self.current_month = 1
                self.current_year += 1
            else:
                self.current_month += 1
        self.main_container.content = self.create_calendar(
            self.current_year, self.current_month
        )
        self.page.update()

    def get_calendar(self):
        # Adiciona o GestureDetector para controlar o swipe do calendário
        return ft.GestureDetector(
            content=self.main_container,
            on_horizontal_drag_end=self.handle_swipe,
        )
