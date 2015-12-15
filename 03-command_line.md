# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > 1. `rm -v` removes files and lists files that have been removed
2. `find` finds files that include the string you specify; formatted like `find DIR -name SEARCHTERM -print` 
3. `man` looks up documentation for a given command; use `/` to search
4. `apropos` looks up commands containing a given keyword
5. `ls -lh` lists files in a directory in detailed view, with well-formatted sizes
6. `touch` makes a new empty file
7. `mv` move file; can also be used to rename a file by passing new file name
8. `grep` searches for given strings within files; use `-i` to ignore case
9. `cat > FILENAME.txt` prompts you for text and then writes that text to a file
10. `head` and `tail` used to view only the beginning or end of a file; use `head -n NUMBEROFLINES FILENAME.txt`

>> Other useful commands:
* `ctrl + C` to exit out of a command
* `.` to reference current directory
* `~` to reference home directory
* `tab` to autocomplete 
* `up arrow` to repeat previous lines

---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

> > `ls` lists the files in the current working directory (simple view). `ls -a` lists files including hidden files. `ls -l` lists files with details. `ls -lh` lists files with details and shows file sizes in a 'human readable' format, i.e. with B, K, etc. for bytes, kilobytes, etc. One can use `ls -la` to list all files including hidden files in detailed view and `ls -lah` to do the same, with the addition of reformatting file sizes.

---


---

What does `xargs` do? Give an example of how to use it.

> > `xargs` takes one or more arguments and then executes an action on them. For example, you can use `xargs` to find all files in a given directory that match a given naming parameter and then delete them -- `find . -name '*.txt' | xargs rm -v`.

---

