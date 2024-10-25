import flet as ft
from views.layout.menus import menu_appbar
from views.layout.home import home
from views.clients_form.clients_view import clients_view
from views.clients_form.clients_add import clients_add
from views.clients_form.clients_view_card import client_card
from views.clients_form.clients_update import clients_update
from views.gigs_form.gigs_add import gigs_add


def main(page: ft.Page):
    page.title = "My App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.width = 400
    page.window.height = 932

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

    app_bar = menu_appbar(page)

    def route_change(e):
        # Se a rota for a raiz ("/"), mostra o botão para adicionar cliente
        page.views.clear()  # Limpa as views anteriores
        page.route == "/"
        page.views.append(
            ft.View(
                route="/",
                appbar=app_bar,
                controls=[home(page)],
                padding=ft.padding.all(0),
            )
        )

        if e.route == "/view_client":
            page.views.append(
                ft.View(
                    route="/view_client",
                    appbar=app_bar,
                    controls=[clients_view(page)],  # Chama a visualização dos clientes
                    padding=ft.padding.all(0),
                )
            )
        elif e.route == "/client_add":
            page.views.append(
                ft.View(
                    route="/client_add",
                    appbar=app_bar,
                    controls=[clients_add(page)],
                    padding=ft.padding.all(0),
                )
            )
        elif e.route.startswith("/client_card"):
            try:
                client_id = int(e.route.split("/")[-1])
                page.views.append(
                    ft.View(
                        route=f"/client_card/{client_id}",
                        appbar=app_bar,
                        controls=[client_card(page, client_id)],
                        padding=ft.padding.all(5),
                    )
                )
            except ValueError:
                print("Invalid client ID provided in the route.")
        elif e.route.startswith("/client_update"):
            try:
                client_id = int(e.route.split("/")[-1])
                page.views.append(
                    ft.View(
                        route=f"/client_update/{client_id}",
                        appbar=app_bar,
                        controls=[clients_update(page, client_id)],
                        padding=ft.padding.all(5),
                    )
                )
            except ValueError:
                print("Invalid client ID provided in the route.")

        elif e.route == "/gig_add":
            page.views.append(
                ft.View(
                    route="/gig_add",
                    appbar=app_bar,
                    controls=[gigs_add(page)],
                    padding=ft.padding.all(5),
                )
            )
        page.update()

    def view_pop(view):
        if len(page.views) > 1:  # Apenas remove a view se houver mais de uma
            page.views.pop()
            top_view = page.views[-1]
            page.go(top_view.route)  # Vai para a rota da última view no stack

    # Configura os eventos de mudança de rota e de pop nas views
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    # Inicia com a rota atual
    page.go(page.route)

    page.add(app_bar)


if __name__ == "__main__":
    ft.app(target=main)
