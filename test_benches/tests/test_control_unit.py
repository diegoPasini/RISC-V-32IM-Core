import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_control_unit(dut):
    """Test Control Unit for various opcodes"""
    test_vectors = [
        {"opcode": 0b0110011, "expected": {"branch": 0, "mem_read": 0, "mem_to_reg": 0, "alu_op": 0b10, "mem_write": 0, "alu_src": 0, "reg_write": 1}},
        {"opcode": 0b0000011, "expected": {"branch": 0, "mem_read": 1, "mem_to_reg": 1, "alu_op": 0b00, "mem_write": 0, "alu_src": 1, "reg_write": 1}},
        {"opcode": 0b0100011, "expected": {"branch": 0, "mem_read": 0, "mem_to_reg": 0, "alu_op": 0b00, "mem_write": 1, "alu_src": 0, "reg_write": 0}},
        {"opcode": 0b1100011, "expected": {"branch": 1, "mem_read": 0, "mem_to_reg": 0, "alu_op": 0b01, "mem_write": 0, "alu_src": 1, "reg_write": 0}},
        {"opcode": 0b0010011, "expected": {"branch": 0, "mem_read": 0, "mem_to_reg": 0, "alu_op": 0b10, "mem_write": 0, "alu_src": 0, "reg_write": 1}},
    ]

    for vector in test_vectors:
        dut.opcode.value = vector["opcode"]

        await Timer(2, units='ns')

        assert dut.branch.value == vector["expected"]["branch"], f"Test failed for opcode={bin(vector['opcode'])}: branch"
        assert dut.mem_read.value == vector["expected"]["mem_read"], f"Test failed for opcode={bin(vector['opcode'])}: mem_read"
        assert dut.mem_to_reg.value == vector["expected"]["mem_to_reg"], f"Test failed for opcode={bin(vector['opcode'])}: mem_to_reg"
        assert dut.alu_op.value == vector["expected"]["alu_op"], f"Test failed for opcode={bin(vector['opcode'])}: alu_op"
        assert dut.mem_write.value == vector["expected"]["mem_write"], f"Test failed for opcode={bin(vector['opcode'])}: mem_write"
        assert dut.alu_src.value == vector["expected"]["alu_src"], f"Test failed for opcode={bin(vector['opcode'])}: alu_src"
        assert dut.reg_write.value == vector["expected"]["reg_write"], f"Test failed for opcode={bin(vector['opcode'])}: reg_write"
