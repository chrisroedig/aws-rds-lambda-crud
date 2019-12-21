from models import Climb

class Climbs():
    def __init__(self, params={}, query_params={}):
        self.params = params
        self.query_params = query_params

    def post(self):
        self.climb = Climb.create(self.params)
        return self.climb.to_dict()
    
    def get(self):
        self.climbs = Climb.all()
        return [ c.to_dict() for c in self.climbs ]   