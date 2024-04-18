import flet as ft
from ui import window_ui, text_input, Button, text_input_outline, icon_button_eleveted
import time
import json
from hashhhshshshs import derive_key, decrypt_file, encrypt_file
import os
from generate import generate_password, regenerate_password

passwords = []
key = None

version = "- 1.6"
documents_path = os.path.expanduser(r"~\Documents")



def main(page: ft.Page):
    page.title = f"Hashirama {version}"
    page.window_width = 1000
    page.window_height = 620
    page.window_maximizable = False
    page.window_resizable = False
    page.bgcolor = window_ui["bgcolor"]
    page.padding = 0
    page.theme_mode = ft.ThemeMode.DARK

    class PassObject(ft.UserControl):
        def __init__(self, name, passsword, icon="assets/safe.png", note="", new_pass: bool=False):
            super().__init__()
            self.name = name
            self.icon = icon
            self.note = note
            self.passsword = passsword
            self.ctc = ft.IconButton(ft.icons.COPYRIGHT_ROUNDED, icon_color="#636363", on_click=self.copy_to,
                                     style=ft.ButtonStyle(surface_tint_color=ft.colors.TRANSPARENT,
                                                          shadow_color=ft.colors.TRANSPARENT,
                                                          overlay_color=ft.colors.with_opacity(0.01, ft.colors.WHITE)),
                                     visible=False)

            self.rmv = ft.IconButton(ft.icons.HIGHLIGHT_REMOVE, icon_color="#636363", on_click=self.remove,
                                     style=ft.ButtonStyle(surface_tint_color=ft.colors.TRANSPARENT,
                                                          shadow_color=ft.colors.TRANSPARENT,
                                                          overlay_color=ft.colors.with_opacity(0.01, ft.colors.WHITE)),

                                     visible=False)
            self.object = ft.Container(content=ft.Row([
                ft.Row([ft.Image(icon, height=30, width=30, border_radius=50, fit=ft.ImageFit.FILL),
                        ft.Text(self.name, weight=ft.FontWeight.BOLD, width=100, overflow=ft.TextOverflow.ELLIPSIS)],),
                ft.Row([
                    self.ctc,
                    self.rmv
                ], spacing=0)
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN), width=230, height=50, bgcolor=ft.colors.TRANSPARENT,
                border_radius=10, padding=5, on_hover=self.onhover, on_click=self.open_page, offset=ft.Offset(0, 0), opacity=1, animate_offset=ft.animation.Animation(300, ft.AnimationCurve.EASE_IN_OUT), animate_opacity=ft.animation.Animation(300, ft.AnimationCurve.EASE_IN_OUT))

            if new_pass:
                self.open_page("e")

        def onhover(self, e):
            if e.data == "true":
                self.ctc.visible = True
                self.rmv.visible = True
                e.control.bgcolor = "#1D1D1D"
            else:
                self.ctc.visible = False
                self.rmv.visible = False
                e.control.bgcolor = ft.colors.TRANSPARENT

            self.ctc.icon_color = "#636363"

            e.control.update()

        def copy_to(self, e):
            self.ctc.icon_color = ft.colors.GREEN_300
            self.ctc.update()
            page.set_clipboard(self.passsword)
        def open_page(self, e):
            def change(e):
                if password_typing.value == "":
                    saved_button.disable(True)
                    return

                if name_typing.value == "":
                    saved_button.disable(True)
                    return


                if password_typing.value != self.passsword:
                    saved_button.disable(False)
                elif name_typing.value != self.name:
                    saved_button.disable(False)
                elif note_typing.value != self.note:
                    saved_button.disable(False)
                elif ico_path.value != self.icon:
                    saved_button.disable(False)

                else:
                    saved_button.disable(True)

            def confirm(e):
                self.passsword = password_typing.value
                self.name = name_typing.value
                self.note = note_typing.value
                self.icon = ico_path.value
                password_name.value = self.name
                password_name.update()
                json_data = {
                    "passwords": [],
                }

                for object in password_column.controls:
                    object: PassObject
                    json_data['passwords'].append(
                        {"name": object.name, "icon": object.icon, "passsword": object.passsword, "note": object.note})

                global passwords
                passwords.clear()
                for obj in json_data['passwords']:
                    passwords.append(obj)

                password_column.controls.clear()
                password_column.controls = [
                    PassObject(password['name'], password['passsword'], password['icon'], password['note']) for
                    password in passwords]
                password_column.update()

                data_str = json.dumps(json_data, ensure_ascii=False, indent=4, separators=(',', ': '))

                encrypt_file(fr"{documents_path}\Hashirama\data.hashirama", bytes(data_str, "utf-8"), derive_key(key))
                print("Готово")
                saved_button.disable(True)




            password_typing.value = self.passsword
            name_typing.value = self.name
            note_typing.value = self.note
            password_name.value = self.name
            ico_path.value = self.icon
            password_typing.on_change = change
            name_typing.on_change = change
            note_typing.on_change = change
            ico_path.on_change = change
            icon_prewiew.src = self.icon
            icon_prewiew.update()
            password_typing.update()
            name_typing.update()
            note_typing.update()
            ico_path.update()
            password_name.update()
            saved_button.reset_onclick(confirm)
            saved_button.disable(True)

        def remove(self, e):
            def close(e):
                page.overlay.pop()
                page.update()

            def delete(e):
                delw.disable(True)
                close(e)
                self.object.opacity = 0
                self.object.update()
                time.sleep(0.3)
                password_column.controls.remove(self)
                password_column.update()

                json_data = {
                    "passwords": [],
                }

                for object in password_column.controls:
                    object: PassObject
                    json_data['passwords'].append(
                        {"name": object.name, "icon": object.icon, "passsword": object.passsword, "note": object.note})

                global passwords
                passwords.clear()
                for obj in json_data['passwords']:
                    passwords.append(obj)

                password_column.controls.clear()
                password_column.controls = [
                    PassObject(password['name'], password['passsword'], password['icon'], password['note']) for
                    password in passwords]
                password_column.update()

                data_str = json.dumps(json_data, ensure_ascii=False, indent=4, separators=(',', ': '))

                encrypt_file(fr"{documents_path}\Hashirama\data.hashirama", bytes(data_str, "utf-8"), derive_key(key))
                print("Готtово")
            cancel = Button("Оставить", "text", close)
            delw = Button("Удалить", "danger", delete)
            modal = ft.Container(
                ft.Column(
                    [ft.Text("Вы уверены?", weight=ft.FontWeight.BOLD, size=25),
                     ft.Text("Удалив пароль вы не сможете его восстановить!", size=15, weight=ft.FontWeight.W_300,
                             color="#636363"),
                     ft.Container(height=20),
                     ft.Row([cancel, delw], alignment=ft.MainAxisAlignment.END)]
                ),
                width=400,
                height=180,
                bgcolor="#171717",
                padding=15,
                border_radius=20,
                scale=0,
                animate_scale=ft.animation.Animation(200, ft.AnimationCurve.EASE_OUT_BACK)
            )
            page.overlay.append(ft.Stack([ft.Container(modal, bgcolor=ft.colors.with_opacity(0.5, ft.colors.BLACK),
                                                       blur=ft.Blur(10, 10), alignment=ft.alignment.center)]))
            page.update()
            time.sleep(0.1)
            modal.scale = 1
            modal.update()


        def build(self):

            return self.object



    def first_start():
        os.makedirs(fr"{documents_path}\Hashirama", exist_ok=True)

        def conf(e):
            join_button.loading(True)
            try:
                global key
                key = join_text.value
                json_data = {"passwords": []}
                data_str = json.dumps(json_data, ensure_ascii=False, indent=4, separators=(',', ': '))

                encrypt_file(fr"{documents_path}\Hashirama\data.hashirama", bytes(data_str, "utf-8"), derive_key(key))
                page.overlay.pop()
                page.update()
            except Exception as e:
                join_button.loading(False)
                join_button.disable(True)
                modal.height = modal.height + 22
                join_text.error_text = f"Запустите с правами админестратора 🥲"
                join_text.update()
                modal.update()


        join_button = Button("Создать", style="primary", border_radius=20, width=130, on_click=conf)
        join_text = ft.TextField(hint_text="Ключ доступа", **text_input_outline,
                                 focused_border_color="#ffffff",
                                 color="#2A2A2A", focused_color="#ffffff")
        modal = ft.Container(
            ft.Column(
                [ft.Text("Добро пожаловать!", size=20, weight=ft.FontWeight.BOLD),

                 ft.Column([ft.Text("Придумайте ключ доступа. (ЗАПОМНИТЕ ЕГО!)", size=12), join_text],),
                 ft.Row([join_button], alignment=ft.MainAxisAlignment.END)]
            ),
            width=400,
            height=200,
            bgcolor="#171717",
            padding=15,
            border_radius=20
        )
        key_in_p = ft.Stack([ft.Container(modal, bgcolor=ft.colors.with_opacity(0.2, ft.colors.BLACK),
                                          blur=ft.Blur(5, 5), alignment=ft.alignment.center)])
        page.overlay.append(key_in_p)
        page.update()

    def search_password(e):
        password_column.controls.clear()
        if input_name.value == "":
            for password in passwords:
                password_column.controls.append(PassObject(name=password['name'],
                                                           passsword=password['passsword'],
                                                           icon=password['icon'],
                                                           note=password['note']))
            password_column.update()
            return

        for password in passwords:
            if input_name.value.lower() in password['name'].lower():
                password_column.controls.append(PassObject(name=password['name'],
                                                           passsword=password['passsword'],
                                                           icon=password['icon'],
                                                           note=password['note']))
        password_column.update()

    def new_password(e):
        password_column.controls.append(PassObject(name="Новый пароль", passsword="", icon="assets/safe.png", note="", new_pass=True))
        password_column.update()


    input_name = ft.TextField(hint_text="Поиск", hint_style=ft.TextStyle(color="#2A2A2A", size=14), content_padding=ft.padding.only(10, 0), border_width=1, border_radius=15, height=30, border_color="#2A2A2A", focused_border_color="#ffffff", focused_border_width=0.6,
                              show_cursor=False, color="#2A2A2A", focused_color="#ffffff", selection_color=ft.colors.with_opacity(0.2, "#ffffff"), on_change=search_password)


    password_column = ft.Column([], spacing=5, scroll=ft.ScrollMode.HIDDEN)
    navigation = ft.Container(ft.Column([
        input_name,
        ft.Divider(height=1, color="#2A2A2A"),
        ft.Container(content=password_column, height=page.window_height - 165, width=230),
        Button("Новый пароль", "success", border_radius=10, on_click=new_password, width=230)
    ]), width=250, height=page.window_height, bgcolor="#080808", padding=10)

    def pick_icon(e: ft.FilePickerResultEvent):
        photo = (
            ", ".join(map(lambda f: f.path, e.files)) if e.files else "assets/safe.png"
        )
        ico_path.value = photo
        ico_path.update()

    pick_files_dialog = ft.FilePicker(on_result=pick_icon)
    page.overlay.append(pick_files_dialog)

    def icon_reset(e):
        icon_prewiew.src = ico_path.value
        icon_prewiew.update()

    def generate(e):
        if password_typing.value == "":
            new_pass = generate_password(16)
        else:
            new_pass = regenerate_password(password_typing.value)
        password_typing.value = new_pass
        password_typing.update()

    password_typing = ft.TextField(hint_text="Пароль...", **text_input, width=593)
    name_typing = ft.TextField(hint_text="Название...", max_length=35, **text_input)
    note_typing = ft.TextField(hint_text="Тут можно написать доп информацию и так далее", **text_input, max_length=100)
    icon_prewiew = ft.Image("assets/safe.png", height=50, width=50, border_radius=50, fit=ft.ImageFit.FILL)
    ico_path = ft.TextField(value="assets/safe.png", **text_input, disabled=True, text_size=12)
    saved_button = Button("Сохранить", style="primary", width=200)

    password_name = ft.Text("Новый пароль", size=30, weight=ft.FontWeight.W_900)
    password_gen_button = ft.IconButton(ft.icons.VPN_KEY_ROUNDED, icon_color=ft.colors.WHITE12, width=55, height=55, **icon_button_eleveted, on_click=generate)



    content = ft.Container(ft.Column([password_name,
                                      ft.Container(border=ft.border.all(1, "#282828"), border_radius=20, width=700, height=455, content=ft.Column([
                                          ft.Container(ft.Column([ft.Row(
                                              [ft.Text("*", color="red", size=20), ft.Text("Введите пароль: ")],
                                              spacing=0),
                                                                  ft.Row([password_typing, password_gen_button]), ])),

                                          ft.Container(ft.Column([ft.Row(
                                              [ft.Text("*", color="red", size=20), ft.Text("Название пароля: ")],
                                              spacing=0),
                                                                  name_typing, ])),

                                          ft.Container(ft.Column([ft.Text("Заметка: "),
                                                                  note_typing, ])),
                                          ft.Row([ft.Container(content=icon_prewiew, width=70, height=70, alignment=ft.alignment.center, bgcolor="#0F0F0F", border=ft.border.all(1, "#242424"), border_radius=15, on_click=lambda _: pick_files_dialog.pick_files(
                        allow_multiple=False,
                        file_type=ft.FilePickerFileType.IMAGE
                    )),
                                                  ico_path, Button(text="Загрузить", on_click=icon_reset, style="default", border_radius=15)])
                                      ]), padding=20),

                                      ft.Container(ft.Row([saved_button], alignment=ft.MainAxisAlignment.END), width=700)



                                      ], scroll=ft.ScrollMode.HIDDEN), height=page.window_height, width=page.window_width - 250, padding=10)

    page.add(ft.Row([navigation, content], spacing=0))
    saved_button.disable(True)






    def click(e):
        join_button.loading(True)
        global key
        key = join_text.value
        data = decrypt_file(fr"{documents_path}\Hashirama\data.hashirama", derive_key(key))


        if data == "418":
            join_button.loading(False)
            join_button.disable(True)
            modal.height = modal.height + 22
            join_text.error_text = "Неправильный ключ"
            join_text.update()
            modal.update()
            time.sleep(2)
            modal.height = modal.height - 22
            join_text.error_text = None
            join_text.update()
            modal.update()
            join_button.disable(False)

        elif data == "404":
            join_button.loading(False)
            join_button.disable(True)
            modal.height = modal.height + 22
            join_text.error_text = "Ошибка 404 (Файл ненайден)"
            join_text.update()
            modal.update()
            time.sleep(2)
            modal.height = modal.height - 22
            join_text.error_text = None
            join_text.update()
            modal.update()
            join_button.disable(False)
        else:
            global passwords
            data = json.loads(data)
            passwords = data["passwords"]
            join_button.loading(False)
            key_in_pu_t.controls[0].opacity = 0
            key_in_pu_t.update()
            time.sleep(0.2)
            page.overlay.remove(key_in_pu_t)
            page.update()
            password_column.controls = [PassObject(password['name'], password['passsword'], password['icon'], password['note']) for
                                        password in passwords]
            password_column.update()

    if not os.path.exists(fr"{documents_path}\Hashirama\data.hashirama"):
        first_start()
    else:
        join_button = Button("Войти", style="primary", border_radius=20, width=130, on_click=click)
        join_text = ft.TextField(hint_text="Ключ доступа", **text_input_outline, focused_border_color="#ffffff", color="#2A2A2A",  focused_color="#ffffff")
        modal = ft.Container(
            ft.Column(
              [ft.Text("Введите ключ", size=20, weight=ft.FontWeight.BOLD),
               join_text,
               ft.Row([join_button], alignment=ft.MainAxisAlignment.END)]
            ),
            width=400,
            height=180,
            bgcolor="#171717",
            padding=15,
            border_radius=20
        )
        key_in_pu_t = ft.Stack([ft.Container(modal, bgcolor=ft.colors.with_opacity(0.2, ft.colors.BLACK), blur=ft.Blur(5, 5), alignment=ft.alignment.center, opacity=1, animate_opacity=ft.animation.Animation(200, ft.AnimationCurve.EASE_IN_OUT))])
        page.overlay.append(key_in_pu_t)
        page.update()



ft.app(target=main)