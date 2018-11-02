Installation:

Before do: pip install pyyaml
Otherwise it wouldn't work!

pip install YamlDB

How to use?

at first we need to import YamlDB, duh

after that do database = database(file_path)

e.g.

	import YamlDB
	
	database = database("data.yml")
	
Now, to input and write stuff to the database file we have 2 options
Regular dump or in the code it will be database.dump(data)
and the safe dump or in the code it will be database.safe_dump(data)

Now what both of them do is,
Dump just writes stuff into the file but deleting stuff that's already written in-it
Safe Dump will write stuff to the file but without deleting already written stuff!

Other commands (Useful at most):

database.devs() -- Will display the list of developers that worked on the project
database.current_file() -- Will display current file name, path and size (In bytes)
