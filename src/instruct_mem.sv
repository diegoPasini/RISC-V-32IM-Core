module instruct_mem (
    input wire [31:0] addr,
    output wire [31:0] instr
);
    reg [31:0] mem [0:255];

    assign instr = addr;
endmodule   