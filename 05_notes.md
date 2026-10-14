# VIM PRACTICE 5: Prose and Markdown

Exercises:

1. Move by word (w, b, e), by sentence ( ) and ( ( ), and by paragraph ( } and { ).
2. Fix the misspelled words below. Turn on spell check with :set spell, then use ]s and z=.
3. Reflow the long paragraph with gqap.
4. Turn the unordered list into a numbered list using visual block mode and :s.
5. Capitalize the first letter of every heading with ~ or gUl.
6. Uppercase a whole line with gUU and lowercase it with guu.
7. Use yap and P to duplicate a paragraph, then dap to delete one.
8. Use :g/^$/d to remove blank lines, then undo with u.
9. Use * on a word to find every other occurrence.
10. Use ct. to change text up to the next period.

## the quick start guide

Vim is a modal editor, wich means that the same keys do different things depending on the mode you are in. Normal mode is for moving around and issuing commands, insert mode is for typing text, visual mode is for selecting text, and command-line mode is for things like saving, searching, and substituting. New users offten get stuck because they try to type in normal mode, but the trick is to press i first. Once you internalize that idea, the editor starts to feel less like an obstacle and more like a language you are slowly learning to speak. Every command is a verb, a noun, or both, and you combine them to say exactly what you want the editor to do, for example delete inner word, or change around paren.

## things to remember

- Press Esc to return to normal mode
- Press i to insert before the cursor
- Press a to append after the cursor
- Press o to open a new line below
- Press dd to delete a line
- Press yy to yank a line
- Press p to paste after the cursor
- Press u to undo
- Press . to repeat the last change
- Press :wq to save and quit

## a seperate paragraph to rearrange

This paragraph should come before the quick start guide. Move it there with dap and then P at the top of the file. Afterwards, practice jumping back and forth between the two locations with Ctrl-o and Ctrl-i, or set a mark with ma and return to it with the backtick followed by a.

## tiny table

| key | action          |
|-----|-----------------|
| h   | left            |
| j   | down            |
| k   | up              |
| l   | right           |

Practice editing a column with Ctrl-v, then j several times, then c to change all of them at once.
