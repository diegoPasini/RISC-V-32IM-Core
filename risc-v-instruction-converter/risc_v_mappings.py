
# * Reference for mappings can be found:
# * https://riscv.org/wp-content/uploads/2017/05/riscv-spec-v2.2.pdf
# * Pg. 116 contains the instruction sheet for RV32I

### * Opcode Mappings for RV32I: * ###
OPCODE_MAPPINGS = {
    "LUI" : "0110111",
    "AUIPC" : "0010111",
    "JAL" : "1101111",
    "JALR" : "1100111",
    "BEQ" : "1100011",
    "BNE" : "1100011",
    "BLT" : "1100011",
    "BGE" : "1100011",
    "BLTU" : "1100011",
    "BGEU" : "1100011",
    "LB" : "0000011",
    "LH" : "0000011",
    "LW" : "0000011",
    "LBU" : "0000011",
    "LHU" : "0000011",
    "SB" : "0100011",
    "SH" : "0100011",
    "SW" : "0100011",
    "ADDI" : "0010011",
    "SLTI" : "0010011",
    "SLTIU" : "0010011",
    "JALR" : "1100111",
    "XORI" : "0010011",
    "ORI" : "0010011",
    "ANDI" : "0010011",
    "SLLI" : "0010011",
    "SRLI" : "0010011",
    "SRAI" : "0010011",
    "ADD" : "0110011",
    "SUB" : "0110011",
    "SLL" : "0110011",
    "SLT" : "0110011",
    "SLTU" : "0110011",
    "XOR" : "0110011",
    "SRL" : "0110011",
    "SRA" : "0110011",
    "OR" : "0110011",
    "AND" : "0110011",
    "FENCE" : "0001111",
    "ECALL" : "1110011",
    "EBREAK" : "1110011",
    "CSRRW" : "1110011",
    "CSRRS" : "1110011",
    "CSRRC" : "1110011",
    "CSRRWI" : "1110011",
    "CSRRSI" : "1110011",
    "CSRRCI" : "1110011"
}


### * Operations Categories * ###
R_TYPES = ["SLLI", "SRLI", "SRAI", "ADD", "SUB", "SLL", "SLT", "SLTU", "XOR", "SRL", "SRA", "OR", "AND"]

I_TYPES = ["JALR", "LB", "LH", "LW", "LBU", "LHU", "ADDI", "SLTI", "SLTIU", "XORI", "ORI", "ANDI", "SLLI", "SRLI", "SRAI", "CSRRW", "CSRRS", "CSRRC", "CSRRWI", "CSRRSI", "CSRRCI"]

U_TYPES = ["LUI", "AUIPC"]

B_TYPES = ["BEQ", "BNE", "BLT", "BGE", "BLTU", "BGEU"]

S_TYPES = ["SB", "SH", "SW"]

J_TYPES = ["JAL"]



### * Register Mappings * ###
REGISTER_MAPPINGS = {f"x{i}": f"{i:05b}" for i in range(32)}

ABI_NAMES = [
    "zero", "ra", "sp", "gp", "tp",
    "t0", "t1", "t2", "s0", "s1",
    "a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7",
    "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "s11",
    "t3", "t4", "t5", "t6"
]

# For easier reference, the ABI_REGISTER_MAPPINGS are added to REGISTER_MAPPINGS
ABI_REGISTER_MAPPINGS = {name: f"{i:05b}" for i, name in enumerate(ABI_NAMES)}
REGISTER_MAPPINGS.update(ABI_REGISTER_MAPPINGS)

# Funct Mappings:
FUNCT3_MAPPINGS = {
    "BEQ": "000",
    "BNE": "001",
    "BLT": "100",
    "BGE": "101",
    "BLTU": "110",
    "BGEU": "111",
    "LB": "000",
    "LH": "001",
    "LW": "010",
    "LBU": "100",
    "LHU": "101",
    "SB": "000",
    "SH": "001",
    "SW": "010",
    "ADDI": "000",
    "SLTI": "010",
    "SLTIU": "011",
    "JALR" : "000",
    "XORI": "100",
    "ORI": "110",
    "ANDI": "111",
    "SLLI": "001",
    "SRLI": "101",
    "SRAI": "101",
    "ADD": "000",
    "SUB": "000",
    "SLL": "001",
    "SLT": "010",
    "SLTU": "011",
    "XOR": "100",
    "SRL": "101",
    "SRA": "101",
    "OR": "110",
    "AND": "111",
    "CSRRW": "001",
    "CSRRS": "010",
    "CSRRC": "011",
    "CSRRWI": "101",
    "CSRRSI": "110",
    "CSRRCI": "111",
}

FUNCT7_MAPPINGS = {
    "SLLI": "0000000",
    "SRLI": "0000000",
    "SRAI": "0100000",
    "ADD": "0000000",
    "SUB": "0100000",
    "SLL": "0000000",
    "SLT": "0000000",
    "SLTU": "0000000",
    "XOR": "0000000",
    "SRL": "0000000",
    "SRA": "0100000",
    "OR": "0000000",
    "AND": "0000000",
}


