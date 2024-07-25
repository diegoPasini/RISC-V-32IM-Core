module alu (
    input [31:0] a,
    input [31:0] b,
    input [3:0] control
    output reg [31:0] alu_result,
    output reg zero
);
    always @(*)
    begin
        zero <= 0;
        case(control)  
            4b'0000 : begin 
                alu_result <= a & b;
            end
            
            4b'0001 : begin
                alu_result <= a | b;
            end
            
            4b'0010 : begin
                alu_result <= a + b;
            end
            
            4b'0110 : begin
                alu_result <= a - b;
            end

            default: begin
                alu_result <= a;
            end
        endcase
    end
endmodule