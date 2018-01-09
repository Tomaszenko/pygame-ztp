from app.models import MutantObject


class BiggerObject(MutantObject):
    def __init__(self, base_object, how_many_bigger):
        super().__init__(base_object)
        self._how_many_bigger = how_many_bigger

    def get_size(self):
        return self.width * self._how_many_bigger,\
               self.height * self._how_many_bigger

    def get_name(self):
        return super().get_name()
