import os
import sys
import json
from pathlib import Path
from cocotb.runner import get_runner, get_results

SIM_BUILD_DIR = "./sim_build"
CONFIG_FILE = "./test_benches/test_config.json"
TEST_FOLDER = "tests"

def load_config(config_file):
    with open(config_file, 'r') as file:
        config = json.load(file)
    return config

def get_verilog_sources(source_dir):
    proj_path = Path(__file__).resolve().parent.parent
    source_path = proj_path / source_dir
    verilog_sources = [str(f) for f in source_path.glob('*.sv')]
    return verilog_sources

def runCocotbTests():
    config = load_config(CONFIG_FILE)
    verilog_source_dir = config["verilog_source_dir"]
    modules = config["modules"]
    proj_path = Path(__file__).resolve().parent.parent
    hdl_toplevel_lang = os.getenv("HDL_TOPLEVEL_LANG", "verilog")
    sim = "verilator"
    assert hdl_toplevel_lang == "verilog"

    verilog_sources = get_verilog_sources(verilog_source_dir)

    sys.path.insert(0, TEST_FOLDER)

    pointsEarned = 0
    total_tests = 0
    total_passed = 0
    total_failed = 0

    try:
        print("Modules to be tested: ", modules)
        for top_module in modules:
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

            test_module_name = f"test_benches.tests.test_{top_module}"
            test_module = __import__(test_module_name, fromlist=[''])
            test_cases = [func for func in dir(test_module) if callable(getattr(test_module, func)) and func.startswith("test_")]

            for testcase in test_cases:
                results_file = runr.test(
                    seed=12345,
                    waves=True,
                    hdl_toplevel=top_module,
                    test_module=test_module_name,
                    testcase=testcase,
                )
                results = get_results(results_file)
                total_tests += 1
                if results == 0:
                    total_passed += 1
                else:
                    total_failed += 1

    finally:
        print(f"Total Tests: {total_tests}, Passed: {total_passed}, Failed: {total_failed}")