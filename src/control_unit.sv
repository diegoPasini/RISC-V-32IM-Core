`timescale 1ns / 1ps

module control_unit(
    input [6:0] opcode,
    output reg branch,
    output reg mem_read,
    output reg mem_to_reg,
    output reg [1:0] alu_op,
    output reg mem_write,
    output reg alu_src,
    output reg reg_write
);
   always@(*) begin
        case (opcode)
            // R-type instructions
            7'b0110011: begin 
                mem_to_reg <= 0;
                reg_write <= 1;
                mem_read <= 0;
                mem_write <= 0;
                branch <= 0;
                alu_op <= 2'b10;
                alu_src <= 0;
            end
            
            // LW Instruction
            7'b0000011: begin
                mem_to_reg <= 1;
                reg_write <= 1;
                mem_read <= 1;
                mem_write <= 0;
                branch <= 0;
                alu_op <= 2'b00;
                alu_src <= 1;
            end


            // SW Instruction
            7'b0100011: begin
                mem_to_reg <= 0;
                reg_write <= 0;
                mem_read <= 0;
                mem_write <= 1;
                branch <= 0;
                alu_op <= 2'b00;
                alu_src <= 0;
            end
            

            // BEQ Instruction 
            7'b1100011: begin
                mem_to_reg <= 0;
                reg_write <= 0;
                mem_read <= 0;
                mem_write <= 0;
                branch <= 1;
                alu_op <= 2'b01;
                alu_src <= 1;
            end


            // I-format instruction, not LW
            7'b0010011: begin
                mem_to_reg <= 0;
                reg_write <= 1;
                mem_read <= 0;
                mem_write <= 0;
                branch <= 0;
                alu_op <= 2'b10;
                alu_src <= 0;
            end

            // Default:
            default: begin
                mem_to_reg <= 0;
                reg_write <= 1;
                mem_read <= 0;
                mem_write <= 0;
                branch <= 0;
                alu_op <= 2'b00;
                alu_src <= 0;
            end
        endcase
   end
endmodule