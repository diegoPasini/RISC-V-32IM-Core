import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_alu(dut):
    """Test ALU for various operations"""
    test_vectors = [
        {"a": 10, "b": 5, "control": 0b0000, "expected_result": 10 & 5},
        {"a": 10, "b": 5, "control": 0b0001, "expected_result": 10 | 5},
        {"a": 10, "b": 5, "control": 0b0010, "expected_result": 10 + 5},
        {"a": 10, "b": 5, "control": 0b0110, "expected_result": 10 - 5},
        {"a": 5, "b": 5, "control": 0b0110, "expected_result": 0},
    ]

    for vector in test_vectors:
        dut.a.value = vector["a"]
        dut.b.value = vector["b"]
        dut.control.value = vector["control"]

        await Timer(2, units='ns')

        assert dut.alu_result.value == vector["expected_result"], (
            f"Test failed with a={vector['a']}, b={vector['b']}, control={bin(vector['control'])}, "
            f"expected_result={vector['expected_result']}, got={dut.alu_result.value}"
        )