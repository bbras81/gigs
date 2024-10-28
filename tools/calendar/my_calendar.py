import flet as ft
from datetime import datetime
import calendar


class MyCalendar:
    def __init__(self, page):
        self.page = page
        self.current_day = datetime.today().day
        self.current_month = datetime.today().month
        self.current_year = datetime.today().year
        self.selected_day = None  # Dia selecionado pelo usuário
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
        self.main_container = None

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
                    str(self.current_year),
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
        # Define o contorno do dia atual e o fundo do dia selecionado
        border = (
            ft.border.all(1, ft.colors.BLUE)
            if day == self.current_day
            and self.current_month == datetime.today().month
            and self.current_year == datetime.today().year
            else None
        )

        bgcolor = ft.colors.BLUE_100 if self.selected_day == day else None

        day_col = ft.Column(
            controls=[
                ft.Text(
                    str(day),
                    size=16,
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
            height=50,
            col=1,
            border_radius=ft.border_radius.all(25),
            border=border,  # Aplica a borda se for o dia atual
            bgcolor=bgcolor,  # Aplica o fundo se for o dia selecionado
            alignment=ft.alignment.center,
            content=day_col,
            on_click=lambda _: self.select_day(day),  # Função de clique
        )

    def select_day(self, day):

        self.selected_day = day  # Define o dia selecionado
        self.update_calendar()  # Atualiza o calendário para refletir a seleção

    def create_calendar(self):
        month_range = calendar.monthrange(self.current_year, self.current_month)
        first_day_weekday = calendar.weekday(self.current_year, self.current_month, 1)
        month_calendar = ft.ResponsiveRow(
            columns=7,
            alignment=ft.MainAxisAlignment.START,
        )

        # Adiciona os dias do mês ao calendário
        for day in range(1, month_range[1] + 1):
            month_calendar.controls.append(self.days_month(day))

        # Preenchendo os dias vazios no início do mês
        for _ in range(first_day_weekday):
            month_calendar.controls.insert(
                0,
                ft.Container(
                    height=48,
                    col=1,
                    border_radius=ft.border_radius.all(25),
                    alignment=ft.alignment.center,
                ),
            )

        return month_calendar

    def update_calendar(self):
        # Atualiza o conteúdo do calendário para o novo mês/ano
        self.main_container.content.controls = [
            self.get_month_year_row(),
            self.get_week_days_row(),
            self.create_calendar(),
        ]
        self.page.update()

    def get_calendar(self):
        # Container principal do calendário com deteção de gestos de swipe
        self.main_container = ft.Container(
            content=ft.Column(
                controls=[
                    self.get_month_year_row(),
                    self.get_week_days_row(),
                    self.create_calendar(),
                ]
            )
        )
        return ft.GestureDetector(
            content=self.main_container,
            on_horizontal_drag_end=self.handle_swipe,
        )

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
        self.update_calendar()  # Atualiza o calendário com o novo mês/ano
