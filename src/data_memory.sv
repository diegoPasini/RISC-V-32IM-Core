`timescale 1ns / 1ps

module data_memory(
    input wire clk,                 
    input wire mem_write,           
    input wire mem_read,            
    input wire [31:0] address,      
    input wire [31:0] write_data,   
    output reg [31:0] read_data     
);
    reg [7:0] memory [0:1023];

    always @(posedge clk) begin
        if (mem_write) begin
            memory[address] = write_data[7:0];
            memory[address + 1] = write_data[15:8];
            memory[address + 2] = write_data[23:16];
            memory[address + 3] = write_data[31:24];
        end
    end

    always @(*) begin
        if (mem_read) begin
            read_data = {memory[address + 3], memory[address + 2], memory[address + 1], memory[address]};
        end else begin
            read_data = 32'b0;
        end
    end
endmodule