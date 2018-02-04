# Coding Style Guide

## Documentation

Documentation strings ("docstrings") are an integral part of the Python language. They need to be in the following places:

* At the top of each file describing the purpose of the module.
* Below each class definition describing the purpose of the class.
* Below each function definition describing the purpose of the function.

Docstrings describe **what** is being done, **not** how.

## Comments

 Comments should describe **how** a section of code is accomplishing something.

## Global Variables

Global variables should never be used.(Except for **CONSTANTS**) Avoiding their use is good programming practice.

## Indentation

Each indent level should be indented by `spaces:4`

## Names

All variable, function, class, and method names must be at least 3 characters. The first character of a name should follow these conventions:

* Variable names should always start with a lower case letter. (Except for variables that represent constants, which should use all upper case letters.)
* Function and method names should always start with a lower case letter.
* Class names should always start with an upper case letter.

Further, we will follow the common Python convention that variable, function, and method names should not have any capital letters in them. You can separate words in a name with an underscore character, as follows: `some_variable_name`. Similarly, class names should not contain underscores, and instead use capitalization to separate words, as follows: `𝚂𝚘𝚖𝚎𝙲𝚕𝚊𝚜𝚜𝙽𝚊𝚖𝚎`.

## Class and Instance fields

Class and instance fields should never be accessed directly from outside the class. You should therefore always start your field names with an underscore. Even if you don't, you still should not access them from outside of the class.

You will often see public fields in Python programs (and in programs of other languages). This is not a good habit to get into. Instead, all fields should always be private. If there is good reason to make the data in the field accessible outside the class, you should create a method to do so. By convention in other languages, these methods are usually named `𝚐𝚎𝚝_𝚏𝚒𝚎𝚕𝚍`, where `𝚏𝚒𝚎𝚕𝚍` is the name of the field. You should follow this convention.

You should avoid the use of class fields, which are declared in the scope of the class itself and are common to all instances of the class. Instead, you should use instance fields (defined as attributes of `s𝚎𝚕𝚏`). These will be unique to each instance of the class.

## Scope

You should not use names that knowingly duplicate other names in an outer scope. This would make the name in the outer scope impossible to access. In particular, you should never use names that are the same as existing Python built-in functions. For example, if you were to name one of your local variables `𝚖𝚊𝚡` inside of a function, you would then not be able to call `𝚖𝚊𝚡()` from within that function.

## Arguments and local variables

While there is not necessarily a maximum number of arguments a function can take or a maximum number of local variables you can have, too many arguments or variables lead to unnecessarily complex and unreadable programs. Pylint will enforce maximum numbers of arguments, variables, methods, etc. If you run into limits that Pylint complains about, you should restructure your program to break it into smaller pieces. This will result in more readable and maintainable code.

Further, you should not have function arguments or local variables declared that are never used, except in rare circumstances. Sometimes, you do need to have a variable that you never use. A common case is in a loop that just needs to execute a certain number of times:

```python
for num in range(42):
    #Do something 42 times
```

In this case, you should name the variable with the `𝚍𝚞𝚖𝚖𝚢_` prefix. This indicates clearly to you, others, and Pylint that the variable is intentionally unused.

```python
for dummy_num in range(42):
    #do something 42 times
```
