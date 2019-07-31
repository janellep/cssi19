story = """One for {0}
Two for {1}
Three for a girl
And four for a boy
{2} for silver
six for gold
Seven for a secret
Never to be told
Eight for a {3} over the sea
{4} for a lover as true as can be"""

adjective = raw_input("Enter an adjective: ")
noun1 = raw_input("Enter an noun: ")
number1 = raw_input("Enter a number as a word: ")
noun2 = raw_input("Enter a second noun: ")
number2 = raw_input("Enter a number as a word: ")

#display the story using string interpol
print story.format(adjective,noun1,number1,noun2,number2)
