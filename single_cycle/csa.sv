`timescale 1ns / 1ps

module carry_select_adder_16bit (
    input wire [15:0] a,
    input wire [15:0] b,
    input wire cin,
    output wire [15:0] sum,
    output wire cout
);
    wire [3:0] sum0_0, sum0_1, sum1_0, sum1_1, sum2_0, sum2_1, sum3_0, sum3_1;
    wire cout0_0, cout0_1, cout1_0, cout1_1, cout2_0, cout2_1, cout3_0, cout3_1;
    wire c1, c2, c3;

    rca rca0 (
        .a(a[3:0]),
        .b(b[3:0]),
        .cin(cin),
        .sum(sum[3:0]),
        .cout(c1)
    );

    rca rca1_0 (
        .a(a[7:4]),
        .b(b[7:4]),
        .cin(1'b0),
        .sum(sum1_0),
        .cout(cout1_0)
    );

    rca rca1_1 (
        .a(a[7:4]),
        .b(b[7:4]),
        .cin(1'b1),
        .sum(sum1_1),
        .cout(cout1_1)
    );

    assign {cout0_1, sum[7:4]} = (c1 == 1'b0) ? {cout1_0, sum1_0} : {cout1_1, sum1_1};

    rca rca2_0 (
        .a(a[11:8]),
        .b(b[11:8]),
        .cin(1'b0),
        .sum(sum2_0),
        .cout(cout2_0)
    );

    rca rca2_1 (
        .a(a[11:8]),
        .b(b[11:8]),
        .cin(1'b1),
        .sum(sum2_1),
        .cout(cout2_1)
    );

    assign {cout1_1, sum[11:8]} = (cout0_1 == 1'b0) ? {cout2_0, sum2_0} : {cout2_1, sum2_1};

    rca rca3_0 (
        .a(a[15:12]),
        .b(b[15:12]),
        .cin(1'b0),
        .sum(sum3_0),
        .cout(cout3_0)
    );

    rca rca3_1 (
        .a(a[15:12]),
        .b(b[15:12]),
        .cin(1'b1),
        .sum(sum3_1),
        .cout(cout3_1)
    );

    assign {cout, sum[15:12]} = (cout1_1 == 1'b0) ? {cout3_0, sum3_0} : {cout3_1, sum3_1};

endmodule