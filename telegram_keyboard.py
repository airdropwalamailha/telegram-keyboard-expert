"""
Telegram Keyboard Library
Complete solution for all types of Telegram buttons

Author: Your Name
Version: 1.0
"""

import json
import requests


class TelegramKeyboard:
    """Main class for Telegram Bot keyboard management"""
    
    def __init__(self, bot_token):
        """
        Initialize with bot token
        
        Args:
            bot_token (str): Your Telegram Bot API token
        """
        self.bot_token = bot_token
        self.base_url = f"https://api.telegram.org/bot{bot_token}"
    
    
    # ==================== REPLY KEYBOARDS ====================
    
    def create_reply_keyboard(self, buttons, resize=True, one_time=False, 
                             selective=False, placeholder=None):
        """
        Create a reply keyboard (bottom of screen)
        
        Args:
            buttons (list): 2D list of button texts
                Example: [["Button 1", "Button 2"], ["Button 3"]]
            resize (bool): Make buttons smaller
            one_time (bool): Hide keyboard after one use
            selective (bool): Show to specific users only
            placeholder (str): Placeholder text in input field
        
        Returns:
            dict: Keyboard markup
        """
        keyboard = {
            "keyboard": buttons,
            "resize_keyboard": resize,
            "one_time_keyboard": one_time,
            "selective": selective
        }
        
        if placeholder:
            keyboard["input_field_placeholder"] = placeholder
        
        return keyboard
    
    
    def create_text_button(self, text):
        """
        Create simple text button
        
        Args:
            text (str): Button text
        
        Returns:
            str: Button text
        """
        return text
    
    
    def create_contact_button(self, text):
        """
        Create contact sharing button
        
        Args:
            text (str): Button text
        
        Returns:
            dict: Contact button
        """
        return {
            "text": text,
            "request_contact": True
        }
    
    
    def create_location_button(self, text):
        """
        Create location sharing button
        
        Args:
            text (str): Button text
        
        Returns:
            dict: Location button
        """
        return {
            "text": text,
            "request_location": True
        }
    
    
    def create_poll_button(self, text, poll_type="regular"):
        """
        Create poll creation button
        
        Args:
            text (str): Button text
            poll_type (str): 'regular' or 'quiz'
        
        Returns:
            dict: Poll button
        """
        return {
            "text": text,
            "request_poll": {
                "type": poll_type
            }
        }
    
    
    def create_web_app_button(self, text, url):
        """
        Create Web App button
        
        Args:
            text (str): Button text
            url (str): Web App URL
        
        Returns:
            dict: Web App button
        """
        return {
            "text": text,
            "web_app": {
                "url": url
            }
        }
    
    
    def remove_keyboard(self):
        """
        Remove/hide keyboard
        
        Returns:
            dict: Remove keyboard markup
        """
        return {"remove_keyboard": True}
    
    
    # ==================== INLINE KEYBOARDS ====================
    
    def create_inline_keyboard(self, buttons):
        """
        Create inline keyboard (attached to message)
        
        Args:
            buttons (list): 2D list of inline buttons
                Example: [[btn1, btn2], [btn3]]
        
        Returns:
            dict: Inline keyboard markup
        """
        return {
            "inline_keyboard": buttons
        }
    
    
    def create_callback_button(self, text, callback_data):
        """
        Create callback button (for inline keyboard)
        
        Args:
            text (str): Button text
            callback_data (str): Data to send when clicked
        
        Returns:
            dict: Callback button
        """
        return {
            "text": text,
            "callback_data": callback_data
        }
    
    
    def create_url_button(self, text, url):
        """
        Create URL button (opens link)
        
        Args:
            text (str): Button text
            url (str): URL to open
        
        Returns:
            dict: URL button
        """
        return {
            "text": text,
            "url": url
        }
    
    
    def create_login_button(self, text, url):
        """
        Create login button (Telegram Login Widget)
        
        Args:
            text (str): Button text
            url (str): Login URL
        
        Returns:
            dict: Login button
        """
        return {
            "text": text,
            "login_url": {
                "url": url
            }
        }
    
    
    def create_switch_inline_button(self, text, query="", current_chat=False):
        """
        Create switch inline button
        
        Args:
            text (str): Button text
            query (str): Inline query
            current_chat (bool): Switch in current chat or new chat
        
        Returns:
            dict: Switch inline button
        """
        if current_chat:
            return {
                "text": text,
                "switch_inline_query_current_chat": query
            }
        else:
            return {
                "text": text,
                "switch_inline_query": query
            }
    
    
    def create_game_button(self, text):
        """
        Create game button
        
        Args:
            text (str): Button text
        
        Returns:
            dict: Game button
        """
        return {
            "text": text,
            "callback_game": {}
        }
    
    
    def create_pay_button(self, text):
        """
        Create payment button
        
        Args:
            text (str): Button text
        
        Returns:
            dict: Pay button
        """
        return {
            "text": text,
            "pay": True
        }
    
    
    # ==================== SEND MESSAGE METHODS ====================
    
    def send_message(self, chat_id, text, keyboard=None, parse_mode=None):
        """
        Send message with optional keyboard
        
        Args:
            chat_id (int/str): Chat ID
            text (str): Message text
            keyboard (dict): Keyboard markup (optional)
            parse_mode (str): 'HTML' or 'Markdown' (optional)
        
        Returns:
            dict: Response from Telegram API
        """
        url = f"{self.base_url}/sendMessage"
        
        data = {
            "chat_id": chat_id,
            "text": text
        }
        
        if parse_mode:
            data["parse_mode"] = parse_mode
        
        if keyboard:
            data["reply_markup"] = json.dumps(keyboard)
        
        response = requests.post(url, data=data)
        return response.json()
    
    
    def send_with_reply_keyboard(self, chat_id, text, buttons, **kwargs):
        """
        Send message with reply keyboard
        
        Args:
            chat_id: Chat ID
            text: Message text
            buttons: 2D list of buttons
            **kwargs: Additional keyboard options
        
        Returns:
            dict: API response
        """
        keyboard = self.create_reply_keyboard(buttons, **kwargs)
        return self.send_message(chat_id, text, keyboard)
    
    
    def send_with_inline_keyboard(self, chat_id, text, buttons, **kwargs):
        """
        Send message with inline keyboard
        
        Args:
            chat_id: Chat ID
            text: Message text
            buttons: 2D list of inline buttons
            **kwargs: Additional options
        
        Returns:
            dict: API response
        """
        keyboard = self.create_inline_keyboard(buttons)
        return self.send_message(chat_id, text, keyboard, **kwargs)
    
    
    def send_remove_keyboard(self, chat_id, text):
        """
        Send message and remove keyboard
        
        Args:
            chat_id: Chat ID
            text: Message text
        
        Returns:
            dict: API response
        """
        keyboard = self.remove_keyboard()
        return self.send_message(chat_id, text, keyboard)
    
    
    # ==================== CALLBACK QUERY ====================
    
    def answer_callback_query(self, callback_query_id, text=None, 
                              show_alert=False, url=None):
        """
        Answer callback query (inline button click)
        
        Args:
            callback_query_id (str): Callback query ID
            text (str): Notification text
            show_alert (bool): Show as alert or toast
            url (str): URL to open
        
        Returns:
            dict: API response
        """
        url_endpoint = f"{self.base_url}/answerCallbackQuery"
        
        data = {
            "callback_query_id": callback_query_id,
            "show_alert": show_alert
        }
        
        if text:
            data["text"] = text
        
        if url:
            data["url"] = url
        
        response = requests.post(url_endpoint, data=data)
        return response.json()
    
    
    def edit_message_text(self, chat_id, message_id, text, keyboard=None):
        """
        Edit message text (for inline keyboards)
        
        Args:
            chat_id: Chat ID
            message_id: Message ID to edit
            text: New text
            keyboard: New keyboard (optional)
        
        Returns:
            dict: API response
        """
        url = f"{self.base_url}/editMessageText"
        
        data = {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": text
        }
        
        if keyboard:
            data["reply_markup"] = json.dumps(keyboard)
        
        response = requests.post(url, data=data)
        return response.json()
    
    
    # ==================== PRESET KEYBOARDS ====================
    
    def main_menu(self, register=True, login=True, help=True, custom_buttons=None):
        """
        Create common main menu keyboard
        
        Args:
            register (bool): Include register button
            login (bool): Include login button
            help (bool): Include help button
            custom_buttons (list): Additional custom buttons
        
        Returns:
            list: Button layout
        """
        buttons = []
        
        row1 = []
        if register:
            row1.append("📝 Register")
        if login:
            row1.append("🔐 Login")
        
        if row1:
            buttons.append(row1)
        
        row2 = []
        if help:
            row2.append("ℹ️ Help")
        
        if custom_buttons:
            for btn in custom_buttons:
                row2.append(btn)
        
        if row2:
            buttons.append(row2)
        
        return buttons
    
    
    def yes_no_keyboard(self, yes_text="✅ Yes", no_text="❌ No"):
        """
        Create Yes/No keyboard
        
        Args:
            yes_text (str): Yes button text
            no_text (str): No button text
        
        Returns:
            list: Button layout
        """
        return [[yes_text, no_text]]
    
    
    def back_button(self, text="🔙 Back"):
        """
        Create back button keyboard
        
        Args:
            text (str): Button text
        
        Returns:
            list: Button layout
        """
        return [[text]]
    
    
    def number_keyboard(self, start=1, end=9, columns=3):
        """
        Create number keyboard
        
        Args:
            start (int): Starting number
            end (int): Ending number
            columns (int): Buttons per row
        
        Returns:
            list: Button layout
        """
        buttons = []
        row = []
        
        for num in range(start, end + 1):
            row.append(str(num))
            
            if len(row) == columns:
                buttons.append(row)
                row = []
        
        if row:
            buttons.append(row)
        
        return buttons
    
    
    def pagination_keyboard(self, current_page, total_pages, callback_prefix="page"):
        """
        Create pagination inline keyboard
        
        Args:
            current_page (int): Current page number
            total_pages (int): Total pages
            callback_prefix (str): Callback data prefix
        
        Returns:
            list: Inline button layout
        """
        buttons = []
        row = []
        
        # Previous button
        if current_page > 1:
            row.append(self.create_callback_button(
                "⬅️ Previous",
                f"{callback_prefix}_{current_page - 1}"
            ))
        
        # Page indicator
        row.append(self.create_callback_button(
            f"📄 {current_page}/{total_pages}",
            "page_info"
        ))
        
        # Next button
        if current_page < total_pages:
            row.append(self.create_callback_button(
                "Next ➡️",
                f"{callback_prefix}_{current_page + 1}"
            ))
        
        buttons.append(row)
        return buttons


# ==================== HELPER FUNCTIONS ====================

def create_button_grid(items, columns=2, callback_prefix="item"):
    """
    Create button grid from list of items
    
    Args:
        items (list): List of item names
        columns (int): Buttons per row
        callback_prefix (str): Callback data prefix
    
    Returns:
        list: Button layout for inline keyboard
    """
    kb = TelegramKeyboard("")
    buttons = []
    row = []
    
    for i, item in enumerate(items):
        row.append(kb.create_callback_button(item, f"{callback_prefix}_{i}"))
        
        if len(row) == columns:
            buttons.append(row)
            row = []
    
    if row:
        buttons.append(row)
    
    return buttons


def create_emoji_keyboard(emojis, columns=5):
    """
    Create emoji keyboard
    
    Args:
        emojis (list): List of emojis
        columns (int): Emojis per row
    
    Returns:
        list: Button layout
    """
    buttons = []
    row = []
    
    for emoji in emojis:
        row.append(emoji)
        
        if len(row) == columns:
            buttons.append(row)
            row = []
    
    if row:
        buttons.append(row)
    
    return buttons
