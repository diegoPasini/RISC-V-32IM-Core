`timescale 1ns / 1ps

module alu_control_module (
    input [1:0] alu_op,
    input [3:0] func,
    output reg [3:0] alu_control
);
    always @(*) begin
    case (alu_op)
        2'b00: alu_control = 4'b0010;
        2'b01: alu_control = 4'b0110;
        2'b10: begin
            case (func)
                4'b0000: alu_control = 4'b0010;
                4'b1000: alu_control = 4'b0110; 
                4'b0111: alu_control = 4'b0000;
                4'b0110: alu_control = 4'b0001;
                default: alu_control = 4'bxxxx; 
            endcase
        end
        default: alu_control = 4'bxxxx;
    endcase
end
endmodule