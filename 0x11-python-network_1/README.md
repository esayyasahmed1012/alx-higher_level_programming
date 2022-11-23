
You have a captain's log due before 2022-10-23 (in 1 day)! Log it now!
0x11. Python - Network #1
Python
Scripting
Back-end
API
 By: Guillaume, CTO at Holberton School
 Weight: 1
 Project will start Oct 21, 2022 6:00 AM, must end by Oct 22, 2022 6:00 AM
 was released at Oct 21, 2022 12:00 PM
 An auto review will be launched at the deadline
Resources
Read or watch:

HOWTO Fetch Internet Resources Using urllib Package
Quickstart with Requests package
Requests package
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
How to fetch internet resources with the Python package urllib
How to decode urllib body response
How to use the Python package requests #requestsiswaysimplerthanurllib
How to make HTTP GET request
How to make HTTP POST/PUT/etc. request
How to fetch JSON resources
How to manipulate data from an external service
Copyright - Plagiarism
You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
You are not allowed to publish any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.
Requirements
General
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file at the root of the repo, containing a description of the repository
A README.md file, at the root of the folder of this project, is mandatory
Your code should use the pycodestyle (version 2.8.*)
All your files must be executable
The length of your files will be tested using wc
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
You must use get to access to dictionary value by key (it won’t throw an exception if the key doesn’t exist in the dictionary)
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
Your code should not be executed when imported (by using if __name__ == "__main__":)
Tasks
0. What's my status? #0
mandatory
Write a Python script that fetches https://alx-intranet.hbtn.io/status

You must use the package urllib
You are not allowed to import any packages other than urllib
The body of the response must be displayed like the following example (tabulation before -)
You must use a with statement
guillaume@ubuntu:~/0x11$ ./0-hbtn_status.py | cat -e
Body response:$
    - type: <class 'bytes'>$
    - content: b'OK'$
    - utf8 content: OK$
guillaume@ubuntu:~/0x11$ 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x11-python-network_1
File: 0-hbtn_status.py
   
1. Response header value #0
mandatory
