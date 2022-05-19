# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    def __init__(self):
        self.direction = None
        self.field = None
        self.x = None
        self.y = None
        self.speed = 1
        self.state = None

    def _get_speed(self):
        if self.state is None:
            return self.speed
        elif self.state == 'fly':
            return self.speed * 1.2
        elif self.state == 'crawl':
            return self.speed * 0.5
        else:
            raise ValueError('Неизвестное состояние')

    def move_unit(self):
        speed = self._get_speed
        if self.direction == 'UP':
            self.field.set_unit(x=self.x, y=self.y + speed, unit=self)
        elif self.direction == 'DOWN':
            self.field.set_unit(x=self.x, y=self.y - speed, unit=self)
        elif self.direction == 'LEFT':
            self.field.set_unit(x=self.x - speed, y=self.y, unit=self)
        elif self.direction == 'RIGTH':
            self.field.set_unit(x=self.x + speed, y=self.y, unit=self)
        else:
            raise ValueError('Неизвестное направление')


#     ...
