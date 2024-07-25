import os
import json
from pathlib import Path
from cocotb.runner import get_runner, get_results
import cocotb
from cocotb.triggers import RisingEdge, Timer
from cocotb.result import TestFailure
import pytest
import random

SIM_BUILD_DIR = "sim_build"

def runCocotbTests(pytestconfig):
    hdl_toplevel_lang = os.getenv("HDL_TOPLEVEL_LANG", "verilog")
    sim = "verilator"
    proj_path = Path(__file__).resolve().parent
    assert hdl_toplevel_lang == "verilog"
    verilog_sources = [ "/home/penn/RISC-V-R32I-Core/ALU/rca.sv", "/home/penn/RISC-V-R32I-Core/ALU/csa.sv"]

    all_tests = ["rca", "carry_select_adder_16bit"]
    tests_to_run = all_tests

    tests_requested = pytestconfig.getoption("tests")
    if tests_requested:
        tests_to_run = []
        for tr in tests_requested.split(","):
            assert tr in all_tests, f'Invalid test "{tr}" requested, expecting a comma-separated list from {all_tests}'
            tests_to_run.append(tr)

    pointsEarned = 0
    try:
        print("Tests Requested: ", tests_requested)
        for top_module in tests_to_run:
            print("Top Module: ", top_module)
            runr = get_runner(sim)
            runr.build(
                verilog_sources=verilog_sources,
                hdl_toplevel=top_module,
                vhdl_sources=[],
                includes=[proj_path],
                build_dir=SIM_BUILD_DIR,
                always=True,
                build_args=['--assert', '--trace', '--trace-structs']
            )

            results_file = runr.test(
                seed=12345,
                waves=True,
                hdl_toplevel=top_module,
                test_module=Path(__file__).stem,
                testcase="test_" + top_module,
            )
            total_failed = get_results(results_file)
            pointsEarned += len(all_tests) - total_failed[0]
    finally:
        total_failed = get_results(Path(SIM_BUILD_DIR,'runCocotbTests.results.xml'))
        # 1 point per test
        pointsEarned += total_failed[0] - total_failed[1]
        pointsPossible = total_failed[0]     
        points = { 'pointsEarned': pointsEarned, 'pointsPossible': pointsPossible }
        with open('points.json', 'w') as f:
            json.dump(points, f, indent=2)
            pass
        pass


if __name__ == "__main__":
    runCocotbTests()
    pass


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

@cocotb.test()
async def test_carry_select_adder_16bit(dut):
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