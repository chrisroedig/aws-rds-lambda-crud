import database
from orator import Model

class Climb(Model):
    __fillable__ = [                                                \
        'location_type', 'route_ref', 'route_color', 'rope_style',  \
        'yds_grade_posted', 'yds_grade_estimated',                  \
        'completed', 'falls', 'takes', 'notes',                     \
        'notes'                                                     \
    ]
    