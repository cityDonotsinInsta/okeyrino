# Our first goal in de lang to write dat programm
#                      
        
# print(4 + 4 - 2);

from lexer import Lexer
from parser3 import Parser
from codegen import CodeGen


fname = "input.toy"
with open(fname) as f:
    text_input = f.read()


#"""
text_input = """
print(2 + 4 - 3);
"""
#"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)


codegen = CodeGen()

module = codegen.module
builder = codegen.builder
printf = codegen.printf


pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()


codegen.create_ir()
codegen.save_ir("output.li")

print("Okey text")