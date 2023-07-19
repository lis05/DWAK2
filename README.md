# DWAK2 - An improved version of DWAK CPU architecture

DWAK2 is 64 bit. Therefore, all instructions are 64bit, and one word is 64bits.
Due to the simulation software limitations, addresses will be 24bit.


## TERMINOLOGY
- reg - means a register index.
    Can be one of: `R0`, `R1`, `R2`, `R3`, `CF`, `DV`, `SB`, `SH`, `IP`

- [mem] - means a memory address.
    Can be one of: `[const]`, `[reg]`

- const - means a constant value.
    Can be any hex, decimal, or binary number.


## REGISTERS
### General usage registers R0, R1, R2, R3.
Used in general computations.

- R0 has register index 0, size of 64bits.
- R1 has register index 1, size of 64bits.
- R2 has register index 2, size of 64bits.
- R3 has register index 3 size of 64bits.
### Return register RP.
Contains return data of the last function call.

- RR has register index 0xFA, size of 64bits

### Return pointer register RP.
Points to the return address that CPU has to return to after exiting a function call.

- RP has register index 0xFB, size of 64bits

### Conditional flag register CF.
Contains a value that indicates the result of the last CMP instruction.
The values is a bitmask, with each set bit meaning a certain condition.

    1 means "equal", 2 means "not equal",
    4 means "less", 8 means "less equal",
    16 means "greater", 32 means "greater equal".
        
- CF has register index 0xFC, size of 64bits.

### Stack registers SB, SH.
Used in stack operations. SB points to the base of the stack, and SH points to the head of the stack. 
    
- SB has register index 0xFD, size of 64bits.
- SH has register index 0xFE, size of 64bits.
    
### Instruction pointer register IP.
This is a special register that shoudn't be directly changed.
Points to the next instruction that has to be executed. 

- IP has register index 0xFF, size of 64bits.
----
#### Implementation
Registers are combined into one single regfile. 
It can both read two registers and write to one register.


## INSTRUCTIONS
### 1. MOV X, Y
Moves data from Y to X
Can move data to registers or memory.
Can move data from registers, memory, or move constant values. However, can't move data from memory to memory.

#### Syntax:
```
MOV reg, reg
MOV reg, const
MOV reg, [const]
MOV reg, [reg]
MOV [const], const
MOV [const], reg
MOV [reg], const
MOV [reg], reg
```
#### Binary representation

```
MOV reg, reg
    3       =1. size in words
    8       =0. opcode
    8       register index (first argument)
    8       register index (second argument)
    37      unused
MOV reg, const
    3       =2. size in words
    8       =1. opcode
    8       register index (first argument)
    45      unused

    64      constant (second argument)
MOV reg, [const]
    3       =2. size in words
    8       =2. opcode
    8       register index (first argument)
    45      unused

    64      constant (second argument)
MOV reg, [reg]
    3       =1. size in words
    8       =3. opcode
    8       register index (first argument)
    8       register index (second argument)
    37      unused
MOV [const], const
    3       =3. size in words
    8       =4. opcode
    53      unused

    64      const (first argument)

    64      const (first argument)
MOV [const], reg
    3       =2. size in words
    8       =5. opcode
    8       register index (second argument)
    45      unused

    64      const (first argument)
MOV [reg], const
    3       =2. size in words
    8       =6. opcode
    8       register index (first argument)
    45      unused

    64      const (second argument)
MOV [reg], reg
    3       =1. size in words
    8       =7. opcode
    8       register index (first argument)
    8       register index (second argument)
    37      unused
```
#### Implementation
It is implemented as a one single chip that is made of 8 smaller chips, each corresponding to one of the opcodes.

### ARITHM
ARITHM instuction executes some arithmetic operation on numbers X and Y, storing result in X.
There are a few operations supported:
```
ADD X, Y. aopcode 0, stores X+Y in X.
SUB X, Y. aopcode 1, stores X-Y in X.
MUL X, Y. aopcode 2, stores X*Y in X.
DIVQ X, Y. aopcode 3, stores X//Y in X.
DIVR X, Y. aopcode 4, stores X%Q in X.
AND X, Y. aopcode 5, stores X AND Y in X.
OR X, Y.  aopcode 6, stores X OR Y in X.
XOR X, Y. aopcode 7, stores X XOR Y in X.
NOT X, Y. aopcode 8, stores NOT X in X.
SHL X, Y. aopcode 9, stores X<<Y in X.
SHR X, Y. aopcode 10, stores X>>Y in X.
```

#### Syntax
```
ARITHM OP, reg, reg
ARITHM OP, reg, const
ARITHM OP, reg, [const]
ARITHM OP, reg, [reg]
ARITHM OP, [const], const
ARITHM OP, [const], reg
ARITHM OP, [reg], const
ARITHM OP, [reg], reg
```

#### Binary representation
```
ARITHM OP, reg, reg
    3       =1. size in words
    8       =8. opcode
    4       aopcode (first argument)
    8       register index (second argument)
    8       register index (third argument)
    33      unused
ARITHM OP, reg, const
    3       =2. size in words
    8       =9. opcode
    4       aopcode (first argument)
    8       register index (second argument)
    41      unused

    64      constant (third argument)
ARITHM OP, reg, [const]
    3       =2. size in words
    8       =10. opcode
    4       aopcode (first argument)
    8       register index (second argument)
    41      unused

    64      constant (third argument)
ARITHM OP, reg, [reg]
    3       =1. size in words
    8       =11. opcode
    4       aopcode (first argument)
    8       register index (second argument)
    8       register index (third argument)
    33      unused
ARITHM OP, [const], const
    3       =3. size in words
    8       =12. opcode
    4       aopcode (first argument)
    49      unused

    64      constant (second argument)

    64      constant (second argument)
ARITHM OP, [const], reg
    3       =2. size in words
    8       =13. opcode
    4       aopcode (first argument)
    8       register index (third argument)
    41      unused

    64      constant (second argument)
ARITHM OP, [reg], const
    3       =2. size in words
    8       =14. opcode
    4       aopcode (first argument)
    8       register index (second argument)
    41      unused

    64      constant (third argument)
ARITHM OP, [reg], reg
    3       =1. size in words
    8       =15. opcode
    4       aopcode (first argument)
    8       register index (second argument)
    8       register index (third argument)
    33      unused
```
#### Implementation
Implemented as a single chip with 8 smaller chips(each for one opcode) inside.

#### Notes
ARITHM OP, X, Y instruction is simplified to OP, X, Y in the assembler.

### CMP
CMP compares two values, and writes the result into CF register.
Values are bitmasks.
```
1 means "equal", 2 means "not equal",
4 means "less", 8 means "less equal",
16 means "greater", 32 means "greater equal".
```

#### Syntax
```
CMP reg, reg
CMP reg, const
CMP reg, [const]
CMP reg, [reg]
CMP [const], const
CMP [const], reg
CMP [reg], const
CMP [reg], reg
CMP const, const
```

#### Binary representation
```
CMP reg, reg
    3       =1. size in words
    8       =16. opcode
    8       register index (first argument)
    8       register index (second argument)
    37      unused
CMP reg, const
    3       =2. size in words
    8       =17. opcode
    8       register index (first argument)
    45      unused

    64      constant (second argument)
CMP reg, [const]
    3       =2. size in words
    8       =18. opcode
    8       register index (first argument)
    45      unused

    64      constant (second argument)
CMP reg, [reg]
    3       =1. size in words
    8       =19. opcode
    8       register index (first argument)
    8       register index (second argument)
    37      unused
CMP [const], const
    3       =3. size in words
    8       =20. opcode
    53      unused

    64      constant (first argument)

    64      constant (second argument)
CMP [const], reg
    3       =2. size in words
    8       =21. opcode
    8       register index (second argument)
    45      unused

    64      constant (first argument)
CMP [reg], const
    3       =2. size in words
    8       =22. opcode
    8       register index (first argument)
    45      unused

    64      constant (second argument)
CMP [reg], reg
    3       =1. size in words
    8       =23. opcode
    8       register index (first argument)
    8       register index (second argument)
    37      unused
CMP const, const
    3       =3. size in words
    8       =24. opcode
    53      unused

    64      constant (first argument)

    64      constant (second argument)
```

### JMP
Jumps to a memory address if some condition was met (sets IP to that address).
The condition is determined by the conditional code, or condcode:
```
0 (JE)  - jump if CF has bit 0 (equal)
1 (JNE) - jump if CF has bit 1 (not equal)
2 (JL)  - jump if CF has bit 2 (less)
3 (JLE) - jump if CF has bit 3 (less equal)
4 (JG)  - jump if CF has bit 4 (greater)
5 (JGE) - jump if CF has bit 5 (greater equal)
6 (JMP) - unconditional jump
```

#### Syntax
```
JMP CND, const
JMP CND, reg
JMP CND, [const]
JMP CND, [reg]
```

#### Binary representation
```
JMP CND, const
    3       =2. size in words
    8       =25. opcode
    3       condcode (first argument)
    50      unused

    64      constant (second argument)
JMP CND, reg
    3       =1. size in words
    8       =26. opcode
    3       condcode (first argument)
    8       register index (second argument)
    42      unused
JMP CND, [const]
    3       =2. size in words
    8       =27. opcode
    3       condcode (first argument)
    50      unused

    64      constant (second argument)
JMP CND, [reg]
    3       =1. size in words
    8       =28. opcode
    3       condcode (first argument)
    8       register index (second argument)
    42      unused
```
#### Notes
JMP CND, X instruction is simplified to CND X in the assembler.

### PUSH, POP
These two instructions are implemented using ARITHM and MOV instructions.
PUSH pushes a word at SH address in RAM, and POP pops a word from the SH address in RAM. 
When pushing, SH register is decremented by 1. When popping, it's incremented by 1.

#### Syntax
```
PUSH const
PUSH reg
PUSH [const]
PUSH [reg]

POP reg
POP [const]
POP [reg]
```

### CALL, RET
Call calls a function. Ret returns from a function. Both are implemented as a set of MOV, ARITHM, and JMP instructions.

CALL Pushes all registers on the stack, and ret pops them. Also uses a RP register to return to the right location after leaving a function. Setups a new stack frame as well.


RET pops all registers, and jumps to address stored in RP

Note that RR register is not pushed nor poped. It is used as return value.

#### Syntax
```
CALL const
CALL reg
CALL [const]
CALL [reg]

RET
```

### DONE
Stops everything
#### Syntax
```
DONE
```
#### Binary representation

```
DONE
    3       =1. size in words
    8       =255. opcode
    53      unused
```

## MEMORY:
### 1. Instruction memory - 8 words.
Contains instruction and data that has to be executed. Filled in fetch part of the cycle.

#### Implementation
It is a chip with three input pins that are used to write a word. 8 output pins are used to read words.
    
### 2. Program ROM - 2^10 words.
Contains the initial program. When DWAK starts, the program gets loaded into RAM at address 0.

#### implementation    
Implemented as an EEPROM and a circuit that loads itself into RAM when the computer boots.

The circuit simply reads 1024 words and writes them into RAM at the respectifull address. When it reaches 1024-th word, it toggles a register that stops further writing to RAM.

### 3. RAM - 2^24 words.
Random Access Memory. The initial program is loaded at address 0.       
Memory at the end of RAM is used for external devices. TODO(like VGA memory)

#### implementation
Implemented as a RAM with one write and two read ports.
    

## WHAT HAPPENS WHEN DWAK BOOTS:
The initial program in the ROM gets loaded into RAM at address 0. It starts executing the instructions


## WHAT HAPPENS AFTER DWAK BOOTS:
CPU performs a CPU cycle.
This happens in two stages.

### 1. Fetch
CPU reads the next instruction. It loads it, as well as its data (if opcode requires), into the instruction memory. 
Each word is read in one CPU cycle.
At the end of the Fetch stage, IP points to the next instruction.

### 2. Execute
CPU reads the content of the instruction memory, and sends its content to the right instruction chip. 
The chip then executes the instruction in one CPU cycle. 
All instruction chips have access to registers and RAM.

---
#### Implementation
There is a special thing called mode. There are 3 modes:
```
0 - read next instuction
1 - read and transfer data from RAM to the instruction memory
2 - execute instruction from the instruction memory
```

the mode cycles in 0-1-2-0 cycle


## HOW INSTRUCTION CHIPS WORK:
Each chip is given its input data that came from the instruction. 
If chip has to read some data from registers or RAM, it does it by sending the request to the output pins, which instantly deliver the request. 
Registers and RAM return the requested information instantly. The chip receives it. If now it has to read some more info - the process repeats.
When the chip is done reading, it instantly calculates the result data and sends it to registers and RAM to store.
Data is stored at the next CPU cycle.


## TODO
- [x] Design registers
- [x] Implements registers
- [x] Design RAM
- [x] Implement RAM
- [x] Design program ROM
- [x] Implement program ROM
- [x] Design instruction memory
- [x] Implement instruction memory 
- [x] Design Fetch stage
- [x] Implement Fetch stage
- [x] Design `MOV`
- [x] Implement `MOV`
- [x] Design `ADD`
- [x] Implement `ADD`
- [x] Design `SUB`
- [x] Implement `SUB`
- [x] Design `MUL`
- [x] Implement `MUL`
- [x] Design `DIVQ`
- [x] Implement `DIVQ`
- [x] Design `DIVR`
- [x] Implement `DIVR`
- [x] Design `OR`
- [x] Implement `OR`
- [x] Design `AND`
- [x] Implement `AND`
- [x] Design `XOR`
- [x] Implement `XOR`
- [x] Design `NOT`
- [x] Implement `NOT`
- [x] Design `SHL`
- [x] Implement `SHL`
- [x] Design `SHR`
- [x] Implement `SHR`
- [ ] Design `CMP`
- [ ] Implement `CMP`
- [ ] Design `JMP`
- [ ] Implement `JMP`
- [ ] Design `JE`
- [ ] Implement `JE`
- [ ] Design `JNE`
- [ ] Implement `JNE`
- [ ] Design `JL`
- [ ] Implement `JL`
- [ ] Design `JLT`
- [ ] Implement `JLT`
- [ ] Design `JG`
- [ ] Implement `JG`
- [ ] Design `JGT`
- [ ] Implement `JGT`
- [ ] Design `PUSH`
- [ ] Implement `PUSH`
- [ ] Design `POP`
- [ ] Implement `POP`
- [ ] Design `CALL`
- [ ] Implement `CALL`
- [ ] Design `RET`
- [ ] Implement `RET`

       
    
        
        
        
        

            
               
            
            
            
                
    
    
    
     



