# emoji_text
Generates emoji text for use with slack emoji

Words are defined with letters in 3x5 grids consisting of a foreground and background string. When used with slack emoji codes - eg colon b colon - these can be used to generate pasteable emoji-based words.

>>> print_emoji_word("hello", ":pray:", ":b:")

:pray::pray::pray::pray::pray::pray::pray::pray::pray::pray::pray::pray::pray::pray::pray::pray::pray::pray::pray::pray::pray:

:pray::b::pray::pray::pray::b::b::b::pray::b::pray::pray::pray::b::pray::pray::pray::b::b::b::pray:

:pray::b::pray::pray::pray::b::pray::pray::pray::b::pray::pray::pray::b::pray::pray::pray::b::pray::b::pray:

:pray::b::b::b::pray::b::b::b::pray::b::pray::pray::pray::b::pray::pray::pray::b::pray::b::pray:

:pray::b::pray::b::pray::b::pray::pray::pray::b::pray::pray::pray::b::pray::pray::pray::b::pray::b::pray:

:pray::b::pray::b::pray::b::b::b::pray::b::b::b::pray::b::b::b::pray::b::b::b::pray:

:pray::pray::pray::pray::pray::pray::pray::pray::pray::pray::pray::pray::pray::pray::pray::pray::pray::pray::pray::pray::pray:

Letters are parsed from a the letters.yaml file with each letter consisting of 5 numbers, the binary representation of this being the 3x5 foreground/background definition. 

eg e : 74747

1  1  1

1  0  0

1  1  1

1  0  0

1  1  1
