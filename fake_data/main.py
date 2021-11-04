import json

from model import user, user_address, test_join, ginny


def test1():
    res = user.get_by_id(1)
    print(res.id, res.name, res.phone)


def test2():
    array = [user.User(name='lmaber', phone='13005497255'),
             user.User(name='xxxx', phone='123456789')]
    res = user.batch_create(array)
    print(res)


def test3():
    array = []

    for i in range(1, 1101):  # 左闭右开，插入1100条数据0
        array.append(user.User(name='测试用户%d' % i, phone='1234567890%d' % i))  # id 自动递增，把数据插入列表中
        if i % 200 == 0:  # 每200条数据拼装成1条SQL语句插入后，清除列表中已经插入的数据
            print(i)
            user.batch_create(array)
            array.clear()

    if len(array) > 0:
        print(len(array))
        user.batch_create(array)


def test4():
    res = user.update_by_id(1, "更2311")
    print(res)
    # res = user.update_by_id(2, "更新122", "123114")
    # print(res)
    # res = user.update_by_id(5, phone="3456ee")
    # print(res)
    # res = user.update_by_id(4)
    # print(res)


def test5():
    res = user.get_by_name("更新11")
    for u in res:
        print(u.id, u.name, u.phone)


def test6():
    res = user_address.get_by_id(1)
    print(res.id, res.name, res.address)


# 2表联查
def test7():
    res = test_join.get_user_addr()
    print(res)
    for v in res:
        u = v["User"]
        addr = v["UserAddress"]
        print(u.id, u.name, addr.address)


# 3表联查
def test8():
    res = test_join.list_user_addr_sex()
    print(res)  # 返回值为列表，即返回列表为3个元组，每个元组含有3张表。
    for (user, addr, sex) in res:
        print(user.name, addr.address, sex.sex)
    # for v in res:
    #     user, addr, sex = v["User"], v["UserAddress"], v["UserSex"]
    #     print(user.name, addr.address, sex.sex)


# 3表联查带条件
def test9():
    res = test_join.get_user_addr_sex_by_addr("NN")
    print(res)
    for (user, addr, sex) in res:
        # user, addr, sex = v["User"], v["UserAddress"], v["UserSex"]
        print(user.name, addr.address, sex.sex)


# 3表联查带条件
def test10():
    # 法1：报错的话，打断点，看data和fileds字段
    # user, addr, sex = test_join.get_user_addr_sex()
    # print(user.name, addr.address, sex.sex)
    # 法2：
    # res = test_join.get_user_addr_sex()
    # print(res)
    # print(res.User.name, res.UserAddress.address, res.UserSex.sex)
    # 法3：
    res = test_join.get_user_addr_sex()
    print(res)
    print(res[0].name, res[1].address, res[2].sex)


# 查找ginny表记录中不同的项
# 1、把data的key value值单独表示，字典和id\type放在一个class绑定，初始化；
# 2、判断ginny表是否为空值或者字符长度为0，则返回无
# 3、赋值
# 2、遍历查找data1是否在data2里，如不在，取出；
# 3、遍历查找data2是否在data1里，如不在，取出；
# 打印全部取出的全部数据

def test12():
    class TmpRecord:
        record = None
        data_k = ""
        data_v = ""

        def __init__(self, record, data_k, data_v):
            self.record = record  # record表示表中每一行的字段
            self.data_k = data_k  # data_k表示表中每一行字段里data字段的key值。
            self.data_v = data_v

    try:
        res = ginny.Ginny().get_list()  # 调试发现res为list，res[0]为第一行数据，res[1]为第二行数据
        if res is None or len(res) == 0:
            return

        record1, record2 = res[0], res[1]
        dict1 = json.loads(record1.data)  # 把json string转换成json对象
        dict2 = json.loads(record2.data)
        if dict1 is None or dict2 is None:
            return

        out_put_list = []
        for k, v in dict1.items():
            if k not in dict2:
                out_put_list.append(TmpRecord(record1, k, v))
        for k, v in dict2.items():
            if k not in dict1:
                out_put_list.append(TmpRecord(record2, k, v))

        for data in out_put_list:
            # 遍历列表，每个data代表输出的一行数据结果，结果包含record和record里的data字典kv(kv已经用data_k和data_v表示)
            print("id: %d, type: %d, data_k: %s, data_v: %s" %
                  (data.record.id, data.record.type, data.data_k, data.data_v))

    except Exception as e:
        print(e)


if __name__ == '__main__':
    # test1()
    # test2()
    # test3()
    # test4()
    # test7()
    # test8()
    # test9()
    # test10()
    # test11()
    test12()
