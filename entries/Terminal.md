# Terminal

-----

## .bashrc
This is a file that basically configures your "profile" when using the terminal. Of course, more modern macs don't use bash, and instead use Z shell, or `zsh`, and their file is called `.zshrc`. Usually these files are used to save commands you may want to use a lot. You can define your own functions and stuff here, preventing you from having the type the same stuff again, or remembering exactly what commands to use for rarely-used but complicated program scripts.

Where does it live?
Your home user directory, but it is hidden, so it can only be seen using `ls -a`.

-----

## PATH variable
This variable is stored in `/etc/paths`.

-----

## /bin vs. /usr/bin
These are both folders where executables are stored. `/bin` seems to be the more 'sacred' one, where the system itself saves things, and `/usr/bin` is where the less essential stuff lives.

-----

## Relative vs. top-level-directory notation
The "cd" command will take you to your user directory, which is not the highest-level directory.

A filepath that begins with `/` signifies that the path is starting from the HIGHEST level directory. On a mac, it's a couple steps up from the user directory.

A filepath that begins with `./` is a relative filepath, and starts from whatever directory you are in.

It's a very small difference with big implications.