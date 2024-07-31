`timescale 1ns / 1ps

module rd_demultiplexer(
    input wire we,              
    input wire [4:0] rd,       
    output reg [31:0] register  
);

always @(*) begin
    if (we) begin
        register = 32'b1 << rd;
    end else begin
        register = 32'b0;
    end
end
endmodule

module register_file(
    input clk,
    input [4:0] rs1,
    input [4:0] rs2,
    input [4:0] rd,
    input [31:0] write_data,
    input reg_write,
    output wire [31:0] rd1,
    output wire [31:0] rd2
);
    wire [31:0] register_one_hot;
    reg [31:0] registers [31:0];

    rd_demultiplexer demux(
        .we(reg_write),
        .rd(rd),
        .register(register_one_hot)
    );

    generate
        genvar i;
        for (i = 0; i < 32; i = i + 1) begin : register_loop
            register reg_inst(
                .clk(clk), 
                .r_enable(register_one_hot[i]),
                .data_in(write_data),
                .data_out(registers[i])            
            );
        end
    endgenerate
    
    assign rd1 = registers[rs1];
    assign rd2 = registers[rs2];
endmodule