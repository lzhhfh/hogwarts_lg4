import random

# 定义fight函数实现游戏逻辑
def fight(enemy_hp,enemy_power):
    my_hp = 1000
    my_power = 200
    # 敌人的血量和攻击力
    print(f"敌人的血量{enemy_hp},攻击力为{enemy_power}")
    # 加入循环，游戏进行多轮
    while True:
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power
        #判断谁的血量小于等于0
        if my_hp <= 0:
            #打印自己的和敌人的剩余血量
            print(f"我的剩余血量为{my_hp}")
            print(f"敌人的剩余血量{enemy_hp}")
            print("我输了")
            break
        elif enemy_hp <= 0:
            print(f"我的剩余血量为{my_hp}")
            print(f"敌人的剩余血量{enemy_hp}")
            print("我赢了")
            break

if __name__ == "__main__":
    # 利用列表推导式生成血量
    hp = [x for x in range(990,1010)]
    print(hp)
    print(type(hp))
    # 让敌人的血量从血量列表中随机挑选一个值
    enemy_hp = random.choice(hp)
    print(enemy_hp)
    #敌人攻击力用randit生成随机整数
    enemy_power = random.randint(190,210)
    print(enemy_hp)
    #调用函数，传入敌人的血量和攻击力
    fight(enemy_hp,enemy_power)