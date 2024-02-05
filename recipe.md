# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem - User stories

As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries


## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```
+------------------------------+
|                              |
| class Diary():               |
|     __init__ args: none      |
|     state:                   |
|         contents {dict}      |
|         todo_list {dict}     |
|     methods:                 |
|         add_diary_entry      |
|         add_todo             |
|         read_entry_by_date   |
|         read_all_entries     |
|         selective_read_entry |
|         mobile_numbers       |
|         read_todo_list       |
|         complete_todo        |
|         clear_todo_list      |
|                              |
+------------------------------+

+------------------------------+
|                              |
| class DiaryEntry():          |
|     args:                    |
|         date, contents       |
|     state:                   |
|         date (date obj)      |
|         contents (str)       |
|                              |
+------------------------------+

+------------------------------+
| class ToDo()                 |
|     parameters:              |
|         task (str)           |
|         complete (bool)      |
|                              |
+------------------------------+
```

```python

class DiaryEntry():

    def __init__(self, contents):
        # Create a new diary entry with the
        # supplied content and give it a date
        self.date = datetime.date.today()
        self.contents = contents


class ToDo():

    def __init__(self, task):
        # Create a new todo task with the supplied
        # task info and set its completion to false
        self.task = task
        self.complete = False


class Diary():

    def __init__(self):
        # Store the diary entries and todo list
        # as dictionaries
        self.contents = {}
        self.todo_list = {}

    def add_diary_entry(self, entry):
        new_entry = DiaryEntry('contents')
        # Add a new diary entry
        pass

    def add_todo(self, entry):
        # Add a new todo task
        pass

    def read_entry_by_date(self, date):
        # Look up and return diary entries for the
        # supplied date
        pass

    def read_all_entries(self):
        # Return all entries
        pass

    def selective_read_entry(self, wpm, mins):
        # Return an appropriate entry based on the user's
        # reading speed and the amount of time they have
        pass
    
    def mobile_numbers(self)
        # Return a list of all the mobile numbers in
        # all diary entries
        pass

    def read_todo_list(self)
        # Return a list of all todo list tasks
        pass
    
    def complete_todo(self, entry)
        # Mark a todo list task as complete
        pass

    def clear_todo_list(self):
        # Remove all completed todo list tasks from the list
        pass


```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python

def test_diary_read_all_entries():
    result = Diary.read_all_entries() =
    assert result == ['1: text', '2: text' etc.]

def test_read_entry_by_date():
    result = Diary.read_entry_by_date('01-01-2024')
    assert result == ['1: text']

def test_selective_read_entry(self, wpm, mins):
    assert result = [appropriate entry]
    
def test_mobile_numbers(self)
    assert result = [0123456789, 1234567890, 2345678901]
    
def test_complete_todo()
    Diary.complete_todo(uncompletedtask3)
    result = Diary.read_todo_list()
    assert result == [uncompletedtask1, uncompletedtask2, completedtask3]

def test_clear_todo_list():
    Diary.clear_todo_list()
    result = Diary.read_todo_list()
    assert result == [uncompletedtask1, uncompletedtask2]

```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```
Tests for diary entry - add empty entry, add 'None' entry
Tests for to do list - add empty entry, add 'None' entry
Tests for diary - add empty diary entry, add empty to do list

```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._