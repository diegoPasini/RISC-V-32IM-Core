import cocotb
from cocotb.triggers import Timer
from cocotb.clock import Clock

@cocotb.test()
async def test_register_file(dut):
    """Test the register file module"""

    # Initialize clock
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.fork(clock.start())

    # Write to all registers
    for i in range(32):
        dut.reg_write <= 1
        dut.rd = i
        dut.write_data = i * 10
        await Timer(10, units="ns")

    # Read from all registers and verify the values
    for i in range(32):
        dut.reg_write = 0
        dut.rs1 = i
        dut.rs2 = (i + 1) % 32
        await Timer(10, units="ns")
        assert dut.rd1.value == i * 10, f"Register {i} read value {dut.rd1.value} expected {i * 10}"
        assert dut.rd2.value == ((i + 1) % 32) * 10, f"Register {(i + 1) % 32} read value {dut.rd2.value} expected {((i + 1) % 32) * 10}"
