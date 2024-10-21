import flet as ft
from datetime import datetime
import calendar


def my_cal(page: ft.Page):

    current_day = datetime.today().day
    current_month = datetime.today().month
    current_year = datetime.today().year
    selected_day = None  # Variável para armazenar o dia selecionado

    def create_calendar(year, month):
        nonlocal selected_day
        month_range = calendar.monthrange(year, month)
        first_day_weekday = calendar.weekday(year, month, 1)

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

        def add_gig(e, day):
            for i in range(len(calendario_days.controls)):
                calendario_days.controls[i].bgcolor = None  # Atualiza o dia selecionado

            calendario_days.controls[day + first_day_weekday - 1].bgcolor = (
                ft.colors.BLUE_100
            )  # Atualiza o dia selecionado
            page.update()  # Atualiza a página para refletir a mudança visual

        month_and_year = ft.Row(
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

        week_header = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"]
        calendar_header = ft.ResponsiveRow(
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

        # Criando os dias do calendário
        calendario_days = ft.ResponsiveRow(
            columns=7,
            controls=[
                ft.Container(
                    height=48,
                    col=1,
                    border_radius=ft.border_radius.all(25),
                    bgcolor=(
                        ft.colors.BLUE_100
                        if selected_day == i and month == current_month
                        else None
                    ),  # Muda o fundo se o dia for selecionado e for o mês atual
                    border=(
                        ft.border.all(1, ft.colors.BLACK)
                        if i == current_day and month == datetime.today().month
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
                for i in range(1, month_range[1] + 1)
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

    main_container = create_calendar(current_year, current_month)

    def handle_swipe(e):
        nonlocal current_month, current_year, selected_day
        selected_day = None  # Limpa a seleção do dia ao mudar de mês
        if e.primary_velocity > 0:  # Swipe para a direita (mês anterior)
            if current_month == 1:
                current_month = 12
                current_year -= 1
            else:
                current_month -= 1
        else:  # Swipe para a esquerda (próximo mês)
            if current_month == 12:
                current_month = 1
                current_year += 1
            else:
                current_month += 1
        main_container.content = create_calendar(current_year, current_month)
        page.update()

    calendar_gesture_detector = ft.GestureDetector(
        content=main_container,
        on_horizontal_drag_end=handle_swipe,
    )

    return calendar_gesture_detector
