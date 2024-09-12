import textwrap
text = """
Failure is probably the fortification in your pole.
It is like a peek your wallet as the thief,
when you are thinking how to spend several hard-won lepta,
when you are wondering whether new money, it has laid background.
Because of you, then at the heart of the most lax,
alert, and most low awareness, and left it godsend failed.
"""

print(textwrap.fill(text, width=70))  # width指定列宽

print(textwrap.fill(text, width=40, initial_indent='  '))  # initial_indent指定首行缩进
print(textwrap.fill(text, width=40, subsequent_indent='**'))  # subsequent_indent指定其他行的缩进
