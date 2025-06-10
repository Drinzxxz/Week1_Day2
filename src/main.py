import flet as ft

def main(page: ft.Page):
    page.window_width = 400
    page.window_height = 800

    top = ft.Text("Akira Creatives", size=20)

    pages = [
        ft.Text("Home"),
        ft.Text("Chat"),
        ft.Text("Settings"),
    ]
    body = ft.Column([pages[0]], expand=True)

    def change(e):
        body.controls[0] = pages[e.control.selected_index]
        page.update()

    nav = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon="home", label="Home"),
            ft.NavigationBarDestination(icon="chat", label="Chat"),
            ft.NavigationBarDestination(icon="settings", label="Settings"),
        ],
        on_change=change
    )

    page.add(top, body, nav)

ft.app(target=main)
