import importlib.util
import os

def read_skill_from_directory(path, name=None):
    # Build full path to the skill's __init__.py
    skill_folder = os.path.join(path, name or "journal")
    init_file = os.path.join(skill_folder, "__init__.py")

    # Dynamically load the skill module
    spec = importlib.util.spec_from_file_location(name or "journal", init_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Return the actual JournalSkill object
    return module.JournalSkill()
