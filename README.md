# DWAK2 - An improved version of DWAK CPU architecture

DWAK2 is 64 bit. Therefore, all instructions are 64bit, and one word is 64bits.
Due to the simulation software limitations, addresses will be 24bit.


## TERMINOLOGY
- reg - means a register index.
    Can be one of: `R0`, `R1`, `R2`, `R3`, `CF`, `QT`, `RM`, `SB`, `SH`, `IP`

- [mem] - means a memory address.
    Can be one of: `[const]`, `[reg]`

- const - means a constant value.
    Can be any hex, decimal, or binary number.


## REGISTERS
### General usage registers R0, R1, R2, R3.
Used in general computations.

- R0 has register index TODO, size of 64bits.
- R1 has register index TODO, size of 64bits.
- R2 has register index TODO, size of 64bits.
- R3 has register index TODO size of 64bits.

### Conditional flag register CF.
Contains a value that indicates the result of the last CMP instruction.

        0 means "equal", 1 means "not equal",
        2 means "less", 3 means "less equal",
        4 means "greater", 5 means "greater equal".
        
- CF has register index TODO, size of 3bits.

### Integer division registers QT, RM.
Used in DIV instruction to store the quotient in QT and the remainder in RM.
    
- QT has register index TODO, size of 64bits.
- RM has register index TODO, size of 64bits.

### Stack registers SB, SH.
Used in stack operations. SB points to the base of the stack, and SH points to the head of the stack. 
    
- SB has register index TODO, size of 64bits.
- SH has register index TODO, size of 64bits.
    
### Instruction pointer register IP.
Points to the next instruction that has to be executed. Shouldn't be directly changed.
    
- IP has register index TODO, size of 64bits.


## INSTRUCTIONS
### 1. MOV
Moves data from one location to another.
Can move data to registers or memory.
Can move data from registers, memory, or move constant values. However, can't move data from memory to memory.

#### Syntax:
```
MOV reg, reg        (opcode TODO)
MOV reg, [mem]      (opcode TODO)
MOV reg, const      (opcode TODO)
MOV [mem], reg      (opcode TODO)
MOV [mem], const    (opcode TODO)
```
#### Binary representation

```
MOV reg, reg
    0-7     opcode TODO
    8-15    register index (first argument)
    16-23   register index (second argument)
    24-63   unused
MOV reg, mem
    0-7     opcode TODO
    8-15    register index (first argument)
    16-39   memory address (second argument)
MOV reg, const
    0-7     opcode TODO
    8-15    register index (first argument)
    16-63   unused

    0-63    constant (second argument)
MOV mem, reg
    0-7     opcode TODO
    8-31    memory address (first argument)
    32-39   register index (second argument)
MOV mem, const
    0-7     opcode TODO
    8-31    memory address (first argument)
    32-63   unused
    
    0-63    constant (second argument)
```

## MEMORY:
### 1. Instruction memory - 16 words.
Contains instruction and data that has to be executed. Filled in fetch part of the cycle.
    
### 2. Program ROM - 2^24 words.
Contains the initial program. When DWAK starts, the program gets loaded into RAM at address 0.
    
### 3. RAM - 2^24 words.
Random Access Memory. The initial program is loaded at address 0.       
Memory at the end of RAM is used for external devices. TODO(like VGA memory)
    

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


## HOW INSTRUCTION CHIPS WORK:
Each chip is given its input data that came from the instruction. 
If chip has to read some data from registers or RAM, it does it by sending the request to the output pins, which instantly deliver the request. 
Registers and RAM return the requested information instantly. The chip receives it. If now it has to read some more info - the process repeats.
When the chip is done reading, it instantly calculates the result data and sends it to registers and RAM to store.
Data is stored at the next CPU cycle.


## TODO
- [ ] Design `MOV`
- [ ] Implement `MOV`
- [ ] Design `ADD`
- [ ] Implement `ADD`
- [ ] Design `SUB`
- [ ] Implement `SUB`
- [ ] Design `MUL`
- [ ] Implement `MUL`
- [ ] Design `DIV`
- [ ] Implement `DIV`
- [ ] Design `OR`
- [ ] Implement `OR`
- [ ] Design `AND`
- [ ] Implement `AND`
- [ ] Design `XOR`
- [ ] Implement `XOR`
- [ ] Design `NOT`
- [ ] Implement `NOT`
- [ ] Design `SHL`
- [ ] Implement `SHL`
- [ ] Design `SHR`
- [ ] Implement `SHR`
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

       
    
        
        
        
        

            
               
            
            
            
                
    
    
    
     



