# 🎮 Telegram Keyboard Library

Complete Python library for creating all types of Telegram bot keyboards with ease!

## 📦 Installation

```bash
pip install requests
```

## 🚀 Quick Start

```python
from telegram_keyboard import TelegramKeyboard

# Initialize
kb = TelegramKeyboard("YOUR_BOT_TOKEN")

# Send message with keyboard
buttons = [
    ["📝 Register", "🔐 Login"],
    ["ℹ️ Help"]
]

kb.send_with_reply_keyboard(
    chat_id=123456789,
    text="Welcome!",
    buttons=buttons
)
```

---

## 📋 Features

✅ **Reply Keyboards** (Bottom of screen)
- Text buttons
- Contact sharing
- Location sharing
- Poll creation
- Web App buttons

✅ **Inline Keyboards** (Attached to message)
- Callback buttons
- URL buttons
- Login buttons
- Switch inline buttons
- Game buttons
- Payment buttons

✅ **Preset Keyboards**
- Main menu
- Yes/No dialogs
- Number pad
- Pagination
- Back buttons

✅ **Helper Functions**
- Button grid creator
- Emoji keyboards
- Dynamic updates

---

## 🎯 Usage Examples

### 1️⃣ Basic Reply Keyboard

```python
from telegram_keyboard import TelegramKeyboard

kb = TelegramKeyboard("YOUR_TOKEN")

buttons = [
    ["Button 1", "Button 2"],
    ["Button 3"]
]

kb.send_with_reply_keyboard(
    chat_id=123456789,
    text="Choose an option:",
    buttons=buttons,
    resize=True,
    one_time=False
)
```

### 2️⃣ Contact & Location Buttons

```python
buttons = [
    [kb.create_contact_button("📱 Share Contact")],
    [kb.create_location_button("📍 Share Location")],
    ["Cancel"]
]

keyboard = kb.create_reply_keyboard(buttons)
kb.send_message(123456789, "Share your info:", keyboard)
```

### 3️⃣ Inline Callback Buttons

```python
buttons = [
    [
        kb.create_callback_button("✅ Approve", "approve"),
        kb.create_callback_button("❌ Reject", "reject")
    ],
    [
        kb.create_callback_button("ℹ️ Info", "info")
    ]
]

kb.send_with_inline_keyboard(
    chat_id=123456789,
    text="Choose action:",
    buttons=buttons
)
```

### 4️⃣ URL Buttons

```python
buttons = [
    [
        kb.create_url_button("🌐 Google", "https://google.com"),
        kb.create_url_button("📱 Telegram", "https://telegram.org")
    ]
]

kb.send_with_inline_keyboard(
    chat_id=123456789,
    text="Useful links:",
    buttons=buttons
)
```

### 5️⃣ Pagination

```python
buttons = kb.pagination_keyboard(
    current_page=2,
    total_pages=5,
    callback_prefix="page"
)

kb.send_with_inline_keyboard(
    chat_id=123456789,
    text="Page 2 of 5",
    buttons=buttons
)
```

### 6️⃣ Main Menu (Preset)

```python
buttons = kb.main_menu(
    register=True,
    login=True,
    help=True,
    custom_buttons=["📞 Contact", "⭐ Rate"]
)

kb.send_with_reply_keyboard(
    chat_id=123456789,
    text="Main Menu:",
    buttons=buttons
)
```

### 7️⃣ Yes/No Dialog

```python
buttons = kb.yes_no_keyboard("✅ Confirm", "❌ Cancel")

kb.send_with_reply_keyboard(
    chat_id=123456789,
    text="Delete file?",
    buttons=buttons,
    one_time=True
)
```

### 8️⃣ Number Keyboard

```python
buttons = kb.number_keyboard(1, 9, columns=3)
buttons.append(["0"])
buttons.append(["Cancel"])

kb.send_with_reply_keyboard(
    chat_id=123456789,
    text="Enter PIN:",
    buttons=buttons
)
```

### 9️⃣ Button Grid

```python
from telegram_keyboard import create_button_grid

items = ["Item 1", "Item 2", "Item 3", "Item 4"]
buttons = create_button_grid(items, columns=2)

kb.send_with_inline_keyboard(
    chat_id=123456789,
    text="Select item:",
    buttons=buttons
)
```

### 🔟 Remove Keyboard

```python
kb.send_remove_keyboard(123456789, "Keyboard hidden!")
```

---

## 🔧 Advanced Features

### Dynamic Keyboard Update

```python
# Update existing message
kb.edit_message_text(
    chat_id=123456789,
    message_id=456,
    text="Updated text",
    keyboard=new_keyboard
)
```

### Answer Callback Query

```python
kb.answer_callback_query(
    callback_query_id="abc123",
    text="Button clicked!",
    show_alert=True
)
```

### Web App Button

```python
buttons = [
    [kb.create_web_app_button("🌐 Open App", "https://example.com/app")]
]
```

### Poll Button

```python
buttons = [
    [kb.create_poll_button("📊 Create Quiz", "quiz")],
    [kb.create_poll_button("📋 Create Poll", "regular")]
]
```

---

## 📖 Complete API Reference

### TelegramKeyboard Class

#### Initialization
```python
kb = TelegramKeyboard(bot_token: str)
```

#### Reply Keyboard Methods

| Method | Description | Returns |
|--------|-------------|---------|
| `create_reply_keyboard(buttons, resize, one_time, selective, placeholder)` | Create reply keyboard | dict |
| `create_text_button(text)` | Simple text button | str |
| `create_contact_button(text)` | Contact sharing button | dict |
| `create_location_button(text)` | Location sharing button | dict |
| `create_poll_button(text, poll_type)` | Poll creation button | dict |
| `create_web_app_button(text, url)` | Web App button | dict |
| `remove_keyboard()` | Hide keyboard | dict |

#### Inline Keyboard Methods

| Method | Description | Returns |
|--------|-------------|---------|
| `create_inline_keyboard(buttons)` | Create inline keyboard | dict |
| `create_callback_button(text, callback_data)` | Callback button | dict |
| `create_url_button(text, url)` | URL button | dict |
| `create_login_button(text, url)` | Login button | dict |
| `create_switch_inline_button(text, query, current_chat)` | Switch inline button | dict |
| `create_game_button(text)` | Game button | dict |
| `create_pay_button(text)` | Payment button | dict |

#### Send Methods

| Method | Description | Returns |
|--------|-------------|---------|
| `send_message(chat_id, text, keyboard, parse_mode)` | Send message | dict |
| `send_with_reply_keyboard(chat_id, text, buttons, **kwargs)` | Send with reply keyboard | dict |
| `send_with_inline_keyboard(chat_id, text, buttons, **kwargs)` | Send with inline keyboard | dict |
| `send_remove_keyboard(chat_id, text)` | Send and hide keyboard | dict |

#### Preset Methods

| Method | Description | Returns |
|--------|-------------|---------|
| `main_menu(register, login, help, custom_buttons)` | Main menu layout | list |
| `yes_no_keyboard(yes_text, no_text)` | Yes/No buttons | list |
| `back_button(text)` | Back button | list |
| `number_keyboard(start, end, columns)` | Number pad | list |
| `pagination_keyboard(current_page, total_pages, callback_prefix)` | Pagination | list |

### Helper Functions

```python
create_button_grid(items, columns, callback_prefix)
create_emoji_keyboard(emojis, columns)
```

---

## 💡 Common Patterns

### Registration Flow

```python
# Step 1: Main menu
buttons = [["📝 Register", "🔐 Login"]]
kb.send_with_reply_keyboard(chat_id, "Welcome!", buttons)

# Step 2: Get contact
buttons = [[kb.create_contact_button("📱 Share Contact")]]
keyboard = kb.create_reply_keyboard(buttons)
kb.send_message(chat_id, "Share contact:", keyboard)

# Step 3: Confirm
buttons = kb.yes_no_keyboard()
kb.send_with_reply_keyboard(chat_id, "Confirm?", buttons, one_time=True)
```

### Settings Menu

```python
buttons = [
    [kb.create_callback_button("🔔 Notifications", "notif")],
    [kb.create_callback_button("🌙 Dark Mode", "dark")],
    [kb.create_callback_button("🔙 Back", "back")]
]
kb.send_with_inline_keyboard(chat_id, "Settings", buttons)
```

### Product Catalog

```python
products = ["Product 1", "Product 2", "Product 3"]
buttons = create_button_grid(products, columns=2, callback_prefix="buy")
buttons.append([kb.create_callback_button("🛒 Cart", "cart")])
kb.send_with_inline_keyboard(chat_id, "Shop:", buttons)
```

---

## 🎨 Emoji Guide

Common emojis for buttons:

```
📝 ✏️ 📋 - Forms/Writing
🔐 🔒 🔑 - Security
ℹ️ ❓ 💡 - Information
✅ ❌ ⚠️ - Status
👤 👥 🏠 - Profile/Home
⚙️ 🛠️ 📊 - Settings/Tools
📱 💻 🌐 - Technology
🛒 💳 🎁 - Shopping
⭐ ❤️ 👍 - Reactions
🔙 ⬅️ ➡️ - Navigation
```

---

## 🐛 Troubleshooting

### Keyboard not showing?
- Check `resize_keyboard=True`
- Ensure bot has permission to send messages
- Verify button format is correct

### Callback not working?
- Make sure you're handling `callback_query` in updates
- Use `answer_callback_query()` to acknowledge clicks
- Check callback_data length (max 64 bytes)

### Buttons not aligned?
- Each row is a list: `[["btn1", "btn2"], ["btn3"]]`
- Use equal number of buttons per row for best appearance

---

## 📄 License

MIT License - Free to use!

---

## 🤝 Contributing

Contributions welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

---

## 📞 Support

Questions? Issues? Contact:
- Telegram: @YourUsername
- GitHub: github.com/yourusername/telegram-keyboard

---

## 🎓 Learn More

- [Telegram Bot API Docs](https://core.telegram.org/bots/api)
- [Keyboard Markup Guide](https://core.telegram.org/bots/api#replykeyboardmarkup)
- [Inline Keyboard Guide](https://core.telegram.org/bots/api#inlinekeyboardmarkup)

---

Made with ❤️ for Telegram Bot Developers
