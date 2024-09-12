from tempfile import TemporaryFile

with TemporaryFile('w+t') as f:
    # Read/write to the file
    f.write('Hello World')
    f.write('Testing')

    # Seek back to beginning and read the data
    f.seek(0)
    data = f.read()
    print(data)

# Temporary files are destroyed as soon as they are closed (including when they are garbage collected).
