import cocotb
from cocotb.triggers import Timer, RisingEdge

async def clock_gen(clk):
    """Generate clock pulses."""
    while True:
        clk.value = 0
        await Timer(1, units='ns')
        clk.value = 1
        await Timer(1, units='ns')

@cocotb.test()
async def test_data_memory(dut):
    """Test Data Memory for read and write operations"""
    cocotb.start_soon(clock_gen(dut.clk))  # Start the clock generator

    test_vectors = [
        {"address": 0x00, "write_data": 0x1234, "mem_write": 1, "mem_read": 0, "expected_read_data": None},
        {"address": 0x04, "write_data": 0x5678, "mem_write": 1, "mem_read": 0, "expected_read_data": None},
        {"address": 0x08, "write_data": 0x9ABC, "mem_write": 1, "mem_read": 0, "expected_read_data": None},
        {"address": 0x0C, "write_data": 0xDEF0, "mem_write": 1, "mem_read": 0, "expected_read_data": None},
        {"address": 0x00, "write_data": 0x0000, "mem_write": 0, "mem_read": 1, "expected_read_data": 0x1234},
        {"address": 0x04, "write_data": 0x0000, "mem_write": 0, "mem_read": 1, "expected_read_data": 0x5678},
        {"address": 0x08, "write_data": 0x0000, "mem_write": 0, "mem_read": 1, "expected_read_data": 0x9ABC},
        {"address": 0x0C, "write_data": 0x0000, "mem_write": 0, "mem_read": 1, "expected_read_data": 0xDEF0},
        {"address": 0x10, "write_data": 0x1357, "mem_write": 1, "mem_read": 0, "expected_read_data": None},
        {"address": 0x14, "write_data": 0x2468, "mem_write": 1, "mem_read": 0, "expected_read_data": None},
        {"address": 0x10, "write_data": 0x0000, "mem_write": 0, "mem_read": 1, "expected_read_data": 0x1357},
        {"address": 0x14, "write_data": 0x0000, "mem_write": 0, "mem_read": 1, "expected_read_data": 0x2468},
    ]

    for vector in test_vectors:
        dut.address.value = vector["address"]
        dut.write_data.value = vector["write_data"]
        dut.mem_write.value = vector["mem_write"]
        dut.mem_read.value = vector["mem_read"]

        await RisingEdge(dut.clk)  # Wait for a rising edge of the clock

        if vector["mem_read"]:
            assert dut.read_data.value == vector["expected_read_data"], (
                f"Test failed for address={hex(vector['address'])}: expected read_data={hex(vector['expected_read_data'])}, got={hex(dut.read_data.value)}"
            )
