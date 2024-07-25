module data_memory(
    input wire clk,                 // Clock
    input wire mem_write,           // Memory write enable
    input wire mem_read,            // Memory read enable
    input wire [1:0] mem_size,      // Memory size (00: byte, 01: half-word, 10: word)
    input wire [31:0] address,      // Memory address
    input wire [31:0] write_data,   // Data to write to memory
    output reg [31:0] read_data     // Data read from memory
);
    reg [7:0] memory [0:1023];

    always @(posedge clk) begin
        if (mem_write) begin
            case (mem_size)
                2'b00: memory[address] <= write_data[7:0];              
                2'b01: {memory[address + 1], memory[address]} <= write_data[15:0];
                2'b10: {memory[address + 3], memory[address + 2], memory[address + 1], memory[address]} <= write_data;
                default: ; 
            endcase
        end
    end

    always @(*) begin
        if (mem_read) begin
            case (mem_size)
                2'b00: read_data <= {24'b0, memory[address]};                    
                2'b01: read_data <= {16'b0, memory[address + 1], memory[address]}; 
                2'b10: read_data <= {memory[address + 3], memory[address + 2], memory[address + 1], memory[address]};
                default: read_data <= 32'b0; 
            endcase
        end else begin
            read_data <= 32'b0;
        end
    end
endmodule