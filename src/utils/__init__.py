from .command_parser import parse_input
from .command_handlers import (
    handle_add_contact,
    handle_search_contact,
    handle_show_all_notes,
    handle_remove_contact,
    handle_show_all_contacts,
    handle_upcoming_birthdays,
    handle_edit_contact,
    handle_add_note,
    handle_search_notes,
    handle_remove_note,
    handle_edit_note,
    handle_add_tag,
    handle_remove_tag,
    handle_sort_notes_by_tags,
)
from .custom_decorators import error_handler
from .suggestion_utils import suggest_command, completer