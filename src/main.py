import flet as ft

def main(page: ft.Page):
    page.title = "Akira Creatives"
    page.window.width = 400
    page.window.height = 800
    page.window.resizable = False

    top_bar = ft.Container(
        content=ft.Row([
            ft.CircleAvatar(
                content=ft.Image(src="Aldrin.png", width=40, height=40),
                radius=20
            ),
            ft.Text("Akira Creatives", size=20, weight=ft.FontWeight.BOLD)
        ], spacing=10),
        padding=10
    )

    pages = [
        ft.Text(""),
        ft.Text(""),
        ft.Text(""),
    ]

    body = ft.Container(content=pages[0], expand=True, alignment=ft.alignment.top_center)

    def change_tab(e):
        body.content = pages[e.control.selected_index]
        page.update()

    nav_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon="home", label="Home"),
            ft.NavigationBarDestination(icon="chat", label="Chat"),
            ft.NavigationBarDestination(icon="settings", label="Settings"),
        ],
        on_change=change_tab
    )

    page.add(top_bar, body, nav_bar)

ft.app(target=main)
