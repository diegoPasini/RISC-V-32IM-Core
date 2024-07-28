import cocotb
from cocotb.triggers import Timer
from cocotb.clock import Clock

@cocotb.test()
async def test_register(dut):
    """Test the register module"""

    clock = Clock(dut.clk, 10, units="ns")
    cocotb.fork(clock.start())

    dut.r_enable <= 1
    dut.data_in <= 42
    await Timer(10, units="ns")
    assert dut.data_out.value == 42, f"Expected data_out to be 42, but got {dut.data_out.value}"

    dut.r_enable <= 0
    dut.data_in <= 100
    await Timer(10, units="ns")
    assert dut.data_out.value == 42, f"Expected data_out to remain 42, but got {dut.data_out.value}"

    dut.r_enable <= 1
    dut.data_in <= 84
    await Timer(10, units="ns")
    assert dut.data_out.value == 84, f"Expected data_out to be 84, but got {dut.data_out.value}"
