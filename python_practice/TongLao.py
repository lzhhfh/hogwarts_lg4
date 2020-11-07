# 定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
#
# see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“师弟是我的！”，
# 如果传入“丁春秋”，打印“叛徒！我杀了你”
#
# fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，
# 进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
#
# 定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
# 加入模块化改造
# 希望各位同学在此基础上可以添加自己的“freestyle”哦

class TongLao:
    def __init__(self,my_hp,my_power):
        self.my_hp = my_hp
        self.my_power = my_power

    def see_people(self,name):
        if name == "无崖子":
            print("师弟！！！！")
        elif name == "李秋水":
            print("师弟是我的！")
        elif name == "丁春秋":
            print("叛徒！我杀了你")
        else:
            print(("发射生死符"))

    def fight_zms(self,enemy_hp,enemy_power):
        self.my_power *= 10
        self.my_hp /= 2
        print(f"我的武力增加到{self.my_power}, 血量减低到{self.my_hp}")
        while True:
            my_hp = self.my_hp - enemy_power
            enemy_hp = enemy_hp - self.my_power

            if (self.my_hp > enemy_hp) >= 0:
                # 打印自己的和敌人的剩余血量
                print(f"我的剩余血量为{my_hp}")
                print(f"敌人的剩余血量{enemy_hp}")
                print("我赢了")
                break
            else :
                print(f"我的剩余血量为{my_hp}")
                print(f"敌人的剩余血量{enemy_hp}")
                print("我输了")
                break

if __name__ == "__main__":

    T = TongLao(100,200)
    for i in ["无崖子","李秋水","丁春秋"]:
        T.see_people(i)
    T.fight_zms(5000,50)


class XuZhu(TongLao):
    def __init__(self,my_hp,my_power):
        super(XuZhu,self).__init__(my_hp,my_power)
    def read(self):
        print("罪过罪过")


