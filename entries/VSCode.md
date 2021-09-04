### Excluding Files
In Unity, it can be super annoying to have a `.meta` file for every normal `cs` file you have.  Unity needs them, but as far as I know, I don't. VS code allows you to hide certain file types, and there are some it already hides by default, like `.git` files. First, open your settings with the hotkey `Command + ,` on mac. That's Command and the comma key. Then search `exclude` in the search bar, which will show a result with the header `files:exclude`. There will be a list of excluded files. In order to exclude `.meta` files for example, add this line to that list:
`**/*.meta`. That's it!

### The hella nifty 'Source Control' view
On the left, where the icons for plugin-manage and file-viewer are, there is an icon with three circles connect by lines, depicting a branch branching off of another one. This is the source control view. It does some cool things.

1) Allows you to commit directly with the textbox at the top. Simply type in your commit message and then press the checkmark above, which is easier on the fingers than writing "commit -m """ I think. 
2) This one is even better - See all the changes your currently tracked files have in comparison to the last commit. Tired of command+z-ing backwards, then command+shift+z-ing forwards until you don't know where you "are" anymore? I think this is the solution. If you press on one of the changes, it will open up the "working tree view" which is a double-paned view of your current code and where it diff(er)s from that particular edit. You can press the separate "working tree" button again (it's on the top right and sort of looks like a document being flipped around) to go back to normal view and get back to coding.
3) You can also press `command + enter` for a hella swift commit message
  
### Working Tree View
You don't need to access this through the source control tree. You can also just press the working tree view icon and it will simply show you any changes between your current code and the last commit. Simple.