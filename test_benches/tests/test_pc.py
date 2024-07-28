import cocotb
from cocotb.triggers import Timer
from cocotb.clock import Clock

@cocotb.test()
async def test_pc_reset(dut):
    """Test Program Counter Reset Functionality"""
    clock = Clock(dut.clk, 1, units="ns") 
    cocotb.fork(clock.start())  

    dut.reset.value = 1
    await Timer(1, units='ns')
    assert dut.pc_out.value == 0, f"PC did not reset properly, expected 0 but got {dut.pc_out.value}"

    dut.reset.value = 0
    await Timer(1, units='ns')
    assert dut.pc_out.value == 1, f"PC did not increment properly, expected 1 but got {dut.pc_out.value}"

@cocotb.test()
async def test_pc_increment(dut):
    """Test Program Counter Increment Functionality"""
    clock = Clock(dut.clk, 1, units="ns")
    cocotb.fork(clock.start()) 

    dut.reset.value = 0
    initial_value = dut.pc_out.value

    await Timer(1, units='ns')
    assert dut.pc_out.value == initial_value + 1, f"PC did not increment properly, expected {initial_value + 1} but got {dut.pc_out.value}"

    await Timer(1, units='ns')
    assert dut.pc_out.value == initial_value + 2, f"PC did not increment properly, expected {initial_value + 2} but got {dut.pc_out.value}"
