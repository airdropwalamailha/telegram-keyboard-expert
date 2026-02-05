"""
Telegram Keyboard Library - Usage Examples
Complete examples for all button types
"""

from telegram_keyboard import TelegramKeyboard, create_button_grid, create_emoji_keyboard
import time


# Initialize
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
kb = TelegramKeyboard(BOT_TOKEN)


# ==================== EXAMPLE 1: BASIC REPLY KEYBOARD ====================

def example_basic_reply_keyboard(chat_id):
    """Simple text buttons"""
    
    buttons = [
        ["📝 Register", "🔐 Login"],
        ["ℹ️ Help", "⚙️ Settings"],
        ["❌ Cancel"]
    ]
    
    kb.send_with_reply_keyboard(
        chat_id,
        "Welcome! Choose an option:",
        buttons,
        resize=True,
        one_time=False
    )


# ==================== EXAMPLE 2: CONTACT & LOCATION ====================

def example_contact_location(chat_id):
    """Contact and location sharing buttons"""
    
    buttons = [
        [kb.create_contact_button("📱 Share Contact")],
        [kb.create_location_button("📍 Share Location")],
        ["❌ Cancel"]
    ]
    
    keyboard = kb.create_reply_keyboard(buttons)
    kb.send_message(chat_id, "Please share your info:", keyboard)


# ==================== EXAMPLE 3: POLL BUTTON ====================

def example_poll_button(chat_id):
    """Create poll button"""
    
    buttons = [
        [kb.create_poll_button("📊 Create Quiz", "quiz")],
        [kb.create_poll_button("📋 Create Poll", "regular")],
        ["🔙 Back"]
    ]
    
    keyboard = kb.create_reply_keyboard(buttons)
    kb.send_message(chat_id, "Create a poll or quiz:", keyboard)


# ==================== EXAMPLE 4: WEB APP BUTTON ====================

def example_web_app(chat_id):
    """Web App button"""
    
    buttons = [
        [kb.create_web_app_button("🌐 Open Web App", "https://example.com/webapp")],
        ["🔙 Back"]
    ]
    
    keyboard = kb.create_reply_keyboard(buttons)
    kb.send_message(chat_id, "Open web application:", keyboard)


# ==================== EXAMPLE 5: INLINE CALLBACK BUTTONS ====================

def example_inline_callback(chat_id):
    """Inline buttons with callbacks"""
    
    buttons = [
        [
            kb.create_callback_button("✅ Approve", "approve"),
            kb.create_callback_button("❌ Reject", "reject")
        ],
        [
            kb.create_callback_button("⏸️ Pause", "pause"),
            kb.create_callback_button("▶️ Resume", "resume")
        ],
        [
            kb.create_callback_button("ℹ️ More Info", "info")
        ]
    ]
    
    kb.send_with_inline_keyboard(
        chat_id,
        "Choose an action:",
        buttons
    )


# ==================== EXAMPLE 6: URL BUTTONS ====================

def example_url_buttons(chat_id):
    """Inline buttons with URLs"""
    
    buttons = [
        [
            kb.create_url_button("🌐 Google", "https://google.com"),
            kb.create_url_button("📱 Telegram", "https://telegram.org")
        ],
        [
            kb.create_url_button("💻 GitHub", "https://github.com")
        ]
    ]
    
    kb.send_with_inline_keyboard(
        chat_id,
        "Useful links:",
        buttons
    )


# ==================== EXAMPLE 7: MIXED INLINE BUTTONS ====================

def example_mixed_inline(chat_id):
    """Mix of callback and URL buttons"""
    
    buttons = [
        [
            kb.create_callback_button("📊 View Stats", "stats"),
            kb.create_url_button("📖 Docs", "https://docs.example.com")
        ],
        [
            kb.create_callback_button("⬇️ Download", "download"),
            kb.create_callback_button("🗑️ Delete", "delete")
        ]
    ]
    
    kb.send_with_inline_keyboard(
        chat_id,
        "File Options:",
        buttons
    )


# ==================== EXAMPLE 8: SWITCH INLINE BUTTONS ====================

def example_switch_inline(chat_id):
    """Switch inline query buttons"""
    
    buttons = [
        [kb.create_switch_inline_button("🔍 Search in This Chat", "search", current_chat=True)],
        [kb.create_switch_inline_button("🔍 Search in New Chat", "search", current_chat=False)]
    ]
    
    kb.send_with_inline_keyboard(
        chat_id,
        "Start inline search:",
        buttons
    )


# ==================== EXAMPLE 9: PAGINATION ====================

def example_pagination(chat_id, current_page=1, total_pages=5):
    """Pagination buttons"""
    
    buttons = kb.pagination_keyboard(current_page, total_pages, "page")
    
    kb.send_with_inline_keyboard(
        chat_id,
        f"Page {current_page} of {total_pages}",
        buttons
    )


# ==================== EXAMPLE 10: BUTTON GRID ====================

def example_button_grid(chat_id):
    """Grid of items"""
    
    items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6"]
    buttons = create_button_grid(items, columns=2, callback_prefix="select")
    
    # Add back button
    buttons.append([kb.create_callback_button("🔙 Back", "back")])
    
    kb.send_with_inline_keyboard(
        chat_id,
        "Select an item:",
        buttons
    )


# ==================== EXAMPLE 11: MAIN MENU (PRESET) ====================

def example_main_menu(chat_id):
    """Preset main menu"""
    
    buttons = kb.main_menu(
        register=True,
        login=True,
        help=True,
        custom_buttons=["📞 Contact Us", "⭐ Rate Us"]
    )
    
    kb.send_with_reply_keyboard(
        chat_id,
        "Main Menu:",
        buttons
    )


# ==================== EXAMPLE 12: YES/NO KEYBOARD ====================

def example_yes_no(chat_id):
    """Simple Yes/No keyboard"""
    
    buttons = kb.yes_no_keyboard("✅ Confirm", "❌ Cancel")
    
    kb.send_with_reply_keyboard(
        chat_id,
        "Are you sure you want to delete?",
        buttons,
        one_time=True  # Hide after use
    )


# ==================== EXAMPLE 13: NUMBER KEYBOARD ====================

def example_number_keyboard(chat_id):
    """Number selection keyboard"""
    
    buttons = kb.number_keyboard(1, 9, columns=3)
    buttons.append(["0"])
    buttons.append(["❌ Cancel"])
    
    kb.send_with_reply_keyboard(
        chat_id,
        "Select a number:",
        buttons
    )


# ==================== EXAMPLE 14: EMOJI KEYBOARD ====================

def example_emoji_keyboard(chat_id):
    """Emoji selection keyboard"""
    
    emojis = ["😀", "😂", "😍", "🥰", "😎", "🤔", "😴", "🤗", "😭", "🔥"]
    buttons = create_emoji_keyboard(emojis, columns=5)
    buttons.append(["🔙 Back"])
    
    kb.send_with_reply_keyboard(
        chat_id,
        "Choose your mood:",
        buttons
    )


# ==================== EXAMPLE 15: REMOVE KEYBOARD ====================

def example_remove_keyboard(chat_id):
    """Remove/hide keyboard"""
    
    kb.send_remove_keyboard(chat_id, "Keyboard removed!")


# ==================== EXAMPLE 16: CATEGORIES WITH SUBCATEGORIES ====================

def example_categories(chat_id):
    """Multi-level menu"""
    
    # Main categories
    buttons = [
        [
            kb.create_callback_button("📱 Electronics", "cat_electronics"),
            kb.create_callback_button("👕 Clothing", "cat_clothing")
        ],
        [
            kb.create_callback_button("📚 Books", "cat_books"),
            kb.create_callback_button("🏠 Home", "cat_home")
        ],
        [
            kb.create_callback_button("🍔 Food", "cat_food"),
            kb.create_callback_button("🎮 Gaming", "cat_gaming")
        ]
    ]
    
    kb.send_with_inline_keyboard(
        chat_id,
        "Select a category:",
        buttons
    )


def show_subcategory(chat_id, category):
    """Show subcategory after category selection"""
    
    subcategories = {
        "electronics": ["📱 Phones", "💻 Laptops", "🎧 Audio"],
        "clothing": ["👔 Men", "👗 Women", "👶 Kids"],
        "books": ["📖 Fiction", "📚 Non-Fiction", "📕 Comics"]
    }
    
    items = subcategories.get(category, ["No items"])
    buttons = [[kb.create_callback_button(item, f"item_{item}")] for item in items]
    buttons.append([kb.create_callback_button("🔙 Back to Categories", "back_categories")])
    
    kb.send_with_inline_keyboard(
        chat_id,
        f"Select from {category.title()}:",
        buttons
    )


# ==================== EXAMPLE 17: SETTINGS MENU ====================

def example_settings_menu(chat_id):
    """Settings menu with toggles"""
    
    buttons = [
        [kb.create_callback_button("🔔 Notifications: ON", "toggle_notif")],
        [kb.create_callback_button("🌙 Dark Mode: OFF", "toggle_dark")],
        [kb.create_callback_button("🔊 Sound: ON", "toggle_sound")],
        [kb.create_callback_button("🌐 Language: English", "change_lang")],
        [kb.create_callback_button("🔙 Back to Menu", "main_menu")]
    ]
    
    kb.send_with_inline_keyboard(
        chat_id,
        "⚙️ Settings",
        buttons
    )


# ==================== EXAMPLE 18: RATING SYSTEM ====================

def example_rating(chat_id):
    """Star rating system"""
    
    buttons = [
        [
            kb.create_callback_button("⭐", "rate_1"),
            kb.create_callback_button("⭐⭐", "rate_2"),
            kb.create_callback_button("⭐⭐⭐", "rate_3")
        ],
        [
            kb.create_callback_button("⭐⭐⭐⭐", "rate_4"),
            kb.create_callback_button("⭐⭐⭐⭐⭐", "rate_5")
        ]
    ]
    
    kb.send_with_inline_keyboard(
        chat_id,
        "How would you rate our service?",
        buttons
    )


# ==================== EXAMPLE 19: DYNAMIC KEYBOARD UPDATE ====================

def example_dynamic_update(chat_id, message_id, count=0):
    """Update inline keyboard dynamically"""
    
    buttons = [
        [
            kb.create_callback_button("➖", "decrease"),
            kb.create_callback_button(f"Count: {count}", "count"),
            kb.create_callback_button("➕", "increase")
        ],
        [kb.create_callback_button("🔄 Reset", "reset")]
    ]
    
    keyboard = kb.create_inline_keyboard(buttons)
    
    kb.edit_message_text(
        chat_id,
        message_id,
        f"Current count: {count}",
        keyboard
    )


# ==================== EXAMPLE 20: FULL BOT WITH ALL FEATURES ====================

def full_bot_example():
    """Complete bot with all keyboard types"""
    
    def get_updates(offset=None):
        import requests
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
        params = {"offset": offset, "timeout": 30}
        response = requests.get(url, params=params)
        return response.json()
    
    print("🤖 Bot started with all keyboard types...")
    offset = None
    
    while True:
        try:
            updates = get_updates(offset)
            
            if updates.get("result"):
                for update in updates["result"]:
                    offset = update["update_id"] + 1
                    
                    # Handle messages
                    if "message" in update:
                        chat_id = update["message"]["chat"]["id"]
                        text = update["message"].get("text", "")
                        
                        if text == "/start":
                            example_main_menu(chat_id)
                        
                        elif text == "📝 Register":
                            example_contact_location(chat_id)
                        
                        elif text == "🔐 Login":
                            example_yes_no(chat_id)
                        
                        elif text == "ℹ️ Help":
                            example_url_buttons(chat_id)
                        
                        elif text == "/inline":
                            example_inline_callback(chat_id)
                        
                        elif text == "/numbers":
                            example_number_keyboard(chat_id)
                        
                        elif text == "/emojis":
                            example_emoji_keyboard(chat_id)
                        
                        elif text == "/pagination":
                            example_pagination(chat_id)
                        
                        elif text == "/categories":
                            example_categories(chat_id)
                        
                        elif text == "/settings":
                            example_settings_menu(chat_id)
                        
                        elif text == "/rating":
                            example_rating(chat_id)
                        
                        elif text == "/remove":
                            example_remove_keyboard(chat_id)
                    
                    # Handle callback queries (inline button clicks)
                    elif "callback_query" in update:
                        callback = update["callback_query"]
                        chat_id = callback["message"]["chat"]["id"]
                        message_id = callback["message"]["message_id"]
                        callback_data = callback["data"]
                        callback_id = callback["id"]
                        
                        # Answer callback
                        kb.answer_callback_query(
                            callback_id,
                            f"You clicked: {callback_data}"
                        )
                        
                        # Handle different callbacks
                        if callback_data.startswith("page_"):
                            page = int(callback_data.split("_")[1])
                            example_pagination(chat_id, page, 5)
                        
                        elif callback_data.startswith("rate_"):
                            rating = callback_data.split("_")[1]
                            kb.send_message(chat_id, f"Thanks for {rating}⭐ rating!")
                        
                        elif callback_data.startswith("cat_"):
                            category = callback_data.split("_")[1]
                            show_subcategory(chat_id, category)
            
            time.sleep(0.5)
            
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(3)


# ==================== QUICK TEST FUNCTION ====================

def quick_test(chat_id):
    """Test all keyboard types quickly"""
    
    print("Testing all keyboard types...")
    
    time.sleep(1)
    print("1. Basic Reply Keyboard")
    example_basic_reply_keyboard(chat_id)
    
    time.sleep(2)
    print("2. Contact & Location")
    example_contact_location(chat_id)
    
    time.sleep(2)
    print("3. Inline Callbacks")
    example_inline_callback(chat_id)
    
    time.sleep(2)
    print("4. URL Buttons")
    example_url_buttons(chat_id)
    
    time.sleep(2)
    print("5. Pagination")
    example_pagination(chat_id)
    
    time.sleep(2)
    print("6. Categories")
    example_categories(chat_id)
    
    time.sleep(2)
    print("7. Rating System")
    example_rating(chat_id)
    
    print("✅ All tests completed!")


# ==================== USAGE ====================

if __name__ == "__main__":
    # Replace with your chat ID for testing
    TEST_CHAT_ID = "YOUR_CHAT_ID"
    
    # Test individual examples
    # example_basic_reply_keyboard(TEST_CHAT_ID)
    # example_inline_callback(TEST_CHAT_ID)
    # example_pagination(TEST_CHAT_ID)
    
    # Or run full bot
    full_bot_example()
    
    # Or quick test all
    # quick_test(TEST_CHAT_ID)
