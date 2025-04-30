from semantic_kernel import Kernel, read_skill_from_directory
import os

def initialize_kernel():
    """Initialize and return a Semantic Kernel instance with the 'journal' skill loaded."""
    kernel = Kernel()
    # Determine path to the 'journal' skill directory (relative to this script)
    skill_directory = os.path.join(os.path.dirname(__file__), "skills")
    # Load and import the 'journal' skill into the kernel
    kernel.import_skill(read_skill_from_directory(skill_directory, "journal"), skill_name="journal")
    return kernel
