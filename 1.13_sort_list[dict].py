from operator import itemgetter

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

new = sorted(rows, key=lambda x: x.get('fname'))
print new

new = sorted(rows, key=lambda x: (x.get('lname'), x.get('fname')))
print new

new = sorted(rows, key=itemgetter('fname'))
print new
new = sorted(rows, key=itemgetter('lname', 'fname'))
print new
