import numpy as np
from TDD.TDD import Ini_TDD,Clear_TDD,set_index_order
from TDD.TDD_Q import cir_2_tn,add_trace_line,add_inputs,add_outputs
from TDD.TN import Index,Tensor,TensorNetwork
import time
import random
from qiskit import QuantumCircuit
from qiskit import transpile
from qiskit_aer import AerSimulator