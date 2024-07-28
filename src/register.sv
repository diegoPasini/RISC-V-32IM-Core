`timescale 1ns / 1ps

module register(
    input clk,
    input r_enable, 
    input [31:0] data_in,
    output reg [31:0] data_out 
);
    always @(posedge clk)
    begin 
        if (r_enable)
            data_out = data_in;
    end
endmodule