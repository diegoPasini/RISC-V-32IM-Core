// Implementation of Instruction Register
module instruction_register (
    input logic clk,         
    input logic rst_n,       
    input logic enable,      
    input logic [31:0] instruction_in, 
);
    logic [31:0] instruction_reg;

    
    always_ff @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            instruction_reg = 32'b0;
        end else if (enable) begin
            instruction_reg = instruction_in;
        end
    end

    assign instruction_out = instruction_reg;

endmodule