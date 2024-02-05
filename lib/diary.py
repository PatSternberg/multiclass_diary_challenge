from lib.diary_entry import DiaryEntry


class Diary():

    def __init__(self):
        # Store the diary entries and todo list
        # as dictionaries
        self.contents = {}
        self.contacts = []
        self.diary_number = 0
        self.todo_list = {}

    def add_diary_entry(self, entry):
        # Add a new diary entry
        new_entry = DiaryEntry(entry)
        self.contents[self.diary_number + 1] = new_entry.contents
        self.diary_number += 1
        new_mobile = ''
        for char in entry:
            if char.isdigit():
                new_mobile = new_mobile + char
                if len(new_mobile) == 11:
                    self.contacts.append(new_mobile)
                    new_mobile = ''

    def add_todo(self, task):
        # Add a new todo task
        self.todo_list[task] = False

    def read_entry_by_number(self, number):
        # Look up and return diary entries for the
        # supplied value
        return self.contents[number]

    def read_all_entries(self):
        # Return all entries
        return self.contents

    def selective_read_entry(self, wpm, mins):
        # Return an appropriate entry based on the user's
        # reading speed and the amount of time they have
        total_words = wpm * mins
        result = ''
        for entry in self.contents:
            if len(self.contents[entry]) <= total_words and len(self.contents[entry]) > len(result):
                result = self.contents[entry]
        return result
    
    def mobile_numbers(self):
        # Return a list of all the mobile numbers in
        # all diary entries
        return self.contacts

    def read_todo_list(self):
        # Return a list of all todo list tasks
        return self.todo_list
    
    def complete_todo(self, task):
        # Mark a todo list task as complete
        self.todo_list[task] = True

    def clear_todo_list(self):
        # Remove all completed todo list tasks from the list
        self.todo_list = {k : v for k, v in self.todo_list.items() if v == False}
                
