module alu_control (
    input [1:0] alu_op,
    input [3:0] func,
    output reg [3:0] alu_control
);
    always @(*) begin
    case (ALUOp)
        2'b00: ALUControl <= 4'b0010;
        2'b01: ALUControl <= 4'b0110;
        2'b10: begin
            case (funct)
                4'b0000: ALUControl <= 4'b0010;
                4'b1000: ALUControl <= 4'b0110; 
                4'b0111: ALUControl <= 4'b0000;
                4'b0110: ALUControl <= 4'b0001;
                default: ALUControl <= 4'bxxxx; 
            endcase
        end
        default: ALUControl <= 4'bxxxx;
    endcase
end
endmodule