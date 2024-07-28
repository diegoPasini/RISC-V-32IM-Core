import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_instruct_mem(dut):
    """Test the instruct_mem module"""

    # Initialize the memory with some values
    for i in range(256):
        dut.mem[i] = i

    # Test different addresses
    for addr in range(0, 256, 16):
        dut.addr <= addr
        await Timer(1, units="ns")
        assert dut.instr.value == addr, f"instr={dut.instr.value} expected={addr} for addr={addr}"

    # Test edge cases
    edge_cases = [0, 255, 128, 64]
    for addr in edge_cases:
        dut.addr <= addr
        await Timer(1, units="ns")
        assert dut.instr.value == addr, f"instr={dut.instr.value} expected={addr} for addr={addr}"
