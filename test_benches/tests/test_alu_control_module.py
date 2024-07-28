import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_alu_control_module(dut):
    """Test ALU Control Module for various ALU operations"""
    test_vectors = [
        {"alu_op": 0b00, "func": 0b0000, "expected": 0b0010},
        {"alu_op": 0b01, "func": 0b0000, "expected": 0b0110},
        {"alu_op": 0b10, "func": 0b0000, "expected": 0b0010},
        {"alu_op": 0b10, "func": 0b1000, "expected": 0b0110},
        {"alu_op": 0b10, "func": 0b0111, "expected": 0b0000},
        {"alu_op": 0b10, "func": 0b0110, "expected": 0b0001},
    ]

    for vector in test_vectors:
        dut.alu_op.value = vector["alu_op"]
        dut.func.value = vector["func"]

        await Timer(2, units='ns')

        assert dut.alu_control.value == vector["expected"], (
            f"Test failed with alu_op={bin(vector['alu_op'])}, func={bin(vector['func'])}, "
            f"expected={bin(vector['expected'])}, got={bin(dut.alu_control.value)}"
        )
