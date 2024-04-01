# A-Tensor-Network-Based-Decision-Diagram
See https://github.com/Veriqc/TDD for where the TDD package came from.

## My Tests
The benchmark_plots.ipynb notebook contains varuous plots of the results form the tests done in the benchmarking.ipynb notebook. This includes testing of runtime and memory consumption for the circuits in the benchmarks folder.

From https://github.com/Veriqc/TDD/README.md
## Overview
Decision diagrams have been used in the simulation and equivalence checking of quantum circuits. Inspired by the efficiency and flexibility of Tensor Networks. A tensor network-based decision diagram has been proposed at https://dl.acm.org/doi/10.1145/3514355. This repository gives a proof-of-concept implementation of the Tensor Decision Diagram(TDD) using Python3. 
Part of the benchmarks is coming from https://github.com/iic-jku/qmap/tree/master/examples. For an efficient C++ version of TDD, please see https://github.com/Veriqc/TDD_C. A Local Invertible Map version of TDD (LIMTDD) can be seen at https://github.com/Veriqc/LimTDD/.
@@ -13,91 +19,4 @@ There are three components of our package: TDD, TN, TDD_Q. TDD include the basic
    from TDD.TN import Index,Tensor,TensorNetwork
    from TDD.TDD_Q import cir_2_tn,get_real_qubit_num,add_trace_line,add_inputs,add_outputs
