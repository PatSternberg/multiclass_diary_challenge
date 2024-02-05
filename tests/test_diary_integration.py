from lib.diary import Diary
from lib.diary_entry import DiaryEntry
from lib.todo import ToDo
import pytest

new_diary = Diary()
new_diary.add_diary_entry('First diary entry')
new_diary.add_diary_entry('Second diary entry')
new_diary.add_diary_entry('Third diary entry')
new_diary.add_todo('UncompleteTask1')
new_diary.add_todo('UncompleteTask2')
new_diary.add_todo('CompleteTask3')
new_diary_entry_empty = DiaryEntry('')
# new_diary_entry_none = DiaryEntry()
# new_todo_empty = ToDo('')
# new_todo_none = ToDo()

def test_diary_read_all_entries():
    result = new_diary.read_all_entries()
    assert result == {1: 'First diary entry', 2: 'Second diary entry', 3: 'Third diary entry'}

def test_read_entry_by_number():
    result = new_diary.read_entry_by_number(3)
    assert result == 'Third diary entry'

# new_diary.add_diary_entry('Te')
# new_diary.add_diary_entry('T')
# new_diary.add_diary_entry('Test1')
# new_diary.add_diary_entry('Test')
# new_diary.add_diary_entry('-Test1-')

# def test_selective_read_entry():
#     result = new_diary.selective_read_entry(5,1)
#     assert result == 'Test1'

# new_diary.add_diary_entry('I have two mobile numbers: 01234567890 and 12345678901')
# new_diary.add_diary_entry('Too short a number: 1500 chocolate biscuits')
# new_diary.add_diary_entry('I have one mobile number: 23456789012')

# def test_mobile_numbers():
#     result = new_diary.mobile_numbers()
#     assert result == ['01234567890', '12345678901', '23456789012']
    
def test_complete_todo():
    new_diary.complete_todo('CompleteTask3')
    result = new_diary.read_todo_list()
    assert result == {'CompleteTask3': True, 'UncompleteTask1': False, 'UncompleteTask2': False}

def test_clear_todo_list():
    new_diary.clear_todo_list()
    result = new_diary.read_todo_list()
    assert result == {'UncompleteTask1': False, 'UncompleteTask2': False}

# def test_diary_entry_empty():
#     with pytest.raises(Exception) as e:
#         new_diary.add_diary_entry(new_diary_entry_empty)
#     error_message = str(e.value)
#     assert error_message == 'Diary entry has no content'

# def test_diary_entry_none():
#     with pytest.raises(Exception) as e:
#         new_diary.add_diary_entry(new_diary_entry_none)
#     error_message = str(e.value)
#     assert error_message == 'Diary entry has missing content'

# def test_todo_empty():
#     with pytest.raises(Exception) as e:
#         new_diary.add_todo(new_todo_empty)
#     error_message = str(e.value)
#     assert error_message == 'Task has no content'

# def test_todo_none():
#     with pytest.raises(Exception) as e:
#         new_diary.add_todo(new_todo_none)
#     error_message = str(e.value)
#     assert error_message == 'Task has missing content'