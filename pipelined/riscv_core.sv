`timescale 1ns / 1ps

module riscv_core(
    input  wire clk,
    input  wire reset,
    output logic halt
);
    // Program Counter (PC)
    wire [31:0] addr;
    wire [31:0] pc_next;
    pc pc(
        .clk(clk), 
        .reset(reset), 
        .pc_out(addr), 
        .pc_next(pc_next)
    );

    // Instruction Memory
    wire [31:0] instr;
    instruct_mem instruct(
        .addr(addr), 
        .instr(instr)
    );

    // Control Unit
    wire branch, mem_read, mem_to_reg, mem_write, alu_src, reg_write;
    wire [1:0] alu_op;
    control_unit control(
        .opcode(instr[6:0]), 
        .branch(branch),
        .mem_read(mem_read),
        .mem_to_reg(mem_to_reg),
        .alu_op(alu_op),
        .mem_write(mem_write),
        .alu_src(alu_src),
        .reg_write(reg_write)
    );

    // Register File
    wire [31:0] write_data, rd_1, rd_2;
    register_file registers(
        .clk(clk),
        .rs1(instr[19:15]),
        .rs2(instr[24:20]),
        .rd(instr[11:7]),
        .write_data(write_data),
        .reg_write(reg_write),
        .rd1(rd_1),
        .rd2(rd_2)
    );

    // Immediate Generator
    wire [31:0] imm_out;
    imm_gen immgen(
        .instruction(instr),
        .imm_out(imm_out)
    );

    // ALU Control
    wire [3:0] alu_control;
    alu_control_module alu_ctrl(
        .alu_op(alu_op),
        .func({instr[30], instr[14:12]}),
        .alu_control(alu_control)
    );

    // ALU Source Multiplexer
    wire [31:0] mux_alu_output;
    mux2to1 alu_src_mux(
        .data0(rd_2),
        .data1(imm_out),
        .sel(alu_src),
        .out(mux_alu_output)
    );

    // ALU
    wire [31:0] alu_result;
    alu alu_inst(
        .a(rd_1),
        .b(mux_alu_output),
        .control(alu_control),
        .alu_result(alu_result)
    );

    // Data Memory
    wire [31:0] read_data;
    data_memory data_mem(
        .clk(clk),
        .mem_write(mem_write),
        .mem_read(mem_read),
        .address(alu_result),
        .write_data(rd_2),
        .read_data(read_data)
    );

    // Write-Back Multiplexer
    mux2to1 mem_to_reg_mux(
        .data0(alu_result),
        .data1(read_data),
        .sel(mem_to_reg),
        .out(write_data)
    );

    // PC Update Logic
    wire [31:0] pc_plus_4;
    assign pc_plus_4 = addr + 4;

    wire [31:0] branch_target;
    assign branch_target = addr + (imm_out << 1);

    mux2to1 branch_mux(
        .data0(pc_plus_4),
        .data1(branch_target),
        .sel(branch & zero),
        .out(pc_next)
    );

    assign halt = 1'b0;

endmodule

module mux2to1 (
    input  logic [31:0] data0, 
    input  logic [31:0] data1, 
    input  logic        sel,   
    output logic [31:0] out    
);

    assign out = sel ? data1 : data0;

endmodule