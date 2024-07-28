`timescale 1ns / 1ps

module pc (
    input wire clk,
    input wire reset,
    output reg [31:0] pc
);
    always @(posedge clk or posedge reset) begin
        if (reset) begin 
            pc <= 32'b0;
        end else begin
            pc <= pc + 1;
        end 
    end
endmodule