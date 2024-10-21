import flet as ft


def modal_alert(page, error_text=None):
    alert = ft.AlertDialog(
        title=ft.Text("Erro"),
        content=ft.Text(error_text),
        actions=[
            ft.TextButton(
                text="Ok", on_click=lambda _: page.close(alert)
            )  # Fecha o diálogo
        ],
    )

    # Adiciona o alerta à página usando overlay
    page.overlay.append(alert)
    alert.open = True
    page.update()
