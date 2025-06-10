import flet as ft

def main(page: ft.Page):
    page.title = "Calculator"
    page.window_width = 300
    page.window_height = 500

    input_field = ft.TextField(label="Enter expression", hint_text="e.g. 2 + 3", width=250)

    result_text = ft.Text(value="Result: ", size=20)

    def calculate(e):
        try:
            result = eval(input_field.value)
            result_text.value = f"Result: {result}"
        except:
            result_text.value = "Error: Invalid input"
        page.update()

    calc_button = ft.ElevatedButton(text="Calculate", on_click=calculate)

    page.add(
        ft.Column([
            input_field,
            calc_button,
            result_text
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True)
    )

ft.app(target=main)
