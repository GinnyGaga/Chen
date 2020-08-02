# class Response:
#     def __init__(self, content):
#         self.data = content
#
#     def get_body(self):
#         return self.data



class User:
    # def query_user_info(self, offset):
    #     user_info_list = [] # 表示返回的用户信息列表
    #     count = n # 表示总用户量
    #     success = True  # 表示是否请求成功
    #     return Response({"user_info_list":user_info_list,
    #                 "count":count,
    #                 "success":success})  # 类的实例化对象
    #
    # def get_xxx(self):
    #     rsp = self.query_user_info(0)
    #     rsp.get_body()

    def query_user_info(self, offset):
        user_info_list = [] # 表示返回的用户信息列表
        count = n # 表示总用户量
        success = True  # 表示是否请求成功
        return {"user_info_list":user_info_list,
                    "count":count,
                    "success":success}

    # def query_user_all(self):
    #     rsp1 = self.query_user_info(offset=0)
    #     size = len(rsp1["user_info_list"])
    #     if size < rsp1["count"]:
    #         rsp2 = self.query_user_info(offset=size)
    #         size2 = len(rsp2["user_info_list"])
    #         if size2 < rsp2["count"]-size:
    #             rsp3 = self.query_user_info(offset=size)
    #             size3 = len(rsp3["user_info_list"])
    #         else:
    #             return rsp2["user_info_list"]
    #     else:
    #         return rsp1["user_info_list"]

    def query_user_all(self):
        all = []
        current_count = 0
        while(True):
            rsp = self.query_user_info(offset=current_count)
            all.extend(rsp["user_info_list"])
            current_count += len(rsp["user_info_list"])
            if current_count >= rsp["count"]:
                break
        return all


    def get_use_from_info(self):
        data = {"ecode":"OK",
                "XXX":"XXX",
                "users":[
                    {"name":"name1"},
                    {"name":"name2"}
                ],
                "total_num":50
                }
        users = data["users"]
        if len(users) == 0:
            return
        user1_info = users[0]
        user1_name = user1_info["name"]

    return response.Response(rsp)

rsp = self.query_user_info()
data = rsp.get_body()



