import ctypes
import os
import numpy as np

# Load the C library
lib_path = os.path.join(os.path.dirname(__file__), '..', 'C', 'teacher_model.so')
teacher_lib = ctypes.CDLL(lib_path)

# Define argument and return types for C functions
teacher_lib.init_teacher.argtypes = [ctypes.c_void_p, ctypes.c_int]
teacher_lib.update_teacher_knowledge.argtypes = [ctypes.c_void_p, ctypes.c_int]
teacher_lib.get_teacher_knowledge.argtypes = [ctypes.c_void_p]
teacher_lib.get_teacher_knowledge.restype = ctypes.POINTER(ctypes.c_double)
teacher_lib.suggest_resource.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
teacher_lib.suggest_resource.restype = ctypes.c_int

class TeacherModel:
    def __init__(self, n_states):
        self.n_states = n_states
        self.teacher = ctypes.c_void_p()
        teacher_lib.init_teacher(ctypes.byref(self.teacher), n_states)

    def update_knowledge(self, state):
        teacher_lib.update_teacher_knowledge(self.teacher, state)

    def get_knowledge(self):
        knowledge_ptr = teacher_lib.get_teacher_knowledge(self.teacher)
        return np.ctypeslib.as_array(knowledge_ptr, shape=(self.n_states,))

    def suggest_resource(self, student_beliefs):
        beliefs_array = (ctypes.c_double * self.n_states)(*student_beliefs)
        return teacher_lib.suggest_resource(self.teacher, beliefs_array)