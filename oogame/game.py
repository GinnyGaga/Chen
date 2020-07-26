# -*- coding: UTF-8 –*-

import requests
from oogame.url import population_url
import json


class Game(object):

    def population_recommend_request(self, type=1, limit=10, offset=0):
        """
        查询某一页的数据
        :param type: 查询类型
        :param limit: 页大小
        :param offset: 偏移量
        :return: 查询结果
        """
        url = population_url
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) \
             Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows \
             WindowsWechat",
            "content-type": "application/json"
        }
        d = {
            "type": type,
            "limit": limit,
        }
        if offset != 0:
            d["offset"] = offset
        res = requests.get(url=url, headers=headers, params=d)
        return res

    def population_recommend_list_one_page(self, type=1, limit=10, offset=0) -> (list, int, bool):
        rsp = self.population_recommend_request(type, limit, offset)
        content = rsp.text
        try:
            content_json = json.loads(content)
            success = content_json["success"]
            data = content_json["data"]
            if success is True:
                return data["data"], data["count"], True
            else:
                print("population_recommend_list failed. rsp: {}".format(content))
                return None, None, False
        except Exception as e:
            print("population_recommend_list failed. err：{}".format(e))
            return None, None, False

    def population_recommend_list_all(self, page_size=10):
        offset = 0
        while (True):
            data_list, count, success = self.population_recommend_list_one_page(limit=page_size, offset=offset)
            if success is not True:
                break
            else:
                print(data_list)
                offset += page_size
                if offset >= count:
                    break

    # def test(self, v):
    #     param1 = "参数1"
    #     if v == 1:
    #         param1 = "哈哈"
    #
    #     return param1, "参数2", "参数3", 1


if __name__ == "__main__":
    # test = Game()
    # test.population_recommend_list(offset=10)
    # tuple1 = Game().test(1)
    # print(tuple1[1])
    # param1, param2, param3, param4 = Game().test(1)
    # print(param2)

    Game().population_recommend_list_all()

