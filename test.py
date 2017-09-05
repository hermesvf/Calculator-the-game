from solve import addOptionNode, evaluation

def test_sum():
    ops = []
    input_ops = ['+1','+256']
    for i in input_ops:
        addOptionNode(ops,i)
    assert evaluation(0,ops) == 257

def test_subs():
    ops = []
    input_ops = ['-1','-256']
    for i in input_ops:
        addOptionNode(ops,i)
    assert evaluation(0,ops) == -257

def test_div():
    ops = []
    input_ops = ['/-1','/5']
    for i in input_ops:
        addOptionNode(ops,i)
    assert evaluation(10,ops) == -2

def test_mult():
    ops = []
    input_ops = ['*1','*256']
    for i in input_ops:
        addOptionNode(ops,i)
    assert evaluation(1,ops) == 256

def test_append():
    ops = []
    input_ops = ['A1','A5','A6']
    for i in input_ops:
        addOptionNode(ops,i)
    assert evaluation(0,ops) == 156

def test_alter_sign():
    ops = []
    input_ops = ['S']
    for i in input_ops:
        addOptionNode(ops,i)
    assert evaluation(1,ops) == -1
    assert evaluation(0,ops) == 0
    assert evaluation(1,ops*2) == 1
    assert evaluation(1,ops*33) == -1
    assert evaluation(33,ops) == -33

def test_exchange():
    ops = []
    input_ops = ['X1:3']
    for i in input_ops:
        addOptionNode(ops,i)
    assert evaluation(1,ops) == 3

    ops = []
    input_ops = ['X12:34']
    for i in input_ops:
        addOptionNode(ops,i)
    assert evaluation(212,ops) == 234

def test_shift_left():
    ops = []
    input_ops = ['L']
    for i in input_ops:
        addOptionNode(ops,i)
    assert evaluation(123,ops) == 12
    assert evaluation(123,ops*2) == 1
    assert evaluation(123,ops*3) == 0
    assert evaluation(123,ops*5) == 0
    assert evaluation(0,ops*5) == 0
