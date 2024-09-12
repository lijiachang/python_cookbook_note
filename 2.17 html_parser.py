import html
s = "Elements are written as '<tar>text</tag>'"

print(html.escape(s))
print(html.escape(s, quote=False))

