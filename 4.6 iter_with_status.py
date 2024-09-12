from collections import deque


class LineHistory:
    """带有历史状态的生成器"""
    def __init__(self, lines, hist_len=3):
        self.lines = lines
        self.history = deque(maxlen=hist_len)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


file_lines = ['hello word', 'this is test', 'python file test', 'end of file']
lines = LineHistory(file_lines)

for line in lines:
    if 'python' in line:
        for lineno, line_info in lines.history:
            print(f'{lineno}:{line_info}')

lines = LineHistory(file_lines)
it = iter(lines)
print(next(it))
print(next(it))