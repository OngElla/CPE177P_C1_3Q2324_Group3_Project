from flet import *

def main(page: Page):
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    isLogin = Text("Login",
        weight = "bold",
        color = "white",
        size = 20,

        offset = transform.Offset(0,0),
        animate_offset = animation.Animation(duration=300)
    )

    def ganti(e):
        ctx.bgcolor = "teal" if isLogin.value == "Login" else "white"
        ctx.height = 500 if isLogin.value == "Login" else 150
        ctx.width = 300 if isLogin.value == "Login" else 200
        ctx.border_radius = 0 if isLogin.value == "Login" else 100

        print(isLogin.value)

        isLogin.value = "Sign Up" if isLogin.value == "Login" else "Login"
        isLogin.offset = transform.Offset(5,0) if isLogin.value == "Login" else transform.Offset(0,0) 

        register_btn.value = "Sign Up" if isLogin.value == "Login" else "Login"
        register_btn.offset = transform.Offset(0,0) if isLogin.value == "Login" else transform.Offset(5,0)

        txt_box_register.visible = True if isLogin.value == "Sign Up" else False

        page.update()

    # REGISTER
    txt_box_register = Container(
        content = Column([
            TextField(label = "Username",
                border_color = "white",
                color = "white"
                ),
            TextField(label = "Password",
                border_color = "white",
                color = "white"
                ),
            ElevatedButton("Login",
                width = page.window_width,
                on_click = ganti

                )

            ])

        )

    txt_box_register.visible = False

    register_btn = ElevatedButton("Sign Up",
        on_click = ganti,
        offset = transform.Offset(0,0),
        animate_offset = animation.Animation(duration=300)
    )

    ctx = Container(
        bgcolor = "white", 
        border_radius = 100,
        padding = 20,
        width = 200,
        alignment = alignment.center,
        height = 150,
        animate = animation.Animation(duration = 300, curve = "easeInOut"),
        content = Column([
            isLogin,
            txt_box_register,
            register_btn
            ])
    )

    page.add(
        ctx
    )

app(target = main)
