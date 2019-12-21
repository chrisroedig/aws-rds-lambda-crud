import database
from orator import Model, mutator
import re

class Climb(Model):
    __fillable__ = [                                                \
        'location_type', 'route_ref', 'route_color', 'rope_style',  \
        'yds_grade_posted', 'yds_grade_estimated',                  \
        'completed', 'falls', 'takes', 'notes',                     \
        'notes', 'created_at'                                                     \
    ]
    
    __yds_modifier_value = {
        '-' : -0.25,
        '+' : +0.25,
        ''  : 0.0
    }

    @mutator
    def yds_grade_posted(self, value):
        self.set_raw_attribute('yds_grade_posted', value)
        yds_num = self.compute_yds_numerical(value)
        self.yds_numerical_posted = yds_num
    
    def compute_yds_numerical(self, val):
        match = re.match('\d.(\d{1,2})(\D?)',val)
        if match is None:
            return 
        grade_int = match[1]
        grade_modifier = match[2]
        return float(grade_int) + self.__yds_modifier_value.get(grade_modifier, 0.0)