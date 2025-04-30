
class Kernel:
    def __init__(self):
        self.skills = {}

    def import_skill(self, skill, skill_name=None):
        self.skills[skill_name or 'default'] = skill
