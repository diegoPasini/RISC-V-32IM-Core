TOPLEVEL_LANG = verilog
SIM = verilator
VERILOG_SOURCES = $(PWD)/ALU/rca.sv
TOPLEVEL = rca
MODULE = test_benches.ALU_tests.test_adder

# Verilator flags for VCD generation
EXTRA_ARGS += --trace --trace-structs


# Including the Cocotb Makefile
include $(shell cocotb-config --makefiles)/Makefile.sim