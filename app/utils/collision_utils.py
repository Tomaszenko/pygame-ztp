class CollisionUtils:
    @staticmethod
    def calculate_cut(a1, b1, a2, b2):
        begin = max(a1, a2)
        end = min(b1, b2)
        return max(0, end - begin)

    @staticmethod
    def check_collision(object1, object2):
        object1_width, object1_height = object1.get_size()
        object2_width, object2_height = object2.get_size()
        a = CollisionUtils.calculate_cut(object1.x, object1.x + object1_width, object2.x, object2.x + object2_width)
        b = CollisionUtils.calculate_cut(object1.y - object1_height, object1.y, object2.y - object2_height, object2.y)
        area = a * b
        if area != 0:
            return True
        else:
            return False
