def complete_all_todos(lst):
    for todo in lst['todos']:
        todo['completed'] = True

    return None

def error_for_list_title(title, lists):
    if any(lst['title'] == title for lst in lists):
        return "The title must be unique."
    elif not 1 <= len(title) <= 100:
        return "The title must be between 1 and 100 characters"
    else:
        return None
    
def error_for_todo(todo):
    if not 1 <= len(todo) <= 100:
        return "Todo must be between 1 and 100 characters"
    else:
        return None

def find_list_by_id(list_id, lists):
    return next((lst for lst in lists if lst['id'] == list_id), None)

def find_todo_by_id(todo_id, lst):
    return next((todo for todo in lst if todo['id'] == todo_id), None)

def is_list_completed(lst):
    return len(lst['todos']) > 0 and todos_remaining(lst) == 0

def is_todo_completed(todo):
    return todo['completed']

def sort_items(items, sorting_func):
    alpha_sorted = sorted(items, key=lambda item: item['title'].casefold())
    return sorted(alpha_sorted, key=lambda item: sorting_func(item))

def todos_remaining(lst):
    return sum(1 for todo in lst['todos'] if not todo['completed'])
