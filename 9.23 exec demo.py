# a = 13
# exec('b = a + 1')
# print(b)

def test4():
    a = 13
    loc = {'a': a}
    glb = {}

    exec('b = a + 1', glb, loc)  # 注意 glb和loc的顺序， 如果反了会报错。 因为exec的第二个参数是global， 第三个参数是local
    b = loc['b']

    print(b)


test4()
