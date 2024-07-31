`timescale 1ns / 1ps

module pc (
    input wire clk,
    input wire reset,
    output reg [31:0] pc_out
);
    always @(posedge clk or posedge reset) begin
        if (reset) begin 
            pc_out = 32'b0;
        end else begin
            pc_out = pc_out + 1;
        end 
    end
endmodule