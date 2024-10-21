import flet as ft
from views.layout.menus import menu_appbar
from views.layout.home import home
from views.clients_form.clients_view import clients_view
from views.clients_form.clients_add import clients_add


def main(page: ft.Page):
    page.title = "My App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.width = 400
    page.window.height = 932

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
            )
        )
        if e.route == "/view_client":
            page.views.append(
                ft.View(
                    route="/view_client",
                    appbar=app_bar,
                    controls=[clients_view(page)],  # Chama a visualização dos clientes
                )
            )
        elif e.route == "/client_add":
            page.views.append(
                ft.View(
                    route="/client_add",
                    appbar=app_bar,
                    controls=[clients_add(page)],
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
