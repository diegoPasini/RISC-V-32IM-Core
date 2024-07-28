import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_rca(dut):
    """Test Ripple Carry Adder (RCA) for multiple random input combinations"""
    for _ in range(100):
        a = random.randint(0, 15)
        b = random.randint(0, 15)
        cin = random.randint(0, 1)

        dut.a.value = a
        dut.b.value = b
        dut.cin.value = cin

        await Timer(2, units='ns')

        expected_sum = (a + b + cin) % 16
        expected_cout = (a + b + cin) // 16

        assert dut.sum.value == expected_sum, f"Test failed with a={a}, b={b}, cin={cin}, expected sum={expected_sum}, got {dut.sum.value}"
        assert dut.cout.value == expected_cout, f"Test failed with a={a}, b={b}, cin={cin}, expected cout={expected_cout}, got {dut.cout.value}"