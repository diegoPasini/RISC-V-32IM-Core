import cocotb
from cocotb.triggers import Timer
from cocotb.regression import TestFactory
from cocotb.clock import Clock
import random

@cocotb.test()
async def test_imm_gen(dut):
    """Test the imm_gen module"""

    def check_output(instruction, expected_imm):
        dut.instruction <= instruction
        yield Timer(1, units="ns") 
        assert dut.imm_out.value == expected_imm, f"imm_out={dut.imm_out.value} expected={expected_imm}"


    for _ in range(10):
        instruction = random.randint(0, 2**32-1)
    
        opcode = instruction & 0x7F
        if opcode == 0b0010011:  # I-type
            expected_imm = ((instruction >> 20) & 0xFFF) | ((instruction >> 31) * 0xFFFFF000)
        elif opcode == 0b0100011:  # S-type
            expected_imm = ((instruction >> 7) & 0x1F) | ((instruction >> 25) * 0x7F) | ((instruction >> 31) * 0xFFFFF000)
        elif opcode == 0b1100011:  # B-type
            expected_imm = ((instruction >> 7) & 0x1E) | ((instruction >> 25) * 0x3F) | ((instruction >> 31) * 0xFFFFF000)
        elif opcode == 0b0110111:  # U-type
            expected_imm = (instruction & 0xFFFFF000)
        elif opcode == 0b1101111:  # J-type
            expected_imm = ((instruction >> 12) & 0xFF) | ((instruction >> 20) & 0x1) | ((instruction >> 21) * 0x7F) | ((instruction >> 31) * 0xFFFFF000)
        else:
            expected_imm = 0

        dut.instruction <= instruction
        await Timer(10, units="ns")
        assert dut.imm_out.value == expected_imm, f"imm_out={dut.imm_out.value} expected={expected_imm} for instruction={instruction:032b}"