# Writing Notes

Notes are simple text files with some extra flavor, in the shape of Markdown syntax and support for extra properties (see [[foam-note-properties]]).

## Foam Syntax

Foam uses standard Markdown, with a few added twists:

- the title of a note (e.g. in the [[foam-graph-visualization]]) is given by precedence based on:
  - the `title` property (see [[foam-note-properties]])
  - the first `# heading 1` of the file
  - the file name
