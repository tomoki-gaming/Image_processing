import flet as ft
def main(page:ft.page):
    page.title = "img process"
    page.window_width = 640
    page.window_height = 480
    menu = ft.ElevatedButton("Menu",icon="menu")
    images = ft.GridView(
        expand=1,
        runs_count=3,
        max_extent=180,
        child_aspect_ratio=1.0,
        spacing=10,
        run_spacing=10,
    )
    page.add(menu,images)

    crop = ft.TextButton(text="crop")
    rem_bg = ft.TextButton(text="remove back")
    resize = ft.TextButton(text="resize")
    rotate = ft.TextButton(text="rotate")
    hsv = ft.TextButton(text="hsv change")
    gray = ft.TextButton(text = "gray change")
    images.controls = [crop,rem_bg,resize,rotate,hsv,gray]

    page.update()

ft.app(target=main)