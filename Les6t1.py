#Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке
# (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить
# соответствующее сообщение и завершать скрипт.

class TrafficLight:

    _color = ''

    #color = ['red', 'yellow', 'green']

    def running(self):
        count = 0
        for count in range(13):
            if count < 7:
                _color = 'red'
                print(_color)
                count = +1
            elif  7 <= count < 9:
                _color = 'yellow'
                print(_color)
                count = +1
            elif 9 <= count < 13:
                _color = 'green'
                print(_color)
                count = +1
            else: _color = 'red'
            print(_color)


light_a = TrafficLight()
light_a.running()


