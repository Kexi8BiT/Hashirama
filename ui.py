import flet as ft


class Button(ft.UserControl):
    def __init__(self, text, style, on_click=None, width=None, height=None, border_radius=30):
        super().__init__()
        """
        text: str,
        style: ['default', 'primary', 'success', 'danger', 'warning'],"""
        self.text = text
        self.style = style
        self.on_click = on_click
        self.width = width
        self.height = height
        self.border_radius = border_radius
        style = self.get_button_style(self.style)
        self.button = ft.ElevatedButton(content=ft.Text(self.text), width=self.width, height=self.height, **style)

    def get_button_style(self, style):
        if style == "primary":
            return {
                "color":"#ffffff",
                "bgcolor":"#0074FA",
                "on_click": self.on_click,
                "style":ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=self.border_radius),
                    shadow_color=ft.colors.TRANSPARENT,
                    overlay_color=ft.colors.with_opacity(0.1, ft.colors.WHITE),
                    padding=20)
            }
        elif style == "success":
            return {
                "color": "#000000",
                "bgcolor": "#18C964",
                "on_click": self.on_click,
                "style": ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=self.border_radius),
                    shadow_color=ft.colors.TRANSPARENT,
                    overlay_color=ft.colors.with_opacity(0.1, ft.colors.BLACK),
                    padding=20)
            }
        elif style == "danger":
            return {
                "color": "#ffffff",
                "bgcolor": "#EE3232",
                "on_click": self.on_click,
                "style": ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=self.border_radius),
                    shadow_color=ft.colors.TRANSPARENT,
                    overlay_color=ft.colors.with_opacity(0.2, ft.colors.RED_100),
                    padding=20)
            }
        elif style == "warning":
            return {
                "color": "#000000",
                "bgcolor": "#F5A524",
                "on_click": self.on_click,
                "style": ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=self.border_radius),
                    shadow_color=ft.colors.TRANSPARENT,
                    overlay_color=ft.colors.with_opacity(0.1, ft.colors.BLACK),
                    padding=20)
            }

        elif style == "text":
            return {
                "color": "#ffffff",
                "bgcolor": ft.colors.TRANSPARENT,
                "on_click": self.on_click,
                "style": ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=self.border_radius),
                    shadow_color=ft.colors.TRANSPARENT,
                    overlay_color=ft.colors.with_opacity(0.1, ft.colors.WHITE),
                    padding=20,
                    surface_tint_color=ft.colors.TRANSPARENT,
                    bgcolor=ft.colors.TRANSPARENT)
            }

        else:
            return {
                "color": "#ffffff",
                "bgcolor": "#151515",
                "on_click": self.on_click,
                "style": ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=self.border_radius),
                    shadow_color=ft.colors.TRANSPARENT,
                    overlay_color=ft.colors.with_opacity(0.2, ft.colors.WHITE),
                    padding=20)
            }

    def loading(self, status, size = 20):
        if status == True:
            self.button.content = ft.ProgressRing(width=20, height=20, color="#ffffff")
            self.button.disabled = True
        elif status == False:
            self.button.content = ft.Text(self.text)
            self.button.disabled = False

        self.button.update()

    def disable(self, status):
        if status == True:
            self.button.disabled = True
        elif status == False:
            self.button.disabled = False

        self.button.update()

    def reset_onclick(self, func):
        self.button.on_click = func
        self.on_click = func
        self.button.update()



    def build(self):
        return self.button




icon_button_eleveted = {
                "style": ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=15),
                    bgcolor=ft.colors.with_opacity(0.06, ft.colors.WHITE),
                    shadow_color=ft.colors.TRANSPARENT,
                    overlay_color=ft.colors.with_opacity(0.1, ft.colors.WHITE),

                    surface_tint_color=ft.colors.TRANSPARENT,
                    side=ft.BorderSide(1, "#242424"))
            }

window_ui = {
    "bgcolor": ft.colors.BLACK,
    "color": ft.colors.WHITE,
}

text_input = {
  "bgcolor": ft.colors.with_opacity(0.06, ft.colors.WHITE),
  "border_radius": 15,
  "border_width": 1,
  "border_color": "#242424",
  "cursor_color": "#CCCCCC",
  "hint_style": ft.TextStyle(color="#2A2A2A"),
  "selection_color":ft.colors.with_opacity(0.2, "#ffffff")
}

text_input_outline = {
  "bgcolor": ft.colors.TRANSPARENT,
  "border_radius": 15,
  "border_width": 1,
  "border_color": "#2A2A2A",
  "cursor_color": "#CCCCCC",
  "hint_style": ft.TextStyle(color="#2A2A2A"),
  "selection_color":ft.colors.with_opacity(0.2, "#ffffff")
}
