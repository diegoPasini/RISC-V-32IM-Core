module IF_ID (
    input wire clk,
    input wire rst_n,
    input wire [31:0] pc_in,
    input wire [31:0] instruction_in,
    output reg [31:0] pc_out,
    output reg [31:0] instruction_out
);
    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            pc_out <= 32'b0;
            instruction_out <= 32'b0;
        end else begin
            pc_out <= pc_in;
            instruction_out <= instruction_in;
        end
    end
endmodule