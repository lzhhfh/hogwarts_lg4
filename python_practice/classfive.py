#定义手机类
class Cellphone:
    #定义属性：手机颜色、品牌、价格、操作系统
    def __init__(self,color,brand,price,operating_system):
        self.color = color
        self.brand = brand
        self.price = price
        self.operating_system = operating_system
        print(f"手机颜色是{color},品牌是{brand},操作系统是{operating_system},价格为{price}")

my_celllphone = Cellphone('balck','huawei',3500,'android')

#定义电脑类
class Computer:
    #定义属性：品牌、配置、系统
    def __init__(self,brand,price,operating_system):
        self.brand = brand
        self.price = price
        self.operating_system = operating_system
        print(f"我的电脑品牌是{brand},价格是{operating_system},操作系统为{price}")

my_computer = Computer('lenovo','win10',3500,)

#定义洗衣机类
class Washingmachine:
    #定义洗衣机属性：品牌、洗衣时间、电量
    def __init__(self,brand,washtime,valume):
        self.brand = brand
        self.washtime = washtime
        self.valume = valume
        print(f"洗衣机品牌是{brand},洗衣时长{washtime}分钟,一次耗电{valume}度")

my_Washingmachine = Washingmachine('haier','20',1,)


class Cup:
    #定义水杯属性：容积、颜色、材质
    def __init__(self,volume,color,texture):
        self.volume = volume
        self.color = color
        self.texture = texture
        print(f"水杯容积是{volume}毫升,颜色是{color},材质是{texture}")

my_Cup = Cup('500','白色','陶瓷',)

class Light:
    #定义灯的颜色、材质、耗电量
    def __init__(self, color, texture, volume):
        self.volume = volume
        self.color = color
        self.texture = texture
        print(f"灯的颜色是{color},材质是{texture},开灯耗电量{volume}度")

mylight = Light('白色','塑料',1)




