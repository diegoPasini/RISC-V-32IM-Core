import unittest
from asm_to_riscv import assembly_instruction

class TestRiscVAssembly(unittest.TestCase):
    def test_lui_instruction(self):
        self.assertEqual(assembly_instruction("LUI x1, 1000"), "00000000001111101000000010110111")
        
    def test_auipc_instruction(self):
        self.assertEqual(assembly_instruction("AUIPC x1, 1000"), "00000000001111101000000010010111")
    
    # I-type instruction tests
    def test_addi_instruction(self):
        self.assertEqual(assembly_instruction("ADDI x1, x2, 10"), "00000000101000010000000010010011")
        
    def test_lw_instruction(self):
        self.assertEqual(assembly_instruction("LW x1, 0(x2)"), "00000000000000010010000010000011")
        
    def test_jalr_instruction(self):
        self.assertEqual(assembly_instruction("JALR x1, 0(x2)"), "00000000000000010000000011100111")
        
    def test_ori_instruction(self):
        self.assertEqual(assembly_instruction("ORI x1, x2, 255"), "00001111111100010110000010010011")
    
    # # S-type instruction tests
    def test_sw_instruction(self):
        self.assertEqual(assembly_instruction("SW x1, 0(x2)"), "00000000000100010010000000100011")
        
    def test_sh_instruction(self):
        self.assertEqual(assembly_instruction("SH x1, 0(x2)"), "00000000000100010001000000100011")
        
    def test_sb_instruction(self):
        self.assertEqual(assembly_instruction("SB x1, 0(x2)"), "00000000000100010000000000100011")
    
    # # B-type instruction tests
    def test_beq_instruction(self):
        self.assertEqual(assembly_instruction("BEQ x1, x2, 20"), "00000000001000001000101001100011")
        
    def test_bne_instruction(self):
        self.assertEqual(assembly_instruction("BNE x1, x2, 20"), "00000000001000001001101001100011")
        
    def test_blt_instruction(self):
        self.assertEqual(assembly_instruction("BLT x1, x2, 20"), "00000000001000001100101001100011")
        
    def test_bge_instruction(self):
        self.assertEqual(assembly_instruction("BGE x1, x2, 20"), "00000000001000001101101001100011")
        
    def test_bltu_instruction(self):
        self.assertEqual(assembly_instruction("BLTU x1, x2, 20"), "00000000001000001110101001100011")
        
    def test_bgeu_instruction(self):
        self.assertEqual(assembly_instruction("BGEU x1, x2, 20"), "00000000001000001111101001100011")
    
    # # J-type instruction tests
    def test_jal_instruction(self):
        self.assertEqual(assembly_instruction("JAL x1, 2000"), "01111101000000000000000011101111")
    
    # # R-type instruction tests
    def test_add_instruction(self):
        self.assertEqual(assembly_instruction("ADD x1, x2, x3"), "00000000001100010000000010110011")
        
    def test_sub_instruction(self):
        self.assertEqual(assembly_instruction("SUB x1, x2, x3"), "01000000001100010000000010110011")
        
    def test_and_instruction(self):
        self.assertEqual(assembly_instruction("AND x1, x2, x3"), "00000000001100010111000010110011")
        
    def test_or_instruction(self):
        self.assertEqual(assembly_instruction("OR x1, x2, x3"), "00000000001100010110000010110011")
        
    def test_xor_instruction(self):
        self.assertEqual(assembly_instruction("XOR x1, x2, x3"), "00000000001100010100000010110011")
        
    def test_sll_instruction(self):
        self.assertEqual(assembly_instruction("SLL x1, x2, x3"), "00000000001100010001000010110011")
        
    def test_srl_instruction(self):
        self.assertEqual(assembly_instruction("SRL x1, x2, x3"), "00000000001100010101000010110011")
        
    def test_sra_instruction(self):
        self.assertEqual(assembly_instruction("SRA x1, x2, x3"), "01000000001100010101000010110011")
    
    # # Edge cases
    def test_edge_case_lui(self):
        self.assertEqual(assembly_instruction("LUI x3, 1048575"), "11111111111111111111000110110111")
        
    def test_edge_case_addi(self):
        self.assertEqual(assembly_instruction("ADDI x0, x0, -1"), "11111111111100000000000000010011")
    
    def test_slli_instruction(self):
        self.assertEqual(assembly_instruction("SLLI x1, x2, 3"), "00000000001100010001000010010011")
        
    def test_srli_instruction(self):
        self.assertEqual(assembly_instruction("SRLI x1, x2, 3"), "00000000001100010101000010010011")
        
    def test_srai_instruction(self):
        self.assertEqual(assembly_instruction("SRAI x1, x2, 3"), "01000000001100010101000010010011")
        
    def test_slti_instruction(self):
        self.assertEqual(assembly_instruction("SLTI x1, x2, 5"), "00000000010100010010000010010011")
        
    def test_sltiu_instruction(self):
        self.assertEqual(assembly_instruction("SLTIU x1, x2, 5"), "00000000010100010011000010010011")
        
    def test_lbu_instruction(self):
        self.assertEqual(assembly_instruction("LBU x1, 0(x2)"), "00000000000000010100000010000011")
        
    def test_lhu_instruction(self):
        self.assertEqual(assembly_instruction("LHU x1, 0(x2)"), "00000000000000010101000010000011")
        
    def test_sb_edge_case(self):
        self.assertEqual(assembly_instruction("SB x31, 1023(x2)"), "00111111111100010000111110100011")
        
    def test_sh_edge_case(self):
        self.assertEqual(assembly_instruction("SH x31, 1023(x2)"), "00111111111100010001111110100011")
        
    def test_sw_edge_case(self):
        self.assertEqual(assembly_instruction("SW x31, 1023(x2)"), "00111111111100010010111110100011")
        
    def test_slt_instruction(self):
        self.assertEqual(assembly_instruction("SLT x1, x2, x3"), "00000000001100010010000010110011")
        
    def test_sltu_instruction(self):
        self.assertEqual(assembly_instruction("SLTU x1, x2, x3"), "00000000001100010011000010110011")
                        
    def test_ecall_instruction(self):
        self.assertEqual(assembly_instruction("ECALL"), "00000000000000000000000001110011")
        
    def test_ebreak_instruction(self):
        self.assertEqual(assembly_instruction("EBREAK"), "00000000000100000000000001110011")
        
    def test_csrrw_instruction(self):
        self.assertEqual(assembly_instruction("CSRRW x1, 0, x2"), "00000000000000010001000011110011")
        
    def test_csrrs_instruction(self):
        self.assertEqual(assembly_instruction("CSRRW x1, 1, x2"), "00000000000100010001000011110011")
        
    def test_csrrc_instruction(self):
        self.assertEqual(assembly_instruction("CSRRW x1, 2, x2"), "00000000001000010001000011110011")
        
    def test_csrrwi_instruction(self):
        self.assertEqual(assembly_instruction("CSRRWI x1, 0, 1"), "00000000000000001101000011110011")
        
    def test_csrrsi_instruction(self):
        self.assertEqual(assembly_instruction("CSRRSI x1, 1, 1"), "00000000000100001110000011110011")
        
    def test_csrrci_instruction(self):
        self.assertEqual(assembly_instruction("CSRRCI x1, 2, 1"), "00000000001000001111000011110011")

    # Invalid instruction
    def test_invalid_format(self):
        with self.assertRaises(Exception):
            assembly_instruction("ADD x1 x2")

if __name__ == '__main__':
    unittest.main()