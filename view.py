        page.window_resizable = False
        page.vertical_alignment = "start"
        self.header = Text("Генератор паролей", size=26, weight="bold", color="#1976d2")
        self.length_input = TextField(
            label="Длина пароля (6–20)",
            value="12",
            width=130,
            text_align="center",
            keyboard_type="number",
            tooltip="Введите длину пароля от 6 до 20",
        )
        self.uppercase_cb = Checkbox(label="Заглавные буквы (A-Z)", value=True)
        self.lowercase_cb = Checkbox(label="Строчные буквы (a-z)", value=True)
        self.digits_cb = Checkbox(label="Цифры (0-9)", value=True)
        self.symbols_cb = Checkbox(label="Символы (!@#$%*/:;)", value=True)
        self.generate_btn = ElevatedButton("Сгенерировать", icon=icons.VPN_KEY)
        self.password_output = Text(value="", selectable=True, size=20, weight="bold", color="#0d47a1")
        self.copy_btn = IconButton(icon=icons.CONTENT_COPY, tooltip="Копировать пароль")
        self.snackbar = SnackBar()
        page.add(
            self.header,
            self.length_input,
            Row([self.uppercase_cb, self.lowercase_cb], alignment="start"),
            Row([self.digits_cb, self.symbols_cb], alignment="start"),
            self.generate_btn,
            Row([self.password_output, self.copy_btn], alignment="spaceBetween"),
            self.snackbar,
        )
