import flet as ft

def main(page: ft.Page):
    page.title = "Flet Cloud Demo"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(ft.Text("Hello from Flet Cloud!", size=30))

ft.app(target=main)  # Use ft.page() for cloud hosting
