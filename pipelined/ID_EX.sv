module ID_EX (
    input wire clk,
    input wire rst_n,
    input wire [31:0] pc_in,
    input wire [31:0] rs1_data_in,
    input wire [31:0] rs2_data_in,
    input wire [31:0] imm_in,
    input wire [4:0] rs1_in,
    input wire [4:0] rs2_in,
    input wire [4:0] rd_in,
    input wire [1:0] alu_op_in,
    input wire mem_read_in,
    input wire mem_write_in,
    input wire reg_write_in,
    input wire alu_src_in,
    input wire branch_in,
    input wire mem_to_reg_in,
    output reg [31:0] pc_out,
    output reg [31:0] rs1_data_out,
    output reg [31:0] rs2_data_out,
    output reg [31:0] imm_out,
    output reg [4:0] rs1_out,
    output reg [4:0] rs2_out,
    output reg [4:0] rd_out,
    output reg [1:0] alu_op_out,
    output reg mem_read_out,
    output reg mem_write_out,
    output reg reg_write_out,
    output reg alu_src_out,
    output reg branch_out,
    output reg mem_to_reg_out
);
    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            pc_out <= 32'b0;
            rs1_data_out <= 32'b0;
            rs2_data_out <= 32'b0;
            imm_out <= 32'b0;
            rs1_out <= 5'b0;
            rs2_out <= 5'b0;
            rd_out <= 5'b0;
            alu_op_out <= 2'b0;
            mem_read_out <= 1'b0;
            mem_write_out <= 1'b0;
            reg_write_out <= 1'b0;
            alu_src_out <= 1'b0;
            branch_out <= 1'b0;
            mem_to_reg_out <= 1'b0;
        end else begin
            pc_out <= pc_in;
            rs1_data_out <= rs1_data_in;
            rs2_data_out <= rs2_data_in;
            imm_out <= imm_in;
            rs1_out <= rs1_in;
            rs2_out <= rs2_in;
            rd_out <= rd_in;
            alu_op_out <= alu_op_in;
            mem_read_out <= mem_read_in;
            mem_write_out <= mem_write_in;
            reg_write_out <= reg_write_in;
            alu_src_out <= alu_src_in;
            branch_out <= branch_in;
            mem_to_reg_out <= mem_to_reg_in;
        end
    end
endmodule