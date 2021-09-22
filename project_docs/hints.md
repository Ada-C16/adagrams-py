# Hints

Here are some of the terms and concepts for _Adagrams_, what they mean, and how we might represent them as data.

Term | Definition | Representation
---    | ---  | ---
Letter or Tile | A single English capital letter | 1-character string (`"A"`, `"B"`, etc)
Letter Pool | The set of 98 letters (9 `A`s, 2 `B`s, etc) used to play the game | Up to you (see wave 1)
Hand/Letter Bank | A set of 10 tiles that the player can use to construct a word | A list of ten 1-character strings, like `["A", "P", "K", "A", "E", "F", "W", "H", "F", "Q"]`
Word | A word submitted by the user | `"FISH"`, `"DEVELOPERS"`, `"ZZHYT"`, `"A"`
Drawing | Constructing a new hand using letters from the pool | function
