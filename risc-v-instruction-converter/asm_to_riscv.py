from risc_v_mappings import (
    OPCODE_MAPPINGS,
    R_TYPES,
    I_TYPES,
    U_TYPES,
    B_TYPES,
    S_TYPES,
    J_TYPES,
    REGISTER_MAPPINGS,
    FUNCT3_MAPPINGS, 
    FUNCT7_MAPPINGS
)   

def to_bin(value, bits):
    return format(value if value >= 0 else (1 << bits) + value, f'0{bits}b')


def assembly_instruction(instruction):
    hasImm = False
    if "(" in instruction:
        hasImm = True

    parts = instruction.replace(',', '').replace('(', ' ').replace(')', '').split()
    op = parts[0]
    opcode = OPCODE_MAPPINGS[op]

    try: 
        if op in R_TYPES:
            if op == "SLLI" or op == "SRLI" or op == "SRAI":
                rd = REGISTER_MAPPINGS[parts[1]]
                rs1 = REGISTER_MAPPINGS[parts[2]]
                rs2 = to_bin(int(parts[3]), 5)
            
            else:
                rd = REGISTER_MAPPINGS[parts[1]]
                rs1 = REGISTER_MAPPINGS[parts[2]]
                rs2 = REGISTER_MAPPINGS[parts[3]]
            
            funct3 = FUNCT3_MAPPINGS[op]
            funct7 = FUNCT7_MAPPINGS[op]
            return funct7 + rs2 + rs1 + funct3 + rd + opcode
        
        elif op in I_TYPES:
            rd = REGISTER_MAPPINGS[parts[1]]

            if op in ["CSRRW", "CSRRS", "CSRRC"]:
                hasImm = True
            
            if op in  ["CSRRWI", "CSRRSI", "CSRRCI"]:
                rs1 = to_bin(int(parts[3]), 5)
                imm = to_bin(int(parts[2]), 12)
            else: 
                if hasImm:
                    rs1 = REGISTER_MAPPINGS[parts[3]]
                    imm = to_bin(int(parts[2]), 12)
                else:
                    rs1 = REGISTER_MAPPINGS[parts[2]]
                    imm = to_bin(int(parts[3]), 12)

            funct3 = FUNCT3_MAPPINGS[op]
            return imm + rs1 + funct3 + rd + opcode

        elif op in U_TYPES:
            rd = REGISTER_MAPPINGS[parts[1]]
            imm = to_bin(int(parts[2]), 20)
            return imm + rd + opcode

        elif op in B_TYPES:
            rs1 = REGISTER_MAPPINGS[parts[1]]
            if hasImm:
                rs2 = REGISTER_MAPPINGS[parts[3]]
                imm = to_bin(int(parts[2]), 12)
            else: 
                rs2 = REGISTER_MAPPINGS[parts[2]]
                imm = to_bin(int(parts[3]), 12)

            funct3 = FUNCT3_MAPPINGS[op]
            imm_4_1_11 = imm[7:11] + imm[0]
            imm_12 = imm[11] + imm[1:7]
            return imm_12  + rs2 + rs1 + funct3 + imm_4_1_11 + opcode

        elif op in S_TYPES:
            rs2 = REGISTER_MAPPINGS[parts[1]]
            if hasImm:
                rs1 = REGISTER_MAPPINGS[parts[3]]
                imm = to_bin(int(parts[2]), 12)
            else: 
                rs1 = REGISTER_MAPPINGS[parts[2]]
                imm = to_bin(int(parts[3]), 12)
            funct3 = FUNCT3_MAPPINGS[op]
            imm_11_5 = imm[0:7]  
            imm_4_0 = imm[7:12] 
            return imm_11_5 + rs2 + rs1 + funct3 + imm_4_0 + opcode

        elif op in J_TYPES:
            rd = REGISTER_MAPPINGS[parts[1]]
            imm = to_bin(int(parts[2]), 21)
            imm_20 = imm[0]
            imm_10_1 = imm[10:20]
            imm_11 = imm[9]
            imm_19_12 = imm[1:9]
            return imm_20 + imm_10_1 + imm_11 + imm_19_12 + rd + opcode
        
        elif op == "ECALL":
            return "00000000000000000000000001110011"
        
        elif op == "EBREAK":
            return "00000000000100000000000001110011"

        elif op == "FENCE.I":
            return "00000000000000000001000000001111"
        
        elif op == "FENCE":
            pred = to_bin(int(parts[1]), 4)
            succ = to_bin(int(parts[2]), 4)
            return "0000" + pred + succ  + "00000000000000001111"

        else:
            raise ValueError(f"Instruction {op} is not supported in RV32I")
    
    except Exception as e:
        raise Exception(f"Invalid Format for Instruction")

# @param assembly_code
def convert(assembly_code):
    instructions = []
    for line in assembly_code.splitlines():
        instructions.append(assembly_instruction(line))
    return instructions
    
